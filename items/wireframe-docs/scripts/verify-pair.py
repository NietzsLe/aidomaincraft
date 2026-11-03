#!/usr/bin/env python3
"""Verify a wireframe-docs tree.md <-> wireframe.html pair.

Usage:
    python3 verify-pair.py <tree.md> <wireframe.html>

The tree only defines scope; the wireframe is hand-authored (one file,
four breakpoint frames). This script reports every drift between the two
so the designer can rule on it. It never fixes anything by itself.

Exit 0 + PASS line when the pair matches; exit 1 + FAIL lines otherwise.
FAIL classes: missing frame/section/component, extra section/component,
layout/states/effect mismatch, unknown breakpoint, bad width, structural
errors (section outside a frame, component outside a section, duplicates).
"""
import os
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


def norm_set(value):
    return set(s.strip() for s in (value or "").split(",") if s.strip())


class PairHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []  # [(tag, frame_bp_or_None, section_or_None)]
        self.pages = set()
        self.frames = {}  # bp -> {"width": str|None, "sections": {...}}
        self.errors = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        parent_frame = self.stack[-1][1] if self.stack else None
        parent_section = self.stack[-1][2] if self.stack else None
        frame = parent_frame
        section = parent_section
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
                                    "effect": norm_set(a.get("data-wf-effect", ""))}
        self.stack.append((tag, frame, section))

    def handle_endtag(self, tag):
        if self.stack:
            self.stack.pop()


def verify(tree_path, html_path):
    fails = []
    try:
        tree = parse(tree_path)
    except FileNotFoundError:
        return ["file not found: %s" % tree_path]
    except TreeError as e:
        return ["tree.md khong PASS check.py: %s" % e]
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
        for name in got_sections:
            if name not in {n for n, _m, _c in tree["sections"]}:
                fails.append("[%s] thua section '%s'" % (bp, name))
    return fails


def main(argv):
    if len(argv) < 3 or "-h" in argv or "--help" in argv:
        print("usage: python3 verify-pair.py <tree.md> <wireframe.html>")
        return 2
    fails = verify(argv[1], argv[2])
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
          "components (tree<->wireframe khop)" % (tree["page"], nsec, ncomp))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
