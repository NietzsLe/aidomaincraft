#!/usr/bin/env python3
"""Kiem tra flow.md cua wireframe-docs trong 1 suite.

Usage:
    python3 check-flow.py <suite-dir> [flow.md]

Doc moi flows/<ten>.md, doi chieu voi tree + data + wireframe cua suite:
- FAIL (exit 1): Entry thieu/sai; go: tro toi target khong ton tai;
  Action/Input tro toi component/key khong ton tai; step sai dinh dang.
- WARN (khong chan): trang mo coi; step giua khong co loi di; destructive
  khong qua dialog; thieu nhanh loi cho form; step thieu Expect;
  thieu goi y deep-link/loading.

Khong bao gio sua file. Chi doc + bao cao.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check import TreeError, parse  # noqa: E402

BREAKPOINTS = ("sm", "md", "lg", "xl")
GO_RE = re.compile(r"go:\s*(page|dialog|drawer|back)\s*:?\s*(.*)\s*$")
STEP_RE = re.compile(r"^## Step\s+(\d+)\s*:\s*(.+?)\s*$")
KEYVAL_RE = re.compile(r"^-\s*([A-Za-z]+)\s*:\s*(.*)$")
DESTRUCTIVE_RE = re.compile(r"xóa|hủy|xoa|huy|delete", re.I)
LOADING_RE = re.compile(r"tải|load|đang|chờ|tai", re.I)
LOADING_STATE = re.compile(r"load|tải|pending|skeleton|spinner", re.I)


def parse_action(text, where):
    """'  `Type` **Label**' -> (type, label) or None + error string."""
    m = re.match(r"`([^`]+)`\s*(.+?)\s*$", text.strip())
    if not m:
        return None, ("Action sai dinh dang (can `Kieu` **Nhan**) tai %s"
                       % where)
    label = re.sub(r"^\*\*(.+)\*\*$", r"\1", m.group(2).strip()).strip()
    if not label:
        return None, ("Action thieu nhan tai %s" % where)
    return (m.group(1).strip(), label), None


def parse_flow(path):
    """-> (meta, steps, errors). Step = dict with keys below."""
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    meta = {}
    steps = []
    cur = None
    errors = []
    for ln, raw in enumerate(lines, 1):
        line = raw.strip()
        m = re.match(r"^# Flow:\s*(.+?)\s*$", line)
        if m:
            if "name" in meta:
                errors.append("dong %d: nhieu dong '# Flow:'" % ln)
            meta["name"] = m.group(1)
            continue
        m = re.match(r"^## Step\s+(\d+)\s*:\s*(.+?)\s*$", line)
        if m:
            cur = {"n": int(m.group(1)), "title": m.group(2), "line": ln,
                   "page": None, "action": None, "expect": None,
                   "go": [], "inputs": [], "branches": []}
            steps.append(cur)
            continue
        if cur is None:
            m = KEYVAL_RE.match(line)
            if m and m.group(1) in ("Entry", "Pre", "Req", "Terminal"):
                meta[m.group(1).lower()] = m.group(2).strip()
            continue
        m = KEYVAL_RE.match(line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if key == "Page":
            parts = [p.strip() for p in val.split("|")]
            cur["page"] = parts[0]
            for part in parts[1:]:
                pm = re.match(r"Action\s*:\s*(.+)$", part, re.I)
                if pm:
                    act, err = parse_action(pm.group(1),
                                            "dong %d" % ln)
                    if err:
                        errors.append(err)
                    else:
                        cur["action"] = act
                    continue
                em = re.match(r"Expect\s*:\s*(.+)$", part, re.I)
                if em:
                    cur["expect"] = em.group(1).strip()
        elif key == "Action":
            act, err = parse_action(val, "dong %d" % ln)
            if err:
                errors.append(err)
            else:
                cur["action"] = act
        elif key == "Expect":
            cur["expect"] = val
        elif key == "go":
            cur["go"].append(val)
        elif key == "Input":
            im = re.match(r"(.+?)(?:\s*=\s*(.+))?\s*$", val)
            if not im or not im.group(1).strip():
                errors.append("dong %d: Input sai dinh dang "
                              "(can 'Nhãn [= key]')" % ln)
            else:
                _label, _key = im.group(1).strip(), (im.group(2) or "").strip()
                cur["inputs"].append((_label, _key or _label))
        elif key in ("If", "Else"):
            cur["branches"].append(val)
    return meta, steps, errors


def parse_go(text):
    m = GO_RE.match(text.strip())
    if not m:
        return None
    kind, rest = m.group(1), m.group(2).strip()
    if kind == "back":
        return ("back", None)
    if kind == "page":
        return ("page", rest.split()[0] if rest else "")
    return (kind, rest)


def page_tree_path(suite, page):
    cand = os.path.join(suite, page, page + "-tree.md")
    if os.path.isfile(cand):
        return cand
    return os.path.join(suite, page, "tree.md")


def load_tree_data(suite, page):
    tpath = page_tree_path(suite, page)
    try:
        tree = parse(tpath)
    except FileNotFoundError:
        return None, None, ["khong tim thay tree: %s" % tpath]
    except TreeError as e:
        return None, None, ["tree loi %s: %s" % (tpath, e)]
    if tpath.endswith("-tree.md"):
        dpath = tpath[:-len("-tree.md")] + "-data.json"
    else:
        dpath = os.path.join(os.path.dirname(tpath), "data.json")
    try:
        with open(dpath, encoding="utf-8") as f:
            data = json.load(f).get("values", {})
    except (FileNotFoundError, ValueError):
        data = None
    return tree, data, []


def find_comp(tree, ctype, label):
    for _n, _m, comps in tree["sections"]:
        for c in comps:
            if c["label"] == label and (ctype is None or c["type"] == ctype):
                return c
    return None


def check_flow(suite, path):
    fails, warns, infos = [], [], []
    visited = set()
    try:
        meta, steps, errors = parse_flow(path)
    except FileNotFoundError:
        return ["FAIL: khong tim thay flow %s" % path], [], [], set()
    fails.extend("FAIL cau truc: %s" % e for e in errors)
    if "name" not in meta:
        fails.append("FAIL: thieu dong '# Flow: ten'")
        return fails, warns, infos, visited
    name = meta["name"]
    if "entry" not in meta:
        fails.append("FAIL [%s]: thieu dong '- Entry: <page> @ <bp>'" % name)
        return fails, warns, infos, visited
    me = re.match(r"(\S+)\s*@\s*(\w+)\s*$", meta["entry"])
    if not me or me.group(2) not in BREAKPOINTS:
        fails.append("FAIL [%s]: Entry sai dinh dang (can '<page> @ sm|md|lg|xl')"
                     % name)
        return fails, warns, infos
    if not os.path.isfile(page_tree_path(suite, me.group(1))):
        fails.append("FAIL [%s]: Entry tro toi trang khong ton tai '%s'"
                     % (name, me.group(1)))
    if not steps:
        fails.append("FAIL [%s]: khong co '## Step N:' nao" % name)
        return fails, warns, infos, visited
    nums = [s["n"] for s in steps]
    if nums != list(range(1, len(steps) + 1)):
        warns.append("WARN [%s]: danh so step khong lien tuc %s" % (name, nums))
    trees = {}
    has_dialog_go = False
    destructive_steps = []
    for idx, st in enumerate(steps):
        where = "step %d '%s'" % (st["n"], st["title"])
        if not st["page"]:
            fails.append("FAIL [%s] %s: thieu '- Page:'" % (name, where))
            continue
        if st["page"] not in trees:
            tree, data, errs = load_tree_data(suite, st["page"])
            fails.extend("FAIL [%s] %s: %s" % (name, where, e) for e in errs)
            if tree is None:
                continue
            trees[st["page"]] = (tree, data)
        tree, data = trees[st["page"]]
        if st["action"]:
            ctype, label = st["action"]
            comp = find_comp(tree, ctype, label)
            if comp is None:
                fails.append("FAIL [%s] %s: Action '%s %s' khong co trong tree "
                             "trang '%s'" % (name, where, ctype, label,
                                             st["page"]))
            else:
                if re.search(r"xóa|hủy|xoa|huy|delete", comp.get("note", ""),
                             re.I):
                    destructive_steps.append((where, label))
        for gtext in st["go"] + [b for b in st["branches"]]:
            for part in re.findall(r"go:\s*[^,;]+", gtext):
                tgt = parse_go(part)
                if tgt is None:
                    fails.append("FAIL [%s] %s: go: sai dinh dang '%s'"
                                 % (name, where, part.strip()))
                    continue
                kind, dest = tgt
                if kind == "back":
                    continue
                if kind == "page":
                    if not dest or not os.path.isfile(
                            page_tree_path(suite, dest)):
                        fails.append("FAIL [%s] %s: go: toi trang khong ton "
                                     "tai '%s'" % (name, where, dest))
                else:  # dialog | drawer
                    c = find_comp(tree, None, dest)
                    if c is None:
                        fails.append("FAIL [%s] %s: go: %s '%s' khong co "
                                     "trong tree trang '%s'"
                                     % (name, where, kind, dest, st["page"]))
                    elif kind not in {b.strip().lower()
                                      for b in c.get("behavior", set())} \
                            and kind not in {b.strip().lower()
                                             for b in c.get("behavior", [])}:
                        warns.append("WARN [%s] %s: '%s' thieu behavior '%s' "
                                     "(go: %s toi no)" % (name, where, dest,
                                                         kind, kind))
                    has_dialog_go = True
        for label, key in st["inputs"]:
            hit = False
            for _n, _m, comps in tree["sections"]:
                for c in comps:
                    if c["label"] == label:
                        hit = True
                        break
            if not hit:
                fails.append("FAIL [%s] %s: Input field '%s' khong co trong "
                             "tree" % (name, where, label))
            elif data is None or key not in data:
                fails.append("FAIL [%s] %s: Input key '%s' khong co trong "
                             "data.json" % (name, where, key))
        if st["inputs"]:
            has_err_branch = any(re.search(r"lỗi|sai|error|fail|invalid|"
                                           r"không hợp lệ|khong hop le",
                                           b, re.I)
                                 for b in st["branches"])
            if not has_err_branch:
                warns.append("WARN [%s] %s: co Input nhung khong co nhanh loi "
                             "(error/invalid) de designer quyet"
                             % (name, where))
        if not st["expect"]:
            warns.append("WARN [%s] %s: thieu Expect (khong ro ket qua mong "
                         "doi)" % (name, where))
        is_last = (idx == len(steps) - 1)
        has_out = bool(st["go"]) or any("go:" in b for b in st["branches"])
        if not has_out and not is_last:
            warns.append("WARN [%s] %s: step giua khong co loi di tiep "
                         "(dead-end?)" % (name, where))
    # visited pages (orphans computed suite-wide by caller)
    visited |= {st["page"] for st in steps if st["page"]}
    for gtext in [g for st in steps for g in st["go"]] + \
                 [b for st in steps for b in st["branches"]]:
        for part in re.findall(r"go:\s*page:([^\s,;]+)", gtext):
            visited.add(part)
    try:
        pages = [d for d in os.listdir(suite)
                 if os.path.isfile(page_tree_path(suite, d))]
    except FileNotFoundError:
        pages = []
    # (orphan pages warned suite-wide by caller)
    # destructive without dialog
    if destructive_steps and not has_dialog_go:
        for where, label in destructive_steps:
            warns.append("WARN [%s] %s: '%s' co the la destructive nhung flow "
                         "khong qua dialog confirm" % (name, where, label))
    # deep-link hint: go: page:* target page note should mention URL
    for st in steps:
        for gtext in st["go"]:
            for dest in re.findall(r"go:\s*page:([^\s,;]+)", gtext):
                tpath = page_tree_path(suite, dest)
                try:
                    t = parse(tpath)
                    note = ""
                    for _n, m, _c in t["sections"]:
                        note += " " + str(m.get("note", ""))
                    if not re.search(r"url|đường dẫn|duong dan|deep-link|link",
                                     note, re.I):
                        warns.append("WARN [%s]: go: toi page '%s' nhung tree "
                                     "khong ghi chu deep-link/URL"
                                     % (name, dest))
                except (FileNotFoundError, TreeError):
                    pass
    # loading hint: note mentions tai/load/cho but no loading state
    for st in steps:
        if not st["page"] or st["page"] not in trees:
            continue
        tree, _data = trees[st["page"]]
        notes = " ".join(c.get("note", "") for _n, _m, cs in tree["sections"]
                         for c in cs)
        if LOADING_RE.search(notes):
            states = {s for _n, _m, cs in tree["sections"] for c in cs
                      for s in c.get("states", [])}
            if not any(LOADING_STATE.search(s) for s in states):
                warns.append("WARN [%s] trang '%s': note noi tai/load/cho "
                             "nhung khong co state loading (skeleton/spinner)"
                             % (name, st["page"]))
                break
    return fails, warns, ["flow '%s': %d steps" % (name, len(steps))], visited


def main(argv):
    if len(argv) < 2 or "-h" in argv or "--help" in argv:
        print("usage: python3 check-flow.py <suite-dir> [flow.md ...]")
        print("  default: moi flows/*.md trong suite")
        return 2
    suite = argv[1]
    if len(argv) > 2:
        files = argv[2:]
    else:
        fdir = os.path.join(suite, "flows")
        try:
            files = sorted(os.path.join(fdir, f) for f in os.listdir(fdir)
                           if f.endswith(".md"))
        except FileNotFoundError:
            files = []
    if not files:
        print("FAIL: suite '%s' khong co flows/*.md" % suite)
        return 1
    nf = nw = 0
    visited_all = set()
    for fp in files:
        fails, warns, infos, visited = check_flow(suite, fp)
        visited_all |= visited
        for i in infos:
            print("  %s" % i)
        for w in warns:
            print("%s" % w)
            nw += 1
        for f in fails:
            print("%s" % f)
            nf += 1
        print("FLOW %s: %s (%d fail, %d warn)"
              % (fp, "PASS" if not fails else "FAIL", len(fails),
                 len([w for w in warns if w.startswith("WARN")])))
    try:
        pages = [d for d in os.listdir(suite)
                 if os.path.isfile(page_tree_path(suite, d))]
    except FileNotFoundError:
        pages = []
    for pg in sorted(set(pages) - visited_all):
        print("WARN [suite]: trang '%s' mo coi (khong flow nao di toi)" % pg)
        nw += 1
    print("SUITE flows: %d file, %d FAIL, %d WARN" % (len(files), nf, nw))
    return 1 if nf else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
