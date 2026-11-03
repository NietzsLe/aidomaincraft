# ai-website-cloner-template

## Tiếng Việt

### Dùng khi
- Cần tái dựng 1:1 một website đang sống thành code Next.js editable (migrate site mình sở hữu từ WordPress/Webflow/Squarespace, hoặc mất source chỉ còn bản live) mà muốn quy trình kỷ luật (Map → Observe → Build → Compare + `npm run check`).
- Có agent hỗ trợ Agent Skills/command (Claude Code, Codex, Cursor, OpenCode) + browser access + Node 24+, chấp nhận trả tiền inference model (khuyến nghị Opus 5.5; burn token theo số trang × vòng compare).
- Muốn học layout/animation production bằng code thật (observe-only, không build full).

### Bỏ qua khi
- Cần system/design mới pass gates đo được (contrast/focus/fold) → dùng `../hallmark/` (cloner copy design có sẵn, không sinh system/gates).
- Cần 1 landing đúng taste đóng gói có preview, không cần giống URL cụ thể → dùng `../skillry/` (phần web).
- Cần 1 effect/component React lẻ sở hữu source → dùng `../reactbits/`.
- Muốn clone site KHÔNG sở hữu/không được phép, phishing/giả mạo, bê design-copy-logo người khác ra sản phẩm, hoặc site cấm scrape/reproduction trong ToS → cấm tuyệt đối (xem [Cốt lõi bất biến](#cot-loi-bat-bien)).

### Cài đặt (đã clone + `npm install` + `npm run check` xanh trên Linux 30/10/2026; chưa chạy `/clone-website` vì máy này không có browser agent + tránh đụng ToS site thật)
- Cách 1 — template mới (khuyến nghị theo README gốc): bấm `Use this template` trên GitHub đặt tên repo → giao agent: `git clone <repo-mới>`, gỡ origin template nếu cần, `npm install`, `npm run check`.
- Cách 2 — prompt setup copy-paste (nguyên văn README gốc, đã đối chiếu): `Set up https://github.com/JCodesMore/ai-website-cloner-template as a standalone project in a new folder on my computer. Ask me where to put it. Clone the repository, remove its origin remote, install dependencies, and run npm run check. Leave it ready for me to clone a website.`
- Chạy clone (cần agent có browser access; Claude Code/Cursor): `/clone-website https://example.com` (nhiều URL: `/clone-website <url1> <url2> ...`).
- Yêu cầu: Node.js 24+ (máy này v24.22.0 đạt; `.nvmrc` ghi `24`, `package.json` có `engines: node >=24`); không login/tài khoản cho template; Docker tùy chọn (`docker compose up dev --build`, port 3001).
- Kiểm tra (đã chạy 30/10/2026, output thật): `npm install` → 476 packages OK (cảnh báo install-scripts của `msw`/`unrs-resolver` — xem, không approve bừa); `npm run check` (= `lint` + `typecheck` + `build`) → build Next.js 16.3.5 xanh, prerender tĩnh 2 routes (`/`, `/_not-found`).

### Cách item hoạt động
- Tổ chức đứng sau: cá nhân `JCodesMore`, repo template `https://github.com/JCodesMore/ai-website-cloner-template`, license MIT, bản 0.6.1, 80 commits từ 13/03/2026, đẩy cuối 19/10/2026, CI `npm ci` + lint + (typecheck/build) trên Node 24. Số liệu API GitHub ngày 30/10/2026: 38,004★ / 5,583 forks / 164 watchers / 5 issues mở.
- Phương thức hoạt động chung: template Next.js 16 (App Router, React 19, TS strict, shadcn/ui + Tailwind v4 tokens oklch — oklch là không gian màu mặc định của Tailwind v4) dựng sẵn + 1 skill chuẩn `clone-website` (`.agents/skills/clone-website/SKILL.md` 61 dòng + 2 references; Codex/Cursor/OpenCode đọc trực tiếp, Claude Code qua bridge `.claude/commands/clone-website.md`). Agent trigger khi user cho URL + yêu cầu clone/rebuild/reverse-engineer; chạy 4 bước Map (route map — bản đồ URL nguồn → route/file local + ai sở hữu file nào) → Observe (desktop/mobile, states, assets/fonts thật) → Build (components editable, interactions thật) → Compare (side-by-side cùng viewport/state, repair lớn-trước, `npm run check`).
- Khác biệt vận hành theo usecase: clone mới 1 URL (đủ 4 bước từ template trống, xem [Usecase con 1](#usecase-con-1-clone-1-url-11-tu-template-trong)) khác migrate nhiều trang (route map nhiều URL + giữ pathnames + preserve/gộp app, xem [Usecase con 2](#usecase-con-2-migrate-site-nhieu-trang-minh-so-huu)) khác nối trang vào clone có sẵn (extend layout/styles + regression routes cũ, xem [Usecase con 3](#usecase-con-3-them-trang-moi-vao-clone-co-san)) khác compare/repair (không build mới, sửa theo diff lớn-trước + check, xem [Usecase con 4](#usecase-con-4-comparerepair--production-check-tren-clone-co-san)).

### Cốt lõi bất biến
- Quyền trước URL: chỉ clone site mình sở hữu/có cho phép bằng văn bản/mục đích học nội bộ không ship; cấm phishing/giả mạo/bê design-copy-logo-brand người khác ra sản phẩm/cày site cấm scrape (repo "Not Intended For"). Vi phạm = không còn dùng hệ (FAIL pháp lý). Sau khi dùng phải nêu được quyền gì (sở hữu/cho phép/học) + ToS đã check.
- Đủ 4 bước + check xanh mới gọi xong: Map → Observe → Build → Compare rồi `npm run check` (lint + typecheck + build) xanh; cấm gọi pixel-perfect khi chưa compare render (SKILL.md Compare). Không nêu được route map + checks đã chạy + gaps còn lại = chưa thực sự dùng hệ.
- Real content đo được, cấm placeholder: text/assets/fonts lấy từ file source thật (track URL→path, verify content-type/dimensions — URL `.png` có thể trả AVIF); substitute cùng tên khác metrics (icon set khác, font khác) = FAIL.
- Map trước build: route map + file ownership rõ trước khi viết code; giữ routes/assets đã viết, resolve collision trước khi thay; origins khác nhau thì apps riêng trừ khi user chốt gộp (prefix + scoped fonts/styles/layout riêng).
- Thiết kế quan sát được mới rebuild: mỗi observation là 1 sample của 1 rule (đổi width/height/input/state đến khi biết cái gì drive change); phân biệt scroll/click/hover/time-driven (giả click cho section scroll-driven = sản phẩm khác); DOM dump không thay nhìn thật.

### Phần tùy chỉnh
- Được đổi: URL/routes nào in-scope, gộp hay tách app, viewport/state nào observe, chính sách link out-of-scope (rewrite local khi route có trong scope, giữ trỏ source + disclose khi ngoài scope), sections nào delegate song song, giữ/đổi gì sau compare. Cổng duyệt 2 tầng: (1) artifact nào — shortlist URLs/routes + gộp/tách kèm lý do qua question tool, user pick mới chạy (full clone đốt nhiều token Opus — log scope đã duyệt TRƯỚC khi chạy); (2) giữ/đổi gì — diff nào sửa, gap nào giữ lại. Waiver (bỏ compare, ship thẳng) phải quote câu ok tường minh của user. Cấm đưa `must-not` (clone không quyền, phishing, hứa pixel-perfect chưa check) vào danh sách tùy chỉnh.

### Phân công ai làm gì
- Agent chính: check quyền/ToS + shortlist scope (chờ user pick — cấm tự chốt URL rồi clone), Map/Observe/Build/Compare, chạy `npm run check`, trình route map + ảnh compare + gaps; verify build xanh + side-by-side cùng viewport/state + runtime thật (nav, menu mobile, tab/accordion, carousel, overflow ngang, console errors).
- Giao cho claude các bước cần browser ngoài: quan sát source đa viewport/state (kèm URL + states cụ thể), chụp compare, reverse-check đụng hàng khi học — kèm route map + yêu cầu cụ thể; cấm agent tự bịa observation. Không có browser thì agent phải khai báo + dừng (DOM dump không thay thế), cấm claim đã observe.
- Agent verify: `npm run check` xanh + ảnh compare desktop/mobile + routes cũ còn chạy (khi extend) + file `docs/research/<site>/` (brief, asset map, evidence) tồn tại.

### Định vị khác biệt (số liệu API GitHub ngày 30/10/2026)
- So với `abi/screenshot-to-code` (80,901★/9,903 forks, ảnh chụp → code single-shot): khác input + vòng kiểm chứng — s2c sinh code từ 1 ảnh tĩnh; cloner quan sát site sống đa viewport/state bằng browser thật (scroll/click/hover/time-driven), lập route map, build Next.js/shadcn editable nhiều trang, vòng compare/repair + production check. Chọn cloner thay vì s2c khi cần giống hệt URL sống gồm states/responsive/motion + code editable nhiều file (ngưỡng: compare cùng viewport/state + `npm run check` xanh); chọn s2c khi cần mock tĩnh nhanh từ 1 ảnh, chấp nhận single-shot không kiểm chứng đa state.
- So với `firecrawl/firecrawl` (196,886★/10,396 forks, API scraping/extract): khác tầng — firecrawl extract dữ liệu có cấu trúc ở quy mô lớn (làm thay bước Observe khi cần crawl nhiều); cloner rebuild thành app Next.js chạy được. Chọn cloner thay vì firecrawl khi cần app editable hoàn chỉnh; chọn firecrawl khi chỉ cần data/extract hàng loạt, không cần rebuild giao diện.
- So với `../hallmark/` (system + gates trong repo này): cloner copy design có sẵn 1:1 (không sinh tokens/gates/review); hallmark sinh system mới pass gates. Quyết định: cần giống hệt site sống (có quyền) → cloner; cần system mới đạt chuẩn đo được → hallmark; phần custom viết thêm sau clone muốn đạt chuẩn thì sweep lại bằng hallmark.
- Khung trung thực: cloner thắng ở tái dựng 1:1 site sống + cấu trúc editable + check máy; thua ở tốc độ/chi phí (browser loops + token Opus, mỗi trang × mỗi vòng compare đều tốn tiền) và thua ở tính nguyên bản (copy, không system/gates) + phạm vi pháp lý hẹp (quyền/ToS). Cần mới nguyên bản → hallmark; cần taste đóng gói → Skillry web; cần data thô → firecrawl.

### Bản đồ phủ usecase (quét HẾT SKILL.md + 2 references + template + README 30/10/2026 — ★ mạnh nhất đầu)
- ★ Clone 1 URL 1:1 từ template trống (đủ 4 bước + check): xem Usecase 1.
- Migrate site nhiều trang mình sở hữu (route map + giữ pathnames + preserve/gộp app): xem Usecase 2.
- Thêm trang mới vào clone có sẵn (extend + regression routes cũ): xem Usecase 3.
- Compare/repair + production check trên clone có sẵn (không build mới): xem Usecase 4.
- Trung bình: học/deconstruct observe-only (đọc SKILL bước 2 + `inspection-guide.md` + `framer-and-motion.md`, ra `docs/research/<site>/` brief + asset map + measurements, không build) → dùng khi chỉ cần hiểu layout/animation để tự viết lại.
- Trung bình: chạy bằng Docker (`docker compose up dev --build`, port 3001; `up app` cho production) → dùng khi cần môi trường cách ly/không muốn cài Node 24 trên máy.
- KHÔNG hỗ trợ → thay thế: backend/logic động sau site (auth, DB, API riêng — clone chỉ mặt quan sát được + interactions, flows thật tự nối) → tự implement; đảm bảo pháp lý/ToS → tự kiểm tra + xin quyền (không hệ nào thay); asset pipeline tự động (thư mục `scripts/` hiện chỉ có `.gitkeep` — agent viết script tải theo từng site) → agent tự viết; text-to-UI nguyên bản → `../hallmark/`; screenshot tĩnh → screenshot-to-code; extract hàng loạt → firecrawl.

### Hồ sơ quyết định
- Việc DÙNG (3+, cụ thể): 1. migrate site mình sở hữu (WordPress/Webflow/Squarespace → Next.js routes giữ pathnames); 2. mất source chỉ còn bản live (rebuild từ URL quan sát được); 3. học production layout/animation (observe-only ra brief + measurements, tự viết lại).
- Việc KHÔNG DÙNG (3+, mỗi việc kèm hệ thay thế): 1. system/design mới pass gates → dùng `../hallmark/`; 2. landing taste đóng gói nhanh → dùng `../skillry/` (phần web); 3. mock tĩnh từ 1 ảnh → dùng screenshot-to-code; 4. data/extract hàng loạt → dùng firecrawl; 5. clone không quyền/phishing → không dùng hệ nào (cấm).
- Free / tổng + giá: template 0đ MIT toàn bộ (nguồn `LICENSE` + `package.json` 0.6.1, đọc 30/10/2026). Phí ngoài duy nhất: tiền inference model (Opus 5.5 khuyến nghị; tốn theo số trang × vòng compare) — repo không công bố con số/clone → `chưa xác minh`, cấm đoán; không subscription/tài khoản cho template.
- Ma sát cài đặt: 4 bước (`git clone`/Use-template → `npm install` → `npm run check` → `/clone-website <URL>`). ĐÃ chạy thử đến `npm run check` xanh (476 pkgs; build Next 16.3.5 prerender 2 routes) — output thật ở [Cài đặt](#cai-dat-da-clone--npm-install--npm-run-check-xanh-tren-linux-30102026-chua-chay-clone-website-vi-may-nay-khong-co-browser-agent--tranh-dung-tos-site-that). Rào cản: Node 24+ (`engines >=24`, `.nvmrc` 24); agent có browser access (không có thì dừng, DOM dump không thay thế); chưa chạy `/clone-website` thật (máy này không có browser agent + tránh đụng ToS site thật).
- Đối thủ viral cùng phân khúc: `abi/screenshot-to-code` (80,901★/9,903 forks, ảnh→code single-shot) vs `firecrawl` (196,886★/10,396 forks, API extract). Số API GitHub 30/10/2026.
- Chọn nó thay vì đối thủ khi: cần giống hệt URL sống (states/responsive/motion quan sát bằng browser thật) + code Next.js/shadcn editable nhiều trang + compare cùng viewport/state + `npm run check` xanh. Ví dụ đổi lựa chọn: migrate blog WordPress 5 trang của mình giữ pathnames → cloner; mock nhanh từ ảnh chụp → s2c; chỉ cần extract data hàng loạt → firecrawl.
- TUYỆT ĐỐI không dùng khi: không có quyền/ToS cấm; phishing/giả mạo/bê design-copy-brand người khác; máy không có Node 24+ và không cài được; agent không có browser access mà vẫn cố clone (observation bịa = FAIL).

### Usecase con 1: clone 1 URL 1:1 từ template trống
- Khi dùng: có 1 URL (quyền đã xác minh) cần tái dựng thành trang Next.js editable.
- Khi bỏ qua: nhiều trang/migrate → Usecase 2; nối vào clone có sẵn → Usecase 3; chỉ sửa clone có sẵn → Usecase 4; system mới → hallmark.
- Cơ chế khác các usecase khác ở đâu: duy nhất chạy đủ 4 bước từ template trống (root clone đầu tiên được thay homepage template); các usecase khác giữ/extend/compare trên code đã có.
- Lệnh copy-paste (trong agent có browser): `/clone-website https://example.com` (nguồn README gốc + bridge `.claude/commands/clone-website.md`; chuỗi trước đó: setup 4 bước ở [Cài đặt](#cai-dat-da-clone--npm-install--npm-run-check-xanh-tren-linux-30102026-chua-chay-clone-website-vi-may-nay-khong-co-browser-agent--tranh-dung-tos-site-that)).
- Ngưỡng số cần đạt: route map 1 URL → 1 đích + file ownership rõ; desktop + mobile cùng viewport/scroll/state với source; controls hứa gì làm nấy; `npm run check` xanh (lint + typecheck + build, đã xác minh xanh trên template); gaps còn lại nêu chính xác từng cái, cấm gọi pixel-perfect khi chưa compare.
- Ví dụ input-output (minh họa, không phải mặc định — shortlist URL/scope + user pick trước): input "clone landing công ty mình (sở hữu đã xác minh), scope 1 trang chủ" → output `src/app/page.tsx` + `src/components/sites/acme/*` + `public/sites/acme/*` (fonts/ảnh/SVG thật) + `docs/research/acme/` (brief, asset map, screenshots desktop/mobile) + ảnh compare + check xanh + list gaps.
- Pitfalls riêng: query/fragment là states của cùng route (không tách route mới); escape `_ @ [ ] ( )` theo cơ chế framework rồi verify URL thật; `.png` có thể trả AVIF (verify content-type/dimensions); substitute icon/font cùng tên khác metrics = sai.
- Phân công usecase này: agent chính check quyền/ToS + Map/Observe/Build/Compare + check + trình compare; giao claude observe browser đa state (kèm URL + states) + chụp compare; verify bằng check xanh + ảnh cùng viewport/state + runtime controls.

### Usecase con 2: migrate site nhiều trang mình sở hữu
- Khi dùng: site mình sở hữu nhiều trang (vd blog WordPress 5 trang) cần sang Next.js giữ pathnames.
- Khi bỏ qua: 1 trang → Usecase 1; thêm trang sau này → Usecase 3; design mới → hallmark.
- Cơ chế khác các usecase khác ở đâu: route map nhiều URL + giữ pathnames source + shared components dùng chung mọi state + quyết gộp/tách app (origins khác → apps riêng; gộp thì prefix + scoped fonts/styles/layout); UC1 chỉ 1 đích, UC3 chỉ extend.
- Lệnh copy-paste: `/clone-website <url1> <url2> ...` (nhiều URL 1 lệnh, nguồn bridge `argument-hint: "<url1> [<url2> ...]"`); xong chạy `npm run check`.
- Ngưỡng số cần đạt: mọi URL có đích + ownership; pathnames giữ nguyên; shared components cover mọi state quan sát (hover/focus/breakpoints); routes cũ còn chạy sau khi thêm; check xanh.
- Ví dụ input-output (minh họa — scope + gộp/tách do user pick trước): input "migrate blog WordPress 5 trang (`/`, `/about`, 3 bài) giữ pathnames, 1 app" → output 5 routes + shared header/footer (mọi state) + assets `public/sites/blog/*` + links nội bộ rewrite local + out-of-scope giữ trỏ source có disclose + check xanh.
- Pitfalls riêng: tên readable collide thì thêm port/hash phân biệt; thêm trang thì extend layout/styles chung, cấm thay styles trang cũ; scripted scroll bypass behavior (smooth scroll) — drive bằng input thật (wheel/touch/keyboard/pointer).
- Phân công usecase này: agent chính lập route map + shared trước + delegate từng trang độc lập (kèm screenshots/measurements/file đích/finish line) + hồi quy; giao claude observe từng trang + compare; verify bằng check xanh + mọi routes (cũ+mới) chạy.

### Usecase con 3: thêm trang mới vào clone có sẵn
- Khi dùng: đã có clone chạy, cần thêm 1+ trang từ cùng/dạng source.
- Khi bỏ qua: clone mới hoàn toàn → Usecase 1/2; chỉ sửa diff → Usecase 4.
- Cơ chế khác các usecase khác ở đâu: không thay layout/styles chung (extend, reuse components vừa khớp), resolve collision trước khi thay, regression bắt buộc routes cũ; UC2 build shared từ đầu, UC3 bị ràng buộc bởi shared có sẵn.
- Lệnh copy-paste: `/clone-website <new-url>` (chạy trong app đã có clone) rồi `npm run check`.
- Ngưỡng số cần đạt: trang mới đúng scope + dùng lại shared vừa khớp; styles/routes cũ nguyên vẹn (verify chạy lại); collision resolve trước thay; check xanh.
- Ví dụ input-output (minh họa — trang mới do user pick scope trước, không phải mặc định): input "thêm `/pricing` vào clone blog (user đã pick scope)" → output route `/pricing` reuse header/footer + styles chung không đổi + regression `/`, `/about` còn chạy + check xanh.
- Pitfalls riêng: thay styles chung làm vỡ trang cũ (lỗi phổ biến nhất của extend); route collide mà ghi đè không hỏi = FAIL; assets mới trùng tên cũ thì đặt tên phân biệt + track URL→path.
- Phân công usecase này: agent chính diff shared (reuse/bổ sung) + build trang + regression + check; giao claude observe trang mới + compare; verify bằng check xanh + routes cũ pass.

### Usecase con 4: compare/repair + production check trên clone có sẵn
- Khi dùng: clone đã build cần soát diff với source và sửa đến ngưỡng ship (không build mới).
- Khi bỏ qua: cần build thêm → Usecase 1/2/3.
- Cơ chế khác các usecase khác ở đâu: không viết mới; montage side-by-side cùng viewport/scroll/state (chờ fonts/media/reveal settle) → sửa diff lớn-trước (geometry, missing layers, typo/wrap, crop → spacing/motion) → recheck → chạy production check.
- Lệnh copy-paste: `npm run check` (lint + typecheck + build; đã xác minh xanh) + compare bằng browser ở cùng viewport/scroll/state (nguồn SKILL.md bước 4).
- Ngưỡng số cần đạt: soát toàn trang ở mọi điểm từng phát hiện rule đổi + 1 viewport rộng hơn design; animated regions check 3 states (initial/active/settled, gồm reverse scroll); không runtime errors/missing assets/overflow ngang; check xanh; gaps còn lại nêu chính xác (cấm gọi pixel-perfect khi chưa check).
- Ví dụ input-output (minh họa — scope compare đã duyệt, không phải mặc định): input "clone homepage xong, soát với source" → output list diff (header lệch 8px, thiếu hover state menu, wrap sai ở 1280px) → fix theo thứ tự lớn-trước → recheck + check xanh + gaps (video hero chỉ autoplay muted — nêu rõ).
- Pitfalls riêng: compare khác viewport/state rồi kết luận giống = FAIL; sửa spacing/motion trước geometry/typo (sai thứ tự); assert class-names thay vì check browser ở boundaries.
- Phân công usecase này: agent chính montage + fix lớn-trước + recheck + check; giao claude chụp full-size sections + test scroll/pointer bằng input thật; verify bằng check xanh + diff list đóng hết hoặc ghi gaps.

### Các bước chung
1. Xác minh quyền + ToS site nguồn (sở hữu/cho phép/học) → shortlist URLs/routes + gộp/tách qua question tool, user pick mới chạy (log scope trước vì tốn token).
2. Setup 4 bước ([Cài đặt](#cai-dat-da-clone--npm-install--npm-run-check-xanh-tren-linux-30102026-chua-chay-clone-website-vi-may-nay-khong-co-browser-agent--tranh-dung-tos-site-that)) + đọc skill chuẩn (Codex/Cursor/OpenCode đọc trực tiếp, Claude Code qua bridge).
3. Map: route map + file ownership + conventions app (`sites/<site>/`, `public/sites/<site>/`, `docs/research/<site>/`).
4. Observe: desktop + mobile, scroll hết lazy/sticky, exercise menus/tabs/accordion/carousel/hover/links; mỗi observation là sample của 1 rule; lưu screenshots + brief + asset map; đọc `inspection-guide.md` (+ `framer-and-motion.md` cho Framer/animated).
5. Build: fonts/width/colors/assets/routes/shared trước; sections bằng content thật; delegate sections độc lập sau khi shared có owner; chạy check sau slice tích hợp.
6. Compare: cùng viewport/scroll/state, sửa lớn-trước, recheck, test runtime thật, `npm run check` xanh; nêu gaps chính xác.
7. Deliver: hướng dẫn chạy + route map + ảnh compare desktop/mobile + checks đã chạy + gaps.

### Prompt mẫu
- "Setup repo này từ JCodesMore/ai-website-cloner-template (prompt setup nguyên văn README), Node 24. Scope clone: homepage công ty mình (sở hữu đã xác minh, ToS cho phép) — 1 URL, 1 app. Chạy Map→Observe→Build→Compare + npm run check. Trình route map + ảnh compare + gaps trước khi tôi duyệt ship. Không placeholder, không gọi pixel-perfect khi chưa compare."
- "Migrate blog WordPress 5 trang của mình (liệt kê URLs) sang Next.js giữ pathnames, 1 app: lập route map, shared components cover mọi state, links nội bộ rewrite local, out-of-scope disclose. Regression + npm run check xanh."
- "Thêm /pricing (URL kèm) vào clone blog có sẵn: reuse shared, cấm đổi styles chung, resolve collision trước khi thay, regression routes cũ, npm run check xanh."

### Pitfalls
- Clone không quyền/ToS cấm/phishing/bê brand-copy người khác → FAIL pháp lý (dù repo có "Not Intended For", agent vẫn phải check trước mỗi URL).
- Gọi pixel-perfect khi chưa compare render = FAIL chuẩn skill (phải nêu gaps chính xác).
- Placeholder/substitute cùng tên khác metrics (icon set khác, font khác) → sai metrics/shapes, audit bằng content-type/dimensions thật.
- Query/fragment tách route mới (chúng là states); `_ @ [ ] ( )` không escape; tên collide không thêm port/hash.
- Giả click cho section scroll-driven; scripted scroll bypass smooth-scroll; DOM dump thay nhìn thật; assert class-names thay check browser.
- `scripts/` trống (chỉ `.gitkeep`) — agent tự viết script tải asset theo site, đừng đợi có sẵn.
- Sửa spacing/motion trước geometry/typo/missing-layers (sai thứ tự repair); thay styles chung khi extend làm vỡ trang cũ.
- Burn token không log scope trước (Opus × trang × vòng compare) — vi phạm cổng delegate tốn kém.

### Tham khảo sử dụng (số chốt 30/10/2026; review sâu độc lập: chưa xác minh — không bịa)
- Nhận xét sâu: KHÔNG tìm thấy bài critique sâu độc lập (không HN/bài kỹ thuật; Reddit r/ClaudeCode + r/vibecoding chỉ là announcement/khen ngắn + 1 chê đắt giá: "clone website chính là việc browser làm khi bạn visit — tải html/css/js/assets rồi load") → quyết định dùng dựa vào chạy thật ([Cài đặt](#cai-dat-da-clone--npm-install--npm-run-check-xanh-tren-linux-30102026-chua-chay-clone-website-vi-may-nay-khong-co-browser-agent--tranh-dung-tos-site-that)) + stars, không dựa buzz. Ghi `chưa xác minh`.
- Dấu hiệu độc lập (không phải review sâu, đọc với bias): SkillsLLM listing 37,079★; SourceForge mirror; demo YouTube; Discord cộng đồng; CI xanh + CHANGELOG semver đều (0.6.1, 80 commits) → xác nhận repo sống + quy trình thật, lật "template phong trào" thành "đáng thử trên site mình".
- Số trung bình có trọng số: 38,004★ / 5,583 forks / 164 watchers / 5 issues mở (API GitHub 30/10/2026). Trọng số: cùng phân khúc s2c 80,901★ (lớn hơn nhưng khác input single-shot — không suy ra hơn/kém) vs firecrawl 196,886★ (khác tầng extract — chỉ so định vị).
- Mâu thuẫn: buzz star cao vs thiếu critique sâu + chi phí token/clone chưa công bố → phán quyết: thử 0đ template trên site mình + đo token thực tế, chưa nhận migrate thuê khi chưa biết bill.
- Tiếng Việt: không tìm thấy review Việt → `chưa xác minh`.

### Tham khảo
- Repo + setup prompt + Use/Not-Use Cases: https://github.com/JCodesMore/ai-website-cloner-template (đọc 30/10/2026; MIT; v0.6.1; tạo 13/03/2026; đẩy cuối 19/10/2026).
- Nguồn đã mở kiểm tra: `.agents/skills/clone-website/SKILL.md` (61 dòng, 4 bước), `references/inspection-guide.md` (41) + `framer-and-motion.md` (37), `.claude/commands/clone-website.md`, `AGENTS.md`, `package.json` (Next 16.3.5, React 19.2.4, Node >=24, scripts check), `.github/workflows/ci.yml` + `token-badge.yml`, `CHANGELOG.md` (Keep-a-Changelog, semver).
- Đã chạy xác minh 30/10/2026: `git clone --depth 1` OK, `npm install` (476 pkgs, Node v24.22.0), `npm run check` xanh (lint + typecheck + build, prerender `/` + `/_not-found`). Chưa chạy: `/clone-website` (không browser agent + tránh ToS), Docker.
- Số liệu: API GitHub `JCodesMore/ai-website-cloner-template` + `abi/screenshot-to-code` + `firecrawl/firecrawl` (30/10/2026); SkillsLLM listing; Reddit r/ClaudeCode + r/vibecoding.
- Đối thủ: https://github.com/abi/screenshot-to-code (80,901★) + https://github.com/firecrawl/firecrawl (196,886★) + `../hallmark/` (system mới, trong repo này).

### Được dùng ở đâu
- Dùng CHO UI (rebuild/migrate/extend/compare site thành Next.js): xem `../../domains/ui/using-ai-website-cloner-template.md` — index `../../domains/ui/README.md`.

### Quay lại index
- Về `../../domains/ui/README.md` (so rebuild 1:1 vs system mới vs taste đóng gói vs bricks lẻ).
- Xem thêm item liên quan: `../hallmark/` khi cần system mới/sweep phần custom; `../skillry/` (phần web) khi cần taste đóng gói; `../reactbits/` khi cần bricks React.

---

## English

### When to use
- Need a 1:1 rebuild of a live website into editable Next.js code (migrating a self-owned WordPress/Webflow/Squarespace site, or lost source with only the live build left) via a disciplined flow (Map → Observe → Build → Compare + `npm run check`).
- Agent supports skills/commands (Claude Code, Codex, Cursor, OpenCode) + browser access + Node 24+, with model-inference spend accepted (Opus 5.5 recommended; token burn scales with pages × compare loops).
- Want to learn production layouts/animations from real code (observe-only, no full build).

### When to skip
- New system/design must pass measurable gates (contrast/focus/fold) → use `../hallmark/` (the cloner copies an existing design, generates no system/gates).
- One packaged-taste landing with preview, no specific URL to match → use `../skillry/` (web part).
- One owned-source React effect/component → use `../reactbits/`.
- Cloning an unowned/unpermitted site, phishing/impersonation, shipping someone else's design-copy-logos, or source sites whose ToS bans scraping/reproduction → absolutely forbidden (see [Invariant core](#invariant-core)).

### Install (cloned + `npm install` + green `npm run check` on Linux 30/10/2026; `/clone-website` not run — no browser agent on this machine + avoiding real-site ToS issues)
- Route 1 — new template (per origin README): click `Use this template` on GitHub, name the repo → hand the agent: `git clone <new-repo>`, drop the template origin if needed, `npm install`, `npm run check`.
- Route 2 — verbatim setup prompt (checked against origin README): `Set up https://github.com/JCodesMore/ai-website-cloner-template as a standalone project in a new folder on my computer. Ask me where to put it. Clone the repository, remove its origin remote, install dependencies, and run npm run check. Leave it ready for me to clone a website.`
- Run a clone (agent needs browser access; Claude Code/Cursor): `/clone-website https://example.com` (multiple URLs: `/clone-website <url1> <url2> ...`).
- Requirements: Node.js 24+ (this machine v24.22.0 passes; `.nvmrc` pins `24`, `package.json` has `engines: node >=24`); no login/account for the template; optional Docker (`docker compose up dev --build`, port 3001).
- Verify (ran 30/10/2026, real outputs): `npm install` → 476 packages OK (install-script warnings from `msw`/`unrs-resolver` — review, never blindly approve); `npm run check` (= `lint` + `typecheck` + `build`) → green Next.js 16.3.5 build, 2 statically prerendered routes (`/`, `/_not-found`).

### How the item works
- Backing organization: individual `JCodesMore`, template repo `https://github.com/JCodesMore/ai-website-cloner-template`, MIT license, v0.6.1, 80 commits since 13/03/2026, last push 19/10/2026, CI (`npm ci` + lint + typecheck/build) on Node 24. GitHub API 30/10/2026: 38,004 stars / 5,583 forks / 164 watchers / 5 open issues.
- Core operating method: pre-scaffolded Next.js 16 template (App Router, React 19, strict TS, shadcn/ui + Tailwind v4 oklch tokens — oklch is Tailwind v4's default colour space) + one canonical `clone-website` skill (`.agents/skills/clone-website/SKILL.md`, 61 lines + 2 references; Codex/Cursor/OpenCode read it directly, Claude Code via the `.claude/commands/clone-website.md` bridge). The agent triggers on user-supplied URLs + clone/rebuild/reverse-engineer asks; runs Map (route map — source-URL → local-route/file map + file ownership) → Observe (desktop/mobile, states, real assets/fonts) → Build (editable components, real interactions) → Compare (side-by-side at matched viewport/state, largest-first repair, `npm run check`).
- Per-usecase operating differences: fresh single-URL clone (all 4 steps from the empty template, see [Sub-usecase 1](#sub-usecase-1-11-clone-of-one-url-from-the-empty-template)) vs multi-page migration (multi-URL route map + preserved pathnames + preserve/combine apps, see [Sub-usecase 2](#sub-usecase-2-migrating-a-self-owned-multi-page-site)) vs extending an existing clone (extend layout/styles + regress old routes, see [Sub-usecase 3](#sub-usecase-3-adding-pages-to-an-existing-clone)) vs compare/repair (no new build, largest-first fixes + check, see [Sub-usecase 4](#sub-usecase-4-comparerepair--production-check-on-an-existing-clone)).

### Invariant core
- Rights before URLs: clone only self-owned sites / written permission / internal-only learning, never ship; no phishing/impersonation/shipping others' design-copy-brand-assets/scraping ToS-banned sites (origin "Not Intended For"). Violation = no longer using the system (legal FAIL). After use, state the right basis (ownership/permission/learning) + ToS checked.
- All 4 steps + green check before calling done: Map → Observe → Build → Compare, then green `npm run check` (lint + typecheck + build); calling anything pixel-perfect before rendered comparison is forbidden (SKILL.md Compare). Unable to state route map + checks run + remaining gaps = the system was not really used.
- Measured real content, no placeholders: text/assets/fonts from actually-loaded source files (track URL→path, verify content-type/dimensions — a `.png` URL may return AVIF); same-named different-metrics substitutes (other icon sets/fonts) = FAIL.
- Map before build: route map + file ownership clear before writing code; keep written routes/assets, resolve collisions before replacing; separate apps per origin unless the user settles on combined (prefix + separately scoped fonts/styles/layout).
- Only rebuild what was observed: each observation is one sample of one rule (vary width/height/input/state until the driver is known); tell scroll/click/hover/time-driven apart (a click imitation of a scroll-driven section is a different product); DOM dumps never replace looking.

### Customizable surface
- Tunable: which in-scope URLs/routes, combined vs separate apps, observed viewports/states, out-of-scope link policy (rewrite local when the route is in scope, keep pointing at source + disclose when out of scope), which sections to delegate in parallel, post-compare keep/change list. Two-level approval gate: (1) which artifact — shortlist of URLs/routes + combine/split with reasons via the question tool, user picks before running (full clones burn heavy Opus tokens — log the approved scope BEFORE running); (2) what stays/changes — which diffs to fix, which gaps to keep. Waivers (skipping compare, shipping straight) must quote the user's explicit ok. Never list `must-not` items (unpermitted cloning, phishing, uncompared pixel-perfect claims) here.

### Work split
- Main agent: rights/ToS check + scope shortlist (wait for user pick — never self-pick URLs then clone), Map/Observe/Build/Compare, runs `npm run check`, presents route map + comparisons + gaps; verifies green build + matched viewport/state side-by-sides + real runtime (nav, mobile menu, tab/accordion states, carousel bounds, horizontal overflow, console errors).
- Hand outside-browser steps to claude: multi-viewport/state source observation (with URLs + concrete states), comparison captures, look-alike reverse-checks when studying — with route map + concrete asks; the agent never invents observations. Without a browser the agent must declare it + stop (DOM dumps don't substitute), never claim observed work.
- Agent verifies: green `npm run check` + desktop/mobile comparisons + old routes still running (on extend) + `docs/research/<site>/` (brief, asset map, evidence) present.

### Differentiating positioning (GitHub API numbers, 30/10/2026)
- Vs `abi/screenshot-to-code` (80,901 stars/9,903 forks, screenshot→code single-shot): input + verification-loop difference — s2c generates code from one static image; the cloner observes the live site across viewports/states with a real browser (scroll/click/hover/time-driven), maps routes, builds multi-page editable Next.js/shadcn, loops compare/repair + production check. Pick the cloner over s2c for matching a live URL including states/responsive/motion + editable multi-file code (bar: matched viewport/state comparison + green `npm run check`); pick s2c for a fast static mock from one image, accepting single-shot output with no multi-state verification.
- Vs `firecrawl/firecrawl` (196,886 stars/10,396 forks, scraping/extract API): layer difference — firecrawl extracts structured data at scale (replaces the Observe step for bulk crawls); the cloner rebuilds a runnable Next.js app. Pick the cloner for a complete editable app; pick firecrawl for bulk data/extracts with no UI rebuild.
- Vs `../hallmark/` (in-repo system + gates): the cloner 1:1-copies an existing design (no tokens/gates/review generated); hallmark generates a new gated system. Decide: match a live site (with rights) → cloner; new standard-meeting system → hallmark; custom parts added post-clone can be re-swept with hallmark.
- Honest frame: the cloner wins on 1:1 live recreation + editable structure + machine check; loses on speed/cost (browser loops + Opus tokens, every page × every compare loop costs money) and on originality (copies, no system/gates) + narrow legal scope (rights/ToS). Original work → hallmark; packaged taste → Skillry web; raw data → firecrawl.

### Coverage map (full SKILL.md + 2 references + template + README scanned 30/10/2026 — ★ strongest first)
- ★ 1:1 clone of one URL from the empty template (all 4 steps + check): see Sub-usecase 1.
- Multi-page self-owned migration (route map + preserved pathnames + preserve/combine apps): see Sub-usecase 2.
- Adding pages to an existing clone (extend + regress old routes): see Sub-usecase 3.
- Compare/repair + production check on an existing clone (no new build): see Sub-usecase 4.
- Medium: observe-only study (read SKILL step 2 + `inspection-guide.md` + `framer-and-motion.md`, produce `docs/research/<site>/` brief + asset map + measurements, no build) → use when understanding a layout/animation to hand-rewrite it.
- Medium: Docker run (`docker compose up dev --build`, port 3001; `up app` for production) → use for an isolated env / no local Node 24 install.
- NOT supported → replacements: dynamic backend/logic behind the site (auth, DB, private APIs — clones cover observable surface + interactions only; real flows self-wired) → implement yourself; legal/ToS clearance → check yourself + get permission (no system replaces it); automated asset pipeline (`scripts/` holds only `.gitkeep` today — the agent writes per-site download scripts) → agent-authored; original text-to-UI → `../hallmark/`; static screenshot → screenshot-to-code; bulk extract → firecrawl.

### Decision dossier
- Jobs SERVED (3+, concrete): 1. migrating a self-owned site (WordPress/Webflow/Squarespace → Next.js routes with preserved pathnames); 2. lost source with only the live build left (rebuild from observable URLs); 3. learning production layouts/animations (observe-only brief + measurements, hand-rewritten).
- Jobs NOT served (3+, each with replacement): 1. new gated system → `../hallmark/`; 2. fast packaged-taste landing → `../skillry/` (web part); 3. static mock from one image → screenshot-to-code; 4. bulk data/extract → firecrawl; 5. unpermitted cloning/phishing → no system at all (forbidden).
- Free / total + price: $0 MIT template in full (sources `LICENSE` + `package.json` 0.6.1, read 30/10/2026). Sole external cost: model inference (Opus 5.5 recommended; scales with pages × compare loops) — the repo publishes no per-clone figure → `unverified`, never guessed; no subscription/account for the template.
- Install friction: 4 steps (`git clone`/Use-template → `npm install` → `npm run check` → `/clone-website <URL>`). RAN through green `npm run check` (476 pkgs; Next 16.3.5 build prerendering 2 routes) — real outputs in [Install](#install-cloned--npm-install--green-npm-run-check-on-linux-30102026-clone-website-not-run--no-browser-agent-on-this-machine--avoiding-real-site-tos-issues). Barriers: Node 24+ (`engines >=24`, `.nvmrc` 24); browser-capable agent (without one, stop — DOM dumps don't substitute); `/clone-website` itself unrunned (no browser agent on this machine + avoiding real-site ToS).
- Viral same-segment opponents: `abi/screenshot-to-code` (80,901 stars/9,903 forks, image→code single-shot) vs `firecrawl` (196,886 stars/10,396 forks, extract API). GitHub API 30/10/2026.
- Pick it over opponents when: a live URL must be matched exactly (states/responsive/motion observed with a real browser) + editable multi-page Next.js/shadcn code + matched viewport/state comparison + green `npm run check`. Choice-flipping example: migrating a self-owned 5-page WordPress blog with preserved pathnames → cloner; fast mock from a screenshot → s2c; bulk data extracts only → firecrawl.
- NEVER use when: no rights/ToS bans it; phishing/impersonation/shipping others' design-copy-brand; no Node 24+ installable; agent has no browser access yet cloning is attempted anyway (fabricated observation = FAIL).

### Sub-usecase 1: 1:1 clone of one URL from the empty template
- When to use: one URL (rights verified) needs rebuilding as an editable Next.js page.
- When to skip: multi-page/migration → Sub-usecase 2; appending to an existing clone → Sub-usecase 3; fixing an existing clone only → Sub-usecase 4; new system → hallmark.
- Mechanism difference: the only flow running all 4 steps from the empty template (a first root clone may replace the untouched homepage); other sub-usecases keep/extend/compare existing code.
- Copy-paste command (inside a browser-capable agent): `/clone-website https://example.com` (sources origin README + `.claude/commands/clone-website.md` bridge; preceding chain: the 4 setup steps in [Install](#install-cloned--npm-install--green-npm-run-check-on-linux-30102026-clone-website-not-run--no-browser-agent-on-this-machine--avoiding-real-site-tos-issues)).
- Numeric bar: 1 URL → 1 destination route map + clear file ownership; desktop + mobile at matched viewport/scroll/state vs source; promised controls perform; green `npm run check` (lint + typecheck + build, verified green on the template); remaining gaps stated one by one, never pixel-perfect without comparison.
- Input-output example (illustrative, not a default — URL/scope shortlist + user pick first): input "clone our company landing (ownership verified), 1-homepage scope" → output `src/app/page.tsx` + `src/components/sites/acme/*` + `public/sites/acme/*` (real fonts/images/SVGs) + `docs/research/acme/` (brief, asset map, desktop/mobile screenshots) + comparisons + green check + gap list.
- Own pitfalls: query/fragments are states of one route (never split new routes); escape `_ @ [ ] ( )` per framework mechanism then verify the real URL; `.png` may return AVIF (verify content-type/dimensions); same-named different-metrics substitutes are wrong.
- Work split for this sub-usecase: main agent does rights/ToS check + Map/Observe/Build/Compare + check + presents comparisons; multi-state browser observation (URLs + states) + comparison captures go to claude; verify via green check + matched viewport/state images + working runtime controls.

### Sub-usecase 2: migrating a self-owned multi-page site
- When to use: a self-owned multi-page site (e.g. 5-page WordPress blog) moves to Next.js with preserved pathnames.
- When to skip: single page → Sub-usecase 1; later additions → Sub-usecase 3; new design → hallmark.
- Mechanism difference: multi-URL route map + preserved source pathnames + shared components covering every observed state + combine/split-app decision (different origins → separate apps; combined → prefix + scoped fonts/styles/layout); Sub-usecase 1 maps one destination, Sub-usecase 3 is constrained by existing shared code.
- Copy-paste command: `/clone-website <url1> <url2> ...` (several URLs in one command, source bridge `argument-hint: "<url1> [<url2> ...]"`); then `npm run check`.
- Numeric bar: every URL has a destination + ownership; pathnames preserved; shared components cover all observed states (hover/focus/breakpoints); old routes still run after additions; green check.
- Input-output example (illustrative — scope + combine/split user-picked first): input "migrate our 5-page WordPress blog (`/`, `/about`, 3 posts), preserved pathnames, one app" → output 5 routes + all-state shared header/footer + assets under `public/sites/blog/*` + internal links rewritten local + out-of-scope left pointing at source with disclosure + green check.
- Own pitfalls: readable-name collisions need port/hash disambiguators; adding pages must extend shared layout/styles, never replace old pages' styles; scripted scrolling bypasses real behavior (smooth scroll) — drive with real inputs (wheel/touch/keyboard/pointer).
- Work split for this sub-usecase: main agent maps routes + builds shared first + delegates independent pages (with screenshots/measurements/destination files/finish line) + regresses; per-page observation + comparison go to claude; verify via green check + all (old+new) routes running.

### Sub-usecase 3: adding pages to an existing clone
- When to use: a working clone exists and needs 1+ pages from the same/similar source.
- When to skip: fully fresh clone → Sub-usecases 1/2; diff fixes only → Sub-usecase 4.
- Mechanism difference: shared layout/styles are constraints (extend, reuse fitting components), collisions resolved before replacing, old-route regression mandatory; Sub-usecase 2 builds shared from scratch, Sub-usecase 3 must not break it.
- Copy-paste command: `/clone-website <new-url>` (run inside the app holding the clone), then `npm run check`.
- Numeric bar: new page in scope + fitting shared reuse; old styles/routes untouched (re-verified running); collisions resolved pre-replacement; green check.
- Input-output example (illustrative — new page user scope-picked first, not a default): input "add `/pricing` (URL attached) to the existing blog clone (scope user-picked)" → output `/pricing` route reusing header/footer + unchanged shared styles + regressed `/`, `/about` still running + green check.
- Own pitfalls: changing shared styles breaks old pages (the most common extend failure); overwriting a colliding route unasked = FAIL; same-named new assets need distinct names + URL→path tracking.
- Work split for this sub-usecase: main agent diffs shared (reuse/extend) + builds the page + regresses + checks; new-page observation + comparison go to claude; verify via green check + old routes passing.

### Sub-usecase 4: compare/repair + production check on an existing clone
- When to use: a built clone needs source diffing and fixing up to ship bar (no new build).
- When to skip: more building needed → Sub-usecases 1/2/3.
- Mechanism difference: no new authoring; side-by-side montage at matched viewport/scroll/state (fonts/media/reveal settled) → largest-first fixes (geometry, missing layers, typo/wrap, crop → spacing/motion) → recheck → production check run.
- Copy-paste command: `npm run check` (lint + typecheck + build; verified green) + browser comparison at matched viewport/scroll/state (source SKILL.md step 4).
- Numeric bar: whole page reviewed at every rule-change point found before + one wider-than-design viewport; animated regions checked in 3 states (initial/active/settled, incl. reverse scroll); zero runtime errors/missing assets/horizontal overflow; green check; remaining gaps stated precisely (never pixel-perfect unchecked).
- Input-output example (illustrative — compare scope pre-approved, not a default): input "homepage clone built, check against source" → output diff list (8 px header drift, missing menu hover state, wrong wrap at 1280 px) → largest-first fixes → recheck + green check + gaps (hero video autoplay-muted only — stated).
- Own pitfalls: comparing at mismatched viewport/state then calling it matching = FAIL; fixing spacing/motion before geometry/typo/missing layers (wrong repair order); asserting class names instead of browser checks at boundaries.
- Work split for this sub-usecase: main agent montages + largest-first fixes + rechecks + checks; full-size section captures + real-input scroll/pointer tests go to claude; verify via green check + diff list closed or gaps recorded.

### Shared steps
1. Verify rights + source-site ToS (ownership/permission/learning) → shortlist URLs/routes + combine/split via question tool, user picks before running (log scope first — token cost).
2. Four setup steps ([Install](#install-cloned--npm-install--green-npm-run-check-on-linux-30102026-clone-website-not-run--no-browser-agent-on-this-machine--avoiding-real-site-tos-issues)) + read the canonical skill (Codex/Cursor/OpenCode directly, Claude Code via bridge).
3. Map: route map + file ownership + app conventions (`sites/<site>/`, `public/sites/<site>/`, `docs/research/<site>/`).
4. Observe: desktop + mobile, full scroll for lazy/sticky, exercise menus/tabs/accordions/carousels/hovers/links; each observation a sample of one rule; save screenshots + brief + asset map; read `inspection-guide.md` (+ `framer-and-motion.md` for Framer/animated).
5. Build: fonts/width/colours/assets/routes/shared first; sections with real content; delegate independent sections after shared has an owner; check after an integrated slice.
6. Compare: matched viewport/scroll/state, largest-first fixes, recheck, real runtime tests, green `npm run check`; state gaps precisely.
7. Deliver: run instructions + route map + desktop/mobile comparisons + checks run + gaps.

### Sample prompts
- "Set this repo up from JCodesMore/ai-website-cloner-template (origin verbatim setup prompt), Node 24. Clone scope: our company homepage (ownership verified, ToS allows) — 1 URL, 1 app. Run Map→Observe→Build→Compare + npm run check. Present route map + comparisons + gaps before I approve shipping. No placeholders, no unchecked pixel-perfect claims."
- "Migrate our 5-page WordPress blog (URLs listed) to Next.js with preserved pathnames, one app: route map, all-state shared components, internal links rewritten local, out-of-scope disclosed. Regression + green npm run check."
- "Add /pricing (URL attached) to the existing blog clone: reuse shared, never change shared styles, resolve collisions before replacing, regress old routes, green npm run check."

### Pitfalls
- Unpermitted/ToS-banned cloning, phishing, shipping others' brand-copy = legal FAIL (the repo's "Not Intended For" doesn't replace the agent checking every URL first).
- Uncompared pixel-perfect claims = skill-standard FAIL (state gaps precisely instead).
- Placeholders / same-named different-metrics substitutes (other icon sets/fonts) → wrong metrics/shapes; audit with real content-type/dimensions.
- Splitting query/fragments into new routes (they are states); unescaped `_ @ [ ] ( )`; un-disambiguated name collisions.
- Click imitations of scroll-driven sections; scripted scroll bypassing smooth-scroll; DOM dumps replacing looking; class-name assertions replacing browser checks.
- `scripts/` is empty (only `.gitkeep`) — the agent authors per-site download scripts, never waits for built-ins.
- Wrong repair order (spacing/motion before geometry/typo/missing layers); breaking old pages when extending shared styles.
- Unlogged-scope token burn (Opus × pages × compare loops) — violates the costly-delegate gate.

### Usage references (numbers pinned 30/10/2026; independent deep review: unverified — never guessed)
- Deep review: NO independent in-depth critique found (no HN/technical review; Reddit r/ClaudeCode + r/vibecoding are announcements/short praise + one valuable skeptic: "cloning a website is literally what your browser does on visit — it downloads html/css/js/assets then loads them") → usage decisions rest on first-hand runs ([Install](#install-cloned--npm-install--green-npm-run-check-on-linux-30102026-clone-website-not-run--no-browser-agent-on-this-machine--avoiding-real-site-tos-issues)) + stars, never on buzz. Recorded as `unverified`.
- Weighty independent signals (not deep reviews, read with bias): SkillsLLM listing 37,079 stars; SourceForge mirror; YouTube demo; community Discord; green CI + steady semver CHANGELOG (0.6.1, 80 commits) → confirms a live repo + real process, flipping "bandwagon template" to "worth a trial on a self-owned site".
- Weighted average: 38,004 stars / 5,583 forks / 164 watchers / 5 open issues (GitHub API 30/10/2026). Weight: same-segment s2c 80,901 stars (bigger but different single-shot input — no better/worse inference) vs firecrawl 196,886 stars (different extract layer — positioning only).
- Conflict: high star buzz vs zero deep critique + unpublished per-clone token cost → verdict: $0 template trial on a self-owned site + measure real tokens first; no paid migration jobs before the bill is known.
- Vietnamese: no Vietnamese review found → `unverified`.

### References
- Repo + verbatim setup prompt + Use/Not-Use Cases: https://github.com/JCodesMore/ai-website-cloner-template (read 30/10/2026; MIT; v0.6.1; created 13/03/2026; last push 19/10/2026).
- Sources opened and checked: `.agents/skills/clone-website/SKILL.md` (61 lines, 4 steps), `references/inspection-guide.md` (41) + `framer-and-motion.md` (37), `.claude/commands/clone-website.md`, `AGENTS.md`, `package.json` (Next 16.3.5, React 19.2.4, Node >=24, check script), `.github/workflows/ci.yml` + `token-badge.yml`, `CHANGELOG.md` (Keep-a-Changelog, semver).
- Verification runs 30/10/2026: `git clone --depth 1` OK, `npm install` (476 pkgs, Node v24.22.0), `npm run check` green (lint + typecheck + build, `/` + `/_not-found` prerendered). Not run: `/clone-website` (no browser agent + real-site ToS avoidance), Docker.
- Numbers: GitHub API `JCodesMore/ai-website-cloner-template` + `abi/screenshot-to-code` + `firecrawl/firecrawl` (30/10/2026); SkillsLLM listing; Reddit r/ClaudeCode + r/vibecoding.
- Opponents: https://github.com/abi/screenshot-to-code (80,901 stars) + https://github.com/firecrawl/firecrawl (196,886 stars) + `../hallmark/` (new systems, in this repo).

### Where used
- Used in `domains/ui/`: see `../../domains/ui/using-ai-website-cloner-template.md` (rebuilding/migrating/extending/comparing sites as Next.js).

### Back to index
- Back to `../../domains/ui/README.md` (1:1 rebuild vs new system vs packaged taste vs single bricks).
- Related items: `../hallmark/` for new systems/sweeping custom additions; `../skillry/` (web part) for packaged taste; `../reactbits/` for React bricks.
