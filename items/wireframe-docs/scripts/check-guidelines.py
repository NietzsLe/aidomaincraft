#!/usr/bin/env python3
"""Evaluate a wireframe-docs tree (+data) against web-interface-guidelines.

Usage:
    python3 check-guidelines.py <tree.md> [data.json]

Reads the same tree.md + <slug>-data.json the pair uses, maps each
component type to its WAI-ARIA role (convention/component-roles.md), and
reports every applicable guidelines rule as PASS/FAIL/WARN/na with
evidence (tree.md line context comes from labels/sections).

FAIL rules block (exit 1); WARNs only advise. na rules are listed with
the reason they need real code, not a wireframe.

Exit 0 + SCORE line when no FAIL; exit 1 otherwise.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check import TreeError, parse, read_block  # noqa: E402

CONVENTION_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "..", "convention")
INTERACTIVE_ROLES = {"button", "checkbox", "switch", "textbox", "searchbox",
                     "combobox", "listbox", "menu", "menubar", "menuitem",
                     "menuitemcheckbox", "menuitemradio", "option", "radio",
                     "radiogroup", "slider", "spinbutton", "tab", "tablist",
                     "tree", "treegrid", "grid", "dialog", "alertdialog"}
PRIMITIVES = {"Section", "Grid", "Stack", "Container"}
PLACEHOLDER = re.compile(r"^(todo|tbd|xxx|\.\.\.|lorem|test|label\d*)$", re.I)
MONEY = re.compile(r"[₫$€]\s*\d|\d\s*[₫$€%]|\b\d{1,3}(,\d{3})+\b")
TRIGGER_NEEDS = {"hover": {"hover"}, "focus": {"focus"},
                 "open": {"open", "expanded", "selected"},
                 "show": {"show", "open", "visible"},
                 "expand": {"expanded", "open"}}
NA_RULES = [
    ("G-contrast", "can mau nen/chu that (chi do duoc tren render mau)"),
    ("G-darkmode", "can color-scheme/meta theme-color o code that"),
    ("G-touch-px", "hit target px khong mo hinh hoa trong wireframe"),
    ("G-virtualize", "virtualize list la quyet dinh code (>50 items that)"),
    ("G-preconnect", "link preconnect thuoc build, khong phai wireframe"),
    ("G-headings", "thu tu section ngam dinh h1-h6, code quyet dinh cuoi"),
    ("G-skiplink", "skip link la chi tiet code"),
    ("G-autocomplete", "autocomplete/type/inputmode khai o code that"),
]

EFFECT_CATALOG = {}


def load_roles():
    roles = {}
    for ln in read_block(os.path.join(CONVENTION_DIR, "component-roles.md"),
                         "role-map"):
        if ":" not in ln:
            raise TreeError("role-map dong sai dinh dang: '%s'" % ln)
        name, role = ln.split(":", 1)
        roles[name.strip()] = role.strip().lower()
    if len(roles) < 10:
        raise TreeError("role-map qua it (%d) — file co van de" % len(roles))
    return roles


def load_effects():
    specs = {}
    for ln in read_block(os.path.join(CONVENTION_DIR, "animations.md"),
                         "anim-catalog"):
        name, spec = ln.split(":", 1)
        specs[name.strip()] = spec.strip()
    return specs


def is_interactive(ctype, roles):
    if ctype in PRIMITIVES:
        return False
    return roles.get(ctype, "generic") in INTERACTIVE_ROLES


def main(argv):
    if len(argv) < 2 or "-h" in argv or "--help" in argv:
        print("usage: python3 check-guidelines.py <tree.md> [data.json]")
        print("  data.json defaults to the tree's sibling <slug>-data.json")
        return 2
    try:
        roles = load_roles()
        effects = load_effects()
        doc = parse(argv[1])
    except (FileNotFoundError, TreeError) as e:
        print("FAIL: %s" % e)
        return 1
    data_arg = argv[2] if len(argv) > 2 else None
    if data_arg is None:
        if argv[1].endswith("-tree.md"):
            data_arg = argv[1][:-len("-tree.md")] + "-data.json"
        elif os.path.basename(argv[1]) == "tree.md":
            data_arg = os.path.join(os.path.dirname(argv[1]) or ".",
                                    "data.json")
        else:
            data_arg = argv[1] + ".data.json"
    fails, warns = [], []
    comps = []
    for name, _meta, cs in doc["sections"]:
        for c in cs:
            comps.append((name, c))

    # G-data: data file exists, valid, non-empty values
    data = None
    try:
        with open(data_arg, encoding="utf-8") as f:
            raw = json.load(f)
        if isinstance(raw, dict) and isinstance(raw.get("values"), dict) \
                and raw["values"]:
            data = raw["values"]
            print("PASS G-data: data file %s hop le (%d keys)"
                  % (data_arg, len(data)))
        else:
            fails.append("G-data: '%s' thieu object 'values' khong rong"
                         % data_arg)
    except FileNotFoundError:
        fails.append("G-data: thieu data file %s" % data_arg)
    except ValueError as e:
        fails.append("G-data: loi JSON %s: %s" % (data_arg, e))

    # G-labels / G-focus / W-notes over interactive components
    for sec, c in comps:
        if not is_interactive(c["type"], roles):
            continue
        where = "[%s] '%s'" % (sec, c["label"])
        if PLACEHOLDER.match(c["label"].strip()):
            fails.append("G-labels %s: nhan placeholder — can nhan that" % where)
        if "focus" not in [s.strip() for s in c["states"]]:
            fails.append("G-focus %s: interactive thieu state 'focus'" % where)
        if not c["note"].strip():
            warns.append("W-notes %s: thieu note (ban phim/focus/hit target "
                         "dinh khai gi?)" % where)

    # G-motion: effect (tru focus-ring) doi reduced
    for sec, c in comps:
        fx = set(c["effect"]) - {"focus-ring"}
        if fx and c.get("reduced", "") not in ("instant", "none"):
            fails.append("G-motion [%s] '%s': effect %s thieu reduced: "
                         "instant|none" % (sec, c["label"], sorted(fx)))

    # G-alt: Avatar/Chart can alt trong note
    for sec, c in comps:
        if c["type"] in ("Avatar", "Chart") and "alt" not in c["note"].lower():
            fails.append("G-alt [%s] '%s': %s can note chua 'alt' mo ta anh"
                         % (sec, c["label"], c["type"]))

    # G-ellipsis + W-numbers over data values
    if data is not None:
        for label, v in data.items():
            vals = v if isinstance(v, list) else [v]
            for x in vals:
                if not isinstance(x, str):
                    continue
                if "..." in x:
                    fails.append("G-ellipsis '%s': dung '...' — phai la '…'"
                                 % label)
                if MONEY.search(x):
                    warns.append("W-numbers '%s': so/tien '%s' — nho Intl.* "
                                 "khi build" % (label, x.strip()[:40]))

    # W-trigger: effect can state kich hoat tuong ung
    for sec, c in comps:
        for f in c["effect"]:
            spec = effects.get(f, "")
            m = re.search(r"\bon\s+(\w+)", spec)
            if m and m.group(1) in TRIGGER_NEEDS:
                need = TRIGGER_NEEDS[m.group(1)]
                if not (need & set(c["states"])):
                    warns.append("W-trigger [%s] '%s': effect '%s' on %s "
                                 "nhung states %s thieu %s"
                                 % (sec, c["label"], f, m.group(1),
                                    c["states"], sorted(need)))

    # na rules, always listed
    for rid, why in NA_RULES:
        print("na %s: %s" % (rid, why))

    npass = 6 - len({f.split()[0] for f in fails})
    for f in fails:
        print("FAIL: %s" % f)
    for w in warns:
        print("WARN: %s" % w)
    print("SCORE: %d/6 applicable rules pass (%d WARN)" % (npass, len(warns)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
