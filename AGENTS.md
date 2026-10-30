# AGENTS.md — aidomaincraft

## Tiếng Việt

Repo này là tra cứu theo usecase. `CHARTER.md` là luật, `VERIFY.md` là checklist chấm đạt/rớt, `templates/` là mẫu điền.

### Tra cứu (dùng cho dự án khác)
1. Đọc `CHARTER.md` (hiện tại: v8).
2. Đọc root `README.md` để chọn domain (`domains/<d>/`).
3. Đọc `domains/<d>/README.md` (điều hướng + định vị + chồng lấn, cho phép nhiều item chính 1 việc) để chọn item + cách dùng.
4. Đọc `domains/<d>/using-<x>.md` để lấy lệnh mẫu + lưu ý RIÊNG cho domain, rồi theo link về `items/<x>/README.md` (nguồn sự thật duy nhất) để đọc cơ chế + ngưỡng chi tiết, làm theo lệnh trong đó.

### Tạo mới (thêm item / thêm cặp item-domain)
- Thêm item mới: copy `templates/item-template.md` thành `items/<x>/README.md`. Thẩm tra nguồn (repo/docs/registry + ít nhất 1 file nguồn). Viết đủ khung v7: `Cách item hoạt động` + `Định vị khác biệt` + `Bản đồ phủ usecase (★)` + usecase 6 field + `Tham khảo sử dụng (review sâu + số có trọng số)` + `Được dùng ở đâu` + song ngữ.
- Thêm cặp item-domain mới (item đã có, dùng cho domain mới): copy `templates/domain-using-template.md` thành `domains/<d>/using-<x>.md`. Chỉ viết phần RIÊNG domain + link về đúng section item gốc, cấm copy nguyên đoạn. Cập nhật `domains/<d>/README.md` + mục `Được dùng ở đâu` trong item gốc trong cùng commit.
- Thêm domain mới: copy `templates/domain-index-template.md`. Mỗi cặp trong domain mới đều cần using-doc.
- Self-review lặp đến khi đạt theo `VERIFY.md` mục E + F6: 1 FAIL là không merge; WARN phải ghi lý do.
- Ghi `CHANGELOG.md` (kèm case đã thử + quyết định ở lượt 3).
- Cài sang repo/thư mục khác: `./scripts/install.sh --target /path/to/project --dry-run` rồi `--backup`; xem `INSTALL.md` (gỡ: `UNINSTALL.md`).

Không commit log, token, PII.

## English

Usability-first lookup repo. `CHARTER.md` is the law, `VERIFY.md` is the pass/fail checklist, `templates/` holds fill-in blanks.

### Lookup (for other projects)
1. Read `CHARTER.md` (current: v7).
2. Read root `README.md` to pick a domain (`domains/<d>/`).
3. Read `domains/<d>/README.md` (routing + positioning + overlap, multiple primaries allowed) to pick the item + way.
4. Read `domains/<d>/using-<x>.md` for domain-specific commands + notes, then follow links to `items/<x>/README.md` (single source of truth) for mechanism + bars, and follow its commands.

### Authoring (add item / add item-domain pair)
- New item: copy `templates/item-template.md` to `items/<x>/README.md`. Verify sources first. Fill the full v7 frame: `How it works` + `Differentiation` + `Coverage map (★)` + 6-field sub-usecases + `Usage references (deep + weighted)` + `Where used` + bilingual.
- New item-domain pair (existing item, new domain use): copy `templates/domain-using-template.md` to `domains/<d>/using-<x>.md`. Domain-only deltas + links to exact item sections, never copied paragraphs. Update `domains/<d>/README.md` + the item's `Where used` in the same commit.
- New domain: copy `templates/domain-index-template.md`. Every pair in it needs a using-doc.
- Iterative self-review per `VERIFY.md` sections E + F6: 1 FAIL blocks merge; WARNs need a recorded reason.
- Add a `CHANGELOG.md` entry (with the tried case + decision from pass 3).

Never commit logs, tokens, or PII.

<!-- BEGIN relay-logs -->
<!-- relay-logs agents-block v4 -->
## Relay — cross-agent work log

This project uses **agent-relay-logs** (`.relay/`). The system is local-only and
ignored by git; it is not a source of truth. Its purpose: other agent sessions
and humans must be able to read your work without asking you.

**Log this much detail — a log of "task X started" is useless:**

| Event | Must contain |
|---|---|
| `start` | what will be done and why (`--goal`), the steps (`--plan`), how "done" is judged (`--accept`), files you expect to touch (`--scope`), keywords (`--tags`) |
| `note` | one line on what just happened (`--text`) + the next step (`--next`); kind: progress/problem/decision/result/blocker |
| `scope` | every path added to the working scope (`--add`) + why (`--why`) |
| `run` | every command expected to take >2 minutes: estimated time (`--eta`), then the measured result |
| `end` | what was actually done (`--done`), every problem and how it was resolved (`--problem`), how it was verified (`--verify`), numbers before/after (`--metric`), files and commits (`--changes`, `--commit`), what the next person must know (`--impact`), open items (`--next`), lesson codes (`--lesson`) |

**Commands**

```bash
# first: see what other sessions are doing right now (now · next · scope clash)
.relay/relay board

# start of a real task (not for pure Q&A) — prints session=… , reuse it below
.relay/relay --agent <name> start "<one-line title>" \
  --goal "<what and why>" --plan "<step 1>" --plan "<step 2>" \
  --scope <path,...> --tags <keyword,...> --accept "<how done is judged>"

# while working: one line per step, at least every 10 minutes
.relay/relay --session <id> note --kind progress --text "<what just happened>" --next "<next step>"

# the working scope changed
.relay/relay --session <id> scope --add <path,...> --why "<reason>"

# a command that takes a while (build, test suite, migration)
.relay/relay --session <id> run --eta 8m -- <command>

# after each big step: pull what other sessions did
.relay/relay --session <id> sync

# when done / abandoning / blocked (exit 1 on gate violation: fix or --force)
.relay/relay --session <id> end --status done|partial|abandoned|blocked \
  --summary "<what the world looks like now>" \
  --done "<step completed>" --problem "<problem> => <how it was resolved>" \
  --verify "<how it was checked> => <result>" \
  --metric "<before> -> <after> (n=..., window=...)" \
  --changes <file,...> --commit <sha> --next "<open item>" --lesson L-nn \
  --impact "<what the next person must know>"
```

**Rhythm (checked by the tool, not by memory):**- `relay tick` prints at most one line when something needs you: silence past
  the reminder, files outside the logged scope, or unread news from other
  sessions. Silence means everything is fine.
- Log at least every 10 minutes of active work. Time inside a declared
  `run`/`wait` window does not count.
- Every command you expect to take more than 2 minutes gets `--eta` first
  (`relay run --eta 8m -- …`). Underestimating past tolerance and
  overestimating wildly both cost score.
- Every scope change gets one `scope` line before you keep working.
- `end` refuses (exit 1, still recorded and closed) on: silence over the limit,
  badly estimated commands, unlogged scope drift, or `done` without `--verify`.
  Re-run with `--force` to accept the penalty.

**Browser interaction (delegated — you have no browser here, and you do not need one):**

Real-browser work (clicking, typing, logged-in sessions, JS-heavy rendering,
visual verification) is still yours to order: delegate it to the `claude` CLI,
which drives a remote Chrome. Do this by default whenever such a task comes up
— no need to be asked first, and no need for local Chrome:

```bash
claude --chrome --model sonnet -p "<exactly what to do>" \
  --dangerously-skip-permissions --output-format text
```

Reading a static page is not this — use `webfetch` for that. Delegate only
when interaction is required.
Rules: describe the expected result in the delegated prompt; never paste
secrets, tokens, or PII into it; log the delegation like any long command
(`run --eta`); verify the outcome yourself afterwards (re-resolve, re-curl,
re-read the page) instead of trusting the report blindly.
If delegation is unavailable in this environment (no `claude` CLI, no
`--chrome` support, or the required sign-in is missing): do NOT silently skip —
tell the user exactly what is missing (which tool, which flag, which login) so
it can be installed.

**Image generation (delegated — you have no image tool here, but you do via Codex):**

Image work (new illustrations, diagrams, assets, mockups — or edits/variants
referencing existing images) is still yours to order: delegate it to the
`codex` CLI, which has a built-in image generation tool. Do this by default
whenever such a task comes up — no need to be asked first:

```bash
# create new
codex exec --skip-git-repo-check -C <project-dir> \
  "Generate <detailed description: subject, style, colors, composition> and save it as ./<path>.png in the working directory. Use your image generation tool."

# edit / variant from reference image(s)
codex exec --skip-git-repo-check -C <project-dir> \
  -i ./ref.png \
  "Generate <what to make> inspired by the attached reference image(s) and save it as ./<path>.png. Use your image generation tool."
```

Rules: describe the expected image in detail in the delegated prompt; never
paste secrets, tokens, or PII into it; log the delegation like any long
command (`run --eta`); verify the outcome yourself afterwards (read the saved
file) instead of trusting the report blindly. Generated files land under
`~/.codex/generated_images/<session>/` before being copied to the working
directory — if the copy is blocked by the sandbox, copy the file over
manually. If delegation is unavailable in this environment (no `codex` CLI or
sign-in missing): do NOT silently skip — tell the user exactly what is
missing so it can be installed. Never claim you cannot generate images without
checking Codex first.

**Session start: make sure the relay itself is compatible (do this yourself):**
- If `.relay/` does not exist here (fresh clone — `.relay` is git-ignored and
  never travels with the repo): fetch the installer repo
  (`git@github.com:NietzsLe/agent-relay-logs.git`, shallow clone is enough) and
  run its `install.sh --target .` before starting real work. If you have no
  network access to it, say so instead of working without a log.
- Run `.relay/relay board` first anyway: if it reports your blocks OUTDATED
  (installed vX, runtime wants vY), rerun the installer to upgrade, then
  continue. Never work a whole session on a stale setup in silence.

Rules:

- Be specific: "fixed the bug" is worthless; "migration deadlock → advisory
  lock; `pytest tests/test_migrate.py` green" is useful.
- Only log real work; never log secrets, tokens, or PII.
- A `start` without an `end` means work is still in progress.
- The log is one file per day — `.relay/data/YYYY-MM-DD.jsonl` (all sessions of
  that day); read cursors live in `.relay/cursors/`, harness keys in `.relay/keys/`.
- The log is only *relatively* complete. "Not in the log" does not mean "did not
  happen" — verify with `git log/status`, files, and the real project state.
- Read `.relay/README.md` for the full model; `relay show <task>` prints one
  task in full, `relay stats` prints the scoreboard.

_This block belongs to **agent-relay-logs** and is managed by its installer. To
uninstall, run `scripts/uninstall.sh` from the agent-relay-logs repository, or
delete everything between this line's marker and the END marker._
<!-- END relay-logs -->
