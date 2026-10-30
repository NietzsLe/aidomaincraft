<!-- BEGIN aidomaincraft -->
<!-- aidomaincraft agents-block v4 -->
## Aidomaincraft — usecase lookup

This project can use **aidomaincraft** (usecase-first lookup for UI + media work).
Source: `https://github.com/NietzsLe/aidomaincraft.git` (ref `main`).
Full rules live in the source repo (`CHARTER.md` = law, `VERIFY.md` = checklist).
Item details live in the source repo — never copy commands/bars into this project.

- When: UI task (page system, React effect, sample landing) or media task
  (launch video, deck, OG image). Otherwise skip — do not load aidomaincraft.
- Lookup (4 steps):
  1. Read source `CHARTER.md` (check version there) + root `README.md` routing.
  2. Read `domains/<d>/README.md` (routing + positioning + overlap matrix).
  3. Read `domains/<d>/using-<x>.md` (domain-only commands + notes).
  4. Follow links to `items/<x>/README.md` (single source of truth) and run
     its copy-paste commands (mechanism + numeric bars).
- Routing: UI → `domains/ui/` (hallmark gated system / reactbits owned bricks /
  skillry packaged web taste); media → `domains/media/` (skillry packaged
  video-deck-OG / awesome-opus5-5-videos free Opus 5.5 prompts).
- Source fetch: if no cached copy exists, run
  `git clone --depth 1 --branch main https://github.com/NietzsLe/aidomaincraft.git ~/.cache/aidomaincraft`
  (fallback `/tmp/aidomaincraft` when HOME is not writable); if offline and
  `.aidomaincraft/` exists in this project, use it; otherwise say the source is
  missing instead of guessing commands.
- Single source: commands, numeric bars and detailed steps live only in
  `items/*/README.md`; `domains/<d>/using-<x>.md` holds domain-only deltas.
- Agent-first versions (the user only talks, you run the commands):
  - At session start, when the task touches UI/media: run
    `python3 ~/.cache/aidomaincraft/scripts/aidomaincraft_setup.py doctor --target .`
    and `.../aidomaincraft_setup.py check-update --target .` yourself
    (read-only, no need to ask; fallback `/tmp/aidomaincraft` when HOME is not
    writable), then report in one plain line, e.g. "lookup blocks v4, up to
    date" or "blocks v4 installed, v5 available — upgrade?".
  - When the user asks in plain words, map and run (no need to explain flags):
    "which version / đang dùng bản nào" → `version --target .`;
    "any update / có bản mới không" → `check-update --target .` (+ `--remote`
    when network is available); "what's new / bản mới có gì" → read the source
    `CHANGELOG.md` newest entry and summarize in 2-3 lines;
    "upgrade / lên bản mới" → ask for confirmation first (one line stating what
    will change), then run `upgrade --target .` (refreshes the vendor snapshot
    when one exists).
  - Rules: read-only commands (`version`, `check-update`, `doctor`, reading
    CHANGELOG) run freely; write commands (`upgrade`, cloning the source) need
    one line of notice + user ok first. Offline or no network → report
    `unknown`, keep working from the local snapshot, never block the task.
    Never hand-edit the block.
- Absolute compliance (applies to every item and every task):
  - must-read: before using an item, read its constraints first (`Dùng khi /
    Bỏ qua khi`, Pitfalls, `must-not` lines in its README).
  - env-gate: declare the environment in one line first (OS, Chrome, network,
    model access, keys, stack). Missing anything → stop, report, propose —
    never work around silently.
  - must-follow: run all steps in the item's order (e.g. Hallmark pre-flight →
    deal → hero-first → sweep; Skillry on Linux → paste-prompt/ZIP, never CLI).
    Silently skipping a step = FAIL.
  - must-verify: run the item's verify command and quote the result (Hallmark
    `sloplint --render`; Skillry `ls SKILL.md` + Free/Premium label; React Bits
    variant + LCP check; awesome-list prompt count + browser test). Open FAIL =
    never report done.
  - must-not (absolute — never proposed, never approvable): waiving Hallmark
    Floor gates; inventing metrics/routes/links; hand-typing Skillry slugs;
    hotlinking stock images; reusing others' API keys/paths; doing browser or
    image work yourself instead of delegating to `claude --chrome` / `codex`.
    If the user asks for one, warn + refuse (or state the risk in writing).
- Hard constraints per item (details in the linked sections):
  - hallmark (`items/hallmark/README.md`): no ship with open FAIL/REFLEX;
    Floor never waived; hero passes the 1280x800 fold + word budget before
    building sections; real screenshots over mocks (`capture.mjs`).
  - reactbits (`items/reactbits/README.md`): exact variant suffix (`-TS-TW`
    vs `-JS-CSS`); motion `transform/opacity` only + reduced-motion fallback;
    re-sweep with Hallmark after installing effects.
  - skillry (`items/skillry/README.md`): Linux never uses CLI (paste-prompt/ZIP
    only); free skills STILL need an account; check the Free/Premium label
    before planning; price excludes external model fees.
  - awesome-opus5-5-videos (`items/awesome-opus5-5-videos/README.md`): not
    installable (clone + copy prompt only); Opus 5.5 access required to
    re-render; drop internal keys/paths from prompts; uneven quality accepted.
  - delegation (you have no browser/image tool of your own): real browser work
    → `claude --chrome --model sonnet -p "..." --dangerously-skip-permissions`;
    image work → `codex exec ...` (image generation tool). Declare availability
    at session start (`claude --chrome`: yes/no, `codex`: yes/no). Missing →
    say exactly what is missing + propose a fallback, wait for ok.
- Adapt-and-approve (fit to environment/user conditions):
  - Detect first: OS, tool availability, network, model/key access, project
    stack, plus user conditions (budget 0đ vs paid ok, offline, speed vs
    standard). Ask one compact question when unknown — never guess.
  - Propose as options, never act first: table A/B/C (what changes, gain,
    loss, exact command) + 1 recommendation line; default = standard flow.
    Example: Skillry on Linux → A paste-prompt (recommended) / B manual ZIP /
    C skip Skillry, use the free engine.
  - Approval gate: every flow change runs only after the user picks an option;
    stop and wait. Record the choice + waiver (what changed, why, who approved)
    in the handoff. `must-not` items are never offered as options.

_This block belongs to **aidomaincraft** and is managed by its installer. To
uninstall, run `scripts/uninstall.sh --target .` from the aidomaincraft
repository, or delete everything between this line's marker and the END marker._
<!-- END aidomaincraft -->
