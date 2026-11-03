#!/usr/bin/env python3
"""Validate a wireframe-docs tree.md against convention/tree-format.md.

Usage:
    python3 check.py <tree.md>

Exit 0 + report line when valid; exit 1 with error lines when invalid.
"""
import sys

sys.path.insert(0, __import__("os").path.dirname(__file__))
from build import parse  # noqa: E402


def main(argv):
    if len(argv) < 2 or "-h" in argv or "--help" in argv:
        print("usage: python3 check.py <tree.md>")
        return 2
    try:
        doc = parse(argv[1])
    except FileNotFoundError:
        print("FAIL: file not found: %s" % argv[1])
        return 1
    if doc is None:
        print("FAIL: see errors above")
        return 1
    nsec = len(doc["sections"])
    ncomp = sum(len(c) for _, c in doc["sections"])
    types = sorted({c["type"] for _, comps in doc["sections"] for c in comps})
    print("PASS: page '%s' · %d sections · %d components · types: %s"
          % (doc["page"], nsec, ncomp, ", ".join(types)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
