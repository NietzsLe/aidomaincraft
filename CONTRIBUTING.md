# CONTRIBUTING.md — đóng góp vào aidomaincraft (CHARTER v10)

## Tiếng Việt

### Ai đóng góp được
- Agent ở mọi runtime (OpenCode, Claude Code, Cursor, Codex, Gemini CLI...) + người. Mọi bước dưới đây dùng git CLI trung lập runtime.
- Lưu ý theo runtime: Plan mode (OpenCode) không được sửa file — chỉ bàn kế hoạch; relay log bắt buộc theo `AGENTS.md` (mọi task thật đều `start`/`note`/`end`); không paste secret/token/PII vào relay, PR, hay prompt delegate.

### Luồng PR chuẩn (6 bước)
1. **Mở nhánh**: `git checkout -b <loai>-<ten>` (vd `item-wireframe-docs`, `fix-ui-matrix`). Không commit thẳng `main`.
2. **Sửa theo CHARTER**: item mới khai `Nguồn gốc` trước (§4b), đúng template (`item-template.md` | `intrinsic-item-template.md`), đủ khung + song ngữ; cặp domain mới đủ using-doc; sửa 3 tầng + `CHANGELOG.md` trong cùng commit.
3. **Self-review** lặp theo `VERIFY.md` mục E (+F6 cho item mới) tới hết FAIL; WARN ghi lý do 1 dòng (sẽ vào CHANGELOG).
4. **Chạy máy**: `bash tests/test.sh` phải `fail=0`; item nội tại chạy thêm tài nguyên của nó (`check.py`/script tương đương) + ghi output vào CHANGELOG.
5. **Ghi CHANGELOG**: entry version mới, kèm case đã thử + quyết định ở lượt 3 (VERIFY E).
6. **Mở PR**: push nhánh, mở PR theo mẫu (`.github/PULL_REQUEST_TEMPLATE.md` tự hiện checklist); link relay session trong mô tả để reviewer đọc log không cần hỏi. Làm việc từ project đã cài aidomaincraft? Xem `INSTALL.md` mục "Local clone" (`.aidomaincraft/src/`) để tham khảo + thử sửa local rồi PR ngược.

### Chuẩn PR (thiếu là yêu cầu sửa)
- 1 PR = 1 việc; commit message `vX.Y: <gì> (<phạm vi>)`, vd `v10.1: item nội tại wireframe-docs + cặp UI`.
- Không commit log, token, PII, file local (`.relay/`, `.test/`, `.aidomaincraft/` đã git-ignored — kiểm tra `git status` trước khi add).
- Mọi khẳng định số (stars/installs/ngày đo) có nguồn + ngày; thiếu số ghi `chưa xác minh`, cấm đoán.
- Reviewer merge khi: 0 FAIL theo VERIFY + test xanh + 3 chiều link sống + song ngữ đồng nội dung.

### Quy tắc review
- 1 FAIL là không merge; WARN giữ lại phải có lý do trong CHANGELOG.
- Tranh chấp khung/luật → sửa CHARTER (bump version) trước, rồi mới sửa nội dung theo luật mới.

---

## English

### Who can contribute
- Agents on any runtime (OpenCode, Claude Code, Cursor, Codex, Gemini CLI...) + humans. All steps below use runtime-neutral git CLI.
- Runtime notes: Plan mode (OpenCode) must not edit files — discuss only; relay logging is mandatory per `AGENTS.md`; never paste secrets/tokens/PII into relays, PRs, or delegate prompts.

### Standard PR flow (6 steps)
1. **Branch**: `git checkout -b <kind>-<name>` (e.g. `item-wireframe-docs`). Never commit straight to `main`.
2. **Follow CHARTER**: new items declare `Origin` first (§4b), use the right template, full frame + bilingual; new domain pairs get using-docs; all 3 layers + `CHANGELOG.md` in the same commit.
3. **Self-review** per `VERIFY.md` section E (+F6 for new items) until zero FAILs; WARNs get a 1-line reason (goes to CHANGELOG).
4. **Run machines**: `bash tests/test.sh` must print `fail=0`; intrinsic items additionally run their own resources + record output in CHANGELOG.
5. **Write CHANGELOG**: new version entry with the tried case + pass-3 decision.
6. **Open PR**: push, follow `.github/PULL_REQUEST_TEMPLATE.md` (auto checklist); link the relay session so reviewers read logs without asking. Working from a project with aidomaincraft installed? See `INSTALL.md` "Local clone" (`.aidomaincraft/src/`) for reference + trial edits, then PR back.

### PR bar (missing = change requested)
- 1 PR = 1 job; message `vX.Y: <what> (<scope>)`.
- Never commit logs, tokens, PII, or local files (`.relay/`, `.test/`, `.aidomaincraft/` are git-ignored — check `git status` before adding).
- Every number (stars/installs/dates) sourced + dated; missing numbers → `unverified`, never guessed.
- Merge when: 0 VERIFY FAILs + green tests + live 3-way links + VI/EN in sync.

### Review rules
- 1 FAIL blocks merge; kept WARNs need a CHANGELOG reason.
- Frame/law disputes → amend CHARTER (version bump) first, then content under the new law.
