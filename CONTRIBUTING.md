# CONTRIBUTING.md — đóng góp vào aidomaincraft (CHARTER v12)

## Tiếng Việt

### Ai đóng góp được
- Agent ở mọi runtime (OpenCode, Claude Code, Cursor, Codex, Gemini CLI...) + người. Mọi bước dưới đây dùng git CLI trung lập runtime.
- Lưu ý theo runtime: Plan mode (OpenCode) không được sửa file — chỉ bàn kế hoạch; relay log bắt buộc theo `AGENTS.md` (mọi task thật đều `start`/`note`/`end`); không paste secret/token/PII vào relay, PR, hay prompt delegate.

### Luồng PR chuẩn (6 bước)
1. **Mở nhánh**: `git checkout -b <loai>-<ten>` (vd `item-dembrandt`, `fix-ui-matrix`). Không commit thẳng `main`.
2. **Sửa theo CHARTER**: item mới khai `Nguồn gốc` trước (§4b), đúng template (`item-template.md` | `intrinsic-item-template.md`), đủ khung + song ngữ; cặp domain mới đủ using-doc; sửa 3 tầng + `CHANGELOG.md` trong cùng commit.
3. **Self-review** lặp theo `VERIFY.md` mục E (+F6 cho item mới) tới hết FAIL; WARN ghi lý do 1 dòng (sẽ vào CHANGELOG).
4. **Chạy máy**: `bash tests/test.sh` phải `fail=0`; item nội tại chạy thêm tài nguyên của nó (`check.py`/script tương đương) + ghi output vào CHANGELOG.
5. **Ghi CHANGELOG**: entry version mới, kèm case đã thử + quyết định ở lượt 3 (VERIFY E).
6. **Mở PR**: push nhánh, mở PR theo mẫu (`.github/PULL_REQUEST_TEMPLATE.md` tự hiện checklist); link relay session trong mô tả để reviewer đọc log không cần hỏi. Làm việc từ project đã cài aidomaincraft? Xem `INSTALL.md` mục "Local clone" (`.aidomaincraft/src/`) để tham khảo + thử sửa local rồi PR ngược.

### Chuẩn PR (thiếu là yêu cầu sửa)
- 1 PR = 1 việc; commit message `vX.Y: <gì> (<phạm vi>)`, vd `v9.4: item dembrandt + cặp UI`.
- Không commit log, token, PII, file local (`.relay/`, `.test/`, `.aidomaincraft/` đã git-ignored — kiểm tra `git status` trước khi add).
- Mọi khẳng định số (stars/installs/ngày đo) có nguồn + ngày; thiếu số ghi `chưa xác minh`, cấm đoán.
- Reviewer merge khi: 0 FAIL theo VERIFY + test xanh + 3 chiều link sống + song ngữ đồng nội dung + tiếng Việt có dấu đầy đủ (docs/CHANGELOG/PR/commit message thiếu dấu = yêu cầu sửa).

### Đóng góp item nội tại (CHARTER v12 §9)
1. **Proposal**: 1 tool = 1 đề xuất — tên kebab-case tiếng Anh, tác giả, lý do ra đời, tài nguyên tự sở hữu (cấm copy code ngoài vào).
2. **Chuẩn hóa**: copy `templates/intrinsic-item-template.md` → `items/<x>/README.md` đủ khung §5d song ngữ; khai 1 dòng `items/REGISTRY.md`; using-doc + index 2 đầu trong cùng commit.
3. **Thử runtime**: suite ở `.aidomaincraft/<item>/` (git-ignored, không commit); script stdlib chạy được (`--help`/demo PASS); quan sát UI bằng browser thật; log relay đầy đủ.
4. **Verify**: self-review VERIFY tới 0 FAIL + `bash tests/test.sh` xanh (thêm case tài nguyên + demo + FAIL đúng mã) + CHANGELOG (case đã thử + quyết định).
5. **PR**: 1 tool = 1 PR theo luồng 6 bước trên; xung đột khung/luật → sửa CHARTER trước.

### Soạn draft trong runtime ở repo đã cài (CHARTER v12 §10)
- Ở repo đã cài, việc chưa ai phủ thì soạn draft theo `templates/runtime-draft-template.md` vào `.aidomaincraft/drafts/<x>/` (git-ignored, cấm commit) + index local `REGISTRY.local.md`; runtime của hệ vẫn chỉ đọc/dùng.
- Draft đạt VERIFY H thì promote: clone `src/` theo `INSTALL.md` mục "Local clone", chuẩn hóa khung nội tại §5d ở đó, rồi PR theo luồng 6 bước trên (khai `items/REGISTRY.md` + using-doc cùng commit).

### Quy tắc review
- 1 FAIL là không merge; WARN giữ lại phải có lý do trong CHANGELOG.
- Tranh chấp khung/luật → sửa CHARTER (bump version) trước, rồi mới sửa nội dung theo luật mới.

---

## English

### Who can contribute
- Agents on any runtime (OpenCode, Claude Code, Cursor, Codex, Gemini CLI...) + humans. All steps below use runtime-neutral git CLI.
- Runtime notes: Plan mode (OpenCode) must not edit files — discuss only; relay logging is mandatory per `AGENTS.md`; never paste secrets/tokens/PII into relays, PRs, or delegate prompts.

### Standard PR flow (6 steps)
1. **Branch**: `git checkout -b <kind>-<name>` (e.g. `item-dembrandt`). Never commit straight to `main`.
2. **Follow CHARTER**: new items declare `Origin` first (§4b), use the right template, full frame + bilingual; new domain pairs get using-docs; all 3 layers + `CHANGELOG.md` in the same commit.
3. **Self-review** per `VERIFY.md` section E (+F6 for new items) until zero FAILs; WARNs get a 1-line reason (goes to CHANGELOG).
4. **Run machines**: `bash tests/test.sh` must print `fail=0`; intrinsic items additionally run their own resources + record output in CHANGELOG.
5. **Write CHANGELOG**: new version entry with the tried case + pass-3 decision.
6. **Open PR**: push, follow `.github/PULL_REQUEST_TEMPLATE.md` (auto checklist); link the relay session so reviewers read logs without asking. Working from a project with aidomaincraft installed? See `INSTALL.md` "Local clone" (`.aidomaincraft/src/`) for reference + trial edits, then PR back.

### PR bar (missing = change requested)
- 1 PR = 1 job; message `vX.Y: <what> (<scope>)`.
- Never commit logs, tokens, PII, or local files (`.relay/`, `.test/`, `.aidomaincraft/` are git-ignored — check `git status` before adding).
- Every number (stars/installs/dates) sourced + dated; missing numbers → `unverified`, never guessed.
- Merge when: 0 VERIFY FAILs + green tests + live 3-way links + VI/EN in sync + Vietnamese fully accented (missing accents in docs/CHANGELOG/PR/commit messages = change requested).

### Intrinsic item contributions (CHARTER v12 §9)
1. **Proposal**: 1 tool = 1 proposal — English kebab-case name, author, why, self-owned resources (never copy outside code in).
2. **Normalize**: copy `templates/intrinsic-item-template.md` → `items/<x>/README.md` (§5d frame, bilingual); one `items/REGISTRY.md` line; using-doc + both index ends in the same commit.
3. **Trial runtime**: suite under git-ignored `.aidomaincraft/<item>/` (never commit); stdlib scripts run (`--help`/demo PASS); UI observations in a real browser; full relay logs.
4. **Verify**: VERIFY self-review to 0 FAILs + green `bash tests/test.sh` (resource + demo + right-code FAIL cases) + CHANGELOG (tried case + decision).
5. **PR**: 1 tool = 1 PR following the 6 steps above; frame/law disputes → amend CHARTER first.

### Drafting in runtime at installed repos (CHARTER v12 §10)
- At an installed repo, uncovered jobs become drafts per `templates/runtime-draft-template.md` under git-ignored `.aidomaincraft/drafts/<x>/` (never commit) + local `REGISTRY.local.md` index; system runtime itself stays read/use-only.
- Drafts passing VERIFY H promote via a `src/` clone per `INSTALL.md` "Local clone": normalize to the §5d intrinsic frame there, then PR through the 6 steps above (`items/REGISTRY.md` + using-doc in the same commit).

### Review rules
- 1 FAIL blocks merge; kept WARNs need a CHANGELOG reason.
- Frame/law disputes → amend CHARTER (version bump) first, then content under the new law.
