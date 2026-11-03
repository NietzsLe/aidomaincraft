#!/usr/bin/env python3
"""Verify a wireframe-docs tree.md <-> data.json <-> wireframe.html trio.

Usage:
    python3 verify-pair.py <tree.md> <wireframe.html> [data.json]

The tree defines scope, the data file holds sample content, the wireframe
is hand-authored (one file, four breakpoint frames). This script reports
every drift between the three so the designer can rule on it. It never
fixes anything by itself. The data file defaults to the tree's sibling
<slug>-data.json.

Exit 0 + PASS line when the trio matches; exit 1 + FAIL lines otherwise.
FAIL classes: missing data file/keys/values, missing frame/section/
component, extra section/component, layout/states/effect/reduced mismatch,
unknown breakpoint, bad width, structural errors.
"""
import json
import os
import re
import sys
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check import (  # noqa: E402
    BREAKPOINTS,
    WIDTHS,
    TreeError,
    eff_layout,
    parse,
)


PLACEHOLDER_RE = re.compile(
    r"(?i)\blorem\b|\bxxx\b|\btodo\b|\[ghi chú\]|\[mô tả\]|\[xxx\]")


def norm_set(value):
    return set(s.strip() for s in (value or "").split(",") if s.strip())


class PairHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []  # [(tag, frame_bp_or_None, section_or_None, label_or_None)]
        self.pages = set()
        self.frames = {}  # bp -> {"width": str|None, "sections": {...}}
        self.text = {}  # (frame, section, label) -> rendered text
        self.errors = []

    def _cur(self):
        for _tag, frame, section, label in reversed(self.stack):
            if label is not None:
                return (frame, section, label)
        return None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        parent_frame = self.stack[-1][1] if self.stack else None
        parent_section = self.stack[-1][2] if self.stack else None
        frame = parent_frame
        section = parent_section
        label = None
        if tag == "input":
            cur = self._cur()
            if cur is not None:
                for k in ("value", "placeholder"):
                    v = (a.get(k) or "").strip()
                    if v:
                        self.text[cur] = self.text.get(cur, "") + " " + v
        if "data-wf-page" in a:
            self.pages.add(a["data-wf-page"].strip())
        if "data-wf-breakpoint" in a:
            bp = a["data-wf-breakpoint"].strip()
            if bp not in BREAKPOINTS:
                self.errors.append("breakpoint '%s' khong hop le (chi nhan: %s)"
                                   % (bp, ", ".join(BREAKPOINTS)))
                bp = None
            else:
                frame = bp
                section = None
                self.frames.setdefault(bp, {"width": a.get("data-wf-width",
                                                           "").strip(),
                                            "sections": {}})
                if "data-wf-width" not in a:
                    self.errors.append("[%s] thieu data-wf-width" % bp)
            if bp is None and "data-wf-breakpoint" in a:
                frame = None
        if "data-wf-section" in a:
            name = a["data-wf-section"].strip()
            if frame is None:
                self.errors.append("section '%s' nam ngoai frame" % name)
            else:
                section = name
                sec = self.frames[frame]["sections"].setdefault(
                    name, {"layout": a.get("data-wf-layout", "").strip(),
                           "comps": {}})
                if "data-wf-layout" not in a:
                    self.errors.append("[%s] section '%s' thieu data-wf-layout"
                                       % (frame, name))
        if "data-wf-component" in a:
            label = a["data-wf-component"].strip()
            if frame is None or section is None:
                self.errors.append("component '%s' nam ngoai section/frame"
                                   % label)
            else:
                comps = self.frames[frame]["sections"][section]["comps"]
                if label in comps:
                    self.errors.append("[%s] section '%s' trung component '%s'"
                                       % (frame, section, label))
                else:
                    comps[label] = {"states": norm_set(a.get("data-wf-states", "")),
                                    "effect": norm_set(a.get("data-wf-effect", "")),
                                    "reduced": (a.get("data-wf-reduced", "") or "").strip(),
                                    "visible_on": norm_set(a.get("data-wf-visible-on", ""))}
                    self.text.setdefault((frame, section, label), "")
        self.stack.append((tag, frame, section, label))

    def handle_endtag(self, tag):
        if self.stack:
            self.stack.pop()

    def handle_data(self, data):
        cur = self._cur()
        if cur is not None:
            self.text[cur] = self.text.get(cur, "") + data


def norm_text(value):
    return " ".join((value or "").split())


def load_data(tree_path, data_path, tree):
    """Returns (data_values_dict, fails). Values: label -> [strings]."""
    if data_path is None:
        if tree_path.endswith("-tree.md"):
            data_path = tree_path[:-len("-tree.md")] + "-data.json"
        elif os.path.basename(tree_path) == "tree.md":
            data_path = os.path.join(os.path.dirname(tree_path) or ".",
                                     "data.json")
        else:
            return None, ["khong xac dinh duoc data file cho '%s' "
                          "(dat ten <slug>-tree.md)" % tree_path]
    try:
        with open(data_path, encoding="utf-8") as f:
            raw = json.load(f)
    except FileNotFoundError:
        return None, ["thieu data file: %s" % data_path]
    except ValueError as e:
        return None, ["data file loi JSON (%s): %s" % (data_path, e)]
    if not isinstance(raw, dict) or not isinstance(raw.get("values"), dict) \
            or not raw["values"]:
        return None, ["data file '%s' thieu object 'values' khong rong"
                       % data_path]
    if raw.get("page", "") != tree["page"]:
        return None, ["data file page '%s' != tree page '%s'"
                       % (raw.get("page", ""), tree["page"])]
    values = {}
    for label, v in raw["values"].items():
        items = v if isinstance(v, list) else [v]
        if not all(isinstance(x, str) and x.strip() for x in items) \
                or not items:
            return None, ["data key '%s' phai la chuoi / mang chuoi khong rong"
                           % label]
        values[label] = [x.strip() for x in items]
    return values, []


def verify(tree_path, html_path, data_path=None):
    fails = []
    try:
        tree = parse(tree_path)
    except FileNotFoundError:
        return ["file not found: %s" % tree_path]
    except TreeError as e:
        return ["tree.md khong PASS check.py: %s" % e]
    data, data_fails = load_data(tree_path, data_path, tree)
    fails.extend(data_fails)
    if data is not None:
        tree_labels = {c["label"] for _, _, comps in tree["sections"]
                       for c in comps}
        for label in sorted(set(tree_labels) - set(data)):
            fails.append("thieu data cho component '%s'" % label)
        for label in sorted(set(data) - tree_labels):
            fails.append("data thua key '%s' (khong co trong tree)" % label)
    try:
        with open(html_path, encoding="utf-8") as f:
            src = f.read()
    except FileNotFoundError:
        return ["file not found: %s" % html_path]
    doc = PairHTML()
    doc.feed(src)
    fails.extend(doc.errors)
    if tree["page"] not in doc.pages:
        fails.append("thieu data-wf-page='%s'" % tree["page"])
    if len(doc.pages) > 1:
        fails.append("nhieu data-wf-page khac nhau: %s"
                      % ", ".join(sorted(doc.pages)))
    for bp in BREAKPOINTS:
        if bp not in doc.frames:
            fails.append("thieu frame breakpoint '%s'" % bp)
            continue
        if doc.frames[bp]["width"] != str(WIDTHS[bp]):
            fails.append("[%s] data-wf-width '%s' != chuan %d"
                         % (bp, doc.frames[bp]["width"], WIDTHS[bp]))
    if fails:
        return fails
    for bp in BREAKPOINTS:
        got_sections = doc.frames[bp]["sections"]
        for name, meta, comps in tree["sections"]:
            hidden_sec = bp in meta["hide"]
            if hidden_sec:
                if name in got_sections:
                    fails.append("[%s] section '%s' bi hide nhung van xuat hien"
                                 % (bp, name))
                continue
            if name not in got_sections:
                fails.append("[%s] thieu section '%s'" % (bp, name))
                continue
            want_layout = eff_layout(meta, bp)
            got_layout = got_sections[name]["layout"]
            if got_layout != want_layout:
                fails.append("[%s] section '%s' layout '%s' != khai '%s'"
                             % (bp, name, got_layout, want_layout))
            want = {c["label"]: c for c in comps if bp not in c["hide"]}
            got = got_sections[name]["comps"]
            for label in want:
                if label not in got:
                    fails.append("[%s] section '%s' thieu component '%s'"
                                 % (bp, name, label))
            for label in got:
                if label not in want:
                    tree_labels = {c["label"] for c in comps}
                    if label in tree_labels:
                        fails.append("[%s] section '%s' component '%s' bi hide "
                                     "nhung van xuat hien" % (bp, name, label))
                    else:
                        fails.append("[%s] section '%s' thua component '%s'"
                                     % (bp, name, label))
            for label in want:
                if label not in got:
                    continue
                if set(want[label]["states"]) != got[label]["states"]:
                    fails.append("[%s] section '%s' component '%s' states %s != "
                                 "khai %s" % (bp, name, label,
                                              sorted(got[label]["states"]),
                                              want[label]["states"]))
                if want[label]["effect"] != got[label]["effect"]:
                    fails.append("[%s] section '%s' component '%s' effect %s != "
                                 "khai %s" % (bp, name, label,
                                              sorted(got[label]["effect"]),
                                              sorted(want[label]["effect"])))
                want_reduced = want[label].get("reduced", "") or ""
                if want_reduced != (got[label].get("reduced", "") or ""):
                    fails.append("[%s] section '%s' component '%s' reduced '%s' != "
                                 "khai '%s'" % (bp, name, label,
                                                got[label].get("reduced", ""),
                                                want_reduced))
                want_vis = want[label].get("visible_on", set()) or set()
                if want_vis != got[label].get("visible_on", set()):
                    fails.append("[%s] section '%s' component '%s' visible-on %s != "
                                 "khai %s" % (bp, name, label,
                                              sorted(got[label].get("visible_on", set())),
                                              sorted(want_vis)))
                if data is not None and label in data:
                    shown = norm_text(doc.text.get((bp, name, label), ""))
                    for val in data[label]:
                        if norm_text(val) not in shown:
                            fails.append("[%s] section '%s' component '%s' thieu "
                                         "gia tri data '%s' trong HTML"
                                         % (bp, name, label, val))
                    tokens = ([want[label]["type"], label]
                              + list(want[label].get("states", []))
                              + sorted(want[label].get("effect", set()))
                              + sorted(want[label].get("behavior", set())))
                    if want[label].get("reduced"):
                        tokens.append(want[label]["reduced"])
                    tokens += sorted(want[label].get("visible_on", set()))
                    tokens += sorted(want[label].get("req", set()))
                    for tok in tokens:
                        if norm_text(tok) not in shown:
                            fails.append("[%s] section '%s' component '%s' khai "
                                         "'%s' nhung khong hien thi"
                                         % (bp, name, label, tok))
        for name in got_sections:
            if name not in {n for n, _m, _c in tree["sections"]}:
                fails.append("[%s] thua section '%s'" % (bp, name))
    flagged = set()
    for (_bp, _name, label), text in doc.text.items():
        if label not in flagged and PLACEHOLDER_RE.search(norm_text(text)):
            flagged.add(label)
            fails.append("placeholder trong block '%s' (viet noi dung that, "
                         "cam lorem/xxx/todo)" % label)
    if data is not None:
        for label, vals in data.items():
            for v in vals:
                if (label, v) not in flagged and PLACEHOLDER_RE.search(
                        norm_text(v)):
                    flagged.add((label, v))
                    fails.append("placeholder trong data '%s' (viet noi dung "
                                 "that, cam lorem/xxx/todo)" % label)
    return fails


def main(argv):
    if len(argv) < 3 or "-h" in argv or "--help" in argv:
        print("usage: python3 verify-pair.py <tree.md> <wireframe.html> [data.json]")
        print("  data.json defaults to the tree's sibling <slug>-data.json")
        return 2
    data_arg = argv[3] if len(argv) > 3 else None
    fails = verify(argv[1], argv[2], data_arg)
    if fails:
        for f in fails:
            print("FAIL: %s" % f)
        return 1
    try:
        tree = parse(argv[1])
    except (FileNotFoundError, TreeError) as e:  # pragma: no cover
        print("FAIL: %s" % e)
        return 1
    nsec = len(tree["sections"])
    ncomp = sum(len(c) for _, _, c in tree["sections"])
    print("PASS: pair '%s' \u00b7 4 breakpoints \u00b7 %d sections \u00b7 %d "
          "components (tree<->wireframe<->data khop)" % (tree["page"], nsec, ncomp))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
