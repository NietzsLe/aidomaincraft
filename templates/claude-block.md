<!-- BEGIN aidomaincraft -->
<!-- aidomaincraft claude-block v8 -->
## Aidomaincraft — usecase lookup

This project can use **aidomaincraft** (usecase-first lookup; covered domains
are listed in the source root `README.md` routing table, not here). The full rules live
in the `aidomaincraft` block of `AGENTS.md` (or in the source repo when that
file is absent).

- Source: `https://github.com/NietzsLe/aidomaincraft.git` (ref `main`).
- When: any task matching a row of the source root `README.md` routing table
  (UI, media, game, reverse, seo, automation, or later domains). No matching
  row → skip.
- Lookup: source `CHARTER.md` + root `README.md` → `domains/<d>/README.md` →
  `domains/<d>/using-<x>.md` → `items/<x>/README.md` (single source of truth).
  Full item list: `items/REGISTRY.md` (never treat the block's examples as complete).
- Fetch when missing or stale (cache is disposable, never trust it blind):
  refresh with `git -C ~/.cache/aidomaincraft pull --ff-only` (on failure:
  delete the cache dir and re-clone), else
  `git clone --depth 1 --branch main https://github.com/NietzsLe/aidomaincraft.git ~/.cache/aidomaincraft`
  (fallback `/tmp/aidomaincraft`); offline → use local `.aidomaincraft/` if
  present, else say missing (with copy + version) instead of guessing.
- System runtime vs in-runtime intake (same rule as `AGENTS.md`, `CHARTER.md`
  §10): runtime only reads/uses; uncovered jobs become drafts under
  git-ignored `.aidomaincraft/drafts/<x>/` + local index (never source
  `items/REGISTRY.md`, never commit), promoted back via `src/` + PR.
- Agent-first versions (user only talks, you run the commands): session start
  on a routed-domain task → refresh the cache, then run the same `doctor` + `check-update` as `AGENTS.md`
  yourself, report one plain line; plain asks map to `version` /
  `check-update` / CHANGELOG summary / `upgrade` (needs user ok first).
- Router skill (one-time per agent): same rule as `AGENTS.md` — if the
  `aidomaincraft` skill is missing, propose one line ("cài skill aidomaincraft
  để tra cứu nhanh?"), then run
  `npx skills add https://github.com/NietzsLe/aidomaincraft --skill aidomaincraft`
  (fallback: copy `skills/aidomaincraft/` from the source into the agent's
  skills dir) only after user ok; confirm it triggers on `aidomaincraft`.
- Core-fidelity + handoff (same as `AGENTS.md`): after use, state the reused
  artifact (slug/variant/skill/gates); handoff = inputs + delegate command +
  expected output + verify method; only the item's customizable surface is
  tunable, after user approval.
- Absolute compliance (same 5 classes as `AGENTS.md`, details there):
  must-read constraints first; env-gate (declare, missing → stop + propose);
  must-follow all steps in order; must-verify (quote the result, open FAIL =
  never done); must-not is absolute (Floor waive, invented metrics, hand-typed
  slugs, stock hotlinks, others' keys, self-doing browser/image instead of
  `claude --chrome` / `codex`) — never proposed, never approvable.
- Adapt-and-approve: detect environment + user conditions, propose A/B/C
  options with a recommendation (default = standard flow), run only after the
  user picks; record choice + waiver in the handoff.

_This block belongs to **aidomaincraft** and is managed by its installer. To
uninstall, run `scripts/uninstall.sh --target .` from the aidomaincraft
repository, or delete everything between this line's marker and the END marker._
<!-- END aidomaincraft -->
