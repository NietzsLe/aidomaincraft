# domains/automation/

## Tiếng Việt

Domain automation — chạy prompt OpenCode lặp lại theo giờ trên máy của chính mình (job định kỳ, polling, nhắc việc, dọn artifacts). Chi tiết gốc sống trong `items/*/README.md`; dùng CHO automation thì đọc `using-*.md` tương ứng.

### Bảng điều hướng: việc → item(s)
| Việc cần làm | Item chính (mỗi cái 1 cách) | Item hỗ trợ | Lệnh bắt đầu |
|---|---|---|---|
| Lập lịch prompt định kỳ (hằng ngày / thứ 2 / mỗi 6 giờ) | `opencode-scheduler` (timer OS + supervisor — xem `using-opencode-scheduler.md`) | — | `Schedule a daily job at 9am to...` (đã khai `plugin` trong `opencode.json`) |
| Polling + alert (check site / deal mới / notifications) | `opencode-scheduler` (run-spec + timeout + skill idempotent — xem `using-opencode-scheduler.md`) | — | `Schedule a job every 6 hours to check...` + `@scheduled-job-best-practices` |
| Giám sát + vòng đời job (xem/sửa/chạy ngay/xóa/dọn) | `opencode-scheduler` (11 tools theo scope — xem `using-opencode-scheduler.md`) | — | `Show my scheduled jobs` / `Show logs for <slug>` |
| Workflow rẽ nhánh / 400+ integration / UI kéo thả | — (không phải việc của domain này) | `opencode-scheduler` không gánh | dùng `n8n` ngoài repo |

Việc lập lịch thuần: cần timer OS + catch-up + scope → opencode-scheduler. Việc polling: cần timeout + skill idempotent + notifications → opencode-scheduler. Việc rẽ nhánh/integration: cần nodes/visual/queue → n8n thay.

### Bảng định vị
| Item | Mục đích điển hình | Vận hành tóm tắt 1 câu | Điểm mạnh | Điểm yếu | Dùng chính khi | Tránh khi | Thay thế bởi | Vì sao chọn A thay vì B trong case này |
|---|---|---|---|---|---|---|---|---|
| `opencode-scheduler` — chi tiết automation ở `using-opencode-scheduler.md`, gốc ở `../../items/opencode-scheduler/README.md` | job prompt lặp lại trong OpenCode bằng timer OS | Wrapper mỏng cài launchd/systemd/schtasks/cron gọi `opencode run` qua supervisor Perl | 1 dòng plugin, 11 tools tiếng tự nhiên, scope theo project, catch-up + overlap-lock + timeout (mac/Linux), 0đ MIT, 517★ | 13 issues nền mở (2.0/NixOS/Windows/API key/scope), Windows mất supervisor, cron không catch-up, không retry/queue | cần 1 job prompt lặp lại trên máy luôn bật, OpenCode 1.x mac/Linux stock | OpenCode 2.0, NixOS, cron Windows phức tạp, workflow rẽ nhánh, máy tắt hẳn | n8n khi cần nodes/integration; chạy tay OS + `opencode run` khi cần kiểm soát từng dòng unit | Chọn opencode-scheduler thay vì n8n/chạy tay khi quyết định phụ thuộc vào gọn-nhẹ trong TUI (1 câu lệnh ra job có log + scope), không phải visual/queue hay kiểm soát unit thủ công |

### Ma trận chồng lấn
| Việc | `opencode-scheduler` | Tiêu chí chọn phân biệt |
|---|---|---|
| Lập lịch prompt định kỳ | chính | cần timer OS + catch-up + scope → opencode-scheduler; chỉ chạy 1 lần → `opencode run` trực tiếp thay thế |
| Polling + alert | chính | cần timeout + skill idempotent + log theo scope → opencode-scheduler; cần rẽ nhánh/duyệt tay → n8n thay thế |
| Giám sát + vòng đời | chính | cần list/get/logs/run/update/delete/cleanup theo scope → opencode-scheduler; lạc scope thì kèm `allScopes:true` |
| Workflow rẽ nhánh / integration | không dùng | `n8n` ngoài repo (không phải việc của domain này) |

### Workflow phối hợp mẫu
Khai plugin (`opencode.json` + restart + `Show scheduler version`) → cài skill best-practices 1 lần → chốt cron + payload + workdir/timeout với user → `schedule_job` bằng tiếng tự nhiên → vận hành bằng `list/get/logs/run/update/delete` đúng scope → job lỗi thì đọc log trước, timer OS sau, `workdir`/MCP/env cuối.

### Danh sách using-doc
- `using-opencode-scheduler.md` — dùng opencode-scheduler CHO automation → gốc `../../items/opencode-scheduler/README.md`

---

## English

Automation domain — recurring OpenCode prompts on your own machine (periodic jobs, polling, reminders, artifact cleanup). Origins at `items/*/README.md`; for automation use read the matching `using-*.md`.

### Routing: job → item(s)
| Job | Primary item(s) (each a different way) | Supporting item | Starter command |
|---|---|---|---|
| Periodic prompt scheduling (daily / Monday / every 6h) | `opencode-scheduler` (OS timer + supervisor — see `using-opencode-scheduler.md`) | — | `Schedule a daily job at 9am to...` (with `plugin` in `opencode.json`) |
| Polling + alerts (site/deal/notification checks) | `opencode-scheduler` (run-spec + timeout + idempotent skill — see `using-opencode-scheduler.md`) | — | `Schedule a job every 6 hours to check...` + `@scheduled-job-best-practices` |
| Monitoring + lifecycle (read/edit/run-now/delete/clean) | `opencode-scheduler` (11 scoped tools — see `using-opencode-scheduler.md`) | — | `Show my scheduled jobs` / `Show logs for <slug>` |
| Branching workflows / 400+ integrations / visual UI | — (out of this domain) | `opencode-scheduler` does not cover it | use external `n8n` |

Pure scheduling: OS timer + catch-up + scope → opencode-scheduler. Polling: timeout + idempotent skill + notifications → opencode-scheduler. Branching/integrations: nodes/visual/queue → n8n instead.

### Positioning
| Item | Typical purposes | 1-sentence operating summary | Strengths | Weaknesses | Use as primary when | Avoid when | Replaced by | Why pick A over B in this case |
|---|---|---|---|---|---|---|---|---|
| `opencode-scheduler` — automation details in `using-opencode-scheduler.md`, origin at `../../items/opencode-scheduler/README.md` | recurring prompt jobs inside OpenCode via OS timers | Thin wrapper installing launchd/systemd/schtasks/cron to call `opencode run` through a Perl supervisor | 1-line plugin, 11 natural-language tools, per-project scopes, catch-up + overlap lock + timeout (mac/Linux), $0 MIT, 517 stars | 13 open foundation issues (2.0/NixOS/Windows/API-key/scope), no Windows supervisor, no cron catch-up, no retry/queue | one recurring prompt on an always-on machine, OpenCode 1.x stock mac/Linux | OpenCode 2.0, NixOS, complex Windows cron, branching workflows, fully-off machines | n8n for nodes/integrations; hand-rolled OS + `opencode run` for full unit control | Pick opencode-scheduler over n8n/hand-rolled when leanness inside the TUI (one sentence to a logged, scoped job) decides, not visuals/queues or hand-owned units |

### Overlap matrix
| Job | `opencode-scheduler` | Distinguishing selection rule |
|---|---|---|
| Periodic prompt scheduling | primary | OS timer + catch-up + scope → opencode-scheduler; one-shot → direct `opencode run` instead |
| Polling + alerts | primary | timeout + idempotent skill + scoped logs → opencode-scheduler; branching/human approval → n8n instead |
| Monitoring + lifecycle | primary | scoped list/get/logs/run/update/delete/cleanup → opencode-scheduler; scope confusion → add `allScopes:true` |
| Branching / integration workflows | do-not-use | external `n8n` (not this domain's job) |

### Sample combined workflow
Declare the plugin (`opencode.json` + restart + `Show scheduler version`) → install the best-practices skill once → settle cron + payload + workdir/timeout with the user → `schedule_job` in natural language → operate via `list/get/logs/run/update/delete` in the right scope → on failure read logs first, OS timer second, `workdir`/MCP/env last.

### Using-doc list
- `using-opencode-scheduler.md` — opencode-scheduler FOR automation → origin `../../items/opencode-scheduler/README.md`
