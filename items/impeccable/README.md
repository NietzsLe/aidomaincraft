# impeccable

## Tiếng Việt

### Dùng khi
- Cần vốn từ design cho agent khi chưa gọi tên được thay đổi ("trang trông AI-slop"): 24 lệnh `/impeccable <động từ> <target>` (polish/bolder/critique/audit/typeset/layout/colorize/animate...).
- Cần detector máy (không LLM, không API key) quét slop + lỗi quality ngay khi agent sửa file (hook), ở CI (`detect` exit 0/2/1) hoặc trên trang sống (Chrome extension overlay).
- Cần review xếp hạng ưu tiên: `critique` (đánh giá heuristic UX) / `audit` (kỹ thuật a11y/perf/responsive/theming, rank từ P0 chặn merge tới P3).
- Cần so sánh trực quan rồi mới chốt code: `live` (pick element so sánh ngay trên trang chạy, Steer là chỉ hướng toàn trang không cần pick) / `generate` (biến thể rồi accept vào source).
- Có `DESIGN.md` muốn giữ: `document` ghi system, detector check drift (font/color/radius/size ngoài system).

### Bỏ qua khi
- Cần system/design mới pass gates máy cứng (contrast 4.5:1, fold 1280x800, word budget) + hero-first + log chống lặp shape → dùng `../hallmark/` (Impeccable không có gates số).
- Cần 1 pass checklist `file:line` dưới 10 phút, không đổi file → dùng `../web-interface-guidelines/` (Impeccable sửa tới nơi nên chậm hơn).
- Cần bricks React animated sở hữu source → dùng `../reactbits/` (Impeccable không cho component nào).
- Offline hoàn toàn hoặc chặn `impeccable.style/api/*`: detector local vẫn chạy nhưng direction catalog + version check cần mạng (catalog local chưa xác minh) → cân nhắc bỏ.
- Native iOS/Android/adaptive: hook bỏ qua khi `PRODUCT.md` khai các platform này → chỉ dùng `audit` thủ công, không kỳ vọng hook/Live.

### Cài đặt
- Yêu cầu: Node 18.19+ (`node --version`; bản ghim 4.5.2 đòi Node 22.18+ theo ssdnodes 31/10/2026 — cài latest 4.8.1 thì 18.19+ đủ theo `/tutorials/getting-started`).
- Cài: `npx impeccable install` (chọn tool + project/global) → reload tool → `/impeccable init` (ghi `PRODUCT.md`). Cập nhật: `npx impeccable update`. Nguồn: homepage + `/tutorials/getting-started` + GitHub README (đã fetch 08/11/2026).
- Kênh khác: plugin marketplace (`plugin marketplace add pbakaus/impeccable`), skills.sh (`npx skills add pbakaus/impeccable`), submodule ghim version, copy tay/ZIP (README.txt chỉ thư mục, không lồng thêm).
- Hook (nên bật): Claude Code/Cursor/Codex/Copilot/Grok Build/Hermes tự đề xuất; Codex cần approve `/hooks`, Grok `/hooks-trust` (hoặc cờ `--trust`), Hermes `hermes plugins enable impeccable-design-hook`. Kiểm tra: `/impeccable hooks status`, `/impeccable doctor`.
- Kiểm tra (đã chạy 08/11/2026): `npm view impeccable` → `4.8.1`/Apache-2.0; GitHub API → 105.742★/6.285 forks/70 issues mở/push 08/11/2026/tạo 16/11/2025; fetch 11 URL (homepage + `/docs` + `/designing` + `/slop` + `/docs/detector` + `/docs/hooks` + `/docs/config` + `/docs/impeccable` + `/privacy` + `/tutorials/getting-started` + `/live-mode`) + GitHub README. Chưa chạy: `install`/`detect`/`init`/`live` thật (không có project UI + browser trên máy này) — ghi WARN.

### Cách item hoạt động
- Tổ chức đứng sau: Paul Bakaus / Renaissance Geek, Inc. (backed a16z), repo `https://github.com/pbakaus/impeccable`, license Apache-2.0, npm `impeccable` 4.8.1, skill 24 lệnh, nhịp update dày (skill v4.5.2 ngày 09/10/2026, v4.6.0 đổi telemetry, push main 08/11/2026).
- Phương thức hoạt động chung: (1) vốn từ 24 lệnh đọc `PRODUCT.md`/`DESIGN.md` rồi build/sửa/review theo đúng việc; (2) detector chạy bằng code (rules Source trên file, rules Browser khi scan URL, rules Design review do agent áp khi `critique`); (3) Live Mode overlay trên localhost để pick-compare-accept; (4) direction catalog qua `api/roll` + telemetry tắt được (`telemetry off` / `DO_NOT_TRACK=1` / `"telemetry": false`).
- Khác biệt vận hành theo usecase: refine UI có sẵn giữ system (chạy 1 lệnh/pass + detector before/after, xem [Usecase con 1](#usecase-con-1-polishrefine-ui-co-san--manh-nhat)) khác build mới (qua `init` + direction picker comp/code-led, xem [Usecase con 2](#usecase-con-2-build-moi-qua-direction-picker)) khác review xếp hạng (P0-P3 rồi mới sửa, xem [Usecase con 3](#usecase-con-3-review-xep-hang-critiqueaudit)) khác iterate trực quan + CI (Live/generate + hook/exit code/ignores, xem [Usecase con 4](#usecase-con-4-iterate-truc-quan-livegenerate--detector-ci)).

### Cốt lõi bất biến
- 1 project = 1 skill design duy nhất: chạy Impeccable cạnh skill design khác trên cùng repo → agent load cả hai, rules xung đột, hook chạy 2 lần (nguồn ssdnodes 31/10/2026). Chọn 1, disable cái còn lại ở local scope.
- Mọi việc qua `/impeccable <động từ> <target>` sau `init` (`PRODUCT.md`): build mới mà thiếu `init` thì brief sai audience/constraint. Shortcut đã `pin` vẫn forward về skill chính.
- Detector là check, không phải thiết kế: scan sạch (exit 0) không có nghĩa design đạt — `critique`/mắt người vẫn bắt buộc trước ship.
- Exception ghi 1 lần (`ignores add-value <rule> <giá trị> --reason "..."`, commit `.impeccable/config.json`), cấm cãi với agent mỗi lần; exit 2 = có findings, không giấu exit code.
- Sau khi dùng phải nêu được: lệnh nào + `PRODUCT.md`/`DESIGN.md` nào đã đọc + detector exit mấy; không nêu được = chưa thực sự dùng hệ.

### Phần tùy chỉnh
- Được đổi: target (1 section/element, càng hẹp càng tốt), buildPath comp-led (mockup trước, cần image gen built-in hoặc `OPENAI_API_KEY` — ref ảnh upload lên OpenAI) vs code-led, direction (safer/bolder), scope ignore (value/file/local), quiet mode. Cổng duyệt 2 tầng: (1) lệnh nào — shortlist (polish vs critique vs generate vs live) kèm lý do qua question tool, user pick mới chạy (2 lệnh 1 pass = 1 diff lớn, truy lỗi sai lệnh); (2) giữ/đổi gì — findings nào fix, cái nào waive có lý do. Waiver (bỏ P0, review offline bản copy, đổi engine/model) phải quote câu ok tường minh của user. Live Apply chạy `codex --dangerously-bypass-approvals-and-sandbox` / `claude --permission-mode bypassPermissions` khi không poll — review staged edits trước, hoặc `IMPECCABLE_LIVE_COPY_AGENT=chat|off`.

### Phân công ai làm gì
- Agent chính: `init` (đọc project, hỏi audience/constraint, ghi `PRODUCT.md`), shortlist 1 lệnh (user pick), chạy lệnh, đọc detector exit + findings, review `git diff` trong scope, ghi exception 1 lần.
- Giao cho claude các bước cần browser/người thật: verify visual (Live overlay, focus/contrast thực, motion, màn hẹp, keyboard) + chụp/compare biến thể — kèm URL/routes + lệnh đã chạy + output mong đợi; cấm agent tự kết luận render đạt khi không có browser.
- Agent verify: detector chạy lại (`before.json` vs `after.json`), findings nhóm lệnh đã gọn, không rule mới ngoài scope, design-system rules sạch, `git diff` nằm trong scope lệnh.

### Định vị khác biệt (số liệu ngày 08/11/2026 trừ khi ghi khác)
- So với `../hallmark/` (~39,5k★, system + gates máy + sweep render trong repo này): khác tầng đảm bảo — Hallmark SINH system mới (scaffold tokens + theme deal + hero-first + sweep) rồi mới check; Impeccable ĐIỀU HÀNH design có sẵn bằng vốn từ + detector + Live, không có gates số. Chọn Impeccable thay vì Hallmark khi cần refine/review/iterate nhanh trên UI đã có mà giữ system; chọn Hallmark khi output phải pass gates merge (contrast/fold/word budget). 2 hệ bổ trợ: Hallmark dựng → Impeccable polish/audit/Live.
- So với `../web-interface-guidelines/` (~1,1k★ repo, ~815k installs skill): khác tốc độ vs chiều sâu — guidelines 1 pass dưới 10 phút ra `file:line`, không đổi file; Impeccable sửa tới nơi + so sánh mắt thấy + xếp hạng P0-P3 nhưng tốn session dài + context hook. Chọn Impeccable thay vì guidelines khi findings cần sửa + mắt thấy (Live/detector), không phải list lỗi nhanh.
- Khung trung thực: Impeccable thắng ở vốn từ 24 lệnh + detector không-LLM + Live pick-element + tôn trọng `DESIGN.md`; thua ở gates số cứng + bricks sở hữu + offline hoàn toàn + chi phí context (description match mọi request frontend; hook `PostToolUse` nhồi findings mỗi edit — ssdnodes).

### Bản đồ phủ usecase (quét HẾT /docs ngày 08/11/2026 — ★ mạnh nhất đầu)
- ★ Refine UI có sẵn giữ system (`polish`/`bolder`/`quieter`/`typeset`/`layout`/`colorize`/`animate`/`delight`): xem Usecase 1.
- Build mới qua direction picker + comp-led (làm mockup trước, cần image gen)/code-led (build thẳng trong code) (`impeccable`/`shape` + `init`): xem Usecase 2.
- Review xếp hạng (`critique`/`audit`, rank từ P0 chặn merge tới P3): xem Usecase 3.
- Trung bình: iterate trực quan (`live`/`generate` + `pin`) + detector CI/hooks/extension + ignores (`detect`/`hooks`/`doctor`): xem Usecase 4.
- Trung bình: system (`document` ghi `DESIGN.md`, `extract` gom pattern) + simplify (`distill`/`clarify`/`adapt`) + harden còn lại (`harden`/`onboard`/`optimize`) + `overdrive` (shader/motion nặng): rải trong Usecase 2-4, dùng khi đúng việc (`craft` là alias cũ, không dùng).
- KHÔNG hỗ trợ → thay thế: gates số merge → `../hallmark/`; checklist `file:line` nhanh → `../web-interface-guidelines/`; bricks React → `../reactbits/`; landing taste đóng gói → `../skillry/` (web); rebuild 1:1 site sống → `../ai-website-cloner-template/`; tokens đo thật + drift CI → `../dembrandt/`.

### Hồ sơ quyết định
- Việc DÙNG (5, cụ thể): 1. polish/refine UI giữ brand + plan names; 2. build page mới có direction chọn được (comp/code-led); 3. critique/audit xếp hạng P0-P3; 4. compare biến thể mắt thấy (Live/generate) rồi accept vào source; 5. detector CI + hook edit-time + check drift `DESIGN.md`.
- Việc KHÔNG DÙNG (5, mỗi việc kèm hệ thay thế): 1. cần gates merge → dùng `../hallmark/`; 2. cần `file:line` dưới 10 phút → dùng `../web-interface-guidelines/`; 3. cần bricks React → dùng `../reactbits/`; 4. native/adaptive (hook skip) → `audit` thủ công, không kỳ vọng Live; 5. offline/chặn API mà cần catalog → bỏ (catalog local chưa xác minh).
- Free / tổng + giá: 0đ toàn bộ skill/CLI/engine/detector/extension, Apache-2.0 (nguồn FAQ + `/privacy` + npm 08/11/2026). Tổng sở hữu = 0đ + tiền model/tool + image gen (built-in hoặc `OPENAI_API_KEY`) + máy online. Pro waitlist (thu email) chưa công bố giá — rủi ro lock-in tương lai.
- Ma sát cài đặt: 4 bước tới lệnh đầu (`install` → reload → `init` → lệnh đầu) so với chuẩn 1 dòng `npx skills add ...`. ĐÃ chạy 08/11/2026: `npm view` + GitHub API + fetch 11 URL docs. Chưa chạy: `install`/`detect`/`init`/`live` thật (ghi WARN). Rào cản: Node 18.19+, approve hook theo harness (Codex `/hooks`, Grok `/hooks-trust`, Hermes plugin), dev server + Chrome/Edge cho Live/URL-scan, image gen cho comp-led, mạng cho catalog/version.
- Đối thủ viral cùng phân khúc: `../hallmark/` (~39,5k★, sinh system + gates) vs `../web-interface-guidelines/` (~1,1k★ repo / ~815k installs skill, checklist nhanh).
- Chọn nó thay vì đối thủ khi: cần vốn từ + review xếp hạng + iterate mắt thấy trên UI có sẵn mà giữ system. Ví dụ đổi lựa chọn: PR polish pricing → Impeccable (Live compare 3 biến thể + detector before/after); dựng design-system mới phải pass gates → Hallmark.
- TUYỆT ĐỐI không dùng khi: offline/chặn fetch mà vẫn claim đủ catalog; 2 skill design cùng project; Live Apply vào production/CSP yếu (docs cấm); gửi ref bí mật qua image gen OpenAI khi chưa được duyệt.

### Usecase con 1: polish/refine UI có sẵn (★ mạnh nhất)
- Khi dùng: có 1 page/section sở hữu hoặc được phép sửa, muốn giữ system mà hết mùi AI-slop.
- Khi bỏ qua: chưa có gì để polish (sang Usecase 2); chỉ cần list lỗi (sang `../web-interface-guidelines/`); cần system mới pass gates (sang `../hallmark/`).
- Cơ chế khác các usecase khác ở đâu: duy nhất giữ system + 1 lệnh/pass + detector before/after đo được; các usecase khác build mới (direction picker), xếp hạng (P0-P3), hoặc mắt thấy (Live).
- Lệnh copy-paste: `/impeccable polish the pricing page` (kèm ràng buộc `Keep our colors and the current plan names`) rồi `npx impeccable detect src/` so với baseline `npx impeccable detect --json src/ > before.json`.
- Ngưỡng số cần đạt: target ≤1 section/pass; `git diff` nằm trong scope lệnh (typeset chỉ chạm font/size/line-height, không đổi palette); detector after gọn findings nhóm lệnh, không rule mới ngoài scope; design-system rules sạch.
- Ví dụ input-output (minh họa, không phải mặc định — target do user pick trước): input "polish pricing cards ở `src/components/Pricing.tsx`" → output diff chỉ spacing/type/hierarchy trong cards + detector after hết `flat-type-hierarchy`/`monotonous-spacing`, không thêm font mới (kẻo dính `font-outside-design-system`).
- Pitfalls riêng: polish cả page 1 pass (diff lớn, truy lỗi sai lệnh — ssdnodes); tin exit 0 = design đạt (detector không chấm taste, vẫn cần Usecase 3); cãi với agent thay vì `ignores add-value ... --reason` + commit config.
- Phân công usecase này: agent chính baseline detector → shortlist lệnh (user pick) → chạy 1 lệnh/pass → review diff; giao claude verify màn hẹp/keyboard/motion thật; verify bằng after.json + diff trong scope.

### Usecase con 2: build mới qua direction picker
- Khi dùng: page mới/redesign, có brief (audience + action + constraint), chấp nhận chọn direction trước khi build.
- Khi bỏ qua: đã có UI (sang Usecase 1); cần gates merge (sang `../hallmark/`); chỉ cần plan dừng trước build (dùng `shape`).
- Cơ chế khác các usecase khác ở đâu: duy nhất qua `init` (`PRODUCT.md`) + direction picker + comp-led/code-led; các usecase khác giữ system hoặc chỉ review/compare.
- Lệnh copy-paste: `/impeccable init` rồi `/impeccable design a signup page for our monthly book club. Help visitors understand the next event and reserve a seat.` (`shape` khi muốn dừng ở plan).
- Ngưỡng số cần đạt: `PRODUCT.md` đã đọc + chốt trước build; comp-led chỉ khi image gen sẵn (không thì code-led, chấp nhận kém tham vọng); direction do user chọn (không nhận đáp án đầu mặc định); mỗi vòng mockup→code cách nhau 1 review.
- Ví dụ input-output (minh họa): input brief book-club + constraint `confirmed dates only` → output `PRODUCT.md` (audience/task/constraint) + direction đã chọn + page code theo direction, không bịa ngày/số chỗ.
- Pitfalls riêng: build không `init` (brief sai audience — FAIL core); comp-led không image gen mà vẫn đòi mockup (mất vòng review); nhận direction đầu tiên mặc định (neo bias — bắt chọn có lý do).
- Phân công usecase này: agent chính đọc project + hỏi gaps + ghi `PRODUCT.md` + trình direction (user pick) → build; giao claude verify visual sau build; verify bằng brief→direction→code khớp + detector sạch primary.

### Usecase con 3: review xếp hạng (critique/audit)
- Khi dùng: chưa biết sửa gì, hoặc cần báo cáo kỹ thuật trước release (a11y/perf/responsive/theming).
- Khi bỏ qua: đã biết nhóm findings (sang Usecase 1); cần `file:line` nhanh (sang guidelines); cần đo tokens thật (sang `../dembrandt/`).
- Cơ chế khác các usecase khác ở đâu: duy nhất xếp hạng (heuristic + P0-P3) rồi mới sửa; các usecase khác sửa trực tiếp hoặc mắt thấy.
- Lệnh copy-paste: `/impeccable critique the pricing page` rồi `/impeccable audit site/index.html` (P0 chặn merge); `/impeccable document` ghi `DESIGN.md` khi system đã chốt; `/impeccable extract` gom pattern lặp.
- Ngưỡng số cần đạt: mọi P0 có owner + plan fix; `critique` đọc findings rồi mới pick nhóm sửa (không sửa mù); không ship khi còn P0 mở.
- Ví dụ input-output (minh họa): input `audit site/index.html` → output báo cáo rank P0 (contrast fail, JS error) → P3 (polish) + pick `typeset`/`harden` fix P0 trước.
- Pitfalls riêng: `audit` sạch primary mà bỏ `critique` (detector không chấm taste); report đẹp thay cho thử task thật (docs bắt try narrow screen + keyboard).
- Phân công usecase này: agent chính chạy review → trình findings rank + pick nhóm (user duyệt) → fix; giao claude verify a11y/perf thực (contrast render, focus, overflow); verify bằng P0 hết + re-scan.

### Usecase con 4: iterate trực quan (live/generate) + detector CI
- Khi dùng: cần mắt thấy 3 biến thể rồi chốt, hoặc kẹp detector vào hook/CI/extension.
- Khi bỏ qua: đã chốt direction bằng lời (sang Usecase 1); review báo cáo là đủ (sang Usecase 3).
- Cơ chế khác các usecase khác ở đâu: duy nhất pick-compare-accept trên page chạy + exit code máy cho CI; các usecase khác làm việc trong chat.
- Lệnh copy-paste: `/impeccable live` (pick element + Steer trên `http://localhost:3000`) hoặc `/impeccable generate 3 bold variants of the pricing cards` (accept 1 vào source, discard còn lại); CI: `npx impeccable detect src/` / `npx impeccable detect http://localhost:3000` / `npx impeccable detect --json .` / `npx impeccable ignores add-value overused-font Inter --reason "Brand font"`; hook: `/impeccable hooks on`.
- Ngưỡng số cần đạt: Live chỉ trên checkout local (cấm inject production/CSP yếu); exit 0 = sạch primary (advisory được phép), exit 2 = có findings, exit 1 = target lỗi (CI fail mọi exit ≠ 0); exception commit `.impeccable/config.json` để team/CI dùng chung.
- Ví dụ input-output (minh họa): input `generate 3 bold variants of the pricing cards` → output 3 biến thể trên page chạy → accept 1 (ghi vào source, xóa preview) + detector after không thêm rule ngoài scope.
- Pitfalls riêng: Live Apply bypass approvals khi không poll (`codex --dangerously-bypass...`) — review staged edits trước hoặc `IMPECCABLE_LIVE_COPY_AGENT=chat|off`; 2 route cài cùng lúc → hook chạy đôi (chọn 1 route); pin npm mà quên pin bundle (installer mặc định fetch endpoint unversioned — ssdnodes).
- Phân công usecase này: agent chính mở session Live/dev server + accept/discard theo user + kẹp CI; giao claude thao tác pick/compare trên browser + verify accept đã vào source; verify bằng diff source + detector after.

### Các bước chung
1. `init` (`PRODUCT.md`) → có system thì `document` (`DESIGN.md`).
2. Baseline: `npx impeccable detect <target>` (+ `--json` lưu `before.json`).
3. Shortlist 1 lệnh kèm lý do qua question tool, user pick mới chạy (1 lệnh/pass).
4. Review `git diff` trong scope lệnh → Live/generate khi cần mắt thấy.
5. Chạy lại detector (`after.json`) → exception 1 lần có `--reason` + commit config.
6. `critique`/audit chốt P0 trước ship; nêu lệnh + files + exit code (core-fidelity).

### Prompt mẫu
- "Polish pricing page, giữ màu brand + tên plan hiện tại. `init` trước nếu thiếu `PRODUCT.md`, baseline detector trước, 1 lệnh mỗi pass."
- "Design signup page cho book club tháng: audience ..., action chính reserve seat, constraint chỉ dùng ngày/số chỗ đã xác nhận. Comp-led nếu có image gen, không thì code-led. Direction tôi chọn, không mặc định."
- "Audit `site/index.html`, rank P0-P3, P0 chặn merge. Findings nào thuộc system (tokens/shape/hero) thì đề xuất Hallmark sửa."
- Ví dụ điền sẵn: "Critique pricing cards ở `src/components/Pricing.tsx` (repo mình): baseline `npx impeccable detect src/components/Pricing.tsx --json > before.json` (08/11/2026), `/impeccable critique the pricing cards`, đọc findings rồi pick 1 nhóm fix bằng `/impeccable typeset`, chạy lại detector so `after.json`."

### Pitfalls
- 2 skill design cùng project (rules xung đột + hook đôi — mỗi edit trigger 2 check, context phình; nguồn ssdnodes).
- Build mới không `init` (thiếu audience/constraint — FAIL core).
- 2 lệnh 1 pass (1 diff lớn, truy lỗi sai lệnh).
- Comp-led không image gen mà vẫn đòi mockup.
- Tin detector sạch = design đạt (thiếu `critique`/mắt người).
- Exception bằng cãi với agent thay vì `ignores add-value --reason` + commit `.impeccable/config.json`.
- Live trên production/CSP yếu (docs cấm — chỉ local checkout).
- Live Apply bypass approvals (`--dangerously-bypass-approvals-and-sandbox` / `--permission-mode bypassPermissions`) khi không poll — review staged edits trước.
- Pin npm mà quên pin bundle/skill (endpoint unversioned — check `version:` trong `SKILL.md`).
- Node không đủ (pinned 4.5.2 cần 22.18+) mà vẫn cài.
- Chặn mạng/catalog mà claim đủ direction (roll request vẫn cần mạng dù đã tắt telemetry).

### Tham khảo sử dụng (quyết định được + số có trọng số, chốt 08/11/2026)
- Nhận xét sâu: [ssdnodes 31/10/2026, Matt Connor](https://www.ssdnodes.com/learn/impeccable-design-skill-for-coding-agents) — *"You install it pinned to a release, run the detector on a page, apply one command, and run the detector again to see what changed"* + *"one design skill owns a project"* + bảng exit 0/2/1 + chi phí context (hook `PostToolUse` + stop hook 30s, đo bằng `claude plugin details`) → xác nhận quyết định: ghim version + loop baseline→1 lệnh→đo lại + 1 skill/project + đo context trước khi bật luôn.
- Nhận xét sâu (chính chủ): [GitHub README](https://github.com/pbakaus/impeccable) (fetch 08/11/2026) + `/docs` — 24 lệnh + 3 đường detector (agent/CI/browser) + Live overlay + telemetry tắt được + Live Apply bypass flags → xác nhận: detector 0đ không key, nhưng Live Apply cần review quyền trước.
- Số trung bình có trọng số: GitHub API 08/11/2026 — 105.742★/6.285 forks/70 issues mở/push 08/11/2026/tạo 16/11/2025 (velocity ~9,6k★/tháng, repo chưa đầy 1 tuổi); npm `impeccable` 4.8.1 Apache-2.0 (`npm view` 08/11/2026); header site `106k`. Trọng số: API + npm đáng tin hơn header làm tròn; stars tăng nhanh nhưng repo trẻ → tin capability, chưa tin độ bền.
- Tiếng Việt: truy vấn `impeccable.style đánh giá` không trả về review Việt độc lập → `chưa xác minh`. Lượt cài Chrome extension → `chưa xác minh`.
- Mâu thuẫn: stars top-tier vs repo chưa đầy 1 tuổi + Pro waitlist chưa giá → phán quyết: dùng 0đ hiện tại thoải mái (Apache-2.0), ghim version, theo dõi giá Pro trước khi khóa workflow team vào catalog cloud.

### Tham khảo
- Repo: https://github.com/pbakaus/impeccable
- Đọc theo thứ tự: GitHub `README.md` (24 lệnh + 3 đường detector + install + Live Apply) → `/tutorials/getting-started` (`init` + `PRODUCT.md` + comp/code-led) → `/designing` (4 modes) → `/slop` (catalog 9 nhóm) → `/docs/detector` + `/docs/hooks` + `/docs/config` (exit codes + ignores) → `/privacy` (telemetry/Pro) → ssdnodes guide (loop pin + context cost).
- Lệnh/điểm đã verify 08/11/2026: `npm view` (4.8.1/Apache-2.0), GitHub API (số liệu trên), fetch 11 URL docs. Chưa chạy thật: `install`/`detect`/`init`/`live` (ghi WARN).

### Được dùng ở đâu
- Dùng CHO UI: xem `../../domains/ui/using-impeccable.md` (polish/review/iterate + detector CI) — index `../../domains/ui/README.md`.
- Liên quan: findings thuộc system → `../hallmark/`; cần pass checklist nhanh → `../web-interface-guidelines/`; bricks React → `../reactbits/`.

### Quay lại index
- Về `../../domains/ui/README.md` để so sánh định vị với `hallmark/` + `web-interface-guidelines/`.
- Xem thêm item liên quan: `../hallmark/` (system + gates) + `../web-interface-guidelines/` (checklist audit) + `../reactbits/` (bricks hiệu ứng).

---

## English

### When to use
- An agent design vocabulary is needed when the change has no name yet ("the page reads AI-generated"): 24 commands as `/impeccable <verb> <target>`.
- A model-free detector (no LLM, no API key) is needed: design hooks on UI edits, CI (`detect` exits 0/2/1), or live pages (Chrome extension overlay).
- Ranked reviews are needed: `critique` (heuristic UX evaluation) / `audit` (technical a11y/perf/responsive/theming, ranked from merge-blocking P0 to P3).
- Visual comparison before committing to code: `live` (pick elements to compare on the running page; Steer gives page-wide direction without picking) / `generate` (compare variants, accept one into source).
- A `DESIGN.md` worth keeping: `document` records the system, the detector checks drift (off-system font/color/radius/size).

### When to skip
- A new system must pass hard machine gates (4.5:1 contrast, 1280x800 fold, word budget) + hero-first + anti-repetition log → use `../hallmark/` (Impeccable has no numeric gates).
- One checklist `file:line` pass under 10 minutes with no file changes → use `../web-interface-guidelines/` (Impeccable fixes things, so it is slower).
- Owned animated React bricks → use `../reactbits/` (no components here).
- Fully offline or `impeccable.style/api/*` blocked: the local detector still runs, but the direction catalog + version check need network (local catalog unverified) → consider skipping.
- Native iOS/Android/adaptive: hooks skip when `PRODUCT.md` declares these platforms → manual `audit` only, no hook/Live expectations.

### Install
- Requires Node 18.19+ (`node --version`; pinned 4.5.2 needs Node 22.18+ per ssdnodes 31/10/2026 — latest 4.8.1 works on 18.19+ per `/tutorials/getting-started`).
- Install: `npx impeccable install` (pick tool + project/global) → reload the tool → `/impeccable init` (writes `PRODUCT.md`). Update: `npx impeccable update`. Sources: homepage + `/tutorials/getting-started` + GitHub README (all fetched 08/11/2026).
- Other routes: plugin marketplace (`plugin marketplace add pbakaus/impeccable`), skills.sh (`npx skills add pbakaus/impeccable`), version-pinned submodule, manual/ZIP copy (README.txt maps folders, no extra nesting).
- Hooks (recommended on): offered on Claude Code/Cursor/Codex/Copilot/Grok Build/Hermes; Codex needs `/hooks` approval, Grok `/hooks-trust` (or `--trust`), Hermes `hermes plugins enable impeccable-design-hook`. Check: `/impeccable hooks status`, `/impeccable doctor`.
- Verified 08/11/2026: `npm view impeccable` → `4.8.1`/Apache-2.0; GitHub API → 105,742 stars / 6,285 forks / 70 open issues / pushed 08/11/2026 / created 16/11/2025; 11 doc URLs fetched + GitHub README. NOT run: real `install`/`detect`/`init`/`live` (no UI project + browser on this machine) — recorded WARN.

### How the item works
- Backing organization: Paul Bakaus / Renaissance Geek, Inc. (a16z-backed), repo `https://github.com/pbakaus/impeccable`, Apache-2.0, npm `impeccable` 4.8.1, 24-command skill, dense update cadence (skill v4.5.2 on 09/10/2026, v4.6.0 telemetry change, main pushed 08/11/2026).
- Core operating method: (1) a 24-command vocabulary reading `PRODUCT.md`/`DESIGN.md` before building/fixing/reviewing; (2) a code-run detector (Source rules on files, Browser rules on URL scans, Design-review rules applied by the agent during `critique`); (3) Live Mode overlay on localhost for pick-compare-accept; (4) a direction catalog via `api/roll` + mögliche opt-out telemetry (`telemetry off` / `DO_NOT_TRACK=1` / `"telemetry": false`).
- Per-usecase differences: refining existing UI in place (one command/pass + detector before/after, [Sub-usecase 1](#sub-usecase-1-polishrefine-existing-ui--strongest)) vs new builds (via `init` + direction picker, comp/code-led, [Sub-usecase 2](#sub-usecase-2-new-build-via-direction-picker)) vs ranked reviews (P0-P3 before fixing, [Sub-usecase 3](#sub-usecase-3-ranked-review-critiqueaudit)) vs visual iteration + CI (Live/generate + hooks/exit codes/ignores, [Sub-usecase 4](#sub-usecase-4-visual-iteration-livegenerate--detector-ci)).

### Invariant core
- One project = one design skill: Impeccable next to another design skill → the agent loads both, rules conflict, hooks fire twice (source: ssdnodes 31/10/2026). Pick one, disable the other at local scope.
- Everything via `/impeccable <verb> <target>` after `init` (`PRODUCT.md`): new builds without `init` get audience/constraints wrong. Pinned shortcuts still forward to the main skill.
- The detector is a check, not a design: a clean scan (exit 0) does not mean the design passes — `critique`/human eyes stay mandatory before shipping.
- Exceptions recorded once (`ignores add-value <rule> <value> --reason "..."`, commit `.impeccable/config.json`), never re-argued per run; exit 2 = findings, never hide the exit code.
- After use, state: which command + which `PRODUCT.md`/`DESIGN.md` were read + which detector exit; otherwise the system was not really used.

### Customizable surface
- Tunables: target (one section/element, narrower is better), buildPath comp-led (mockup first, needs built-in image generation or `OPENAI_API_KEY` — reference images upload to OpenAI) vs code-led, direction (safer/bolder), ignore scope (value/file/local), quiet mode. Two-level approval: (1) which command — shortlist (polish vs critique vs generate vs live) with reasons via the question tool, user picks before running (2 commands per pass = one big diff, wrong blame); (2) what stays/changes — which findings get fixed vs waived with reasons. Waivers (dropping P0s, offline review from a stale copy, engine/model swaps) must quote the user's explicit ok. Live Apply runs `codex --dangerously-bypass-approvals-and-sandbox` / `claude --permission-mode bypassPermissions` when nothing polls — review staged edits first, or set `IMPECCABLE_LIVE_COPY_AGENT=chat|off`.

### Work split
- Main agent: `init` (read the project, ask audience/constraints, write `PRODUCT.md`), shortlist one command (user picks), run it, read detector exit + findings, review `git diff` inside scope, record exceptions once.
- Hand browser/human steps to claude as a whole: visual verification (Live overlay, real focus/contrast, motion, narrow screens, keyboard) + variant capture/comparison — with URLs/routes + commands run + expected output; the agent never asserts render results without a browser.
- Agent verifies: re-run detector (`before.json` vs `after.json`), command-group findings are gone, no new out-of-scope rules, design-system rules clean, `git diff` inside the command's scope.

### Differentiating positioning
- Vs `../hallmark/` (~39.5k stars, system + machine gates + render sweep): different assurance layer — Hallmark GENERATES new systems (token scaffold + theme deal + hero-first + sweep) then checks; Impeccable OPERATES existing designs via vocabulary + detector + Live, with no numeric gates. Pick Impeccable for fast refine/review/iterate on existing UI while keeping the system; pick Hallmark when output must pass merge gates. They complement: Hallmark builds → Impeccable polishes/audits/Lives.
- Vs `../web-interface-guidelines/` (~1.1k repo stars, ~815k skill installs): speed vs depth — guidelines do one sub-10-minute `file:line` pass and change nothing; Impeccable fixes in place + visual comparison + P0-P3 ranking at the cost of longer sessions + hook context. Pick Impeccable when findings need fixing + seeing (Live/detector), not a fast list.
- Honest frame: Impeccable wins on 24-command vocabulary + model-free detector + Live element-picking + `DESIGN.md` respect; loses on hard numeric gates + owned bricks + fully offline use + context cost (description matches every frontend request; `PostToolUse` hooks inject findings per edit — ssdnodes).

### Coverage map (whole `/docs` scanned 08/11/2026 — ★ strongest first)
- ★ Refine existing UI in place (`polish`/`bolder`/`quieter`/`typeset`/`layout`/`colorize`/`animate`/`delight`): see Sub-usecase 1.
- New builds via direction picker + comp-led (mockup first, needs image generation)/code-led (straight-to-code) (`impeccable`/`shape` + `init`): see Sub-usecase 2.
- Ranked reviews (`critique`/`audit`, from merge-blocking P0 to P3): see Sub-usecase 3.
- Medium: visual iteration (`live`/`generate` + `pin`) + detector CI/hooks/extension + ignores (`detect`/`hooks`/`doctor`): see Sub-usecase 4.
- Medium: system (`document` writes `DESIGN.md`, `extract` consolidates patterns) + simplify (`distill`/`clarify`/`adapt`) + remaining harden (`harden`/`onboard`/`optimize`) + `overdrive` (heavy shader/motion): spread across Sub-usecases 2-4, use per job (`craft` is a legacy alias, unused).
- NOT supported → use instead: numeric merge gates → `../hallmark/`; fast `file:line` checklist → `../web-interface-guidelines/`; React bricks → `../reactbits/`; packaged landing taste → `../skillry/` (web); 1:1 live-site rebuild → `../ai-website-cloner-template/`; real measured tokens + drift CI → `../dembrandt/`.

### Decision dossier
- Jobs SERVED (5, concrete): 1. polish/refine UI keeping brand + plan names; 2. new pages with a choosable direction (comp/code-led); 3. `critique`/`audit` ranked P0-P3; 4. visual variant comparison (Live/generate) then accept into source; 5. detector CI + edit-time hooks + `DESIGN.md` drift checks.
- Jobs NOT served (5, each with its replacement): 1. merge gates → `../hallmark/`; 2. sub-10-minute `file:line` → `../web-interface-guidelines/`; 3. React bricks → `../reactbits/`; 4. native/adaptive (hooks skip) → manual `audit`, no Live expectations; 5. offline/blocked API needing the catalog → skip (local catalog unverified).
- Free / total + price: $0 for all skill/CLI/engine/detector/extension, Apache-2.0 (sources: FAQ + `/privacy` + npm 08/11/2026). Total cost = $0 + model/tool fees + image generation (built-in or `OPENAI_API_KEY`) + an online machine. Pro waitlist (collects email) has no published price — future lock-in risk.
- Install friction: 4 steps to the first command (`install` → reload → `init` → first command) vs the 1-line `npx skills add ...` standard. Ran 08/11/2026: `npm view` + GitHub API + 11 doc-URL fetches. NOT run: real `install`/`detect`/`init`/`live` (WARN). Barriers: Node 18.19+, per-harness hook approval (Codex `/hooks`, Grok `/hooks-trust`, Hermes plugin), dev server + Chrome/Edge for Live/URL scans, image generation for comp-led, network for catalog/version.
- Viral same-segment opponents: `../hallmark/` (~39.5k stars, system + gates) vs `../web-interface-guidelines/` (~1.1k repo stars / ~815k skill installs, fast checklist).
- Pick it over opponents when: vocabulary + ranked review + visual iteration on existing UI while keeping the system. Choice-flipping example: PR polishing pricing → Impeccable (Live-compare 3 variants + detector before/after); new gated design system → Hallmark.
- NEVER use when: offline/blocked fetch while claiming full catalog; two design skills in one project; Live Apply onto production/weak CSP (docs forbid); unapproved secret references through OpenAI image generation.

### Sub-usecase 1: polish/refine existing UI (★ strongest)
- When to use: one owned/permitted page/section that should keep its system while losing AI-slop.
- When to skip: nothing exists yet → Sub-usecase 2; a list is enough → `../web-interface-guidelines/`; a new gated system is needed → `../hallmark/`.
- Copy-paste command: `/impeccable polish the pricing page` (with `Keep our colors and the current plan names`) then `npx impeccable detect src/` against the `npx impeccable detect --json src/ > before.json` baseline.
- Numeric bar: ≤1 section per pass; `git diff` stays inside the command's scope (typeset touches only font/size/line-height, never the palette); the after-scan clears the command group's findings with no new out-of-scope rules; design-system rules clean.
- Input-output example (illustrative): `src/components/Pricing.tsx` pricing cards → spacing/type/hierarchy-only diff + after-scan clears `flat-type-hierarchy`/`monotonous-spacing` without adding a new font (which would trip `font-outside-design-system`).
- Own pitfalls: polishing a whole page per pass (big diff, wrong blame — ssdnodes); reading exit 0 as design approval (the detector scores no taste — Sub-usecase 3 still required); arguing with the agent instead of `ignores add-value ... --reason` + config commit.
- Work split: main agent baselines → shortlists (user picks) → runs one command/pass → reviews the diff; claude verifies narrow screens/keyboard/real motion; verify via after.json + in-scope diff.

### Sub-usecase 2: new build via direction picker
- When to use: new pages/redesigns with a brief (audience + action + constraints), direction chosen before building.
- When to skip: UI already exists → Sub-usecase 1; merge gates required → `../hallmark/`; plan-only stopping before build → `shape`.
- Copy-paste command: `/impeccable init` then `/impeccable design a signup page for our monthly book club. Help visitors understand the next event and reserve a seat.` (`shape` for plan-only).
- Numeric bar: `PRODUCT.md` read + settled before building; comp-led only with image generation ready (else code-led, accept humbler visuals); user-chosen direction (never the default first answer); one review between mockup and code rounds.
- Input-output example (illustrative): book-club brief + `confirmed dates only` → `PRODUCT.md` (audience/task/constraint) + chosen direction + direction-faithful page code with no invented dates/seats.
- Own pitfalls: building without `init` (wrong audience — core FAIL); demanding mockups without image generation (lost review rounds); accepting the first direction by default (anchor bias — require a reasoned pick).
- Work split: main agent reads the project + asks gaps + writes `PRODUCT.md` + presents directions (user picks) → builds; claude verifies post-build visuals; verify via brief→direction→code match + primary-clean detector.

### Sub-usecase 3: ranked review (critique/audit)
- When to use: the fix list is unknown, or a technical pre-release report (a11y/perf/responsive/theming) is needed.
- When to skip: the finding group is known → Sub-usecase 1; fast `file:line` needed → guidelines; real measured tokens needed → `../dembrandt/`.
- Copy-paste command: `/impeccable critique the pricing page` then `/impeccable audit site/index.html` (P0 blocks merge); `/impeccable document` records `DESIGN.md` once the system settles; `/impeccable extract` consolidates repeated patterns.
- Numeric bar: every P0 has an owner + fix plan; `critique` findings are read before picking a fix group (no blind fixing); nothing ships with open P0s.
- Input-output example (illustrative): `audit site/index.html` → P0-ranked report (contrast failure, JS error) → P3 (polish) + picked `typeset`/`harden` fixing P0s first.
- Own pitfalls: clean `audit` primary findings used to skip `critique` (the detector scores no taste); a pretty report substituting for actually trying the task (docs require narrow-screen + keyboard trials).
- Work split: main agent reviews → presents ranked findings + fix-group pick (user approves) → fixes; claude verifies real a11y/perf (rendered contrast, focus, overflow); verify via zero P0s + re-scan.

### Sub-usecase 4: visual iteration (live/generate) + detector CI
- When to use: three variants must be seen before deciding, or the detector belongs in hooks/CI/extension.
- When to skip: direction settled in words → Sub-usecase 1; a report suffices → Sub-usecase 3.
- Copy-paste command: `/impeccable live` (pick an element + Steer on `http://localhost:3000`) or `/impeccable generate 3 bold variants of the pricing cards` (accept one into source, discard the rest); CI: `npx impeccable detect src/` / `npx impeccable detect http://localhost:3000` / `npx impeccable detect --json .` / `npx impeccable ignores add-value overused-font Inter --reason "Brand font"`; hooks: `/impeccable hooks on`.
- Numeric bar: Live on local checkouts only (production/weak-CSP injection forbidden); exit 0 = primary-clean (advisories allowed), exit 2 = findings, exit 1 = broken target (CI fails on any nonzero); exceptions committed in `.impeccable/config.json` for team/CI sharing.
- Input-output example (illustrative): `generate 3 bold variants of the pricing cards` → 3 live variants → accept one (written to source, previews removed) + after-detector adds no out-of-scope rules.
- Own pitfalls: Live Apply bypassing approvals when nothing polls (`--dangerously-bypass-approvals-and-sandbox` / `--permission-mode bypassPermissions`) — review staged edits first or set `IMPECCABLE_LIVE_COPY_AGENT=chat|off`; two install routes at once → double hooks (pick one); pinning npm but not the bundle/skill (unversioned endpoint by default — verify `version:` in `SKILL.md`).
- Work split: main agent opens the Live session/dev server + accepts/discards per user + wires CI; claude performs pick/compare in the browser + verifies the accept landed in source; verify via source diff + after-detector.

### Shared steps
1. `init` (`PRODUCT.md`) → `document` (`DESIGN.md`) when a system exists.
2. Baseline: `npx impeccable detect <target>` (+ `--json` into `before.json`).
3. Shortlist one command with reasons via the question tool; run only after the user picks (one command/pass).
4. Review `git diff` inside the command's scope → Live/generate when eyes are needed.
5. Re-run the detector (`after.json`) → one-time exceptions with `--reason` + config commit.
6. `critique`/audit to zero P0s before shipping; state command + files + exit code (core-fidelity).

### Sample prompts
- "Polish the pricing page, keeping brand colors + current plan names. Run `init` first if `PRODUCT.md` is missing, baseline the detector first, one command per pass."
- "Design a monthly book-club signup page: audience ..., main action reserve-a-seat, constraints confirmed dates/seats only. Comp-led with image generation, else code-led. I pick the direction, no defaults."
- "Audit `site/index.html`, rank P0-P3, P0 blocks merge. System-level findings (tokens/shape/hero) go to Hallmark for fixing."
- Filled example: "Critique the pricing cards in `src/components/Pricing.tsx` (my repo): baseline `npx impeccable detect src/components/Pricing.tsx --json > before.json` (08/11/2026), `/impeccable critique the pricing cards`, read the findings then pick one group to fix with `/impeccable typeset`, re-run the detector into `after.json`."

### Pitfalls
- Two design skills in one project (conflicting rules + double hooks — every edit triggers 2 checks, context bloat; source: ssdnodes).
- New builds without `init` (missing audience/constraints — core FAIL).
- Two commands per pass (one big diff, wrong blame).
- Comp-led without image generation while demanding mockups.
- Reading a clean detector as design approval (missing `critique`/human eyes).
- Exceptions via arguing instead of `ignores add-value --reason` + committed `.impeccable/config.json`.
- Live on production/weak CSP (docs forbid — local checkouts only).
- Live Apply bypassing approvals when nothing polls — review staged edits first.
- Pinning npm without pinning the bundle/skill (unversioned endpoint — check `version:` in `SKILL.md`).
- Insufficient Node (pinned 4.5.2 needs 22.18+) while installing anyway.
- Claiming full catalog while network/catalog is blocked (roll requests need network even with telemetry off).

### Usage references (decisive + weighted, pinned 08/11/2026)
- Deep review: [ssdnodes 31/10/2026, Matt Connor](https://www.ssdnodes.com/learn/impeccable-design-skill-for-coding-agents) — *"You install it pinned to a release, run the detector on a page, apply one command, and run the detector again to see what changed"* + *"one design skill owns a project"* + the 0/2/1 exit table + context cost (`PostToolUse` hook + 30s stop hook, measured via `claude plugin details`) → confirms: pin versions + baseline→one-command→remeasure loop + one skill/project + measure context before leaving it always on.
- Deep first-party: [GitHub README](https://github.com/pbakaus/impeccable) (fetched 08/11/2026) + `/docs` — 24 commands + 3 detector routes (agent/CI/browser) + Live overlay + disable-able telemetry + Live Apply bypass flags → confirms: $0 keyless detector, but Live Apply needs a permissions review first.
- Weighted averages: GitHub API 08/11/2026 — 105,742 stars / 6,285 forks / 70 open issues / pushed 08/11/2026 / created 16/11/2025 (~9.6k stars/month, repo under 1 year old); npm `impeccable` 4.8.1 Apache-2.0 (`npm view` 08/11/2026); site header `106k`. Weight: API + npm beat the rounded header; fast-growing stars on a young repo → trust capability, not yet longevity.
- Vietnamese: query `impeccable.style đánh giá` returns no independent Vietnamese review → `unverified`. Chrome extension install count → `unverified`.
- Conflict: top-tier stars vs sub-1-year repo + unpriced Pro waitlist → verdict: use today's $0 freely (Apache-2.0), pin versions, watch Pro pricing before locking team workflows to the cloud catalog.

### References
- Repo: https://github.com/pbakaus/impeccable
- Read order: GitHub `README.md` (24 commands + 3 detector routes + install + Live Apply) → `/tutorials/getting-started` (`init` + `PRODUCT.md` + comp/code-led) → `/designing` (4 modes) → `/slop` (9-group catalog) → `/docs/detector` + `/docs/hooks` + `/docs/config` (exit codes + ignores) → `/privacy` (telemetry/Pro) → ssdnodes guide (pin loop + context cost).
- Verified 08/11/2026: `npm view` (4.8.1/Apache-2.0), GitHub API (numbers above), 11 doc-URL fetches. NOT run for real: `install`/`detect`/`init`/`live` (WARN).

### Where used
- Used FOR UI: see `../../domains/ui/using-impeccable.md` (polish/review/iterate + detector CI) — index `../../domains/ui/README.md`.
- Related: system-level findings → `../hallmark/`; fast checklist passes → `../web-interface-guidelines/`; React bricks → `../reactbits/`.

### Back to index
- Back to `../../domains/ui/README.md` to compare positioning vs `hallmark/` + `web-interface-guidelines/`.
- Related items: `../hallmark/` (system + gates) + `../web-interface-guidelines/` (audit checklist) + `../reactbits/` (motion bricks).
