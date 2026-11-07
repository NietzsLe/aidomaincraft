<!-- BEGIN aidomaincraft -->
<!-- aidomaincraft agents-block v8 -->
## Aidomaincraft — usecase lookup

This project can use **aidomaincraft** (usecase-first lookup; covered domains
are listed in the source root `README.md` routing table, not here).
Source: `https://github.com/NietzsLe/aidomaincraft.git` (ref `main`).
Full rules live in the source repo (`CHARTER.md` = law, `VERIFY.md` = checklist).
Item details live in the source repo — never copy commands/bars into this project.

- When: any task matching a row of the source root `README.md` routing table
  (UI, media, game, reverse, seo, automation, or later domains — e.g. page
  system, React effect, launch video, SEO audit, recurring job). No matching
  row → skip, do not load aidomaincraft.
- Lookup (4 steps):
  1. Read source `CHARTER.md` (check version there) + root `README.md` routing.
  2. Read `domains/<d>/README.md` (routing + positioning + overlap matrix).
  3. Read `domains/<d>/using-<x>.md` (domain-only commands + notes).
  4. Follow links to `items/<x>/README.md` (single source of truth) and run
     its copy-paste commands (mechanism + numeric bars).
- Routing (examples only — the full table lives in source root `README.md`,
  the full item list in `items/REGISTRY.md`; never treat this short list as
  complete): UI → `domains/ui/` (hallmark gated system / reactbits owned bricks /
  skillry packaged web taste); media → `domains/media/` (skillry packaged
  video-deck-OG / awesome-opus5-5-videos free Opus 5.5 prompts); other rows
  (game / reverse / seo / automation) → read the source routing table.
- Source fetch (refresh-first — the local cache is disposable, never trust it
  blind): 1. if `~/.cache/aidomaincraft` (fallback `/tmp/aidomaincraft`) exists,
  refresh it with `git -C ~/.cache/aidomaincraft pull --ff-only` (on failure:
  delete the cache dir and re-clone as below); 2. if missing, run
  `git clone --depth 1 --branch main https://github.com/NietzsLe/aidomaincraft.git ~/.cache/aidomaincraft`;
  3. run `doctor` / `check-update` from the REFRESHED copy; if offline and
  `.aidomaincraft/` exists in this project, use it; otherwise say the source is
  missing (and which copy + version you read) instead of guessing commands.
- Single source: commands, numeric bars and detailed steps live only in
  `items/*/README.md`; `domains/<d>/using-<x>.md` holds domain-only deltas.
- System runtime vs in-runtime intake (`CHARTER.md` §10 — know which mode
  you are in): system runtime only reads/uses (blocks + `doctor` /
  `check-update` / `upgrade` + 4-step source lookup); when no source item
  covers the job, draft a candidate under git-ignored
  `.aidomaincraft/drafts/<x>/` from `templates/runtime-draft-template.md` +
  one line in `.aidomaincraft/drafts/REGISTRY.local.md` (never touch source
  `items/REGISTRY.md`, never commit `.aidomaincraft/`); a draft passing
  `VERIFY.md` H promotes back via a `src/` clone + PR, never as the local
  truth.
- Agent-first versions (the user only talks, you run the commands):
  - At session start, when the task touches a routed domain: refresh the
    source cache first (`git -C ~/.cache/aidomaincraft pull --ff-only`,
    re-clone when it fails; fallback `/tmp/aidomaincraft` when HOME is not
    writable), then run
    `python3 ~/.cache/aidomaincraft/scripts/aidomaincraft_setup.py doctor --target .`
    and `.../aidomaincraft_setup.py check-update --target .` yourself
    (read-only, no need to ask), then report in one plain line, e.g. "lookup blocks v8, up to
    date" or "blocks v7 installed, v8 available — upgrade?".
  - When the user asks in plain words, map and run (no need to explain flags):
    "which version / đang dùng bản nào" → `version --target .`;
    "any update / có bản mới không" → `check-update --target .` (+ `--remote`
    when network is available); "what's new / bản mới có gì" → read the source
    `CHANGELOG.md` newest entry and summarize in 2-3 lines;
    "upgrade / lên bản mới" → ask for confirmation first (one line stating what
    will change), then run `upgrade --target .` (refreshes the vendor snapshot
    when one exists).
  - Router skill (one-time per agent): if the `aidomaincraft` skill is missing,
    propose one line ("cài skill aidomaincraft để tra cứu nhanh?"), then run
    `npx skills add https://github.com/NietzsLe/aidomaincraft --skill aidomaincraft`
    (fallback: copy `skills/aidomaincraft/` from the source into the agent's
    skills dir) only after user ok, and confirm it triggers on `aidomaincraft`.
  - Rules: read-only commands (`version`, `check-update`, `doctor`, reading
    CHANGELOG) run freely; write commands (`upgrade`, cloning the source) need
    one line of notice + user ok first.
- Core-fidelity (prove you really used the system): after using an item, state
  the reused artifact (prompt slug / variant / skill slug + label / passed
  gates). Unable = not actually using it — say so instead of claiming.
  Item cores live in each item's `Invariant core / Customizable surface /
  Work split` sections — read them before use; only the surface is tunable,
  and only after user approval.
- Handoff format (every delegate call): inputs + exact delegate command +
  expected output + verify method. A claude-owned step done by yourself = FAIL.
- Offline or no network → report `unknown`, keep working from the local
  snapshot, never block the task. Never hand-edit the block.
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
