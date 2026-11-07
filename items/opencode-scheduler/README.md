# opencode-scheduler

## Tiếng Việt

### Dùng khi
- Cần chạy prompt OpenCode lặp lại theo giờ (hằng ngày, thứ 2 hằng tuần, mỗi 6 giờ) mà không ngồi canh máy, trên máy macOS/Linux/Windows của chính mình.
- Cần job tự chạy khi máy ngủ rồi thức dậy (catch-up), chống chạy chồng nhau, tự ngắt khi quá lâu, tách log theo từng project.
- Agent hỗ trợ OpenCode plugin (khai `plugin` trong `opencode.json`); máy có `opencode` CLI + backend OS (`launchctl`/`systemd --user`/`schtasks`/`crontab`) + `/usr/bin/perl` cho supervisor.
- Muốn mô tả job bằng tiếng tự nhiên trong TUI OpenCode thay vì viết plist/service thủ công.

### Bỏ qua khi
- Cần workflow nhiều bước có rẽ nhánh, 400+ integration, UI kéo thả → dùng `n8n-io/n8n` thay (xem [Định vị khác biệt](#dinh-vi-khac-biet-so-lieu-ngay-07112026)).
- Cần retry/reporting phức tạp, queue server, chạy khi máy tắt hẳn → không hệ OS-scheduler nào làm được, phải dùng VPS luôn bật + `opencode serve` hoặc nền tảng workflow cloud.
- Máy NixOS, Windows cron phức tạp, hoặc đang ở OpenCode 2.0 → dừng (3 bẫy đã có issue mở, xem [Pitfalls](#pitfalls)).
- Chỉ cần chạy 1 lần ngay → gọi `opencode run` trực tiếp, không cần plugin.

### Cài đặt (đã mở repo + npm + source kiểm tra 07/11/2026; chưa chạy end-to-end vì máy này không có `opencode` CLI)
- Cách duy nhất (theo README gốc): thêm vào `opencode.json` của project:
- `{"plugin": ["opencode-scheduler"]}`
- Khởi động lại OpenCode, rồi ra lệnh bằng tiếng tự nhiên: `Schedule a daily job at 9am to summarize my GitHub notifications`.
- Nguồn đã mở kiểm tra: `package.json` (v1.3.0, MIT, tác giả Benjamin Shafii), `src/index.ts` (3.315 dòng, 11 tools), `README.md` (bảng 4 backend + 11 tools + storage), npm `opencode-scheduler@1.3.0` (17/02/2026).
- Yêu cầu: `opencode` CLI trong PATH (ưu tiên `command -v opencode`, fallback `/opt/homebrew/bin/opencode`, `/usr/local/bin/opencode`, `~/.opencode/bin/opencode` — xem `src/index.ts` hàm `findOpencode`); macOS cần `launchctl`, Linux cần `systemctl --user` hoặc `crontab`, Windows cần `schtasks`; supervisor cần `/usr/bin/perl`.
- Kiểm tra (không cần job thật): `Show scheduler version` → `get_version` trả về bản plugin + bản `opencode --version`.

### Cách item hoạt động
- Tổ chức đứng sau: `different-ai` (Benjamin Shafii), repo `https://github.com/different-ai/opencode-scheduler`, license MIT, npm `opencode-scheduler` v1.3.0 (17/02/2026; chuỗi 0.1.0 tháng 01/2026 → 1.3.0 tháng 02/2026). Nhịp 28 commits. Số liệu GitHub ngày 07/11/2026: 517★ / 45 forks / 13 issues mở / 2 watchers.
- Phương thức hoạt động chung: plugin mỏng bọc `opencode run`. Agent gọi 1 trong 11 tools → plugin ghi job JSON (kèm snapshot `invocation` = câu lệnh `opencode run` đầy đủ) vào `~/.config/opencode/scheduler/scopes/<scopeId>/jobs/*.json` → cài timer vào backend OS → đến giờ OS gọi `supervisor.pl` (Perl) → supervisor khóa chống overlap, ép `OPENCODE_PERMISSION={"question":"deny"}`, chạy `opencode run`, ghi log append + cập nhật metadata + run history JSONL. `run_job` chạy ngay không qua supervisor (fire-and-forget, cùng file log).
- Khác biệt vận hành theo usecase: lập lịch prompt định kỳ (ghi job + cài timer OS, xem [Usecase con 1](#usecase-con-1-lap-lich-prompt-dinh-ky)) khác run-spec nâng cao (map `command/agent/model/files/attachUrl/timeout` thành flags `opencode run`, xem [Usecase con 2](#usecase-con-2-run-spec-nang-cao-commandmodelattachurltimeout)) khác giám sát + vòng đời (đọc/sửa/xóa/log/dọn, không đụng scheduler backend, xem [Usecase con 3](#usecase-con-3-giam-sat-va-vong-doi-job)) khác skill + version (đọc/ghi file skill tĩnh, không chạy agent, xem [Usecase con 4](#usecase-con-4-skill-best-practices-va-version)).

### Cốt lõi bất biến
- Mọi job định kỳ đều đi qua `schedule_job` + cron 5-field + `workdir` scope (`deriveScopeId` từ absolute path, 12 ký tự hash). Viết plist/service tay ngoài plugin mà vẫn gọi là dùng hệ = FAIL khai báo sai.
- Prompt job phải non-interactive + idempotent theo skill `scheduled-job-best-practices` (dòng `@scheduled-job-best-practices` ở đầu prompt, tính ngày bằng `bash date`, bảng seen/notifications, output vào `outputs/`). Job chờ QR/login/confirm = FAIL (scheduled run ép `question: deny`).
- Sau khi dùng phải nêu được: slug + cron + scopeId + artifact tái dùng (skill/câu lệnh). Không nêu được = chưa thực sự dùng hệ.
- Xem [Usecase con 1](#usecase-con-1-lap-lich-prompt-dinh-ky) và [Các bước chung](#cac-buoc-chung).

### Phần tùy chỉnh
- Được đổi: `schedule` (cron 5-field), `prompt` hoặc `command/arguments/files/agent/model/variant/title/share/continue/session/runFormat/port`, `workdir`, `attachUrl`, `timeoutSeconds` (0 = tắt). Cổng duyệt 2 tầng: (1) cron nào + chạy cái gì — trình diễn giải `describeCron` (vd `0 9 * * *` = daily 9 AM) chờ user chốt trước khi cài; (2) giữ/đổi gì ở `update_job` — timeout/attachUrl/workdir đổi phải chốt trước khi ghi lại. Waiver duy nhất (bỏ timeout khi job dài bất thường) phải quote câu ok tường minh của user, không suy diễn. Cấm đưa `must-not` (chờ confirm người, copy secret vào prompt, chạy job khiêu khích khi máy tắt) vào danh sách tùy chỉnh.
- Xem [Usecase con 2](#usecase-con-2-run-spec-nang-cao-commandmodelattachurltimeout) và [Hồ sơ quyết định](#ho-so-quyet-dinh).

### Phân công ai làm gì
- Agent chính làm: chốt cron + nội dung job với user (diễn giải cron ra giờ đọc được, shortlist workdir/attachUrl/timeout kèm lý do qua question tool, user pick mới gọi tool) → gọi đúng tool (`schedule_job`/`update_job`/`run_job`/`delete_job`/`cleanup_global` với `confirm` tường minh) → đọc `job_logs`/`get_job` verify trạng thái + log tồn tại.
- Giao cho claude các bước cần browser/tài khoản ngoài: mở log/artifact job trên browser thật, xác minh secret/API key cho `attachUrl` backend, kiểm tra timer OS ngoài terminal (`launchctl list`, `systemctl --user list-timers`, `schtasks /Query`) khi agent không có quyền shell — kèm slug + scopeId + yêu cầu cụ thể; cấm agent tự bịa output job.
- Agent verify: job file tồn tại ở `scopes/<scopeId>/jobs/<slug>.json` + timer OS tồn tại + log append có dòng `Scheduled run`/`Manual run` + metadata `lastRunStatus` cập nhật.
- Chi tiết theo từng usecase ở [Usecase con 1](#usecase-con-1-lap-lich-prompt-dinh-ky), [Usecase con 2](#usecase-con-2-run-spec-nang-cao-commandmodelattachurltimeout), [Usecase con 3](#usecase-con-3-giam-sat-va-vong-doi-job), [Usecase con 4](#usecase-con-4-skill-best-practices-va-version).

### Định vị khác biệt (số liệu ngày 07/11/2026)
- So với `n8n-io/n8n` (fair-code workflow automation, 204k★/60,6k forks, 400+ integrations, self-host/cloud): khác cơ chế ở nơi chạy — n8n là server workflow có UI + nodes + queue; opencode-scheduler là wrapper mỏng cài timer OS gọi `opencode run`, không server, không UI, không rẽ nhánh. Chọn opencode-scheduler thay vì n8n khi cần 1 job prompt lặp lại trong TUI OpenCode với 1 dòng khai báo plugin, không muốn dựng stack workflow (ngưỡng: 1 file `opencode.json` so với 1 service n8n + credentials + nodes); chọn n8n khi quyết định phụ thuộc vào nodes/integration/rẽ nhánh/retry visual, chấp nhận self-host + học nodes.
- So với chạy tay `cron/systemd/launchd + opencode run` (baseline chính chủ, nền `anomalyco/opencode` 225k★, 0 cài thêm): khác ở envelope — chạy tay phải tự viết plist/service + tự lo overlap/timeout/log/metadata; plugin sinh sẵn supervisor (khóa overlap, `question: deny`, timeout SIGTERM→SIGKILL, log + JSONL + metadata atomic). Chọn plugin thay vì chạy tay khi cần catch-up khi thức máy (launchd `StartCalendarInterval`/systemd `Persistent=true`), scope theo project, và quản lý bằng tiếng tự nhiên (`list_jobs`, `job_logs`); chọn chạy tay khi ở NixOS/Windows phức tạp/OpenCode 2.0 (plugin đang có 3 issues mở #28/#14/#25) hoặc cần kiểm soát từng dòng plist/service.
- Khung trung thực: opencode-scheduler thắng ở gọn-nhẹ trong OpenCode (517★ nhưng đúng việc, 0đ MIT); thua ở quy mô workflow (n8n 204k★) và thua ở kiểm soát tay khi backend OS lỗi.

### Bản đồ phủ usecase (quét HẾT README + `src/index.ts` 3.315 dòng + 11 tools + 4 backend 07/11/2026 — ★ mạnh nhất đầu)
- ★ Lập lịch prompt định kỳ (`schedule_job` core + cron + workdir scope): xem Usecase 1.
- Run-spec nâng cao (`command/arguments/files/agent/model/variant/title/share/continue/session/runFormat/port/attachUrl/timeoutSeconds` → flags `opencode run`): xem Usecase 2.
- Giám sát + vòng đời (`list_jobs`/`get_job`/`job_logs`/`run_job`/`update_job`/`delete_job`/`cleanup_global`): xem Usecase 3.
- Trung bình: skill best-practices + version (`get_skill`/`install_skill`/`get_version`): xem Usecase 4.
- Trung bình: backend OS 4 đường (launchd supervised / systemd supervised / schtasks subset cron / cron fallback không catch-up): dùng khi chọn máy chạy, xem [Usecase con 1](#usecase-con-1-lap-lich-prompt-dinh-ky) + [Pitfalls](#pitfalls).
- KHÔNG hỗ trợ → thay thế: retry chính sách phức tạp/queue server → n8n hoặc worker tự viết (PRD `PRD-resilient-execution.md` ghi rõ roadmap chưa làm); cron tháng+kết hợp weekday phức tạp trên Windows → tách nhiều job đơn hoặc chuyển mac/Linux; chạy khi máy tắt hẳn → VPS luôn bật; OpenCode 2.0 (`Plugin.define + ctx.tool.transform`, issue #28) → chờ port, không dùng bản này.

### Hồ sơ quyết định
- Việc DÙNG (3+, cụ thể): 1. job nhắc việc hằng ngày 9h (`0 9 * * *` săn deal/poster dưới $100 gửi Telegram); 2. polling mỗi 6 giờ (`0 */6 * * *` check website up + alert Slack khi down); 3. tóm tắt thứ 2 hằng tuần (`30 8 * * 1` tóm GitHub notifications); 4. dọn artifacts đa scope (`cleanup_global` dry-run trước, `confirm:true` sau).
- Việc KHÔNG DÙNG (3+, mỗi việc kèm hệ thay thế): 1. workflow rẽ nhánh/400+ integration → dùng `n8n`; 2. retry/queue/reporting SLA → dùng worker/cloud scheduler (PRD chưa làm); 3. cron phức tạp tháng+weekday trên Windows → dùng mac/Linux hoặc tách job (lỗi có thông điệp rõ trong `ensureWindowsRepresentable`); 4. chạy khi máy tắt → dùng VPS luôn bật.
- Free / tổng + giá: 100% free, 0đ (MIT — nguồn `package.json` + `LICENSE`, đọc 07/11/2026). Chi phí thật: máy giữ online + token LLM mỗi lần job chạy (trả theo provider model, không thuộc plugin).
- Ma sát cài đặt: 1 bước khai báo plugin trong `opencode.json` + restart OpenCode. ĐÃ mở kiểm tra đến bước đọc `schedule_job` (`src/index.ts` dòng 2540), `findOpencode` + `getEnhancedPath`, 4 backend install, supervisor Perl. Chưa chạy end-to-end (máy này không có `opencode` CLI — ghi rõ, không bịa output). Rào cản: cần `opencode` CLI trong PATH; `/usr/bin/perl`; backend OS tương ứng; API key/model auth cho `opencode run` (issue #12 mất env trên launchd; `opencode-scheduler.json` `env.set/preserve` để bù).
- Đối thủ viral cùng phân khúc: `n8n-io/n8n` (204k★/60,6k forks, fair-code, 400+ integrations) vs chạy tay OS scheduler + `opencode run` (0 cài thêm, nền `anomalyco/opencode` 225k★). Số đo 07/11/2026 qua webfetch GitHub + npm registry.
- Chọn nó thay vì đối thủ khi: cần job prompt lặp lại ngay trong OpenCode bằng 1 câu tiếng tự nhiên + quản lý bằng 11 tools, không muốn dựng server workflow hay viết plist/service tay. Ví dụ đổi lựa chọn: brief "mỗi sáng 9h tóm notifications" trên laptop mac → plugin (timer + log + scope sẵn); brief "deal mới → enrich → CRM → Slack có duyệt tay" → n8n.
- TUYỆT ĐỐI không dùng khi: job cần tương tác (QR/login/confirm — scheduled run ép deny); máy NixOS/Windows cron phức tạp/OpenCode 2.0 chưa port; cần chạy khi máy tắt hẳn; muốn nhét secret vào prompt thay vì `env.set`.

### Usecase con 1: lập lịch prompt định kỳ
- Khi dùng: có 1 prompt lặp lại theo giờ cố định và muốn OS tự gọi khi đến giờ, kể cả sau giấc ngủ máy.
- Khi bỏ qua: chỉ chạy 1 lần → `opencode run` trực tiếp; cần rẽ nhánh/integration → n8n; cron Windows phức tạp → tách job hoặc đổi OS.
- Cơ chế khác các usecase khác ở đâu: duy nhất ghi job JSON + snapshot `invocation` + cài timer OS (launchd plist / systemd service+timer `Persistent=true` / schtasks / crontab block); các usecase khác chỉ đọc/sửa/log, không đụng backend OS.
- Lệnh copy-paste (đã đối chiếu README + `src/index.ts` dòng 2540): trong TUI OpenCode sau khi khai plugin, ra lệnh `Schedule a daily job at 9am to search Facebook Marketplace for posters under $100 and send the top 5 deals to my Telegram` (plugin tự map thành `schedule_job` với `schedule: 0 9 * * *`). Cron copy được: `0 9 * * *` (hằng ngày 9h), `0 */6 * * *` (mỗi 6 giờ), `30 8 * * 1` (thứ 2 8h30), `0 9,17 * * *` (9h + 17h).
- Ngưỡng số cần đạt: cron đúng 5-field (sai → `Invalid cron`); slug từ tên (`standing desk` → `standing-desk`); job file sinh tại `scopes/<scopeId>/jobs/<slug>.json` (scopeId = basename + 12 ký tự hash từ workdir); timer OS tồn tại (`launchctl list | grep opencode` / `systemctl --user list-timers | grep opencode` / `schtasks /Query /TN "\\OpenCode\\opencode-job-*"`).
- Ví dụ input-output (minh họa, không phải mặc định — cron nào cũng phải diễn giải + user chốt trước): input "mỗi sáng 9h săn standing desk dưới $300" → output job `standing-desk`, `schedule: 0 9 * * * (daily at 9:00 AM)`, `Platform: launchd/systemd`, log `~/.config/opencode/logs/scheduler/<scopeId>/standing-desk.log`, metadata `lastRunAt/lastRunStatus`.
- Pitfalls riêng: trùng tên trong scope → `already exists in this workspace scope`; legacy pre-v1.2.0 ở `~/.config/opencode/jobs/` gây nhầm → dùng `includeLegacy:true` khi list; Windows cron phức tạp → lỗi rõ + tách job; cron fallback không catch-up khi ngủ.
- Phân công usecase này: agent chính diễn giải cron + chốt scope/workdir với user trước khi gọi `schedule_job`; giao claude kiểm tra timer OS ngoài terminal khi cần; verify bằng job file + timer OS + log có dòng `Scheduled run`.

### Usecase con 2: run-spec nâng cao (command/model/attachUrl/timeout)
- Khi dùng: job không chỉ là prompt thuần mà cần `command`/`agent`/`model`/`files`/`attachUrl`/`timeoutSeconds`/`workdir` riêng (vd chạy `opencode run --command` hoặc bám backend `opencode serve`).
- Khi bỏ qua: prompt thuần hằng ngày → Usecase 1; chỉ xem/sửa/xóa → Usecase 3.
- Cơ chế khác các usecase khác ở đâu: duy nhất build `invocation` (`buildOpencodeArgs`) map run-spec thành flags `opencode run` (`--command/--agent/--model/--file/--title/--format/...`) + snapshot vào job để scheduled run ổn định khi sửa run; Usecase 1 chỉ cần prompt + cron, Usecase 3 không build invocation.
- Lệnh copy-paste: `Schedule a daily job at 9am from /path/to/project to run my-task` (map `workdir` để lấy đúng `opencode.json`/MCP) và `Update the standing-desk job to use attachUrl http://localhost:4096` (map `attachUrl`) và `schedule_job` với `timeoutSeconds: 600` (quá 600s → SIGTERM, 5s sau SIGKILL). Nguồn README mục Tools + Reference + `src/index.ts` `schedule_job`/`update_job`.
- Ngưỡng số cần đạt: `timeoutSeconds` số nguyên, 0 = tắt; `attachUrl` URL backend `opencode serve/web` còn sống; `workdir` absolute path tồn tại, chứa `opencode.json` MCP cần thiết; files map thành từng `--file` lặp lại.
- Ví dụ input-output (minh họa): input "job check site mỗi 6h, ngắt sau 10 phút, bám backend local 4096" → output job có `timeoutSeconds: 600`, `attachUrl: http://localhost:4096`, supervisor log dòng `Timeout after 600 seconds` khi quá giờ.
- Pitfalls riêng: Windows scheduled run hiện không qua supervisor → no-overlap/timeout không đảm bảo; `OPENCODE_PERMISSION` ép `question: deny` nên job nào cần hỏi là treo-thành-skip; sai `workdir` → thiếu MCP/env (issue #12).
- Phân công usecase này: agent chính shortlist model/command/files/timeout kèm lý do, user pick mới gọi tool; giao claude xác minh backend `attachUrl` sống; verify bằng `get_job` hiện đủ `run` fields + `invocation.command/args`.

### Usecase con 3: giám sát và vòng đời job
- Khi dùng: đã có job và cần xem/sửa/chạy ngay/xóa/dọn (vận hành hằng ngày).
- Khi bỏ qua: tạo job mới → Usecase 1/2; cài skill → Usecase 4.
- Cơ chế khác các usecase khác ở đâu: chỉ đọc/ghi job JSON + log + lock, không cài timer mới (trừ `update_job` đổi cron thì ghi lại timer); `run_job` spawn `opencode run` fire-and-forget, không qua supervisor Perl.
- Lệnh copy-paste: `Show my scheduled jobs` (`list_jobs`, mặc định current scope; `allScopes:true` đa scope) → `Show details for standing-desk` (`get_job`) → `Show logs for standing-desk` (`job_logs`, `tailLines/maxChars`) → `Run the standing-desk job now` (`run_job`) → `Update standing-desk to run at 10am` (`update_job`) → `Delete the standing-desk job` (`delete_job` xoá cả scoped + legacy) → `Run scheduler global cleanup` (`cleanup_global`, mặc định dry-run `{confirm:false}`, xoá thật `{confirm:true}`, kèm history `{confirm:true, includeHistory:true}`).
- Ngưỡng số cần đạt: `get_job`/`job_logs` của scope khác trả `not found` trừ khi `allScopes:true` (issue #11 đúng bẫy này); log ≤5000 chars mặc định, `tailLines` kẹp 1–5000; `delete_job` gỡ cả unit OS scoped + legacy; `cleanup_global` báo số artifacts theo nhóm jobs/locks/logs/runs/units.
- Ví dụ input-output (minh họa): input `list_jobs` ở project A → output chỉ job scope A; input `list_jobs` với `allScopes:true` → output mọi scope + legacy khi `includeLegacy:true`; input `job_logs` → output đuôi log có `=== Scheduled run <ISO> runId=... ===` hoặc `=== Manual run ... ===`.
- Pitfalls riêng: nhầm scope là lỗi phổ biến nhất (tên giống nhau khác workdir); `run_job` không chống overlap (chỉ scheduled run có lock); xóa mà timer OS còn sót → kiểm tra lại bằng lệnh OS.
- Phân công usecase này: agent chính gọi đúng tool + truyền `allScopes/includeLegacy/confirm` tường minh sau khi hỏi user khi thao tác xóa/dọn; giao claude mở log dài trên browser khi tail lớn; verify bằng `get_job` sau mỗi mutate + log có marker run.

### Usecase con 4: skill best-practices và version
- Khi dùng: muốn prompt job bền (non-interactive + idempotent + quan sát được) hoặc cần biết bản plugin/opencode đang chạy.
- Khi bỏ qua: đã có skill trong repo → không cài lại; chỉ lập lịch thuần → Usecase 1.
- Cơ chế khác các usecase khác ở đâu: không chạy agent, chỉ đọc/ghi file skill tĩnh (`SKILL.md` 1 mẫu duy nhất `scheduled-job-best-practices`) và đọc `package.json` + `opencode --version`; các usecase khác đều chạm job runtime.
- Lệnh copy-paste: `Install the scheduled job best practices skill` (`install_skill` → ghi `.opencode/skill/scheduled-job-best-practices/SKILL.md`; đã tồn tại thì cần `overwrite:true`) và `Get skill from opencode-scheduler and add it to my skills` (`get_skill`) và `Show scheduler version` (`get_version`). Sau cài, thêm `@scheduled-job-best-practices` lên đầu mọi prompt job.
- Ngưỡng số cần đạt: đúng 1 skill (`scheduled-job-best-practices`, alias `job-best-practices/scheduled-jobs/scheduler`); file ghi đúng `suggestedPath`; `get_version` trả cả 2 bản (plugin + opencode).
- Ví dụ input-output (mẫu thật từ `src/index.ts`): skill ép tính ngày bằng `TODAY="$(date +%F)"` (mac `date -v+1d`, linux `date -d`), checklist preflight (tool/env sẵn sàng mới chạy), output contract `Status/Reason/Outputs/Notifications`, idempotency qua `outputs/<job>/seen.json`.
- Pitfalls riêng: cài đè không báo `overwrite` → lỗi `File already exists`; quên `@...` ở đầu prompt → skill không có tác dụng; skill là prose, không thay được supervisor/timeout máy.
- Phân công usecase này: agent chính cài skill + nhắc user chèn `@` vào prompt job; không cần claude; verify bằng file `SKILL.md` tồn tại + `get_version` có output.

### Các bước chung
1. Khai plugin 1 dòng trong `opencode.json` + restart OpenCode, verify bằng `Show scheduler version`.
2. Chốt cron (diễn giải giờ đọc được) + nội dung (prompt hay command/model/files) + `workdir`/`attachUrl`/`timeoutSeconds` với user trước khi gọi tool.
3. Cài skill `scheduled-job-best-practices` 1 lần, chèn `@scheduled-job-best-practices` vào đầu prompt job.
4. Gọi `schedule_job` bằng tiếng tự nhiên, đọc `scopeId` + timer platform trả về.
5. Vận hành bằng Usecase 3 (`list/get/logs/run/update/delete/cleanup` với đúng scope và `confirm` tường minh).
6. Khi job lỗi: đọc `job_logs` trước, rồi kiểm tra timer OS, rồi kiểm tra `workdir` có `opencode.json`/MCP/env.

### Prompt mẫu
- "Schedule a daily job at 9am to search Facebook Marketplace for posters under $100 and send the top 5 deals to my Telegram. Chốt cron `0 9 * * *` và workdir trước khi cài."
- "Schedule a job every 6 hours to check if my website is up and alert me on Slack if it is down. Đặt `timeoutSeconds: 600` để không treo."
- "Show my scheduled jobs với `allScopes:true`, rồi show logs cho job lỗi nhiều nhất, chỉ rõ scope nào."
- "Install the scheduled job best practices skill, rồi viết lại prompt job săn desk theo Output Contract Status/Reason/Outputs/Notifications."

### Pitfalls
- OpenCode 2.0 fail load (issue #28, 11/10/2026): plugin chưa port `Plugin.define + ctx.tool.transform` → không dùng bản này trên OpenCode 2.0.
- NixOS sai `OnCalendar` + hardcode `/usr/bin/perl` + PATH macOS-only (issue #14, 12/04/2026) → không dùng trên NixOS khi chưa fix.
- Windows `schtasks` bare `opencode` FILE NOT FOUND (issue #25, 10/09/2026) + ghost jobs do scope workdir (issue #13, 30/03/2026) → Windows chỉ cron đơn, kiểm tra `schtasks /Query` sau cài.
- Launchd plist thiếu API key env (issue #12, 26/03/2026) → bù bằng `~/.config/opencode/opencode-scheduler.json` (`env.set/preserve`, `preserveOpencodeEnv`), không nhét secret vào prompt.
- `get_job`/`job_logs` `not found` dù `list_jobs --allScopes` thấy (issue #11, 18/03/2026) → luôn kèm đúng scopeId khi đọc/log.
- Cron fallback không catch-up khi ngủ; systemd cần `Persistent=true` mới catch-up; Windows không qua supervisor nên mất no-overlap/timeout.
- `run_job` fire-and-forget, không lock → bấm 2 lần là chạy 2 tiến trình.

### Tham khảo sử dụng (số chốt 07/11/2026; code đọc 07/11/2026)
- Nhận xét sâu: `rogs.me/2026-04` "OpenCode as a server: AI agents that work while I sleep" — "scheduler plugin + systemd timers, 30 phút setup, jobs saved hours every week" → xác nhận quyết định dùng cho máy luôn bật, lật từ "plugin 500★ chưa kiểm chứng" thành "đáng thử cho 1 job thật". Nguồn độc lập có URL + ngày, không ẩn danh.
- Nhận xét sâu thứ 2: `opencode.ai/docs/ecosystem` liệt kê `opencode-scheduler` trong bảng plugin chính thức ("Schedule recurring jobs using launchd (Mac) or systemd (Linux) with cron syntax") → xác nhận không phải plugin trôi nổi. `composio.dev/content/best-opencode-plugins` xếp vào nhóm best plugins.
- Số trung bình có trọng số: 517★ / 45 forks / 13 issues mở / 2 watchers (GitHub 07/11/2026) + npm 1.3.0 (17/02/2026, chuỗi 0.1.0→1.3.0 trong 6 tuần). Trọng số: 517★ nhỏ hơn `n8n` 204k★ khoảng 400 lần và nhỏ hơn nền `anomalyco/opencode` 225k★ — tin cậy thấp hơn hẳn, phải đọc issues trước khi dùng production. Không có ratings/installs trung tâm (plugin phân tán qua npm + GitHub).
- Mâu thuẫn: review sâu khen gọn-nhẹ vs 13 issues mở toàn lỗi nền (2.0/NixOS/Windows/API key/scope) → phán quyết: dùng tốt trên macOS/Linux stock + OpenCode 1.x, tránh Windows/NixOS/OpenCode 2.0 cho tới khi #28, #14, #25 đóng.
- Tiếng Việt: không tìm thấy review Việt → `chưa xác minh`.

### Tham khảo
- Repo + Install + How It Works + bảng backend/tools/storage: https://github.com/different-ai/opencode-scheduler (đọc 07/11/2026; MIT; v1.3.0).
- Nguồn đã mở kiểm tra: `src/index.ts` (11 tools dòng 2540–3277, `deriveScopeId` dòng 87, `findOpencode` dòng 623, `createLaunchdPlist` dòng 1037, `createSystemdService/Timer` dòng 1136/1174, `schtasks` dòng 1252, cron fallback dòng 1319, `buildRunEnvironment` dòng 2231, `runJobNow` dòng 2294), `package.json` (v1.3.0), `PRD-resilient-execution.md` (roadmap resiliency chưa làm), npm registry `opencode-scheduler` (time.created 06/01/2026, 1.3.0 modified 17/02/2026).
- Issues đã đọc: #28 (OpenCode 2.0), #27/#3 (systemd OnCalendar), #25/#13 (Windows), #14 (NixOS), #12 (API key), #11 (scope), #16 (PATH), #15 (fn3), #20 (phantom), #8 (commands), #2 (Windows support).
- Đối thủ: https://github.com/n8n-io/n8n (204k★/60,6k forks 07/11/2026) + https://github.com/anomalyco/opencode (225k★ nền cho đường chạy tay).
- Review: https://rogs.me/2026/04/opencode-as-a-server-ai-agents-that-work-while-i-sleep + https://opencode.ai/docs/ecosystem + https://composio.dev/content/best-opencode-plugins.

### Được dùng ở đâu
- Dùng CHO automation (job định kỳ, polling, nhắc việc, dọn artifacts): xem `../../domains/automation/using-opencode-scheduler.md` — index `../../domains/automation/README.md`.

### Quay lại index
- Về `../../domains/automation/README.md` (so job prompt lặp lại vs workflow n8n vs chạy tay khi backend OS lỗi).
- Xem thêm item liên quan: chưa có (domain automation mới chỉ có 1 item).

---

## English

### When to use
- Recurring OpenCode prompts (daily, Monday weekly, every 6 hours) on your own macOS/Linux/Windows machine.
- Jobs that catch up after sleep, never overlap, auto-kill on timeout, with per-project log isolation.
- OpenCode plugin host (`plugin` in `opencode.json`); `opencode` CLI + OS backend + `/usr/bin/perl`.
- Natural-language scheduling inside the OpenCode TUI instead of hand-written plists/services.

### When to skip
- Multi-step branching workflows, 400+ integrations, drag-drop UI → use `n8n-io/n8n` instead (see [Differentiating positioning](#differentiating-positioning-github-numbers-07112026)).
- Complex retry/queues/server-side SLA, or running while the machine is fully off → no OS scheduler covers it; use an always-on VPS + `opencode serve` or a cloud workflow platform.
- NixOS, complex Windows cron, or OpenCode 2.0 → stop (3 open issues, see [Pitfalls](#pitfalls)).
- One-shot runs → call `opencode run` directly.

### Install (repo + npm + source read 07/11/2026; no end-to-end run — no `opencode` CLI on this machine)
- Single route (per origin README): add to project `opencode.json`:
- `{"plugin": ["opencode-scheduler"]}`
- Restart OpenCode, then prompt `Schedule a daily job at 9am to summarize my GitHub notifications`.
- Sources read: `package.json` (v1.3.0, MIT, Benjamin Shafii), `src/index.ts` (3,315 lines, 11 tools), `README.md` (4 backends + 11 tools + storage), npm `opencode-scheduler@1.3.0` (17/02/2026).
- Requires: `opencode` CLI on PATH; macOS `launchctl`, Linux `systemctl --user` or `crontab`, Windows `schtasks`; `/usr/bin/perl` for the supervisor.
- Check (no real job needed): `Show scheduler version` → `get_version` returns plugin + `opencode --version`.

### How the item works
- Backing organization: `different-ai` (Benjamin Shafii), repo `https://github.com/different-ai/opencode-scheduler`, MIT, npm v1.3.0 (17/02/2026; 0.1.0 Jan 2026 → 1.3.0 Feb 2026). 28 commits. GitHub 07/11/2026: 517 stars / 45 forks / 13 open issues / 2 watchers.
- Core operating method: thin wrapper around `opencode run`. 1 of 11 tools → job JSON (+ `invocation` snapshot) in `~/.config/opencode/scheduler/scopes/<scopeId>/jobs/*.json` → OS timer installed → at fire time the OS calls `supervisor.pl` → overlap lock, forced `OPENCODE_PERMISSION={"question":"deny"}`, `opencode run`, appended logs + metadata + JSONL history. `run_job` is fire-and-forget without the supervisor.
- Per-usecase operating differences: periodic prompt scheduling (writes job + OS timer, see [Sub-usecase 1](#sub-usecase-1-periodic-prompt-scheduling)) vs advanced run-spec (maps command/model/files/attachUrl/timeout to `opencode run` flags, see [Sub-usecase 2](#sub-usecase-2-advanced-run-spec-commandmodelattachurltimeout)) vs monitoring + lifecycle (reads/mutates/logs, no scheduler writes, see [Sub-usecase 3](#sub-usecase-3-job-monitoring-and-lifecycle)) vs skill + version (static skill file only, see [Sub-usecase 4](#sub-usecase-4-best-practices-skill-and-version)).

### Invariant core
- Every periodic job goes through `schedule_job` + 5-field cron + `workdir` scope (`deriveScopeId`, 12-char hash). Hand-written units outside the plugin are not using the system.
- Job prompts must be non-interactive + idempotent per `scheduled-job-best-practices` (`@scheduled-job-best-practices` first line, `bash date`, seen-file, `outputs/`). Jobs waiting on QR/login/confirmations = FAIL.
- After use, state slug + cron + scopeId + reused artifact. Cannot = not really used.
- See [Sub-usecase 1](#sub-usecase-1-periodic-prompt-scheduling) and [Shared steps](#shared-steps).

### Customizable surface
- Tunable: `schedule`, `prompt` or `command/arguments/files/agent/model/variant/title/share/continue/session/runFormat/port`, `workdir`, `attachUrl`, `timeoutSeconds` (0 = off). Two-level gate: (1) which cron + what runs — human-readable `describeCron` approved pre-install; (2) what stays/changes on `update_job`. Sole waiver (dropping a timeout) must quote the explicit user ok. Never list `must-not` items here.
- See [Sub-usecase 2](#sub-usecase-2-advanced-run-spec-commandmodelattachurltimeout) and [Decision dossier](#decision-dossier).

### Work split
- Main agent: settle cron + payload + workdir/attachUrl/timeout with the user (question tool, user picks before any tool call) → call the right tool with explicit scope/`confirm` → verify via `job_logs`/`get_job`.
- Hand to claude: browser/account steps (long-log inspection, `attachUrl` backend checks, OS timer checks without shell) with slug + scopeId; never invent job output.
- Agent verifies: job file + OS timer + appended `Scheduled/Manual run` log lines + updated `lastRunStatus`.
- Per-usecase details in Sub-usecases 1–4.

### Differentiating positioning (GitHub numbers, 07/11/2026)
- Vs `n8n-io/n8n` (fair-code automation, 204k stars/60.6k forks, 400+ integrations): server workflow with UI/nodes/queues vs thin OS-timer wrapper with no server/UI/branching. Pick this over n8n for one recurring prompt inside OpenCode with one plugin line; pick n8n for nodes/integrations/branching/visual retry.
- Vs hand-rolled `cron/systemd/launchd + opencode run` (baseline, base `anomalyco/opencode` 225k stars, zero installs): hand-rolled means self-written units + self-owned overlap/timeout/logs; the plugin ships the supervisor envelope (lock, deny-questions, SIGTERM→SIGKILL, atomic metadata). Pick the plugin for sleep catch-up, project scopes, and natural-language ops; pick hand-rolled on NixOS/complex Windows/OpenCode 2.0 (open issues #28/#14/#25) or when every unit line must be owned.
- Honest frame: wins on in-OpenCode leanness ($0 MIT); loses on workflow scale (n8n 204× stars) and on hand control when OS backends break.

### Coverage map (full README + 3,315-line `src/index.ts` + 11 tools + 4 backends scanned 07/11/2026 — ★ strongest first)
- ★ Periodic prompt scheduling (`schedule_job` + cron + scope): see Sub-usecase 1.
- Advanced run-spec (command/model/files/attachUrl/timeout → `opencode run` flags): see Sub-usecase 2.
- Monitoring + lifecycle (`list/get/logs/run/update/delete/cleanup_global`): see Sub-usecase 3.
- Medium: best-practices skill + version (`get_skill/install_skill/get_version`): see Sub-usecase 4.
- Medium: 4 OS backends (supervised launchd / supervised systemd / schtasks cron subset / cron fallback without catch-up).
- NOT supported → replacements: policy retry/queues → n8n or own worker (`PRD-resilient-execution.md` is roadmap-only); complex month+weekday Windows cron → split jobs or mac/Linux; fully-off machines → always-on VPS; OpenCode 2.0 → wait for the port (#28).

### Decision dossier
- Jobs SERVED (3+): 1. daily 9am deal hunt (`0 9 * * *`); 2. 6-hour uptime polling (`0 */6 * * *`); 3. Monday report (`30 8 * * 1`); 4. multi-scope cleanup (`cleanup_global` dry-run then `confirm:true`).
- Jobs NOT served (3+, each with replacement): 1. branching/integration workflows → `n8n`; 2. SLA retry/queues → workers/cloud schedulers; 3. complex Windows month+weekday cron → mac/Linux or split jobs; 4. fully-off machines → always-on VPS.
- Free / total + price: 100% free, $0 (MIT). Real cost: an online machine + per-run LLM tokens.
- Install friction: 1 step (plugin line + restart). Read through `schedule_job`, `findOpencode`, 4 backend installers, Perl supervisor. No end-to-end run (no `opencode` CLI here — stated, not invented). Barriers: `opencode` CLI on PATH; `/usr/bin/perl`; matching OS backend; model auth (issue #12; `opencode-scheduler.json` `env.set/preserve` compensates).
- Viral same-segment opponents: `n8n-io/n8n` (204k/60.6k, fair-code, 400+ integrations) vs hand-rolled OS scheduler + `opencode run` (zero installs, base `anomalyco/opencode` 225k). Measured 07/11/2026 via GitHub webfetch + npm registry.
- Pick it over opponents when: one recurring prompt inside OpenCode via one natural sentence + 11-tool ops, no workflow server or hand-written units wanted.
- NEVER use when: interactive jobs; NixOS/complex Windows/OpenCode 2.0; fully-off machines; secrets pasted into prompts.

### Sub-usecase 1: periodic prompt scheduling
- When to use: one fixed-hour prompt the OS should fire, including post-sleep catch-up.
- When to skip: one-shot → direct `opencode run`; branching/integrations → n8n; complex Windows cron → split or switch OS.
- Mechanism difference: the only flow writing job JSON + `invocation` snapshot + OS timer; others only read/mutate/log.
- Copy-paste command: `Schedule a daily job at 9am to search Facebook Marketplace for posters under $100 and send the top 5 deals to my Telegram` (maps to `schedule_job`, `schedule: 0 9 * * *`). Copyable crons: `0 9 * * *`, `0 */6 * * *`, `30 8 * * 1`, `0 9,17 * * *`.
- Numeric bar: valid 5-field cron; slug from name; job at `scopes/<scopeId>/jobs/<slug>.json`; OS timer present.
- Input-output example (illustrative): "9am standing-desk hunt under $300" → job `standing-desk`, `daily at 9:00 AM`, platform line, per-scope log, `lastRunAt/lastRunStatus`.
- Own pitfalls: same-name collision in scope; legacy `~/.config/opencode/jobs/` confusion → `includeLegacy:true`; complex Windows cron → guided error + split; cron fallback has no catch-up.
- Work split for this sub-usecase: main agent settles cron + scope pre-call; claude checks OS timers without shell when needed; verify via job file + timer + `Scheduled run` log.

### Sub-usecase 2: advanced run-spec (command/model/attachUrl/timeout)
- When to use: jobs needing command/agent/model/files/attachUrl/timeout/workdir (not plain prompts).
- When to skip: plain daily prompt → Sub-usecase 1; pure ops → Sub-usecase 3.
- Mechanism difference: only flow building `invocation` via `buildOpencodeArgs` into `opencode run` flags + snapshotting it.
- Copy-paste command: `Schedule a daily job at 9am from /path/to/project to run my-task` (workdir) + `Update the standing-desk job to use attachUrl http://localhost:4096` + `timeoutSeconds: 600` (SIGTERM then SIGKILL after 5s).
- Numeric bar: integer `timeoutSeconds`, 0 = off; live `attachUrl`; existing absolute `workdir` with `opencode.json`.
- Input-output example (illustrative): 6h site check + 10-minute cap + local 4096 backend → `timeoutSeconds: 600`, `attachUrl`, `Timeout after 600 seconds` log line when hit.
- Own pitfalls: Windows runs skip the supervisor (no overlap/timeout); forced `question: deny` skips interactive jobs; wrong `workdir` loses MCP/env (#12).
- Work split for this sub-usecase: main agent shortlists model/command/timeout, user picks; claude verifies `attachUrl`; verify via `get_job` run fields + invocation.

### Sub-usecase 3: job monitoring and lifecycle
- When to use: list/read/run/edit/delete/clean existing jobs.
- When to skip: new jobs → Sub-usecases 1/2; skills → Sub-usecase 4.
- Mechanism difference: job JSON + log + lock reads/writes only; `run_job` spawns without the Perl supervisor.
- Copy-paste command: `Show my scheduled jobs` (`list_jobs`, `allScopes:true` for all) → `Show details for standing-desk` (`get_job`) → `Show logs for standing-desk` (`job_logs`) → `Run the standing-desk job now` (`run_job`) → `Update standing-desk to run at 10am` (`update_job`) → `Delete the standing-desk job` (`delete_job`) → `Run scheduler global cleanup` (`cleanup_global`, `{confirm:false}` dry-run, `{confirm:true}` real, `includeHistory:true` with logs).
- Numeric bar: cross-scope reads need `allScopes:true` (#11); logs default 5000 chars, `tailLines` clamped 1–5000; deletes remove scoped + legacy OS units; cleanup reports per-group counts.
- Input-output example (illustrative): project-A `list_jobs` → scope-A jobs only; `allScopes:true` → all scopes; `job_logs` → tail with `=== Scheduled run <ISO> runId=... ===`.
- Own pitfalls: same name in different workdirs is the top confusion; `run_job` has no overlap lock; stale OS timers need manual re-check.
- Work split for this sub-usecase: main agent passes explicit scope/`confirm` (ask before delete/clean); claude opens long logs in a browser; verify via post-mutate `get_job` + run markers.

### Sub-usecase 4: best-practices skill and version
- When to use: durable job prompts or checking running versions.
- When to skip: skill already installed; pure scheduling → Sub-usecase 1.
- Mechanism difference: static skill file only, no agent run.
- Copy-paste command: `Install the scheduled job best practices skill` (`install_skill` → `.opencode/skill/scheduled-job-best-practices/SKILL.md`, `overwrite:true` to replace) + `Get skill from opencode-scheduler and add it to my skills` (`get_skill`) + `Show scheduler version` (`get_version`). Prefix every job prompt with `@scheduled-job-best-practices`.
- Numeric bar: exactly 1 skill (aliases `job-best-practices/scheduled-jobs/scheduler`); exact `suggestedPath`; `get_version` returns both versions.
- Input-output example (real template): `TODAY="$(date +%F)"`, preflight checklist, `Status/Reason/Outputs/Notifications` contract, `outputs/<job>/seen.json` idempotency.
- Own pitfalls: re-install without `overwrite` errors `File already exists`; missing `@` prefix disables the skill; prose cannot replace supervisor/timeouts.
- Work split for this sub-usecase: main agent installs + reminds the `@` prefix; no claude needed; verify via file existence + version output.

### Shared steps
1. Declare the plugin line in `opencode.json` + restart, verify with `Show scheduler version`.
2. Settle cron (human-readable) + payload + workdir/attachUrl/timeout with the user pre-call.
3. Install `scheduled-job-best-practices` once, prefix job prompts with `@scheduled-job-best-practices`.
4. Call `schedule_job` in natural language, record `scopeId` + platform.
5. Operate via Sub-usecase 3 with exact scopes and explicit `confirm`.
6. On failure: `job_logs` first, then OS timer, then `workdir` MCP/env.

### Sample prompts
- "Schedule a daily job at 9am to search Facebook Marketplace for posters under $100 and send the top 5 deals to my Telegram. Settle cron `0 9 * * *` and workdir pre-install."
- "Schedule a job every 6 hours to check if my website is up and alert me on Slack if it is down. Cap with `timeoutSeconds: 600`."
- "Show my scheduled jobs with `allScopes:true`, then show logs for the most failing job, naming its scope."
- "Install the scheduled job best practices skill, then rewrite the desk-hunt prompt to the Status/Reason/Outputs/Notifications contract."

### Pitfalls
- OpenCode 2.0 load failure (#28, 11/10/2026): no `Plugin.define + ctx.tool.transform` port yet.
- NixOS wrong `OnCalendar` + hardcoded `/usr/bin/perl` + macOS-only PATH (#14, 12/04/2026).
- Windows bare-`opencode` FILE NOT FOUND (#25, 10/09/2026) + workdir ghost jobs (#13, 30/03/2026) → simple crons only, re-check `schtasks /Query`.
- Launchd plist missing API-key env (#12, 26/03/2026) → compensate via `opencode-scheduler.json` (`env.set/preserve`), never paste secrets into prompts.
- Cross-scope `not found` despite `--allScopes` listing (#11, 18/03/2026) → always carry the exact scopeId.
- Cron fallback has no sleep catch-up; only systemd `Persistent=true` catches up; Windows skips the supervisor (no overlap/timeout).
- `run_job` is lock-free — double-invoking runs twice.

### Usage references (numbers pinned 07/11/2026; code read 07/11/2026)
- Deep review: `rogs.me/2026-04` "OpenCode as a server" — "scheduler plugin + systemd timers, 30-minute setup, jobs saved hours every week" → confirms always-on-machine use, flipping "500-star unproven" to "worth one real job". Independent sourced review with date.
- Second deep signal: `opencode.ai/docs/ecosystem` lists `opencode-scheduler` ("Schedule recurring jobs using launchd (Mac) or systemd (Linux) with cron syntax") → not a drifting plugin. `composio.dev/content/best-opencode-plugins` ranks it among best plugins.
- Weighted average: 517 stars / 45 forks / 13 open issues / 2 watchers (GitHub 07/11/2026) + npm 1.3.0 (17/02/2026, 0.1.0→1.3.0 in 6 weeks). Weight: 517 stars is ~400× smaller than `n8n` 204k and far below base `anomalyco/opencode` 225k — much lower trust weight, read issues before production. No central ratings/installs (npm + GitHub distribution).
- Conflict: deep praise for leanness vs 13 open foundation issues (2.0/NixOS/Windows/API-key/scope) → verdict: good on stock macOS/Linux + OpenCode 1.x, avoid Windows/NixOS/OpenCode 2.0 until #28, #14, #25 close.
- Vietnamese: no Vietnamese review found → `unverified`.

### References
- Origin + install + 4-backend/tool/storage reference: https://github.com/different-ai/opencode-scheduler (read 07/11/2026; MIT; v1.3.0).
- Checked sources: `src/index.ts` (11 tools lines 2540–3277, `deriveScopeId` line 87, `findOpencode` line 623, launchd line 1037, systemd lines 1136/1174, schtasks line 1252, cron fallback line 1319, `buildRunEnvironment` line 2231, `runJobNow` line 2294), `package.json` (v1.3.0), `PRD-resilient-execution.md` (unbuilt resiliency roadmap), npm `opencode-scheduler` (created 06/01/2026, 1.3.0 modified 17/02/2026).
- Issues read: #28 (OpenCode 2.0), #27/#3 (systemd OnCalendar), #25/#13 (Windows), #14 (NixOS), #12 (API key), #11 (scope), #16 (PATH), #15 (fn3), #20 (phantom), #8 (commands), #2 (Windows support).
- Opponents: https://github.com/n8n-io/n8n (204k/60.6k 07/11/2026) + https://github.com/anomalyco/opencode (225k base for hand-rolled).
- Reviews: https://rogs.me/2026/04/opencode-as-a-server-ai-agents-that-work-while-i-sleep + https://opencode.ai/docs/ecosystem + https://composio.dev/content/best-opencode-plugins.

### Where used
- Used FOR automation (periodic jobs, polling, reminders, artifact cleanup): see `../../domains/automation/using-opencode-scheduler.md` — index `../../domains/automation/README.md`.

### Back to index
- Back to `../../domains/automation/README.md` (recurring prompt jobs vs n8n workflows vs hand-rolled on broken OS backends).
- Related item: none yet (automation starts with 1 item).
