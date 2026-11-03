#!/usr/bin/env python3
"""Rà soát cuối 1 wireframe-docs suite (DoD gate trước khi trình/chốt).

Usage:
    python3 check-suite.py <suite-dir>

Chạy toàn bộ kiểm tra của suite và in báo cáo gộp:
1. brief.md tồn tại + có mã REQ-xxx (thiếu = FAIL).
2. Mỗi trang: check.py PASS, verify-pair.py 3 chân PASS,
   check-guidelines.py 0 FAIL (thiếu = FAIL, WARN giữ nguyên để designer duyệt).
3. Mọi flow: check-flow.py PASS (thiếu = FAIL).
4. Đối chiếu REQ: mã tree cite mà brief không có = FAIL;
   REQ brief không trang nào cite = WARN; component không cite req = WARN.
5. player.html tồn tại + mới hơn mọi nguồn (không thì WARN build lại).
6. Link nội bộ trong *-wireframe.html trỏ file .html tồn tại (gãy = FAIL).

Exit 0 khi không có FAIL (WARN không chặn). Không sửa file.
"""
import json
import os
import re
import subprocess
import sys
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check import TreeError, parse as parse_tree  # noqa: E402

REQ_RE = re.compile(r"^REQ-[A-Za-z0-9-]+$")
HREF_RE = re.compile(r"""\s+href\s*=\s*["']([^"'#]+)["']""", re.IGNORECASE)


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()


def page_tree_path(suite, page):
    cand = os.path.join(suite, page, page + "-tree.md")
    if os.path.isfile(cand):
        return cand
    gen = os.path.join(suite, page, "tree.md")
    if os.path.isfile(gen):
        return gen
    return cand


def main(argv):
    if len(argv) < 2 or "-h" in argv or "--help" in argv:
        print("usage: python3 check-suite.py <suite-dir>")
        return 2
    suite = argv[1]
    here = os.path.dirname(os.path.abspath(__file__))
    fails, warns = [], []

    # 1. brief
    brief_reqs = []
    bpath = os.path.join(suite, "brief.md")
    try:
        with open(bpath, encoding="utf-8") as f:
            for raw in f.read().splitlines():
                m = re.match(r"^\s*-\s*(REQ-[A-Za-z0-9-]+)\s*:", raw.strip())
                if m:
                    brief_reqs.append(m.group(1))
    except FileNotFoundError:
        fails.append("FAIL [suite]: thieu brief.md (DoD muc 1)")
    if not brief_reqs and not any("brief.md" in f for f in fails):
        warns.append("WARN [suite]: brief.md khong co ma REQ-xxx nao")
    print("brief: %d REQ (%s)" % (len(brief_reqs), ", ".join(brief_reqs)
                                   if brief_reqs else "khong co"))

    # 2+3. pages
    try:
        pages = sorted(d for d in os.listdir(suite)
                       if os.path.isdir(os.path.join(suite, d))
                       and (os.path.isfile(os.path.join(suite, d,
                                                        d + "-tree.md"))
                            or os.path.isfile(os.path.join(suite, d,
                                                           "tree.md"))))
    except FileNotFoundError:
        pages = []
    if not pages:
        fails.append("FAIL [suite]: khong co trang nao (thu muc chua tree)")
    seen_reqs = set()
    for pg in pages:
        tp = page_tree_path(suite, pg)
        base, stem = os.path.split(tp)
        if stem.endswith("-tree.md"):
            dp = os.path.join(base, stem[:-len("-tree.md")] + "-data.json")
            hp = os.path.join(base, stem[:-len("-tree.md")] + "-wireframe.html")
        else:
            dp = os.path.join(base, "data.json")
            hp = os.path.join(base, "tree.html")
        code, out = run([sys.executable, os.path.join(here, "check.py"), tp])
        print(out)
        if code != 0:
            fails.append("FAIL [%s]: check.py FAIL" % pg)
        code, out = run([sys.executable, os.path.join(here, "verify-pair.py"),
                         tp, hp, dp])
        print(out)
        if code != 0:
            fails.append("FAIL [%s]: verify-pair.py 3 chan FAIL" % pg)
        code, out = run([sys.executable,
                         os.path.join(here, "check-guidelines.py"), tp, dp])
        print(out)
        if code != 0:
            fails.append("FAIL [%s]: guidelines con FAIL (xem SCORE o tren)"
                         % pg)
        try:
            tree = parse_tree(tp)
            for _n, _m, comps in tree["sections"]:
                for c in comps:
                    for r in c.get("req", set()):
                        seen_reqs.add(r)
        except (FileNotFoundError, TreeError) as e:
            fails.append("FAIL [%s]: %s" % (pg, e))

    # 4. flows: 1 lan duy nhat cho ca suite (orphan check dung pham vi)
    fdir = os.path.join(suite, "flows")
    try:
        flows = sorted(os.path.join(fdir, f) for f in os.listdir(fdir)
                       if f.endswith(".md"))
    except FileNotFoundError:
        flows = []
    if not flows:
        warns.append("WARN [suite]: khong co flows/*.md (chua co flow nao)")
    else:
        code, out = run([sys.executable,
                         os.path.join(here, "check-flow.py"), suite] + flows)
        print(out, end="" if out.endswith("\n") else "\n")
        if code != 0:
            fails.append("FAIL [flows]: check-flow FAIL")

    # 5. internal links inside wireframes
    for root, _dirs, files in os.walk(suite):
        for f in sorted(files):
            if not f.endswith("-wireframe.html") and f != "tree.html":
                continue
            fp = os.path.join(root, f)
            try:
                with open(fp, encoding="utf-8") as fh:
                    src = fh.read()
            except OSError:
                continue
            for m in HREF_RE.finditer(src):
                href = m.group(1).strip()
                if not href or href.startswith(("http://", "https://",
                                                "mailto:", "tel:", "//")):
                    continue
                target = href.split("#", 1)[0].split("?", 1)[0].strip()
                if not target.endswith(".html"):
                    continue
                dest = os.path.normpath(os.path.join(root, target))
                if not os.path.isfile(dest):
                    fails.append("FAIL [link]: %s tro '%s' khong ton tai"
                                  % (os.path.relpath(fp, suite), href))

    # 6. player freshness
    player = os.path.join(suite, "player.html")
    if not os.path.isfile(player):
        warns.append("WARN [suite]: thieu player.html (chay build-flow.py)")
    else:
        newest = 0
        for root, _dirs, files in os.walk(suite):
            if "player.html" in files:
                files = [f for f in files if f != "player.html"]
            for f in files:
                try:
                    newest = max(newest, os.path.getmtime(os.path.join(root,
                                                                       f)))
                except OSError:
                    pass
        try:
            if os.path.getmtime(player) < newest:
                warns.append("WARN [suite]: player.html cu hon nguon "
                             "(build-flow.py lai)")
        except OSError:
            pass

    # 6. REQ coverage
    for r in sorted(seen_reqs - set(brief_reqs)):
        fails.append("FAIL [req]: tree cite '%s' nhung brief.md khong co" % r)
    for r in sorted(set(brief_reqs) - seen_reqs):
        warns.append("WARN [req]: '%s' trong brief nhung chua trang nao cite "
                     "(chua lam hoac de quen)" % r)

    print("SUITE %s: %d FAIL, %d WARN" % (suite, len(fails), len(warns)))
    for f in fails:
        print(f)
    for w in warns:
        print(w)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
