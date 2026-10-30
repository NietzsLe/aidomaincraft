#!/usr/bin/env python3
"""Install, uninstall, and inspect aidomaincraft lookup blocks in a target.

Design goals (mirrors agent-relay-logs, but lookup-only):
- Touch only AGENTS.md, CLAUDE.md, .gitignore and .aidomaincraft/ in the target.
- Never overwrite a whole file: insert/replace one marker block.
- Be idempotent: running install/uninstall twice is safe.
- Default install is reference-only (no vendored docs). --vendor adds an
  offline snapshot under .aidomaincraft/ (git-ignored).
- Versioned on 3 axes: installer version, template block vN, source CHARTER vN.
  `version` prints all three, `check-update` compares installed vs template
  (+ optional remote tag check), `upgrade` re-runs install in one command.
- Dependency-free (Python 3 standard library only).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

INSTALLER_VERSION = "1.1.0"
REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = REPO_ROOT / "templates"

DEFAULT_SOURCE = "https://github.com/NietzsLe/aidomaincraft.git"
DEFAULT_REF = "main"

BEGIN = "<!-- BEGIN aidomaincraft -->"
END = "<!-- END aidomaincraft -->"
BLOCK_RE = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.S)
BLOCK_STAMP_RE = re.compile(r"aidomaincraft\s+(\S+)\s+v(\d+)")
MANIFEST_NAME = "install.json"
VENDOR_DIR = ".aidomaincraft"
GITIGNORE_ENTRIES = {".aidomaincraft", ".aidomaincraft/"}
TARGET_FILES = (
    ("AGENTS.md", "agents-block.md", "--skip-agents"),
    ("CLAUDE.md", "claude-block.md", "--skip-claude"),
)
VENDOR_COPY = ("CHARTER.md", "README.md", "VERIFY.md", "CHANGELOG.md", "domains", "items")


class SetupError(RuntimeError):
    pass


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def stamp():
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


def say(msg, quiet=False):
    if not quiet:
        print(msg)


def fail(msg):
    raise SetupError(msg)


def target_path(value):
    p = Path(value).expanduser().resolve()
    if not p.is_dir():
        fail("target is not a directory: %s" % p)
    return p


def read_text(path):
    raw = path.read_bytes()
    bom = raw.startswith(b"\xef\xbb\xbf")
    if bom:
        raw = raw[3:]
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as ex:
        fail("cannot read %s as UTF-8: %s" % (path, ex))
    crlf = "\r\n" in text
    return text.replace("\r\n", "\n").replace("\r", "\n"), crlf, bom


def write_text(path, text, crlf=False, bom=False, backup=False):
    data = text.replace("\n", "\r\n") if crlf else text
    raw = data.encode("utf-8")
    if bom:
        raw = b"\xef\xbb\xbf" + raw
    if backup and path.exists():
        dst = path.with_name(path.name + ".aidomaincraft-backup-" + stamp())
        n = 1
        while dst.exists():
            dst = path.with_name(path.name + ".aidomaincraft-backup-%s-%d" % (stamp(), n))
            n += 1
        shutil.copy2(path, dst)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".aidomaincraft-", dir=str(path.parent))
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(raw)
        if path.exists():
            os.chmod(tmp, path.stat().st_mode & 0o777)
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def template_block_version(name):
    path = TEMPLATES / name
    if not path.is_file():
        fail("missing template: %s" % path)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as ex:
        fail("cannot read template %s: %s" % (path, ex))
    m = BLOCK_STAMP_RE.search(text)
    if not m:
        fail("template %s has no version stamp (expected '<!-- aidomaincraft <name> vN -->')" % name)
    return int(m.group(2))


def installed_block_version(text):
    m = BLOCK_STAMP_RE.search(text)
    return int(m.group(2)) if m else None


def charter_version(root=None):
    """CHARTER vN of a source checkout (None when unreadable)."""
    path = (root or REPO_ROOT) / "CHARTER.md"
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    m = re.search(r"CHARTER\.md — aidomaincraft — v(\d+)", text)
    return int(m.group(1)) if m else None


def remote_latest_tag(source, timeout=10):
    """Highest vN tag on a git remote. Returns (tag, None) or (None, reason)."""
    if Path(source).expanduser().is_dir():
        return None, "local source (no remote check)"
    try:
        proc = subprocess.run(["git", "ls-remote", "--tags", source, "refs/tags/v*"],
                              capture_output=True, text=True, timeout=timeout)
    except FileNotFoundError:
        return None, "git not found"
    except subprocess.TimeoutExpired:
        return None, "timeout"
    except OSError as ex:
        return None, str(ex)
    if proc.returncode != 0:
        return None, "ls-remote failed (offline?)"
    best = None
    for line in proc.stdout.splitlines():
        parts = line.split()
        if len(parts) != 2:
            continue
        ref = parts[1].replace("refs/tags/", "").replace("^{}", "")
        m = re.fullmatch(r"v(\d+)", ref)
        if m and (best is None or int(m.group(1)) > best[0]):
            best = (int(m.group(1)), ref)
    if best is None:
        return None, "no vN tags found"
    return best[1], None


def render_block(name, source, ref):
    path = TEMPLATES / name
    if not path.is_file():
        fail("missing template: %s" % path)
    text, _, _ = read_text(path)
    text = text.strip() + "\n"
    if source != DEFAULT_SOURCE:
        text = text.replace(DEFAULT_SOURCE, source)
    if ref != DEFAULT_REF:
        text = text.replace("--branch %s" % DEFAULT_REF, "--branch %s" % ref)
        text = text.replace("(ref `%s`)" % DEFAULT_REF, "(ref `%s`)" % ref)
    return text


def upsert_block(path, block, dry_run, backup, header, template_version=None):
    new_block = block.strip()
    if path.exists():
        text, crlf, bom = read_text(path)
        begins, ends = text.count(BEGIN), text.count(END)
        if begins != ends:
            fail("%s has unbalanced aidomaincraft markers (%d BEGIN, %d END); fix it manually" % (path, begins, ends))
        if begins:
            old_v = installed_block_version(text)
            old_label = ("v%d" % old_v) if old_v is not None else "unversioned"
            new_label = ("v%d" % template_version) if template_version is not None else "template"
            state = {"first": True, "identical": True}

            def repl(match):
                if state["first"]:
                    state["first"] = False
                    if match.group(0).strip() != new_block:
                        state["identical"] = False
                    return new_block
                state["identical"] = False
                return ""

            new, count = BLOCK_RE.subn(repl, text)
            if state["identical"] and count == 1:
                return "unchanged (already %s)" % new_label
            if not dry_run:
                write_text(path, new, crlf, bom, backup)
            if count == 1:
                return "updated (%s -> %s)" % (old_label, new_label)
            return "updated (%s -> %s; removed %d duplicate block(s))" % (old_label, new_label, count - 1)
        base = text.rstrip()
        new = (base + "\n\n" if base else "") + new_block + "\n"
        action = "added"
        if not dry_run:
            write_text(path, new, crlf, bom, backup)
        return action
    if not dry_run:
        write_text(path, header + "\n\n" + new_block + "\n", backup=backup)
    return "created"


def remove_block(path, dry_run, backup):
    if not path.exists():
        return "missing"
    text, crlf, bom = read_text(path)
    begins, ends = text.count(BEGIN), text.count(END)
    if begins != ends:
        fail("%s has unbalanced aidomaincraft markers (%d BEGIN, %d END); fix it manually" % (path, begins, ends))
    if begins == 0:
        return "no block"
    new, count = BLOCK_RE.subn("", text)
    new = re.sub(r"\n{3,}", "\n\n", new)
    new = (new.rstrip() + "\n") if new.strip() else ""
    if not dry_run:
        write_text(path, new, crlf, bom, backup)
    return "removed %d block(s)" % count


def ensure_gitignore(target, dry_run):
    path = target / ".gitignore"
    if path.exists():
        text, crlf, bom = read_text(path)
        if any(line.strip() in GITIGNORE_ENTRIES for line in text.splitlines()):
            return False, False, "already present"
        base = text.rstrip()
        new = (base + "\n" if base else "") + ".aidomaincraft/\n"
        if not dry_run:
            write_text(path, new, crlf, bom)
        return True, False, "added .aidomaincraft/"
    if not dry_run:
        write_text(path, ".aidomaincraft/\n")
    return True, True, "created with .aidomaincraft/"


def remove_gitignore(target, manifest, dry_run):
    path = target / ".gitignore"
    if not path.exists():
        return "missing"
    if manifest.get("gitignore_added") is False:
        return "kept (not added by aidomaincraft)"
    text, crlf, bom = read_text(path)
    lines = text.splitlines()
    kept = [line for line in lines if line.strip() not in GITIGNORE_ENTRIES]
    if len(kept) == len(lines):
        return "no .aidomaincraft/ line"
    new = "\n".join(kept)
    new = (new.rstrip() + "\n") if new.strip() else ""
    if not dry_run:
        write_text(path, new, crlf, bom)
    if manifest.get("gitignore_created") and not new.strip():
        if not dry_run:
            path.unlink()
        return "removed .aidomaincraft/ line and deleted empty .gitignore"
    return "removed .aidomaincraft/ line"


def load_manifest(target):
    path = target / VENDOR_DIR / MANIFEST_NAME
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def save_manifest(target, data, dry_run):
    if dry_run:
        return
    d = target / VENDOR_DIR
    d.mkdir(parents=True, exist_ok=True)
    path = d / MANIFEST_NAME
    tmp = path.with_name(path.name + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    os.replace(tmp, path)


def install_vendor(target, source_dir, force, dry_run):
    actions = []
    dest = target / VENDOR_DIR
    if dest.exists() and not dest.is_dir():
        fail("%s exists and is not a directory" % dest)
    for name in VENDOR_COPY:
        src = source_dir / name
        if not src.exists():
            actions.append("%s: missing in source (skipped)" % name)
            continue
        dst = dest / name
        if dst.exists() and not force:
            actions.append("%s: kept existing (use --force to update)" % name)
            continue
        if not dry_run:
            dest.mkdir(parents=True, exist_ok=True)
            if src.is_dir():
                if dst.exists():
                    shutil.rmtree(dst)
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)
        actions.append("%s: %s" % (name, "updated" if dst.exists() and force else "copied"))
    return actions


def cmd_install(args):
    target = target_path(args.target)
    say("aidomaincraft install %s" % INSTALLER_VERSION)
    say("  target: %s" % target)
    say("  source: %s (ref %s)" % (args.source, args.ref))
    say("  mode:   %s" % ("dry-run (no writes)" if args.dry_run else "write"))
    manifest = load_manifest(target) if (target / VENDOR_DIR).exists() else {}
    blocks = []
    created_files = []
    block_versions = dict(manifest.get("block_versions", {}))
    for filename, template, _flag in TARGET_FILES:
        skip = (filename == "AGENTS.md" and args.skip_agents) or (filename == "CLAUDE.md" and args.skip_claude)
        if skip:
            say("  %s: skipped" % filename, args.quiet)
            continue
        path = target / filename
        existed = path.exists()
        if not existed and args.no_create:
            say("  %s: missing (skipped; --no-create)" % filename, args.quiet)
            continue
        tver = template_block_version(template)
        action = upsert_block(path, render_block(template, args.source, args.ref),
                              args.dry_run, args.backup, "# " + filename, template_version=tver)
        say("  %s: %s" % (filename, action), args.quiet)
        blocks.append(filename)
        if not args.dry_run:
            block_versions[filename] = tver
        if not existed:
            created_files.append(filename)
    gi_added, gi_created, gi_msg = False, False, "not needed (reference-only)"
    vendor_actions = []
    if args.vendor:
        if args.no_gitignore:
            gi_msg = "skipped"
        else:
            gi_added, gi_created, gi_msg = ensure_gitignore(target, args.dry_run)
        say("  .gitignore: %s" % gi_msg, args.quiet)
        # Resolve local source dir for snapshot: --source may be a local path.
        src_path = Path(args.source).expanduser()
        if src_path.is_dir():
            source_dir = src_path.resolve()
        else:
            source_dir = REPO_ROOT
        vendor_actions = install_vendor(target, source_dir, args.force, args.dry_run)
        for a in vendor_actions:
            say("  vendor %s" % a, args.quiet)
        if not args.dry_run:
            data = dict(manifest)
            data.update({
                "version": INSTALLER_VERSION,
                "source": args.source,
                "ref": args.ref,
                "last_installed_at": now(),
                "gitignore_added": bool(manifest.get("gitignore_added") or gi_added),
                "gitignore_created": bool(manifest.get("gitignore_created") or gi_created),
                "files": sorted(set(manifest.get("files", [])) | set(blocks)),
                "created_files": sorted(set(manifest.get("created_files", [])) | set(created_files)),
                "block_versions": block_versions,
                "vendor": True,
            })
            data.setdefault("first_installed_at", now())
            save_manifest(target, data, args.dry_run)
            say("  manifest: written", args.quiet)
    else:
        say("  .gitignore: %s" % gi_msg, args.quiet)
        if not args.dry_run and (target / VENDOR_DIR / MANIFEST_NAME).exists():
            # block-only reinstall keeps existing vendor manifest untouched
            pass
    say("")
    if args.dry_run:
        say("dry run complete: no files were written.")
    else:
        cv = charter_version()
        say("versions: installer %s, blocks v%s, source CHARTER %s" % (
            INSTALLER_VERSION,
            max(block_versions.values()) if block_versions else "?",
            ("v%d" % cv) if cv is not None else "?"))
        say("done. Verify with: python3 scripts/aidomaincraft_setup.py doctor --target %s" % target)
        say("Check for updates: python3 scripts/aidomaincraft_setup.py check-update --target %s" % target)
    return 0


def cmd_uninstall(args):
    target = target_path(args.target)
    manifest = load_manifest(target)
    say("aidomaincraft uninstall %s" % INSTALLER_VERSION)
    say("  target: %s" % target)
    say("  mode:   %s" % ("dry-run (no writes)" if args.dry_run else "write"))
    for filename, _template, _flag in TARGET_FILES:
        skip = (filename == "AGENTS.md" and args.skip_agents) or (filename == "CLAUDE.md" and args.skip_claude)
        if skip:
            say("  %s: skipped" % filename, args.quiet)
            continue
        say("  %s: %s" % (filename, remove_block(target / filename, args.dry_run, args.backup)), args.quiet)
    if args.no_gitignore:
        say("  .gitignore: skipped", args.quiet)
    else:
        say("  .gitignore: %s" % remove_gitignore(target, manifest, args.dry_run), args.quiet)
    if not args.dry_run:
        for filename in manifest.get("created_files", []):
            path = target / filename
            if not path.exists():
                continue
            try:
                text, _, _ = read_text(path)
            except SetupError:
                continue
            if text.strip() in ("", "# " + filename):
                path.unlink()
                say("  %s: deleted (created by installer)" % filename, args.quiet)
    vendor_dir = target / VENDOR_DIR
    if args.keep_vendor:
        say("  .aidomaincraft: kept (--keep-vendor)", args.quiet)
    elif not vendor_dir.exists():
        say("  .aidomaincraft: not present", args.quiet)
    elif args.purge:
        if not args.dry_run:
            shutil.rmtree(vendor_dir)
        say("  .aidomaincraft: purged", args.quiet)
    else:
        dest = target / (".aidomaincraft.removed-" + stamp())
        n = 1
        while dest.exists():
            dest = target / (".aidomaincraft.removed-%s-%d" % (stamp(), n))
            n += 1
        if not args.dry_run:
            shutil.move(str(vendor_dir), str(dest))
        say("  .aidomaincraft: moved to %s" % dest.name, args.quiet)
    say("")
    if args.dry_run:
        say("dry run complete: no files were written.")
    else:
        say("done. Review the target's git diff before committing.")
    return 0


def cmd_doctor(args):
    target = target_path(args.target)
    ok = True
    print("aidomaincraft doctor %s" % INSTALLER_VERSION)
    print("target: %s" % target)
    for filename, template, _flag in TARGET_FILES:
        path = target / filename
        if not path.exists():
            print("%s: absent" % filename)
            continue
        text, _, _ = read_text(path)
        begins, ends = text.count(BEGIN), text.count(END)
        status = "ok" if begins == ends == 1 else "PROBLEM"
        print("%s: %d BEGIN / %d END (%s)" % (filename, begins, ends, status))
        if begins != ends or begins > 1:
            ok = False
            continue
        try:
            want = template_block_version(template)
        except SetupError:
            want = None
        have = installed_block_version(text)
        have_label = ("v%d" % have) if have is not None else "unversioned"
        if want is not None and have != want:
            print("%s: block %s installed, template is v%d (outdated)" % (filename, have_label, want))
            print("%s: upgrade with: ./scripts/install.sh --target %s" % (filename, target))
            ok = False
        elif want is not None:
            print("%s: block v%d (up to date)" % (filename, want))
    vendor_dir = target / VENDOR_DIR
    manifest = load_manifest(target)
    if manifest.get("vendor"):
        print(".aidomaincraft: vendor snapshot present (source %s ref %s)" % (manifest.get("source", "?"), manifest.get("ref", "?")))
        if not vendor_dir.is_dir():
            print(".aidomaincraft: PROBLEM (manifest says vendor, dir missing)")
            ok = False
        gitignore = target / ".gitignore"
        if gitignore.exists():
            text, _, _ = read_text(gitignore)
            present = any(line.strip() in GITIGNORE_ENTRIES for line in text.splitlines())
            print(".gitignore: %s" % ("contains .aidomaincraft/" if present else "MISSING .aidomaincraft/"))
            ok = ok and present
        else:
            print(".gitignore: absent (MISSING .aidomaincraft/)")
            ok = False
    else:
        print(".aidomaincraft: reference-only (no vendor snapshot)")
    print("result: %s" % ("OK" if ok else "PROBLEMS FOUND"))
    return 0 if ok else 1


def cmd_version(args):
    target = target_path(args.target)
    print("aidomaincraft version (installer %s)" % INSTALLER_VERSION)
    cv = charter_version()
    print("source CHARTER: %s" % (("v%d" % cv) if cv is not None else "unknown"))
    for _filename, template, _flag in TARGET_FILES:
        try:
            print("template %s: v%d" % (template, template_block_version(template)))
        except SetupError as ex:
            print("template %s: error (%s)" % (template, ex))
    for filename, _template, _flag in TARGET_FILES:
        path = target / filename
        if not path.exists():
            print("%s: absent" % filename)
            continue
        text, _, _ = read_text(path)
        if text.count(BEGIN) != text.count(END) or text.count(BEGIN) == 0:
            print("%s: no valid block" % filename)
            continue
        have = installed_block_version(text)
        print("%s: block %s" % (filename, ("v%d" % have) if have is not None else "unversioned"))
    manifest = load_manifest(target)
    if manifest:
        print("manifest: installer %s, source %s, ref %s, installed %s" % (
            manifest.get("version", "?"), manifest.get("source", "?"),
            manifest.get("ref", "?"), manifest.get("last_installed_at", "?")))
    else:
        print("manifest: none (reference-only or never vendored)")
    return 0


def cmd_check_update(args):
    target = target_path(args.target)
    print("aidomaincraft check-update %s" % INSTALLER_VERSION)
    print("target: %s" % target)
    need = False
    for filename, template, _flag in TARGET_FILES:
        path = target / filename
        if not path.exists():
            print("%s: absent (install first)" % filename)
            need = True
            continue
        text, _, _ = read_text(path)
        if text.count(BEGIN) != text.count(END) or text.count(BEGIN) == 0:
            print("%s: no valid block (reinstall)" % filename)
            need = True
            continue
        try:
            want = template_block_version(template)
        except SetupError:
            want = None
        have = installed_block_version(text)
        if want is not None and have != want:
            print("%s: block v%s installed, template v%d (update available)" % (
                filename, have if have is not None else "?", want))
            need = True
        elif want is not None:
            print("%s: block v%d (up to date)" % (filename, want))
    if args.remote:
        tag, reason = remote_latest_tag(args.source)
        if tag is None:
            print("remote: unknown (%s)" % reason)
        else:
            print("remote: latest tag %s" % tag)
            cv = charter_version()
            if cv is not None and tag != ("v%d" % cv):
                print("remote: source checkout is CHARTER v%d, remote is %s (fetch latest)" % (cv, tag))
                need = True
    if need:
        print("action: ./scripts/install.sh --target %s%s" % (
            target, " --vendor --force" if load_manifest(target).get("vendor") else ""))
        print("result: UPDATE AVAILABLE")
        return 1
    print("result: UP TO DATE")
    return 0


def cmd_upgrade(args):
    target = target_path(args.target)
    manifest = load_manifest(target)
    has_vendor = bool(manifest.get("vendor")) or (target / VENDOR_DIR).is_dir()
    want_vendor = args.vendor or (has_vendor and not args.no_vendor)
    ns = argparse.Namespace(target=str(target), source=args.source, ref=args.ref,
                            vendor=want_vendor, force=True, dry_run=args.dry_run,
                            backup=args.backup, skip_agents=args.skip_agents,
                            skip_claude=args.skip_claude, no_create=args.no_create,
                            no_gitignore=args.no_gitignore, quiet=args.quiet)
    say("aidomaincraft upgrade %s (vendor=%s)" % (INSTALLER_VERSION, "yes" if want_vendor else "no"))
    return cmd_install(ns)


def cmd_bump_blocks(args):
    raw = args.to.strip().lower()
    if raw.startswith("v"):
        raw = raw[1:]
    if not raw.isdigit() or int(raw) < 1:
        fail("--to must be a positive version like v2 (got %r)" % args.to)
    new_v = int(raw)
    changes = []
    for _filename, template, _flag in TARGET_FILES:
        path = TEMPLATES / template
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as ex:
            fail("cannot read template %s: %s" % (path, ex))
        new_text, n = re.subn(r"(aidomaincraft\s+\S+\s+v)\d+", r"\g<1>%d" % new_v, text, count=1)
        if n != 1:
            fail("template %s has no version stamp to bump" % path)
        if new_text != text:
            changes.append((path, new_text))
    reg_path = TEMPLATES / "VERSIONS"
    try:
        reg_text = reg_path.read_text(encoding="utf-8")
    except OSError as ex:
        fail("cannot read %s: %s" % (reg_path, ex))
    new_reg, reg_n = re.subn(r"^(\S+[ \t]+v)\d+[ \t]*$", r"\g<1>%d" % new_v, reg_text, flags=re.M)
    if reg_n == 0:
        fail("%s has no version lines to bump" % reg_path)
    if new_reg != reg_text:
        changes.append((reg_path, new_reg))
    if not changes:
        print("block version already v%d everywhere: nothing to do." % new_v)
        return 0
    for path, new in changes:
        if args.dry_run:
            print("would update %s to v%d" % (path, new_v))
        else:
            path.write_text(new, encoding="utf-8")
            print("updated %s to v%d" % (path, new_v))
    if args.dry_run:
        print("dry run complete: no files were written.")
    else:
        print("done. Next: add/update a content assert in tests/test.sh, run ./tests/test.sh, add a CHANGELOG entry.")
    return 0


def build_parser():
    p = argparse.ArgumentParser(prog="aidomaincraft_setup.py",
                                description="Install, uninstall, or inspect aidomaincraft lookup blocks.")
    p.add_argument("--version", action="version", version=INSTALLER_VERSION)
    sub = p.add_subparsers(dest="cmd", required=True)
    ins = sub.add_parser("install", help="install lookup blocks (reference-only by default)")
    ins.add_argument("--target", default=".", help="target repo or directory (default: current directory)")
    ins.add_argument("--source", default=DEFAULT_SOURCE, help="aidomaincraft source URL or local path")
    ins.add_argument("--ref", default=DEFAULT_REF, help="git branch/tag to clone (reference mode)")
    ins.add_argument("--vendor", action="store_true", help="also copy an offline snapshot into .aidomaincraft/")
    ins.add_argument("--force", action="store_true", help="update existing .aidomaincraft snapshot files")
    ins.add_argument("--dry-run", action="store_true")
    ins.add_argument("--backup", action="store_true")
    ins.add_argument("--skip-agents", action="store_true")
    ins.add_argument("--skip-claude", action="store_true")
    ins.add_argument("--no-create", action="store_true")
    ins.add_argument("--no-gitignore", action="store_true")
    ins.add_argument("--quiet", action="store_true")
    ins.set_defaults(func=cmd_install)
    uns = sub.add_parser("uninstall", help="remove lookup blocks and snapshot")
    uns.add_argument("--target", default=".", help="target repo or directory")
    uns.add_argument("--dry-run", action="store_true")
    uns.add_argument("--purge", action="store_true", help="delete .aidomaincraft/ instead of moving it aside")
    uns.add_argument("--keep-vendor", action="store_true", help="remove only blocks; keep .aidomaincraft/")
    uns.add_argument("--backup", action="store_true")
    uns.add_argument("--skip-agents", action="store_true")
    uns.add_argument("--skip-claude", action="store_true")
    uns.add_argument("--no-gitignore", action="store_true")
    uns.add_argument("--quiet", action="store_true")
    uns.set_defaults(func=cmd_uninstall)
    doc = sub.add_parser("doctor", help="check an installed target")
    doc.add_argument("--target", default=".", help="target repo or directory")
    doc.set_defaults(func=cmd_doctor)
    ver = sub.add_parser("version", help="print installer, template, CHARTER and installed block versions")
    ver.add_argument("--target", default=".", help="target repo or directory")
    ver.set_defaults(func=cmd_version)
    chk = sub.add_parser("check-update", help="compare installed blocks vs templates (+ optional remote tag check)")
    chk.add_argument("--target", default=".", help="target repo or directory")
    chk.add_argument("--source", default=DEFAULT_SOURCE, help="aidomaincraft source URL for --remote")
    chk.add_argument("--remote", action="store_true", help="also check latest vN tag on the git remote (needs network)")
    chk.set_defaults(func=cmd_check_update)
    upg = sub.add_parser("upgrade", help="one-command upgrade: rerun install, refreshing vendor snapshot when present")
    upg.add_argument("--target", default=".", help="target repo or directory")
    upg.add_argument("--source", default=DEFAULT_SOURCE, help="aidomaincraft source URL or local path")
    upg.add_argument("--ref", default=DEFAULT_REF, help="git branch/tag to clone (reference mode)")
    upg.add_argument("--vendor", action="store_true", help="add an offline snapshot on upgrade")
    upg.add_argument("--no-vendor", action="store_true", help="skip refreshing an existing snapshot")
    upg.add_argument("--dry-run", action="store_true")
    upg.add_argument("--backup", action="store_true")
    upg.add_argument("--skip-agents", action="store_true")
    upg.add_argument("--skip-claude", action="store_true")
    upg.add_argument("--no-create", action="store_true")
    upg.add_argument("--no-gitignore", action="store_true")
    upg.add_argument("--quiet", action="store_true")
    upg.set_defaults(func=cmd_upgrade)
    bmp = sub.add_parser("bump-blocks", help="sync marker-block version everywhere")
    bmp.add_argument("--to", required=True, help="new block version, e.g. v2")
    bmp.add_argument("--dry-run", action="store_true")
    bmp.set_defaults(func=cmd_bump_blocks)
    return p


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except SetupError as ex:
        print("error: %s" % ex, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
