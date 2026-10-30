# Uninstall aidomaincraft lookup from a repo or directory

Uninstall is the mirror of install: remove the marker blocks, remove the
`.aidomaincraft/` line from `.gitignore`, and take the snapshot away.
Reference-only installs leave no trace except the two blocks.

## What will change in the target

| Path | Default | `--purge` | `--keep-vendor` |
|---|---|---|---|
| `AGENTS.md`, `CLAUDE.md` | Marker block removed | same | same |
| `.gitignore` | `.aidomaincraft/` line removed | same | same |
| `.aidomaincraft/` | moved to `.aidomaincraft.removed-<ts>/` | deleted | kept in place |
| `AGENTS.md` / `CLAUDE.md` created by installer | deleted if still empty | same | same |

No other files are modified.

## Step 1 — dry run

```bash
./scripts/uninstall.sh --target /path/to/project --dry-run
```

## Step 2 — run

```bash
# Default: remove blocks, move snapshot aside
./scripts/uninstall.sh --target /path/to/project

# Delete snapshot as well
./scripts/uninstall.sh --target /path/to/project --purge

# Remove only blocks; keep snapshot working
./scripts/uninstall.sh --target /path/to/project --keep-vendor
```

Flags: `--backup`, `--skip-agents`, `--skip-claude`, `--no-gitignore` (same
meaning as install).

Uninstall is idempotent: running it on an already-clean target is a no-op.

## Step 3 — verify

```bash
TARGET=/path/to/project
grep -cF '<!-- BEGIN aidomaincraft -->' "$TARGET/AGENTS.md" 2>/dev/null || echo "0 (clean)"
grep -cF '<!-- BEGIN aidomaincraft -->' "$TARGET/CLAUDE.md" 2>/dev/null || echo "0 (clean)"
grep -nF '.aidomaincraft/' "$TARGET/.gitignore" 2>/dev/null || echo "no .aidomaincraft/ line (clean)"
ls -d "$TARGET"/.aidomaincraft.removed-* 2>/dev/null || echo "no removed dir"
ls -d "$TARGET/.aidomaincraft" 2>/dev/null && echo "still present (expected only with --keep-vendor)"
```

Expected: `0 (clean)` for both markers, no `.aidomaincraft/` line.

## Step 4 — review and commit

```bash
git -C "$TARGET" status --short
git -C "$TARGET" diff -- AGENTS.md CLAUDE.md .gitignore
```

## Manual fallback

1. Delete everything between `<!-- BEGIN aidomaincraft -->` and
   `<!-- END aidomaincraft -->` (inclusive) in `AGENTS.md` and `CLAUDE.md`.
2. Remove the `.aidomaincraft/` line from `.gitignore`.
3. Remove or move aside `.aidomaincraft/`.
