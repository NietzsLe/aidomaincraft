# using-opencode-scheduler CHO automation — job định kỳ + polling + vòng đời (CHARTER v12)

> Phần automation của opencode-scheduler KHI DÙNG CHO automation. Gốc ở `../../items/opencode-scheduler/README.md`.

## Tiếng Việt

### Usecase trong domain này
- ★ Lập lịch prompt định kỳ (hằng ngày / thứ 2 / mỗi 6 giờ, catch-up + scope): xem [Usecase con 1](../../items/opencode-scheduler/README.md#usecase-con-1-lap-lich-prompt-dinh-ky).
- Polling + alert với run-spec nâng cao (timeout + attachUrl + workdir + skill idempotent): xem [Usecase con 2](../../items/opencode-scheduler/README.md#usecase-con-2-run-spec-nang-cao-commandmodelattachurltimeout).
- Giám sát + vòng đời (list/get/logs/run/update/delete/cleanup theo scope): xem [Usecase con 3](../../items/opencode-scheduler/README.md#usecase-con-3-giam-sat-va-vong-doi-job).
- Skill best-practices + version (1 lần cho mọi job): xem [Usecase con 4](../../items/opencode-scheduler/README.md#usecase-con-4-skill-best-practices-va-version).

### Lệnh mẫu cụ thể (cho domain này)
- Khai plugin 1 lần rồi verify (khớp từng chữ lệnh gốc): `{"plugin": ["opencode-scheduler"]}` trong `opencode.json` + `Show scheduler version`. Xem [Cài đặt](../../items/opencode-scheduler/README.md#cai-dat-da-mo-repo--npm--source-kiem-tra-07112026-chua-chay-end-to-end-vi-may-nay-khong-co-opencode-cli).
- Job săn deal hằng ngày (automation nhắc việc): `Schedule a daily job at 9am to search Facebook Marketplace for posters under $100 and send the top 5 deals to my Telegram`. Xem [Usecase con 1](../../items/opencode-scheduler/README.md#usecase-con-1-lap-lich-prompt-dinh-ky).
- Job polling có ngắt (automation giám sát): `Schedule a job every 6 hours to check if my website is up and alert me on Slack if it is down` + `timeoutSeconds: 600`. Xem [Usecase con 2](../../items/opencode-scheduler/README.md#usecase-con-2-run-spec-nang-cao-commandmodelattachurltimeout).
- Vận hành hằng ngày (đúng scope automation): `Show my scheduled jobs` (thêm `allScopes:true` khi đa project), `Show logs for standing-desk`, `Run the standing-desk job now`, `Update standing-desk to run at 10am`, `Delete the standing-desk job`, `Run scheduler global cleanup` (dry-run trước). Xem [Usecase con 3](../../items/opencode-scheduler/README.md#usecase-con-3-giam-sat-va-vong-doi-job).
- Skill 1 lần cho mọi job automation: `Install the scheduled job best practices skill` + chèn `@scheduled-job-best-practices` đầu prompt. Xem [Usecase con 4](../../items/opencode-scheduler/README.md#usecase-con-4-skill-best-practices-va-version).

### Lưu ý riêng cho domain
- Lạc scope là bẫy automation số 1 (2 project cùng tên job khác workdir): list mặc định chỉ current scope, phải `allScopes:true` + `includeLegacy:true` khi tìm job cũ. Xem [Usecase con 3](../../items/opencode-scheduler/README.md#usecase-con-3-giam-sat-va-vong-doi-job) và issue #11 trong [Tham khảo](../../items/opencode-scheduler/README.md#tham-khao).
- Job automation phải idempotent vì timer có thể bắn lại sau giấc ngủ (systemd `Persistent=true`): seen-file + output `outputs/` theo skill, không gửi trùng alert. Xem [Usecase con 4](../../items/opencode-scheduler/README.md#usecase-con-4-skill-best-practices-va-version).
- Windows automation chỉ cron đơn (mất supervisor → mất overlap/timeout) + NixOS/OpenCode 2.0 dừng hẳn. Xem [Pitfalls](../../items/opencode-scheduler/README.md#pitfalls).
- Secret automation (API key Telegram/Slack) để trong `opencode-scheduler.json` (`env.set`), không nhét vào prompt (launchd plist chỉ set PATH). Xem [Usecase con 2](../../items/opencode-scheduler/README.md#usecase-con-2-run-spec-nang-cao-commandmodelattachurltimeout).

### Điểm mạnh cốt lõi của item CHO domain này
- Timer OS + catch-up + scope thay cho cron tay: 1 câu tiếng tự nhiên ra job có log/metadata theo project, không viết plist/service. Xem [Usecase con 1](../../items/opencode-scheduler/README.md#usecase-con-1-lap-lich-prompt-dinh-ky).
- Run-spec + timeout + deny-questions cho polling không treo: quá giờ SIGTERM→SIGKILL, job hỏi là skip thay vì kẹt. Xem [Usecase con 2](../../items/opencode-scheduler/README.md#usecase-con-2-run-spec-nang-cao-commandmodelattachurltimeout).
- 11 tools vòng đời theo scope + cleanup dry-run: vận hành hằng ngày không chạm backend OS. Xem [Usecase con 3](../../items/opencode-scheduler/README.md#usecase-con-3-giam-sat-va-vong-doi-job).

### Phân công CHO domain này (1 dòng + link, không copy)
- Agent chính chốt cron + payload + workdir/timeout với chủ máy (qua question tool, user pick mới gọi tool) rồi gọi `schedule_job`/`update_job`/`run_job`/`delete_job`/`cleanup_global`; bước mở log dài/browser ngoài giao claude; verify bằng job file + timer OS + log. Chi tiết: [Phân công gốc](../../items/opencode-scheduler/README.md#phan-cong-ai-lam-gi).

### Link về item gốc (3 chiều — bắt buộc)
- Gốc: `../../items/opencode-scheduler/README.md` (Usecase 1/2/3/4 / Cài đặt / Định vị / Hồ sơ quyết định / Tham khảo sử dụng).
- Index domain: `./README.md`.
- Được liệt kê ngược tại: `../../items/opencode-scheduler/README.md#duoc-dung-o-dau`.

---

## English

Automation use of opencode-scheduler — periodic jobs + polling + lifecycle. Origin at `../../items/opencode-scheduler/README.md`.

### Usecases in this domain
- ★ Periodic prompt scheduling (daily / Monday / every 6h, catch-up + scopes): see [Sub-usecase 1](../../items/opencode-scheduler/README.md#sub-usecase-1-periodic-prompt-scheduling).
- Polling + alerts with advanced run-spec (timeout + attachUrl + workdir + idempotent skill): see [Sub-usecase 2](../../items/opencode-scheduler/README.md#sub-usecase-2-advanced-run-spec-commandmodelattachurltimeout).
- Monitoring + lifecycle (scoped list/get/logs/run/update/delete/cleanup): see [Sub-usecase 3](../../items/opencode-scheduler/README.md#sub-usecase-3-job-monitoring-and-lifecycle).
- Best-practices skill + version (once for all jobs): see [Sub-usecase 4](../../items/opencode-scheduler/README.md#sub-usecase-4-best-practices-skill-and-version).

### Concrete commands (for this domain)
- One-time plugin declaration + verify (word-for-word origin): `{"plugin": ["opencode-scheduler"]}` in `opencode.json` + `Show scheduler version`. See [Install](../../items/opencode-scheduler/README.md#install-repo--npm--source-read-07112026-no-end-to-end-run--no-opencode-cli-on-this-machine).
- Daily deal job (reminder automation): `Schedule a daily job at 9am to search Facebook Marketplace for posters under $100 and send the top 5 deals to my Telegram`. See [Sub-usecase 1](../../items/opencode-scheduler/README.md#sub-usecase-1-periodic-prompt-scheduling).
- Capped polling job (watchdog automation): `Schedule a job every 6 hours to check if my website is up and alert me on Slack if it is down` + `timeoutSeconds: 600`. See [Sub-usecase 2](../../items/opencode-scheduler/README.md#sub-usecase-2-advanced-run-spec-commandmodelattachurltimeout).
- Daily ops (correct automation scope): `Show my scheduled jobs` (add `allScopes:true` for multi-project), `Show logs for standing-desk`, `Run the standing-desk job now`, `Update standing-desk to run at 10am`, `Delete the standing-desk job`, `Run scheduler global cleanup` (dry-run first). See [Sub-usecase 3](../../items/opencode-scheduler/README.md#sub-usecase-3-job-monitoring-and-lifecycle).
- One-time skill for all automation jobs: `Install the scheduled job best practices skill` + `@scheduled-job-best-practices` prefix. See [Sub-usecase 4](../../items/opencode-scheduler/README.md#sub-usecase-4-best-practices-skill-and-version).

### Domain-specific notes
- Scope confusion is automation trap #1 (same job name, different workdirs): default list is current-scope only. See [Sub-usecase 3](../../items/opencode-scheduler/README.md#sub-usecase-3-job-monitoring-and-lifecycle).
- Automation jobs must be idempotent (post-sleep re-fire): seen-file + `outputs/` per skill. See [Sub-usecase 4](../../items/opencode-scheduler/README.md#sub-usecase-4-best-practices-skill-and-version).
- Windows automation is simple-cron only (no supervisor); NixOS/OpenCode 2.0 are stop lines. See [Pitfalls](../../items/opencode-scheduler/README.md#pitfalls).
- Automation secrets live in `opencode-scheduler.json` (`env.set`), never in prompts. See [Sub-usecase 2](../../items/opencode-scheduler/README.md#sub-usecase-2-advanced-run-spec-commandmodelattachurltimeout).

### Core strengths FOR this domain
- OS timers + catch-up + scopes instead of hand cron: one sentence to a logged, scoped job. See [Sub-usecase 1](../../items/opencode-scheduler/README.md#sub-usecase-1-periodic-prompt-scheduling).
- Run-spec + timeout + deny-questions for hang-free polling. See [Sub-usecase 2](../../items/opencode-scheduler/README.md#sub-usecase-2-advanced-run-spec-commandmodelattachurltimeout).
- 11 scoped lifecycle tools + dry-run cleanup: daily ops without touching OS backends. See [Sub-usecase 3](../../items/opencode-scheduler/README.md#sub-usecase-3-job-monitoring-and-lifecycle).

### Work split FOR this domain (1 line + link, never copied)
- Main agent settles cron + payload + workdir/timeout with the machine owner (question tool, user picks before any call), then calls the lifecycle tools; long-log/browser steps go to claude; verify via job file + OS timer + logs. Details: [origin Work split](../../items/opencode-scheduler/README.md#work-split).

### Links to item origin (3-way — required)
- Origin: `../../items/opencode-scheduler/README.md` (Sub-usecases 1/2/3/4 / Install / Positioning / Decision dossier / Usage references).
- Domain index: `./README.md`.
- Backlisted at: `../../items/opencode-scheduler/README.md#where-used`.
