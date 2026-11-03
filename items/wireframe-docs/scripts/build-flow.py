#!/usr/bin/env python3
"""Build a playable player.html for wireframe-docs flows in a suite.

Usage:
    python3 build-flow.py <suite-dir> [flow.md ...]

Parses flows/*.md (strict format, see convention/flows.md), validates them
with check-flow.py (refuses to build on FAIL), inlines each referenced
wireframe frame (all 4 breakpoints) + tree metadata + data values into
templates/player.template.html, writes <suite>/player.html.

Run from anywhere. Stdlib only, no network. Never edit the output by hand:
rebuild after changing flows/trees/wireframes.
"""
import json
import os
import re
import subprocess
import sys
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}


WIRE_FRAME_SCOPE = ("#stage", "#page-stage", ".wf-frame")


def _split_selectors(sel):
    """Split a selector list on top-level commas (ignore parens/quotes)."""
    parts, depth, quote, cur = [], 0, "", []
    for ch in sel:
        if quote:
            cur.append(ch)
            if ch == quote:
                quote = ""
        elif ch in ("'", '"'):
            cur.append(ch)
            quote = ch
        elif ch == "(":
            depth += 1
            cur.append(ch)
        elif ch == ")":
            depth = max(0, depth - 1)
            cur.append(ch)
        elif ch == "," and depth == 0:
            parts.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    parts.append("".join(cur))
    return [x.strip() for x in parts if x.strip()]


def _scope_rule_block(css):
    """Prefix every style rule selector with the player frame scope."""
    out, i, n = [], 0, len(css)
    while i < n:
        while i < n and css[i] in " \t\n\r":
            i += 1
        if i >= n:
            break
        if css[i] == "@":
            j = css.find("{", i)
            semi = css.find(";", i)
            if j == -1 or (semi != -1 and semi < j):
                out.append(css[i:semi + 1] if semi != -1 else css[i:])
                i = len(css) if semi == -1 else semi + 1
                continue
            head = css[i:j].strip()
            depth, k = 1, j + 1
            while k < n and depth:
                if css[k] == "{":
                    depth += 1
                elif css[k] == "}":
                    depth -= 1
                k += 1
            inner = css[j + 1:k - 1]
            name = head.split("(", 1)[0].split(" ", 1)[0]
            if name in ("@media", "@supports", "@container", "@layer"):
                out.append(head + "{" + _scope_rule_block(inner) + "}")
            else:
                out.append(head + "{" + inner + "}")
            i = k
            continue
        j = css.find("{", i)
        if j == -1:
            out.append(css[i:])
            break
        sel = css[i:j].strip()
        depth, k = 1, j + 1
        while k < n and depth:
            if css[k] == "{":
                depth += 1
            elif css[k] == "}":
                depth -= 1
            k += 1
        body = css[j + 1:k - 1]
        scoped = ", ".join(
            "%s %s" % (w, x) for w in WIRE_FRAME_SCOPE for x in _split_selectors(sel))
        out.append(scoped + "{" + body + "}")
        i = k
    return "".join(out)


def scope_wireframe_css(css):
    """Scope author wireframe CSS to player frames.

    Bare element selectors (body/html/:root) become inert on purpose:
    the shell owns page chrome. Keep frame styling in classes.
    """
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    return _scope_rule_block(css.strip())


class FrameExtractor(HTMLParser):
    """Capture raw HTML of each element with data-wf-breakpoint."""

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.frames = {}  # bp -> {"width": str, "html": str}
        self._cur = None
        self._depth = 0
        self._buf = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self._cur is None and "data-wf-breakpoint" in a:
            self._cur = a["data-wf-breakpoint"].strip()
            self.frames.setdefault(self._cur,
                                   {"width": a.get("data-wf-width",
                                                   "").strip(),
                                    "html": ""})
            self._buf = [self.get_starttag_text()]
            self._depth = 1
        elif self._cur is not None:
            self._buf.append(self.get_starttag_text())
            if tag not in VOID:
                self._depth += 1

    def handle_endtag(self, tag):
        if self._cur is not None:
            if tag not in VOID:
                self._buf.append("</%s>" % tag)
                self._depth -= 1
                if self._depth <= 0:
                    self.frames[self._cur]["html"] = "".join(self._buf)
                    self._cur = None
                    self._buf = []

    def handle_data(self, data):
        if self._cur is not None:
            self._buf.append(data)

    def handle_comment(self, data):
        if self._cur is not None:
            self._buf.append("<!--%s-->" % data)


class StyleExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.styles = []
        self._in = False
        self._buf = []

    def handle_starttag(self, tag, attrs):
        if tag == "style":
            self._in = True
            self._buf = []

    def handle_endtag(self, tag):
        if tag == "style" and self._in:
            self._in = False
            text = "".join(self._buf).strip()
            if text:
                self.styles.append(text)

    def handle_data(self, data):
        if self._in:
            self._buf.append(data)


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main(argv):
    if len(argv) < 2 or "-h" in argv or "--help" in argv:
        print("usage: python3 build-flow.py <suite-dir> [flow.md ...]")
        print("  writes <suite>/player.html (overwrite)")
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
    # 1. validate all flows together (suite-wide orphan check)
    cf = os.path.join(HERE, "check-flow.py")
    r = subprocess.run([sys.executable, cf, suite] + files,
                       capture_output=True, text=True)
    sys.stdout.write(r.stdout)
    sys.stderr.write(r.stderr)
    if r.returncode != 0:
        print("FAIL: khong build player khi flow con FAIL")
        return 1
    # 2. parse flows (lightweight re-parse for build data)
    sys.path.insert(0, HERE)
    from check import TreeError, parse as parse_tree  # noqa: E402
    flows = []
    pages_needed = set()
    for fp in files:
        meta, steps = parse_flow_file(fp)
        flows.append({"file": os.path.basename(fp), "meta": meta,
                      "steps": steps})
        if meta.get("entry_page"):
            pages_needed.add(meta["entry_page"])
        for st in steps:
            if st.get("page"):
                pages_needed.add(st["page"])
            for g in st.get("go", []):
                m = re.match(r"page\s*:\s*(\S+)", g)
                if m:
                    pages_needed.add(m.group(1))
    # 3. extract frames + metadata + data per page
    frames, metas, datas, titles, css_list, seen_css = {}, {}, {}, {}, [], set()
    for page in sorted(pages_needed):
        tpath = page_tree_path(suite, page)
        try:
            tree = parse_tree(tpath)
        except (FileNotFoundError, TreeError) as e:
            print("FAIL: %s" % e)
            return 1
        base = os.path.dirname(tpath)
        stem = os.path.basename(tpath)
        if stem.endswith("-tree.md"):
            hpath = os.path.join(base, stem[:-len("-tree.md")] + "-wireframe.html")
            dpath = os.path.join(base, stem[:-len("-tree.md")] + "-data.json")
        else:
            hpath = os.path.join(base, "tree.html")
            dpath = os.path.join(base, "data.json")
        try:
            with open(hpath, encoding="utf-8") as f:
                src = f.read()
        except FileNotFoundError:
            print("FAIL: thieu wireframe %s" % hpath)
            return 1
        fx = FrameExtractor()
        fx.feed(src)
        if not fx.frames:
            print("FAIL: %s khong co khung data-wf-breakpoint" % hpath)
            return 1
        frames[page] = {bp: v["html"] for bp, v in fx.frames.items()}
        sx = StyleExtractor()
        sx.feed(src)
        for css in sx.styles:
            css = scope_wireframe_css(css)
            if css and css not in seen_css:
                seen_css.add(css)
                css_list.append(css)
        pmap = {}
        for _n, _m, comps in tree["sections"]:
            for c in comps:
                pmap[c["label"]] = {
                    "type": c["type"], "note": c.get("note", ""),
                    "states": list(c.get("states", [])),
                    "effect": sorted(c.get("effect", set())),
                    "behavior": sorted(c.get("behavior", set())),
                    "reduced": c.get("reduced", ""),
                    "visible_on": sorted(c.get("visible_on", set())),
                    "req": sorted(c.get("req", set())),
                }
        metas[page] = pmap
        titles[page] = tree.get("page") or page
        try:
            datas[page] = load_json(dpath).get("values", {})
        except (FileNotFoundError, ValueError) as e:
            print("FAIL: data %s: %s" % (dpath, e))
            return 1
    # 4. emit player
    with open(os.path.join(HERE, "..", "templates",
                           "player.template.html"),
              encoding="utf-8") as f:
        tpl = f.read()
    out = tpl.replace("/*__FLOW_DATA__*/",
                      "window.__FLOWS__ = %s;" % json.dumps(flows_json(flows),
                                                           ensure_ascii=False))
    out = out.replace("/*__FRAMES_DATA__*/",
                      "window.__FRAMES__ = %s;" % json.dumps(frames,
                                                             ensure_ascii=False))
    out = out.replace("/*__META_DATA__*/",
                      "window.__META__ = %s;" % json.dumps(metas,
                                                           ensure_ascii=False))
    out = out.replace("/*__DATA_DATA__*/",
                      "window.__DATA__ = %s;" % json.dumps(datas,
                                                           ensure_ascii=False))
    out = out.replace("/*__TITLE_DATA__*/",
                      "window.__PAGE_TITLES__ = %s;" % json.dumps(titles,
                                                                  ensure_ascii=False))
    out = out.replace("/*__WIREFRAME_CSS__*/", "\n".join(css_list))
    dest = os.path.join(suite, "player.html")
    with open(dest, "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote %s (%d flows, %d pages, %d bytes)"
          % (dest, len(flows), len(frames), len(out)))
    return 0


def page_tree_path(suite, page):
    cand = os.path.join(suite, page, page + "-tree.md")
    if os.path.isfile(cand):
        return cand
    return os.path.join(suite, page, "tree.md")


STEP_RE = re.compile(r"^## Step\s+(\d+)\s*:\s*(.+?)\s*$")
KEYVAL_RE = re.compile(r"^-\s*([A-Za-z]+)\s*:\s*(.*)$")


def parse_flow_file(path):
    """Lightweight flow parse for build (validation done by check-flow.py)."""
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    meta = {}
    steps = []
    cur = None
    for raw in lines:
        line = raw.strip()
        m = re.match(r"^# Flow:\s*(.+?)\s*$", line)
        if m:
            meta["name"] = m.group(1)
            continue
        m = STEP_RE.match(line)
        if m:
            cur = {"n": int(m.group(1)), "title": m.group(2), "page": None,
                   "action": None, "expect": None, "go": [], "inputs": [],
                   "branches": []}
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
                am = re.match(r"Action\s*:\s*`([^`]+)`\s*(.+)$", part)
                if am:
                    label = re.sub(r"^\*\*(.+)\*\*$", r"\1",
                                   am.group(2).strip()).strip()
                    cur["action"] = [am.group(1).strip(), label]
                    continue
                em = re.match(r"Expect\s*:\s*(.+)$", part)
                if em:
                    cur["expect"] = em.group(1).strip()
        elif key == "Action":
            am = re.match(r"`([^`]+)`\s*(.+?)\s*$", val)
            if am:
                label = re.sub(r"^\*\*(.+)\*\*$", r"\1",
                               am.group(2).strip()).strip()
                cur["action"] = [am.group(1).strip(), label]
        elif key == "Expect":
            cur["expect"] = val
        elif key == "go":
            cur["go"].append(val)
        elif key == "Input":
            im = re.match(r"(.+?)(?:\s*=\s*(.+))?\s*$", val)
            if im:
                key2 = (im.group(2) or "").strip() or im.group(1).strip()
                cur["inputs"].append([im.group(1).strip(), key2])
        elif key in ("If", "Else"):
            cur["branches"].append(val)
    if "entry" in meta:
        me = re.match(r"(\S+)\s*@\s*(\w+)\s*$", meta["entry"])
        if me:
            meta["entry_page"], meta["entry_bp"] = me.group(1), me.group(2)
    return meta, steps


def flows_json(flows):
    out = []
    for f in flows:
        meta = f.get("meta", {})
        out.append({
            "file": f.get("file", ""),
            "name": meta.get("name", ""),
            "desc": meta.get("pre", ""),
            "terminal": meta.get("terminal", ""),
            "req": meta.get("req", ""),
            "steps": f.get("steps", []),
        })
    return out


if __name__ == "__main__":
    sys.exit(main(sys.argv))
