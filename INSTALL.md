# Install aidomaincraft lookup into a repo or directory

Audience: an agent or human with shell access to a target repo/directory.

The installer is intentionally narrow. Reference-only by default — it touches
only `AGENTS.md` and `CLAUDE.md` (one marker block each). With `--vendor` it
also copies an offline snapshot into `.aidomaincraft/` + `.gitignore`.

```text
<!-- BEGIN aidomaincraft -->
...
<!-- END aidomaincraft -->
```

## What will change in the target

| Path | Default (reference-only) | With `--vendor` |
|---|---|---|
| `AGENTS.md` | Marker block added/updated | same |
| `CLAUDE.md` | Marker block added/updated | same |
| `.aidomaincraft/` | untouched | Snapshot (`domains/`, `items/`, `CHARTER.md`, `README.md`, `VERIFY.md`, `CHANGELOG.md`) + `install.json` (git-ignored) |
| `.gitignore` | untouched | Adds `.aidomaincraft/` |

If `AGENTS.md` or `CLAUDE.md` does not exist, the installer creates a minimal
file. Use `--no-create` to skip missing files.

## Preconditions

1. Python 3.8+: `python3 --version`.
2. The target path exists and is writable.
3. Read the target's existing `AGENTS.md` / `CLAUDE.md` first.
4. Check git state so the diff is easy to review:
   ```bash
   git -C /path/to/project status --short
   ```

## Step 1 — dry run

From the `aidomaincraft` repository:

```bash
./scripts/install.sh --target /path/to/project --dry-run
./scripts/install.sh --target /path/to/project --source https://github.com/NietzsLe/aidomaincraft.git --ref main --dry-run
```

Custom source (local path for dev, fork URL for teams):

```bash
./scripts/install.sh --target /path/to/project --source /home/u/aidomaincraft --dry-run
```

Offline snapshot (copies docs into the target, git-ignored):

```bash
./scripts/install.sh --target /path/to/project --vendor --dry-run
```

## Step 2 — install

```bash
./scripts/install.sh --target /path/to/project --backup
```

Useful flags:

| Flag | Effect |
|---|---|
| `--source <url\|path>` | Aidomaincraft source written into the block (default `https://github.com/NietzsLe/aidomaincraft.git`) |
| `--ref <branch/tag>` | Git ref for the clone command (default `main`) |
| `--vendor` | Copy offline snapshot into `.aidomaincraft/` + `.gitignore` |
| `--force` | Update existing `.aidomaincraft/` snapshot files |
| `--backup` | Write `AGENTS.md.aidomaincraft-backup-<ts>` before editing |
| `--skip-agents` | Do not touch `AGENTS.md` |
| `--skip-claude` | Do not touch `CLAUDE.md` |
| `--no-create` | Do not create a missing `AGENTS.md` / `CLAUDE.md` |
| `--no-gitignore` | Do not modify `.gitignore` (vendor mode) |

Installation is idempotent: running it again replaces the block instead of
adding a second one. Blocks carry a version stamp
(`<!-- aidomaincraft agents-block vN -->`); `doctor` flags outdated blocks.

## Step 3 — verify

```bash
TARGET=/path/to/project
python3 scripts/aidomaincraft_setup.py doctor --target "$TARGET"
grep -cF '<!-- BEGIN aidomaincraft -->' "$TARGET/AGENTS.md"
grep -cF '<!-- BEGIN aidomaincraft -->' "$TARGET/CLAUDE.md"
```

Expected: `doctor` reports `OK`, each `grep -c` prints `1`. Reference-only
installs report `.aidomaincraft: reference-only`.

## Versions and updates

Three axes, all visible via one command:

```bash
python3 scripts/aidomaincraft_setup.py version --target /path/to/project
# installer 1.1.0, template blocks v2, source CHARTER v8, installed blocks vN
```

Check whether a target is behind (exit 0 = up to date, 1 = update available):

```bash
python3 scripts/aidomaincraft_setup.py check-update --target /path/to/project
# optional remote tag check (needs network):
python3 scripts/aidomaincraft_setup.py check-update --target /path/to/project --remote
```

Upgrade in one command (idempotent; refreshes the vendor snapshot when one
exists, unless `--no-vendor`):

```bash
./scripts/install.sh --target /path/to/project
# or explicitly:
python3 scripts/aidomaincraft_setup.py upgrade --target /path/to/project
python3 scripts/aidomaincraft_setup.py upgrade --target /path/to/project --vendor --force
```

Tag scheme: release tags follow the CHARTER version (`v8`, `v9`, ...), so
`--ref v9` pins knowledge and `--remote` compares against the latest `vN` tag.
Session start in an installed project: run `doctor` once; if it reports a
block `outdated`, run the upgrade command above (also printed by `doctor`).
Never hand-edit the block.

## Via agent (no commands needed from the user)

The installed block tells the agent to handle versions itself. The user only
talks; the agent runs the commands:

| User says | Agent runs |
|---|---|
| task touches UI/media (session start) | `doctor` + `check-update` alone, reports one plain line |
| "đang dùng bản nào / which version" | `version --target .` |
| "có bản mới không / any update" | `check-update --target .` (+ `--remote` when network is up) |
| "bản mới có gì / what's new" | reads newest `CHANGELOG.md` entry, summarizes 2-3 lines |
| "lên bản mới / upgrade" | asks one confirmation line first, then `upgrade --target .` |

Rules the block enforces: read-only commands run freely; `upgrade` and
cloning the source need one notice line + user ok first; offline reports
`unknown` and keeps working from the local snapshot.

## Absolute compliance (block v4+)

Every installed block carries the same compliance protocol for all items:

- 5 classes: `must-read` (read the item's constraints first) · `env-gate`
  (declare environment, missing → stop + propose) · `must-follow` (all steps in
  order, silent skip = FAIL) · `must-verify` (run the verify command, quote the
  result, open FAIL = never done) · `must-not` (absolute: Floor waive, invented
  data, hand-typed slugs, stock hotlinks, others' keys, self-doing
  browser/image instead of `claude --chrome` / `codex`).
- Hard constraints per item (hallmark / reactbits / skillry /
  awesome-opus5-5-videos / delegation) with links to the exact source sections.
- Adapt-and-approve: the agent detects environment + user conditions, proposes
  an A/B/C options table (default = standard flow), and runs only the option
  the user picks — recorded as a waiver. `must-not` is never offered.

Agent lookup check (3-minute test): open the cached source and pick a domain:

```bash
git clone --depth 1 --branch main https://github.com/NietzsLe/aidomaincraft.git /tmp/aidomaincraft
ls /tmp/aidomaincraft/domains /tmp/aidomaincraft/items
```

## Step 4 — review and commit

```bash
git -C "$TARGET" status --short
git -C "$TARGET" diff -- AGENTS.md CLAUDE.md .gitignore
```

Commit only tracked changes, and only if the user asked:

```bash
git -C "$TARGET" add AGENTS.md CLAUDE.md
git -C "$TARGET" commit -m "chore: add aidomaincraft lookup"
```

Never commit `.aidomaincraft/` (add it to `.gitignore`; the installer does this
in `--vendor` mode).

## Manual fallback (if the script cannot run)

1. Append `templates/agents-block.md` to `AGENTS.md`.
2. Append `templates/claude-block.md` to `CLAUDE.md`.
3. Run the Step 3 checks.

## Troubleshooting

- **Unbalanced markers** — stop, inspect manually; the installer refuses to guess.
- **`target is not a directory`** — check `--target`.
- **Blocks outdated** — rerun `install.sh --target ...` (no `--force` needed for blocks).
- **Vendor snapshot stale** — rerun with `--vendor --force`.
