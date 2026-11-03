#!/usr/bin/env python3
"""Validate a wireframe-docs tree.md against convention/tree-format.md.

Usage:
    python3 check.py <tree.md>

Exit 0 + report line when valid; exit 1 with error lines when invalid.
check.py is standalone (stdlib only, no sibling imports) and validates ONLY
the tree definition. It never renders wireframes: the hand-authored
wireframe.html is checked against the tree separately by verify-pair.py.
"""
import os
import re
import sys

BREAKPOINTS = ("sm", "md", "lg", "xl")
WIDTHS = {"sm": 360, "md": 768, "lg": 1366, "xl": 1920}
LAYOUTS = ("stack", "grid-2", "grid-3", "grid-4", "sidebar-left", "sidebar-right")
SECTION_KEYS = {"layout", "layout-sm", "layout-md", "layout-lg", "layout-xl", "hide"}
COMP_KEYS = {"note", "states", "effect", "reduced", "ref", "behavior",
             "span", "span-sm", "span-md", "span-lg", "span-xl", "hide"}
BEHAVIORS = {"dialog", "drawer", "sheet", "popover", "menu", "menubar",
             "tabs", "accordion", "pagination", "carousel", "toast",
             "tooltip", "dropdown", "sticky"}
REDUCED = {"instant", "none"}
CUSTOM_FX = re.compile(r"^[a-z0-9-]+$")
URL = re.compile(r"^https?://\S+$")
CONVENTION_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "..", "convention")


class TreeError(Exception):
    pass


def read_block(path, marker):
    """Extract names from a fenced machine block (one entry per line)."""
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        raise TreeError("khong doc duoc %s (nguon that bi mat)" % path)
    m = re.search(r"```%s\n(.*?)```" % re.escape(marker), text, re.S)
    if not m:
        raise TreeError("%s thieu khoi ```%s (nguon that hong)" % (path, marker))
    return [ln.strip() for ln in m.group(1).splitlines() if ln.strip()]


def load_vocab():
    names = read_block(os.path.join(CONVENTION_DIR, "component-roles.md"),
                       "type-vocab")
    if len(names) < 10:
        raise TreeError("type-vocab qua it (%d) — file co van de" % len(names))
    return set(names)


def load_effects():
    specs = {}
    for ln in read_block(os.path.join(CONVENTION_DIR, "animations.md"),
                         "anim-catalog"):
        if ":" not in ln:
            raise TreeError("anim-catalog dong sai dinh dang: '%s'" % ln)
        name, spec = ln.split(":", 1)
        specs[name.strip()] = spec.strip()
    if len(specs) < 5:
        raise TreeError("anim-catalog qua it (%d) — file co van de" % len(specs))
    return specs


TYPE_VOCAB = load_vocab()
EFFECTS = load_effects()


def parse_kv(meta, allowed, where):
    kv = {}
    if not meta:
        return kv
    for part in meta.split("|"):
        part = part.strip()
        if not part:
            continue
        if ":" not in part:
            raise TreeError("%s: metadata '%s' thieu dau ':' (dang key: value)"
                            % (where, part))
        k, v = part.split(":", 1)
        k, v = k.strip().lower(), v.strip()
        if k not in allowed:
            raise TreeError("%s: khoa '%s' khong hop le (cho phep: %s)"
                            % (where, k, ", ".join(sorted(allowed))))
        kv[k] = v
    return kv


def check_behavior(meta, where):
    if "behavior" in meta:
        for b in meta["behavior"].split(","):
            b = b.strip()
            if b not in BEHAVIORS:
                raise TreeError("%s: behavior '%s' khong hop le (chi nhan: %s)"
                                % (where, b, ", ".join(sorted(BEHAVIORS))))


def check_effects(meta, where):
    fx = {s for s in (meta.get("effect", "").split(","))
          if s.strip()}
    fx = {s.strip() for s in fx}
    if not fx:
        return set()
    custom = fx - set(EFFECTS)
    for c in custom:
        if not CUSTOM_FX.match(c):
            raise TreeError("%s: effect tu dat '%s' sai dinh dang "
                            "(chi a-z0-9-gach-ngang)" % (where, c))
    if custom and "ref" not in meta:
        raise TreeError("%s: effect ngoai catalog %s thieu 'ref:' link nguon"
                        % (where, sorted(custom)))
    if not custom and "ref" in meta:
        raise TreeError("%s: 'ref:' thua (effect %s da co trong catalog)"
                        % (where, sorted(fx)))
    if "ref" in meta and not URL.match(meta["ref"].strip()):
        raise TreeError("%s: ref '%s' khong phai URL http(s)"
                        % (where, meta["ref"]))
    non_focus = {f for f in fx if f != "focus-ring"}
    if non_focus:
        r = meta.get("reduced", "").strip()
        if r not in REDUCED:
            raise TreeError("%s: co effect %s thi 'reduced:' bat buoc "
                            "(chi nhan: %s)" % (where, sorted(non_focus),
                                                ", ".join(sorted(REDUCED))))
    return fx


def check_vocab(ctype, where):
    if ctype not in TYPE_VOCAB:
        raise TreeError("%s: Kieu '%s' ngoai von shadcn pin "
                        "(xem convention/component-roles.md)" % (where, ctype))


def check_hide(value, where):
    hidden = set()
    if not value:
        return hidden
    for b in value.split(","):
        b = b.strip()
        if b not in BREAKPOINTS:
            raise TreeError("%s: hide '%s' khong hop le (chi nhan: %s)"
                            % (where, b, ", ".join(BREAKPOINTS)))
        hidden.add(b)
    return hidden


def check_layouts(meta, where):
    for k in ("layout", "layout-sm", "layout-md", "layout-lg", "layout-xl"):
        if k in meta and meta[k] not in LAYOUTS:
            raise TreeError("%s: %s '%s' khong hop le (chi nhan: %s)"
                            % (where, k, meta[k], ", ".join(LAYOUTS)))


def check_spans(meta, where):
    for k in ("span", "span-sm", "span-md", "span-lg", "span-xl"):
        if k in meta:
            try:
                n = int(meta[k])
            except ValueError:
                raise TreeError("%s: %s '%s' phai la so nguyen >= 1"
                                % (where, k, meta[k]))
            if n < 1:
                raise TreeError("%s: %s '%s' phai la so nguyen >= 1"
                                % (where, k, meta[k]))


def eff_value(meta, base_key, bp):
    """Mobile-first resolution: span-{bp} falls back down to the base key."""
    order = ["sm", "md", "lg", "xl"]
    keys = [base_key] + ["%s-%s" % (base_key, b) for b in order]
    idx = order.index(bp) + 1
    val = None
    for k in keys[:idx + 1]:
        if k in meta:
            val = meta[k]
    return val


def eff_layout(section_meta, bp):
    return eff_value(section_meta, "layout", bp) or "stack"


def eff_span(comp_meta, bp):
    return int(eff_value(comp_meta, "span", bp) or 1)


def parse_states(value):
    return [s.strip() for s in value.split(",") if s.strip()] or ["default"]


def parse_set(value):
    return set(s.strip() for s in value.split(",") if s.strip())


def parse(path):
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    page = None
    page_note = ""
    sections = []  # [(name, meta, [comp, ...])]
    cur = None
    for raw in lines:
        line = raw.strip()
        m = re.match(r"^# Page:\s*(.+?)\s*$", line)
        if m:
            if page is not None:
                raise TreeError("hon 1 dong '# Page:'")
            page = m.group(1).strip()
            continue
        if page is not None and not sections and not page_note:
            m = re.match(r"^>\s*(.*)$", line)
            if m and m.group(1).strip():
                page_note = m.group(1).strip()
                continue
        m = re.match(r"^## Section:\s*(.+?)\s*(?:\u2014\s*(.*))?$", line)
        if m:
            name, meta_raw = m.group(1).strip(), (m.group(2) or "").strip()
            where = "section '%s'" % name
            meta = parse_kv(meta_raw, SECTION_KEYS, where)
            check_layouts(meta, where)
            meta["hide"] = check_hide(meta.get("hide", ""), where)
            cur = (name, meta, [])
            sections.append(cur)
            continue
        m = re.match(r"^-\s+`([^`]+)`\s+\*\*([^*]+)\*\*\s*(?:\u2014\s*(.*))?$", line)
        if m:
            if cur is None:
                raise TreeError("component truoc moi '## Section:'")
            ctype, label = m.group(1).strip(), m.group(2).strip()
            meta_raw = (m.group(3) or "").strip()
            where = "component '%s'" % label
            meta = parse_kv(meta_raw, COMP_KEYS, where)
            check_spans(meta, where)
            check_vocab(ctype, where)
            check_behavior(meta, where)
            fx = check_effects(meta, where)
            comp = {
                "type": ctype,
                "label": label,
                "note": meta.get("note", ""),
                "states": parse_states(meta.get("states", "default")),
                "effect": fx,
                "reduced": meta.get("reduced", "").strip(),
                "behavior": {b.strip() for b in meta.get("behavior", "").split(",") if b.strip()},
                "hide": check_hide(meta.get("hide", ""), where),
                "span": meta,
            }
            cur[2].append(comp)
            continue
    if page is None:
        raise TreeError("thieu '# Page:'")
    if not sections:
        raise TreeError("khong co '## Section:'")
    for name, _meta, comps in sections:
        if not comps:
            raise TreeError("section '%s' khong co component" % name)
    return {"page": page, "note": page_note, "sections": sections}


def main(argv):
    if len(argv) < 2 or "-h" in argv or "--help" in argv:
        print("usage: python3 check.py <tree.md>")
        return 2
    try:
        doc = parse(argv[1])
    except FileNotFoundError:
        print("FAIL: file not found: %s" % argv[1])
        return 1
    except TreeError as e:
        print("FAIL: %s" % e)
        return 1
    nsec = len(doc["sections"])
    ncomp = sum(len(c) for _, _, c in doc["sections"])
    types = sorted({c["type"] for _, _, comps in doc["sections"] for c in comps})
    print("PASS: page '%s' \u00b7 %d sections \u00b7 %d components \u00b7 types: %s"
          % (doc["page"], nsec, ncomp, ", ".join(types)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
