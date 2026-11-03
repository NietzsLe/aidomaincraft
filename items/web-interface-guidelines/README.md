# web-interface-guidelines

## Tiếng Việt

### Dùng khi
- Cần review/audit UI code có sẵn (React/Next.js hoặc HTML tĩnh) ra list lỗi `file:line` terse để fix — thay vì review theo taste cảm tính.
- Cần 1 checklist chung cho agent khi sinh UI mới (paste `AGENTS.md` vào project): accessible + nhanh + delightful, 73 MUST + 31 SHOULD + 7 NEVER đã đếm 03/11/2026.
- Muốn audit tập trung: keyboard/focus/forms, animation `prefers-reduced-motion` (tự rút gọn motion cho user đã bật giảm chuyển động), performance (virtualize list >50 items, CLS — Cumulative Layout Shift do ảnh thiếu dimensions, preconnect), i18n (`Intl.*`, `translate="no"`).
- Agent được hỗ trợ (Claude Code, Cursor, Codex, OpenCode...) + có mạng (skill fetch rules tươi mỗi lần review).

### Bỏ qua khi
- Cần system/design mới pass gates máy + theme deal + hero-first + review lạnh → dùng `../hallmark/` (web-interface-guidelines audit checklist, không sinh system/tokens/sweep).
- Cần bricks React animated sở hữu source → dùng `../reactbits/` (guidelines không cho component nào).
- Cần tối ưu React/Next.js performance sâu (waterfall, bundle, server) → dùng skill `react-best-practices` cùng collection `vercel-labs/agent-skills` (guidelines chỉ chạm performance ở mức UI rules).
- Offline hoàn toàn hoặc agent chặn domain `raw.githubusercontent.com` → đừng dùng skill (nó fetch `command.md` mỗi review; không mạng = không rules).
- Muốn skill tự chọn visual direction/palette/layout → không hệ nào trong đây (guidelines audit code, không design thay bạn).

### Cài đặt
- Cách 1 — skill review (khuyến nghị, mọi agent có `npx`): `npx skills add vercel-labs/agent-skills --skill web-design-guidelines` (nguồn `vercel.com/docs/agent-resources/skills` + README collection). Chú ý tên lệch: repo là `web-interface-guidelines`, skill trong collection là `web-design-guidelines` (v1.0.0, `SKILL.md` đã đọc 03/11/2026: fetch `https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md` trước mỗi review).
- Cách 2 — command 1 file (7 agent, script chính chủ): `curl -fsSL https://vercel.com/design/guidelines/install | bash` (nguồn `install.sh` đã đọc: tự detect Amp/Claude Code/Cursor/OpenCode/Windsurf/Antigravity/Gemini CLI, tải `command.md` về đúng thư mục lệnh từng agent → chạy `/web-interface-guidelines <file>`).
- Cách 3 — generate từ đầu (không cài): tải `https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/AGENTS.md` (156 dòng, đã fetch 03/11/2026) bỏ vào root project làm `AGENTS.md` để agent áp khi sinh UI.
- Yêu cầu: Node cho `npx` (cách 1); `curl+bash` (cách 2); mạng mở `raw.githubusercontent.com` (skill fetch rules mỗi review — chặn là FAIL).
- Kiểm tra (đã chạy 03/11/2026): `git clone --depth 1` OK (5 file: `README.md` 130 rules `^- \*\*` + `AGENTS.md` 156 dòng + `command.md` 191 dòng/104 check + `install.sh` + `LICENSE` MIT); `curl` 2 URL raw OK (đầu file khớp `description:` + `Concise rules...`); đọc `SKILL.md` skill v1.0.0 (4 bước fetch→đọc→check→file:line); API GitHub: 1.099★/74 forks/11 watchers/2 issues, tạo 10/09/2025, push 05/10/2026. Chưa chạy: `install.sh` thật (sợ ghi vào `~/.claude` máy này) + `npx skills add` thật (chưa có nhu cầu review UI trên máy này) — ghi rõ WARN.

### Cách item hoạt động
- Tổ chức đứng sau: `vercel-labs` (Vercel), repo `https://github.com/vercel-labs/web-interface-guidelines`, license MIT, `command.md` + `AGENTS.md` + `README.md` (dài, human) + `install.sh` 7 agent. Số liệu API GitHub ngày 03/11/2026: 1.099★ / 74 forks / 11 watchers / 2 issues mở. Skill review sống ở collection riêng `https://github.com/vercel-labs/agent-skills` (33,4k★/2,9k forks): skill `web-design-guidelines` v1.0.0, ~815k installs via skills.sh (02/11/2026, +29,2k/7d — nguồn open-skills tracker).
- Phương thức hoạt động chung: 3 artifact cho 3 việc khác nhau — (1) `README.md` (130 rules chi tiết cho người đọc, 8 sections: Interactions 29 / Content 24 / Forms 19 / Performance 16 / Copywriting 14 / Design 11 / Animations 10 / Layout 7); (2) `AGENTS.md` (156 dòng MUST/SHOULD/NEVER súc tích cho agent khi GENERATE); (3) `command.md` (104 checks + output format cho agent khi REVIEW: đọc files → đối chiếu từng rule → in `file:line` terse theo file, file sạch ghi `✓ pass`, không preamble). Skill `SKILL.md` không chứa rules — nó bắt agent fetch `command.md` tươi trước mỗi review nên rules mới không cần cài lại.
- Khác biệt vận hành theo usecase: review file có sẵn (fetch `command.md` + đọc files + in findings, xem [Usecase con 1](#usecase-con-1-review-ui-code-co-san--manh-nhat)) khác generate mới (paste `AGENTS.md`, agent tự ràng buộc lúc viết, xem [Usecase con 2](#usecase-con-2-generate-ui-moi-theo-agentsmd)) khác audit interactions/animation (keyboard/focus/reduced-motion/touch, xem [Usecase con 3](#usecase-con-3-audit-interactionsanimation-touch)) khác audit performance/content (virtualize/images/CLS/i18n/dark-mode, xem [Usecase con 4](#usecase-con-4-audit-performancetypographyimageslocale)).

### Cốt lõi bất biến
- Fetch rules tươi mỗi review, cấm review bằng trí nhớ: agent phải fetch `https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md` (qua WebFetch) trước mỗi lần check rồi mới đọc files (nguyên văn `SKILL.md` 4 bước). Review không fetch = không còn gọi là dùng hệ.
- Output `file:line` terse, cấm preamble: findings gộp theo file, 1 dòng 1 lỗi + vị trí (`src/Button.tsx:42 - icon button missing aria-label`), file sạch ghi `✓ pass`, bỏ qua giải thích nếu fix đã hiển nhiên (nguồn `command.md` mục Output Format). Báo cáo dài dòng/scored rating = sai hệ.
- Đúng artifact đúng việc: GENERATE → `AGENTS.md` (MUST/SHOULD/NEVER lúc viết); REVIEW → `command.md`/skill (checklist lúc soi). Lấy `README.md` dài để review từng dòng trong agent = sai hệ (nặng context, không có output format).
- Sau khi dùng phải nêu được: nguồn rules nào đã fetch (URL + ngày) + files nào đã check + findings/pass nào; không nêu được = chưa thực sự dùng hệ.

### Phần tùy chỉnh
- Được đổi: files/pattern nào in-scope (`<file-or-pattern>`, không files thì agent hỏi), pillar nào soi sâu (a11y/forms vs animation vs performance vs copy — vd chỉ soi Forms cho trang checkout), mức nghiêm (MUST chặn merge vs SHOULD khuyên). Cổng duyệt 2 tầng: (1) artifact nào — shortlist files/pattern + pillar kèm lý do qua question tool, user pick mới review (review cả repo 1 phát tốn context + findings loãng — log scope đã duyệt TRƯỚC khi chạy); (2) giữ/đổi gì — findings nào fix ngay, cái nào waive có lý do. Waiver (bỏ qua MUST, review offline bằng bản copy cũ) phải quote câu ok tường minh của user. Cấm đưa `must-not` (review bằng trí nhớ, bịa rules, chấm điểm thay file:line) vào danh sách tùy chỉnh.

### Phân công ai làm gì
- Agent chính: shortlist files/pattern (chờ user pick — cấm tự chốt cả repo rồi review), fetch `command.md` tươi, đọc files, chạy checklist, trình findings `file:line` + fix gợi ý, verify lại sau fix.
- Giao cho claude các bước cần browser/người thật: verify visual mà static check không kết luận được (focus ring có bị sticky header che không, contrast thực, motion có flicker không, tap highlight, safe-area notch) — kèm file + rules cần verify + output mong đợi (ảnh/số đo); cấm agent tự kết luận render đạt khi không có browser.
- Agent verify: findings có `file:line` click được + file sạch có `✓ pass` + re-check sau fix hết MUST; visual đã qua claude khi có.

### Định vị khác biệt (số liệu ngày 03/11/2026 trừ khi ghi khác)
- So với `../hallmark/` (39,5k★, system + gates máy + sweep + review lạnh trong repo này): khác tầng — Hallmark SINH system mới (tokens scaffold + theme deal + hero-first + `sloplint --render` + Finish review) rồi mới check; guidelines SOI code có sẵn bằng checklist 130 rules, không sinh/đổi file nào. Chọn guidelines thay vì Hallmark khi code đã có và chỉ cần 1 pass audit nhanh ghi `file:line` (ngưỡng: review xong 1 component <10 phút, không đổi system); chọn Hallmark khi cần page-shape khác per brief + gates đo được (contrast 4.5:1/fold 1280x800/word budget) + sweep đến sạch. 2 hệ bổ trợ nhau: guidelines soi → Hallmark sửa system.
- So với skill `react-best-practices` (cùng collection `vercel-labs/agent-skills` 33,4k★, 40+ rules React/Next.js perf 8 categories): khác trục — best-practices tối ưu React sâu (waterfall/bundle/server/fetch/re-render, Critical→Low); guidelines phủ rộng UX (a11y/focus/forms/animation/typography/images/locale/copy). Chọn guidelines thay vì best-practices khi findings mong đợi là `aria-label`, `transition: all`, `...` → `…`, `Intl.*`; chọn best-practices khi findings là waterfall/bundle/server-component. Trang React mới cần cả hai: generate theo cả 2, review 2 pass.
- Khung trung thực: guidelines thắng ở audit checklist nhanh + rẻ (fetch 1 file, không model đặc biệt, không key) + installs lớn (~815k); thua ở tính sinh system (không tokens/theme/sweep như Hallmark) + thua ở độ sâu React perf (như best-practices) + phụ thuộc mạng (fetch rules mỗi review, offline là chết).

### Bản đồ phủ usecase (quét HẾT README 130 rules + AGENTS.md 156 dòng + command.md 104 checks 03/11/2026 — ★ mạnh nhất đầu)
- ★ Review UI code có sẵn ra `file:line` (toàn bộ `command.md` 104 checks + output format): xem Usecase 1.
- Generate UI mới theo `AGENTS.md` (73 MUST + 31 SHOULD + 7 NEVER lúc viết): xem Usecase 2.
- Trung bình: audit interactions/animation/touch (keyboard 29 rules Interactions + focus rings + reduced-motion + compositor `transform/opacity` + touch/drag/gestures): xem Usecase 3.
- Trung bình: audit performance/typography/images/locale (virtualize >50 items + CLS + preconnect + tabular-nums + `…`/quotes + `Intl.*` + dark-mode + safe-area): xem Usecase 4.
- Trung bình: copywriting Vercel-specific (active voice, Title Case headings, numerals, error message kèm fix, `&` vs `and`) → dùng khi soi docs/marketing page, không phải UI logic.
- Trung bình: cài command cho 7 agent (`install.sh`: Amp/Claude Code/Cursor/OpenCode/Windsurf/Antigravity/Gemini CLI) → dùng khi team nhiều agent cần chung 1 lệnh `/web-interface-guidelines`.
- KHÔNG hỗ trợ → thay thế: sinh system/tokens/theme/sweep → `../hallmark/`; bricks React animated → `../reactbits/`; tối ưu React sâu (waterfall/bundle) → skill `react-best-practices`; landing taste đóng gói → `../skillry/`; chấm điểm/rating → không hệ nào (guidelines chỉ list findings, không score).

### Hồ sơ quyết định
- Việc DÙNG (4, cụ thể): 1. review 1 component/page trước merge ra `file:line` (icon thiếu `aria-label`, `transition: all`, ảnh thiếu dimensions); 2. kẹp `AGENTS.md` vào project để agent sinh UI mới đã đúng rules; 3. audit a11y/forms 1 pass (labels, autocomplete, paste, errors, focus-first-error); 4. audit motion/perf/typo nhanh (reduced-motion, virtualize >50, `…`, `Intl.*`).
- Việc KHÔNG DÙNG (4, mỗi việc kèm hệ thay thế): 1. sinh system mới pass gates → dùng `../hallmark/`; 2. cần bricks React → dùng `../reactbits/`; 3. tối ưu React sâu → dùng skill `react-best-practices`; 4. offline/chặn `raw.githubusercontent.com` → không hệ nào (skill bắt fetch tươi).
- Free / tổng + giá: 100% free, 0đ toàn bộ, MIT (nguồn `LICENSE` repo gốc). Không subscription, không tài khoản, không key, không phí model ngoài (fetch 1 file text). Tổng sở hữu = 0đ + tiền mạng.
- Ma sát cài đặt: 1 bước tới lệnh đầu (`npx skills add vercel-labs/agent-skills --skill web-design-guidelines` rồi `/review my UI <file>`; hoặc `curl .../install | bash` rồi `/web-interface-guidelines <file>`; hoặc tải `AGENTS.md` bỏ vào root). ĐÃ chạy 03/11/2026: clone + đếm (130/156/104) + `curl` 2 URL raw OK + đọc `SKILL.md` v1.0.0 + API GitHub. Chưa chạy: `install.sh` thật + `npx skills add` thật (ghi WARN). Rào cản duy nhất: mạng mở `raw.githubusercontent.com` mỗi review.
- Đối thủ viral cùng phân khúc: `../hallmark/` (39,5k★, sinh system + gates) vs skill `react-best-practices` (cùng collection 33,4k★, React perf sâu).
- Chọn nó thay vì đối thủ khi: cần 1 pass audit checklist nhanh trên code đã có, findings là rules UI cụ thể (`aria-label`, `transition: all`, `...` → `…`), không muốn đổi system hay tối ưu React sâu. Ví dụ đổi lựa chọn: review PR bổ sung form checkout → guidelines; dựng landing mới cần shape khác + pass gates → Hallmark; tối ưu waterfall/bundle Next.js → best-practices.
- TUYỆT ĐỐI không dùng khi: offline/chặn fetch rules; muốn AI tự chọn visual direction thay mình; cần scored report (guidelines chỉ list findings); review bằng trí nhớ không fetch (FAIL core).

### Usecase con 1: review UI code có sẵn (★ mạnh nhất)
- Khi dùng: có 1 file/pattern UI (sở hữu/được phép) cần soi trước merge.
- Khi bỏ qua: sinh mới chưa có file → Usecase 2; chỉ soi interactions → Usecase 3; chỉ soi perf/typo → Usecase 4.
- Cơ chế khác các usecase khác ở đâu: duy nhất fetch `command.md` + đọc files + in findings `file:line`, không viết/sửa file; các usecase khác ràng buộc lúc viết (AGENTS.md) hoặc soi sâu 1 pillar.
- Lệnh copy-paste: `npx skills add vercel-labs/agent-skills --skill web-design-guidelines` rồi prompt agent `Review my UI: src/components/CheckoutForm.tsx` (nguồn `SKILL.md`: fetch guidelines → đọc files → check all rules → output format; không files thì agent hỏi).
- Ngưỡng số cần đạt: findings đủ `file:line` click được (vd `src/CheckoutForm.tsx:42 - icon button missing aria-label`); file sạch ghi `✓ pass`; 0 preamble; MUST hết mới merge.
- Ví dụ input-output (minh họa, không phải mặc định — files do user pick trước): input "review `src/Button.tsx` + `src/Modal.tsx`" → output `## src/Button.tsx` + `src/Button.tsx:42 - icon button missing aria-label` + `src/Button.tsx:67 - transition: all → list properties` + `## src/Modal.tsx ✓ pass`.
- Pitfalls riêng: review bằng trí nhớ không fetch (rules trôi — FAIL core); paste cả repo 1 phát (context tràn, findings loãng — shortlist files trước); đòi scored rating (hệ không score, chỉ list).
- Phân công usecase này: agent chính shortlist files (user pick) → fetch + check + trình findings; giao claude verify visual (focus ring, contrast, motion) khi static không kết luận được; verify bằng re-check hết MUST.

### Usecase con 2: generate UI mới theo AGENTS.md
- Khi dùng: project mới/trang mới, muốn agent viết đúng rules ngay từ đầu.
- Khi bỏ qua: code đã có cần soi → Usecase 1; cần system pass gates → Hallmark.
- Cơ chế khác các usecase khác ở đâu: duy nhất ràng buộc lúc VIẾT (MUST/SHOULD/NEVER trong `AGENTS.md` 156 dòng), không có output findings; các usecase khác check sau khi đã có code.
- Lệnh copy-paste: `curl -sL https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/AGENTS.md -o AGENTS.md` (tải về root project; agent đọc tự động).
- Ngưỡng số cần đạt: code sinh ra đạt 73 MUST (labels, focus-visible, autocomplete, `transform/opacity` only, images có dimensions, `Intl.*`); không dính 7 NEVER (`outline: none` không thay thế, block paste, disable zoom, `transition: all`, `<div onClick>` nav, layout props animate, GIF thay video).
- Ví dụ input-output (minh họa): input "sinh form checkout mới, project đã có AGENTS.md này" → output `CheckoutForm.tsx` có `<label htmlFor>`, `autocomplete`, errors inline + focus first error, submit không pre-disable, buttons có `hover:` + contrast tăng.
- Pitfalls riêng: tưởng có AGENTS.md là khỏi review (vẫn phải review bằng Usecase 1 sau khi sinh); `AGENTS.md` project cũ override (ghi rõ file nào thắng); agent cũ không đọc `AGENTS.md` tự động (phải chỉ rõ trong prompt).
- Phân công usecase này: agent chính tải `AGENTS.md` + sinh code theo MUST; không cần claude trừ khi cần check visual sau sinh (sang Usecase 1 + claude).

### Usecase con 3: audit interactions/animation/touch
- Khi dùng: trang nhiều tương tác (modal/drawer/drag/gesture/animation) cần soi keyboard/focus/motion/touch.
- Khi bỏ qua: form tĩnh → Usecase 1; perf/typo → Usecase 4.
- Cơ chế khác các usecase khác ở đâu: chỉ soi pillar Interactions + Animations + Touch (`command.md` sections Accessibility/Focus/Animation/Touch + `README.md` 29 + 10 rules), bỏ qua perf/typo/copy.
- Lệnh copy-paste: `/web-interface-guidelines src/components/Modal.tsx` (sau Cách 2; hoặc cùng prompt skill nhưng dặn `focus on keyboard, focus states, animation, touch rules only`).
- Ngưỡng số cần đạt: keyboard full APG (WAI-ARIA Authoring Practices Guide — chuẩn pattern bàn phím của W3C) + focus-visible không bị sticky che + hit target ≥24px (mobile 44px) + input font ≥16px mobile + `prefers-reduced-motion` có variant + chỉ `transform/opacity` + autoplay >5s có pause/stop/hide + drag có tap/click + keyboard alternative.
- Ví dụ input-output (minh họa): input "soi `Modal.tsx` pillar interaction" → output `Modal.tsx:12 - missing overscroll-behavior: contain` + `:34 - "..." → "…"` + `pass` cho focus-trap nếu có.
- Pitfalls riêng: static check không thấy focus bị che (phải mở browser thật — giao claude); `pointer: fine` vs coarse nhầm (test hybrid riêng); gesture-only không alternative (WCAG dragging — FAIL).
- Phân công usecase này: agent chính check static; giao claude mở browser verify focus/contrast/motion/tap thật; verify bằng checklist pillar + ảnh/clip khi cần.

### Usecase con 4: audit performance/typography/images/locale
- Khi dùng: trang nặng nội dung/list dài/ảnh nhiều/i18n cần soi perf + typo + images + locale + dark-mode.
- Khi bỏ qua: interactions phức tạp → Usecase 3; review full → Usecase 1.
- Cơ chế khác các usecase khác ở đâu: chỉ soi pillar Performance + Typography + Content Handling + Images + Locale + Dark Mode (`command.md` sections tương ứng), bỏ qua keyboard/animation sâu.
- Lệnh copy-paste: `/web-interface-guidelines src/pages/Feed.tsx` (hoặc prompt skill + dặn `focus on performance, typography, images, locale rules only`).
- Ngưỡng số cần đạt: list >50 items virtualize (`virtua`/`content-visibility: auto`) + ảnh có width/height (CLS) + below-fold `loading="lazy"` + `<link rel="preconnect">` CDN + `…` không `...` + quotes cong + `tabular-nums` cột số + `Intl.DateTimeFormat`/`Intl.NumberFormat` + `color-scheme: dark` + `translate="no"` cho brand/code tokens.
- Ví dụ input-output (minh họa): input "soi `Feed.tsx` 200 rows ảnh" → output `Feed.tsx:88 - large array .map() without virtualization` + `:102 - <img> missing width/height` + `:130 - hardcoded date format, use Intl.DateTimeFormat`.
- Pitfalls riêng: đo perf bằng mắt (phải throttle CPU/network + tắt extension — theo `README.md` Performance); GIF thay video (đổi `<video autoplay muted loop playsinline>` + still); font không subset/preload (FOIT — Flash Of Invisible Text — chữ vô hình chờ font + layout shift).
- Phân công usecase này: agent chính check static + số đo; giao claude đo render thật (throttle, CLS, LCP) khi cần; verify bằng findings + số đo.

### Các bước chung
1. Shortlist files/pattern + pillar (full vs interactions vs perf) kèm lý do qua question tool, user pick mới chạy.
2. Fetch rules tươi (`command.md` cho review, `AGENTS.md` cho generate) — ghi URL + ngày.
3. Review: đọc files → đối chiếu từng rule → in `file:line` terse (file sạch `✓ pass`); Generate: viết code theo MUST/SHOULD/NEVER.
4. Trình findings + fix gợi ý; visual nào static không kết luận được thì giao claude (kèm file + rules + output mong đợi).
5. Fix → re-check tới hết MUST → báo xong kèm nguồn rules + files + findings/pass.

### Prompt mẫu
- "Review UI của `src/components/CheckoutForm.tsx` theo web-interface-guidelines (fetch command.md tươi), pillar forms + a11y trước, output file:line terse, file sạch ghi pass."
- "Tải AGENTS.md web-interface-guidelines vào root project này, rồi sinh form checkout mới tuân thủ 73 MUST (labels, autocomplete, focus-visible, transform/opacity, images dimensions, Intl)."
- "Audit interactions cho `src/components/Modal.tsx`: keyboard APG, focus-visible, overscroll-behavior, reduced-motion, touch-action, gesture alternatives."
- Ví dụ điền sẵn: "Review `src/Button.tsx` (repo mình, 1 file): fetch `https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md` (03/11/2026), check 104 rules, output file:line + pass/fail MUST."

### Pitfalls
- Review bằng trí nhớ không fetch `command.md` (rules trôi theo main — FAIL core, SKILL.md bắt fetch mỗi lần).
- Lẫn tên: skill là `web-design-guidelines` (collection agent-skills), repo là `web-interface-guidelines` — cài sai tên là không thấy skill.
- Paste cả repo 1 phát (context tràn + findings loãng — shortlist files/pattern + user pick trước).
- Đòi scored report/rating (hệ chỉ list findings + `✓ pass` — cần score thì tự chấm ngoài).
- Tưởng checklist thay system (guidelines không sinh tokens/theme/sweep — cần system pass gates thì sang Hallmark).
- Offline/chặn `raw.githubusercontent.com` mà vẫn claim đã review (FAIL — phải khai báo + dừng).
- Visual (focus bị che, contrast, motion flicker) kết luận bằng static (phải giao claude mở browser thật).

### Tham khảo sử dụng (quyết định được + số có trọng số)
- Nhận xét sâu: [uichemy.com design-skills review](https://uichemy.com/design-skills/web-design-guidelines/) (truy cập 03/11/2026) — *"It reviews code and does not generate designs"* + *"If your agent runs without network access... it cannot load the rules"* → xác nhận quyết định: review/audit thì dùng, sinh system/taste thì sang Hallmark; offline thì bỏ. Kèm Best-for/Not-for: hợp React/Next.js pre-merge, không hợp chọn visual direction/match Figma/score.
- Nhận xét sâu (chính chủ): [Vercel changelog 12/01/2026, John Phamous](https://vercel.com/changelog/web-interface-guidelines-now-available-as-an-agent-command) — guidelines thành agent command chính thức; cùng collection còn `react-best-practices` (40+ rules perf) → phân biệt: UI/UX checklist vs React perf sâu.
- Số trung bình có trọng số: repo `web-interface-guidelines` 1.099★/74 forks/11 watchers (API 03/11/2026, tạo 10/09/2025); collection `agent-skills` 33,4k★/2,9k forks; skill `web-design-guidelines` ~815k installs via skills.sh (02/11/2026, +29,2k/7d, nguồn open-skills tracker) vs 664.841 installs (25/09/2026, nguồn vetted.tools — số cũ hơn). Trọng số: installs skills.sh (hành vi cài thật, trăm nghìn mẫu) đáng tin hơn stars repo (1,1k, mới nổi).
- Tiếng Việt: truy vấn `web-interface-guidelines đánh giá` không trả về review Việt độc lập → `chưa xác minh`.
- Mâu thuẫn: installs rất cao (~815k) vs repo stars khiêm tốn (1,1k) → phán quyết: installs thuộc cả collection agent-skills (kênh phân phối lớn), repo rules độc lập còn mới; dùng installs để tin độ phủ, dùng stars + deep review để tin chất lượng rules.

### Tham khảo
- Repo: https://github.com/vercel-labs/web-interface-guidelines
- Đọc theo thứ tự: `README.md` (130 rules human) → `AGENTS.md` (156 dòng MUST/SHOULD/NEVER, generate) → `command.md` (104 checks + output format, review) → `install.sh` (7 agent) → skill `https://github.com/vercel-labs/agent-skills` (`skills/web-design-guidelines/SKILL.md` v1.0.0).
- Quy tắc fetch tươi: `https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md` (review) + `.../AGENTS.md` (generate).

### Được dùng ở đâu
- Dùng CHO UI: xem `../../domains/ui/using-web-interface-guidelines.md` (review/audit UI code) — index `../../domains/ui/README.md`.

### Quay lại index
- Về `../../domains/ui/README.md` để so sánh định vị với `hallmark/` + `reactbits/` + `skillry` (web).
- Xem thêm item liên quan: `../hallmark/` (sinh system + gates) + `../reactbits/` (bricks hiệu ứng).

---

## English

### When to use
- Review/audit existing UI code (React/Next.js or static HTML) into a terse `file:line` finding list — instead of taste-based review.
- Pin a shared checklist for agents generating new UI (drop `AGENTS.md` in the project): accessible + fast + delightful, 73 MUST + 31 SHOULD + 7 NEVER (counted 03/11/2026).
- Focused audits: keyboard/focus/forms, `prefers-reduced-motion` animation, performance (virtualize >50 items, CLS, preconnect), i18n (`Intl.*`, `translate="no"`).
- Supported agent (Claude Code, Cursor, Codex, OpenCode...) + network access (the skill fetches fresh rules every review).

### When to skip
- New system/design needing machine gates + theme deal + hero-first + cold review → use `../hallmark/` (guidelines audit checklists, they generate no system/tokens/sweep).
- Ready-made animated React bricks → use `../reactbits/` (no components here).
- Deep React/Next.js performance (waterfalls, bundles, server) → use the sibling `react-best-practices` skill in `vercel-labs/agent-skills`.
- Fully offline or `raw.githubusercontent.com` blocked → skip the skill (it fetches `command.md` per review; no network = no rules).

### Install
- Option 1 — review skill (recommended, any agent with `npx`): `npx skills add vercel-labs/agent-skills --skill web-design-guidelines` (sources: vercel docs + collection README). Name mismatch: repo = `web-interface-guidelines`, skill = `web-design-guidelines` (v1.0.0; `SKILL.md` read 03/11/2026: fetch `.../command.md` before every review).
- Option 2 — 1-file command (7 agents, official script): `curl -fsSL https://vercel.com/design/guidelines/install | bash` (source `install.sh` read: auto-detects Amp/Claude Code/Cursor/OpenCode/Windsurf/Antigravity/Gemini CLI → run `/web-interface-guidelines <file>`).
- Option 3 — generate from scratch (no install): download `https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/AGENTS.md` (156 lines, fetched 03/11/2026) into the project root.
- Verified 03/11/2026: `--depth 1` clone OK (130 `^- \*\*` rules + 156-line AGENTS.md + 191-line/104-check command.md + MIT LICENSE); both raw URLs fetch OK; GitHub API: 1,099 stars / 74 forks / 11 watchers / 2 issues, created 10/09/2025, pushed 05/10/2026. NOT run: real `install.sh` + real `npx skills add` (WARN recorded).

### How the item works
- Backing organization: `vercel-labs` (Vercel), repo `https://github.com/vercel-labs/web-interface-guidelines`, MIT, `command.md` + `AGENTS.md` + long `README.md` + 7-agent `install.sh`. GitHub API 03/11/2026: 1,099 stars / 74 forks / 11 watchers / 2 open issues. The review skill lives in `https://github.com/vercel-labs/agent-skills` (33.4k stars / 2.9k forks): `web-design-guidelines` v1.0.0, ~815k installs via skills.sh (02/11/2026, +29.2k/7d).
- Core operating method: 3 artifacts for 3 jobs — (1) `README.md` (130 detailed human rules, 8 sections); (2) `AGENTS.md` (156 terse MUST/SHOULD/NEVER lines for GENERATION); (3) `command.md` (104 checks + output format for REVIEW: read files → check every rule → terse per-file `file:line`, clean files get `✓ pass`, no preamble). The skill's `SKILL.md` holds no rules — it forces a fresh `command.md` fetch per review.
- Per-usecase differences: review existing files (fetch + findings, [Sub-usecase 1](#sub-usecase-1-review-existing-ui-code--strongest)) vs generate new UI (`AGENTS.md` constraints at write time, [Sub-usecase 2](#sub-usecase-2-generate-new-ui-from-agentsmd)) vs interaction/animation audit ([Sub-usecase 3](#sub-usecase-3-interactionanimationtouch-audit)) vs performance/content audit ([Sub-usecase 4](#sub-usecase-4-performancetypographyimageslocale-audit)).

### Invariant core
- Fresh-rules fetch per review, never review from memory: fetch `.../command.md` via WebFetch before every check (verbatim `SKILL.md` 4 steps). No fetch = not using the system.
- Terse `file:line` output, no preamble: findings grouped per file, clean files `✓ pass`, skip obvious-fix explanations (`command.md` Output Format). Long prose/scored ratings = off-system.
- Right artifact per job: GENERATE → `AGENTS.md`; REVIEW → `command.md`/skill. Never feed the long `README.md` line-by-line into an agent review.
- After use, state: which rules source was fetched (URL + date) + which files were checked + findings/passes; otherwise not really used.

### Customizable surface
- Tunables: which files/pattern are in scope, which pillar goes deep (a11y/forms vs animation vs performance vs copy), bar level (MUST blocks merge vs SHOULD advises). Two-level approval: (1) shortlist files/pattern + pillar with reasons via the question tool, user picks before any review (full-repo dumps waste context — log approved scope FIRST); (2) what gets fixed vs waived with reasons. Waivers (skipping MUSTs, offline review from a stale copy) must quote the user's explicit ok. Never list `must-not` items here.

### Work split
- Main agent: shortlist files (wait for user pick — never self-pick a whole repo), fetch fresh `command.md`, read files, run the checklist, present `file:line` findings + fixes, re-check after fixes.
- Hand browser/human steps to claude as a whole: visual verification static checks cannot decide (focus obscured by sticky headers, real contrast, motion flicker, tap highlight, notch safe-areas) — with files + rules + expected output; the agent never asserts render results without a browser.
- Agent verifies: clickable `file:line` findings + `✓ pass` on clean files + MUSTs clear on re-check; visuals covered by claude where needed.

### Differentiating positioning
- Vs `../hallmark/` (39.5k stars, system + machine gates + sweep + cold review): different layer — Hallmark GENERATES new systems (token scaffold + theme deal + hero-first + `sloplint --render` + Finish review); guidelines AUDIT existing code against a 130-rule checklist and change nothing. Pick guidelines when code exists and one fast audit pass suffices (bar: one component reviewed <10 min, system untouched); pick Hallmark for per-brief page shapes + measurable gates (4.5:1 contrast / 1280x800 fold / word budget) swept clean. They complement: guidelines find → Hallmark fixes the system.
- Vs the sibling `react-best-practices` skill (same 33.4k-star collection, 40+ React/Next.js perf rules): different axis — best-practices goes deep on React (waterfalls/bundles/server/fetch/re-renders); guidelines go wide on UX (a11y/focus/forms/animation/typography/images/locale/copy). Pick guidelines when expected findings are `aria-label`, `transition: all`, `...` → `…`, `Intl.*`; pick best-practices for waterfall/bundle findings. New React pages need both: generate with both, review in 2 passes.
- Honest frame: guidelines win on fast cheap audits (1 text file fetch, no special model, no keys) + huge installs (~815k); lose on system generation (no tokens/themes/sweeps) + React-perf depth + network dependence (offline kills reviews).

### Coverage map (whole catalog scanned 03/11/2026 — ★ strongest first)
- ★ Review existing UI code into `file:line` (all of `command.md` 104 checks + output format): see Sub-usecase 1.
- Generate new UI from `AGENTS.md` (73 MUST + 31 SHOULD + 7 NEVER at write time): see Sub-usecase 2.
- Medium: interaction/animation/touch audit (keyboard + focus + reduced-motion + compositor props + touch/drag/gestures): see Sub-usecase 3.
- Medium: performance/typography/images/locale audit (virtualize >50 + CLS + preconnect + tabular-nums + `…`/quotes + `Intl.*` + dark-mode + safe-area): see Sub-usecase 4.
- Medium: Vercel-specific copywriting (active voice, Title Case, numerals, fix-carrying errors): use for docs/marketing pages.
- Medium: 7-agent command install (`install.sh`): use when a multi-agent team needs one shared `/web-interface-guidelines` command.
- NOT supported → use instead: system/token/theme/sweep generation → `../hallmark/`; animated React bricks → `../reactbits/`; deep React optimization → `react-best-practices`; packaged landing taste → `../skillry/`; scored reports → nothing here (findings only, no scores).

### Decision dossier
- Jobs SERVED (4, concrete): 1. pre-merge review of 1 component/page into `file:line`; 2. pinning `AGENTS.md` so generated UI already complies; 3. one-pass a11y/form audits; 4. fast motion/perf/typo audits.
- Jobs NOT served (4, each with replacement): 1. new gated systems → `../hallmark/`; 2. React bricks → `../reactbits/`; 3. deep React optimization → `react-best-practices`; 4. offline/blocked fetch → nothing (fresh fetch mandatory).
- Free / total + price: 100% free, $0 total, MIT (source: origin `LICENSE`). No subscription, account, keys, or extra model fees.
- Install friction: 1 step to the first command. Ran 03/11/2026 through: clone + counts + both raw-URL fetches + `SKILL.md` read + GitHub API. NOT run: real `install.sh` + real `npx skills add` (WARN). Only barrier: network access to `raw.githubusercontent.com` per review.
- Viral same-segment opponents: `../hallmark/` (39.5k stars, system + gates) vs `react-best-practices` (same 33.4k-star collection, deep React perf).
- Pick it over opponents when: a fast checklist pass over existing code is needed and findings are concrete UI rules — e.g. checkout-form PR review → guidelines; new landing needing shapes + gates → Hallmark; Next.js waterfall/bundle work → best-practices.
- NEVER use when: offline; AI-picked visual direction wanted; scored reports needed; reviewing from memory without fetching (core FAIL).

### Sub-usecase 1: review existing UI code (★ strongest)
- When to use: 1 owned/permitted UI file/pattern needs a pre-merge check.
- When to skip: nothing exists yet → Sub-usecase 2; interactions only → 3; perf/typo only → 4.
- Copy-paste command: `npx skills add vercel-labs/agent-skills --skill web-design-guidelines` then ask the agent `Review my UI: src/components/CheckoutForm.tsx` (source `SKILL.md`: fetch → read → check all → formatted output; asks when no files given).
- Numeric bar: clickable `file:line` findings; clean files `✓ pass`; zero preamble; MUSTs clear before merge.
- Input-output example (illustrative): `src/Button.tsx` + `src/Modal.tsx` → `## src/Button.tsx` + `src/Button.tsx:42 - icon button missing aria-label` + `src/Button.tsx:67 - transition: all → list properties` + `## src/Modal.tsx ✓ pass`.
- Own pitfalls: reviewing from memory (rules drift — core FAIL); whole-repo dumps (context flood — shortlist first); demanding scored ratings (unsupported).
- Work split: main agent shortlists (user picks) → fetches + checks + presents; claude covers visual verification; verify by MUST-clear re-check.

### Sub-usecase 2: generate new UI from AGENTS.md
- When to use: new project/page that should comply from the first keystroke.
- When to skip: code exists → Sub-usecase 1; gated system needed → Hallmark.
- Copy-paste command: `curl -sL https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/AGENTS.md -o AGENTS.md`.
- Numeric bar: generated code meets 73 MUSTs and avoids all 7 NEVERs.
- Input-output example (illustrative): new checkout form → `<label htmlFor>`, `autocomplete`, inline errors + first-error focus, no pre-disabled submit, `hover:` + raised contrast.
- Own pitfalls: assuming AGENTS.md removes the need for review (still run Sub-usecase 1 after generating); older project `AGENTS.md` conflicts (declare the winner); agents that don't auto-read `AGENTS.md` (name it in the prompt).
- Work split: main agent downloads + generates per MUST; claude only for post-generation visual checks.

### Sub-usecase 3: interaction/animation/touch audit
- When to use: interaction-heavy screens (modals/drawers/drag/gestures/animation).
- When to skip: static forms → Sub-usecase 1; perf/typo → Sub-usecase 4.
- Copy-paste command: `/web-interface-guidelines src/components/Modal.tsx` (or the skill prompt scoped with `focus on keyboard, focus states, animation, touch rules only`).
- Numeric bar: full APG keyboard (WAI-ARIA Authoring Practices Guide) + unobscured focus-visible + ≥24px targets (44px mobile) + ≥16px mobile inputs + `prefers-reduced-motion` variants + `transform`/`opacity` only + >5s autoplay has pause/stop/hide + drag has tap/click + keyboard alternatives.
- Input-output example (illustrative): `Modal.tsx` → `Modal.tsx:12 - missing overscroll-behavior: contain` + `:34 - "..." → "…"`.
- Own pitfalls: static-only verdicts on obscured focus (needs a real browser — hand to claude); `pointer: fine` vs coarse confusion; gesture-only paths (WCAG dragging FAIL).
- Work split: main agent does static checks; claude verifies focus/contrast/motion/tap in a real browser.

### Sub-usecase 4: performance/typography/images/locale audit
- When to use: content-heavy pages (long lists, many images, i18n).
- When to skip: complex interactions → Sub-usecase 3; full review → Sub-usecase 1.
- Copy-paste command: `/web-interface-guidelines src/pages/Feed.tsx` (or the skill prompt scoped with `focus on performance, typography, images, locale rules only`).
- Numeric bar: >50-item lists virtualized + explicit image dimensions (CLS) + below-fold `loading="lazy"` + CDN `<link rel="preconnect">` + `…`/`""`/`tabular-nums` + `Intl.*` dates/numbers + dark `color-scheme` + `translate="no"` on brand/code tokens.
- Input-output example (illustrative): 200-row `Feed.tsx` → `Feed.tsx:88 - large array .map() without virtualization` + `:102 - <img> missing width/height` + `:130 - hardcoded date format, use Intl.DateTimeFormat`.
- Own pitfalls: eyeballing perf (throttle CPU/network + disable extensions per origin Performance section); GIFs instead of video (switch to `<video autoplay muted loop playsinline>` + still); unsubsetted/unpreloaded fonts.
- Work split: main agent does static checks + numbers; claude measures real rendering (throttle, CLS, LCP) when needed.

### Shared steps
1. Shortlist files/pattern + pillar (full vs interactions vs perf) with reasons via the question tool; run only after the user picks.
2. Fetch fresh rules (`command.md` for review, `AGENTS.md` for generate) — record URL + date.
3. Review: read files → check every rule → terse `file:line` (clean files `✓ pass`); Generate: write to MUST/SHOULD/NEVER.
4. Present findings + fixes; hand browser-undecidable visuals to claude (files + rules + expected output).
5. Fix → re-check to zero MUSTs → report with rules source + files + findings/passes.

### Sample prompts
- "Review `src/components/CheckoutForm.tsx` against web-interface-guidelines (fresh command.md fetch), forms + a11y pillar first, terse file:line output, pass marks on clean files."
- "Download the web-interface-guidelines AGENTS.md into this project root, then generate a new checkout form complying with all 73 MUSTs."
- "Audit interactions for `src/components/Modal.tsx`: APG keyboard, focus-visible, overscroll-behavior, reduced-motion, touch-action, gesture alternatives."
- Filled example: "Review `src/Button.tsx` (my repo, 1 file): fetch `https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md` (03/11/2026), check 104 rules, output file:line + MUST pass/fail."

### Pitfalls
- Reviewing from memory without fetching `command.md` (rules drift on main — core FAIL).
- Name confusion: skill = `web-design-guidelines` (agent-skills collection), repo = `web-interface-guidelines` — wrong name finds nothing.
- Whole-repo dumps (context flood + dilute findings — shortlist + user pick first).
- Demanding scored reports (findings + `✓ pass` only — score elsewhere).
- Expecting system generation (no tokens/themes/sweeps — gated systems need Hallmark).
- Claiming a review while offline/fetch-blocked (FAIL — declare + stop).
- Asserting visuals (obscured focus, contrast, motion flicker) from statics (hand to claude with a real browser).

### Usage references (decisive + weighted)
- Deep review: [uichemy.com design-skills review](https://uichemy.com/design-skills/web-design-guidelines/) (accessed 03/11/2026) — *"It reviews code and does not generate designs"* + *"If your agent runs without network access... it cannot load the rules"* → verdict: audits → use; system/taste generation → Hallmark; offline → skip. Best-for/Not-for: fits React/Next.js pre-merge, not visual-direction/Figma-matching/scores.
- First-party: [Vercel changelog 12/01/2026, John Phamous](https://vercel.com/changelog/web-interface-guidelines-now-available-as-an-agent-command) — official agent-command release; sibling `react-best-practices` (40+ perf rules) draws the UI-checklist vs React-perf line.
- Weighted averages: origin repo 1,099 stars / 74 forks / 11 watchers (API 03/11/2026, created 10/09/2025); collection 33.4k stars / 2.9k forks; skill ~815k installs via skills.sh (02/11/2026, +29.2k/7d, open-skills tracker) vs 664,841 installs (25/09/2026, vetted.tools — older). Weight: skills.sh installs (hundreds of thousands of real installs) outweigh repo stars (1.1k, newly nổi).
- Vietnamese: query `web-interface-guidelines đánh giá` returns no independent Vietnamese review → `unverified`.
- Conflict: very high installs (~815k) vs modest repo stars (1.1k) → verdict: installs ride the whole agent-skills distribution channel; repo quality judged via stars + deep review.

### References
- Repo: https://github.com/vercel-labs/web-interface-guidelines
- Read order: `README.md` (130 human rules) → `AGENTS.md` (156 MUST/SHOULD/NEVER lines, generate) → `command.md` (104 checks + output format, review) → `install.sh` (7 agents) → skill collection `https://github.com/vercel-labs/agent-skills` (`skills/web-design-guidelines/SKILL.md` v1.0.0).
- Fresh-fetch rules: `https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md` (review) + `.../AGENTS.md` (generate).

### Where used
- Used FOR UI: see `../../domains/ui/using-web-interface-guidelines.md` (UI code review/audit) — index `../../domains/ui/README.md`.

### Back to index
- Back to `../../domains/ui/README.md` to compare positioning vs `hallmark/` + `reactbits/` + `skillry` (web).
- Related items: `../hallmark/` (system + gates generation) + `../reactbits/` (motion bricks).
