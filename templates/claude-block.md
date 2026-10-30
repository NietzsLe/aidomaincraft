<!-- BEGIN aidomaincraft -->
<!-- aidomaincraft claude-block v5 -->
## Aidomaincraft — usecase lookup

This project can use **aidomaincraft** (UI + media lookup). The full rules live
in the `aidomaincraft` block of `AGENTS.md` (or in the source repo when that
file is absent).

- Source: `https://github.com/NietzsLe/aidomaincraft.git` (ref `main`).
- When: UI task (page system, React effect, sample landing) or media task
  (launch video, deck, OG image). Otherwise skip.
- Lookup: source `CHARTER.md` + root `README.md` → `domains/<d>/README.md` →
  `domains/<d>/using-<x>.md` → `items/<x>/README.md` (single source of truth).
- Fetch when missing:
  `git clone --depth 1 --branch main https://github.com/NietzsLe/aidomaincraft.git ~/.cache/aidomaincraft`
  (fallback `/tmp/aidomaincraft`); offline → use local `.aidomaincraft/` if
  present, else say missing instead of guessing.
- Agent-first versions (user only talks, you run the commands): session start
  on a UI/media task → run the same `doctor` + `check-update` as `AGENTS.md`
  yourself, report one plain line; plain asks map to `version` /
  `check-update` / CHANGELOG summary / `upgrade` (needs user ok first).
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
