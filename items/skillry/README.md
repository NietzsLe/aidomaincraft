# skillry

## Tiếng Việt

### Dùng khi
- Cần 1 output trình bày cụ thể chạy ngay: video launch, landing page, slide deck, OG image, avatar — mà không muốn tự viết workflow.
- Agent được hỗ trợ (Claude Code, Codex, Cursor, OpenCode...) và chấp nhận trả phí nếu skill cần không free.
- Muốn xem trước kết quả thật (preview + installs) trước khi cài.

### Bỏ qua khi
- Cần 1 taste/design system sâu, kiểm soát từng token → dùng `../hallmark/` (Skillry bán output, không bán system).
- Cần bricks code React sở hữu source → dùng `../reactbits/`.
- Việc thuộc backend/data/review code/harness — Skillry không phủ (617 skill toàn là web/video/slides/image).
- Offline hoặc không muốn phụ thuộc trả phí/subscription → dùng skills.sh, awesome-lists, skill chính chủ Anthropic.

### Cài đặt (đã chạy `skillry --help` + `status`; chưa login — CLI trên Linux lỗi secure storage)
- Cách 1 — paste install prompt (khuyến nghị, chạy mọi OS kể cả Linux): mở trang skill → bấm Copy install prompt → paste nguyên văn vào box chat OpenCode (không cần gõ `/` gì thêm), ví dụ `Read https://skillry.dev/skills/bs-mint-noir-saas-site/install.md and follow the instructions to install the skill.` → nếu agent mở browser xin approve thì bấm Approve → giao việc, expect output kiểu `● Loading skill bs-mint-noir-saas-site` rồi `● Writing ...`.
- LƯU Ý tài khoản: free VẪN cần tài khoản Skillry đã đăng nhập (service phải verify entitlement mới trả archive) — đã đối chiếu trang install.md: "Free and premium Skills both require an authenticated account".
- Cách 2 — CLI (chỉ macOS + Node 22+, KHÔNG Linux): `npx --yes skillry-cli@latest login`, rồi `npx --yes skillry-cli@latest install bs-mint-noir-saas-site` (OpenCode là target mặc định → `~/.agents/skills/`; agent khác thêm đúng 1 trong 8 flag: shared, codex, cursor, gemini-cli, opencode, claude-code, kimi-code, antigravity; token chỉ lưu macOS Keychain/Windows Credential Manager). ĐÃ XÁC MINH trên Linux: `skillry status` báo lỗi `Secure session storage is currently supported on macOS and Windows only` — Linux đừng dùng CLI.
- Cách 3 — ZIP thủ công: bấm Download ZIP trên trang skill (không cần Node) → chạy `mkdir -p ~/.agents/skills` rồi unzip file vừa tải vào `~/.agents/skills/` (vd file `bs-mint-noir-saas-site.zip`) sao cho có `~/.agents/skills/<slug>/SKILL.md` (kèm `assets/`, `scripts/` nếu có) → restart OpenCode (thoát hẳn rồi mở lại) để nó load skill mới.
- Đường dẫn khuyên dùng cho OpenCode: `~/.agents/skills/` (mặc định, agent khác đọc ké được); project riêng thì `.agents/skills/` hoặc `.opencode/skills/`.
- Giá đã đối chiếu trang /pricing ngày 2026-10-29: Monthly $9.99, Yearly $79, Founding Lifetime $169 một lần (không hoàn lại); Premium dùng được khi sub còn hiệu lực; "1,000+ people supporting us".
- Kiểm tra: `ls ~/.agents/skills/<slug>/SKILL.md` tồn tại + agent kích hoạt đúng khi mô tả việc khớp `description`.

### Cách item hoạt động
- Tổ chức đứng sau: Skillry team, site `skillry.dev`, chợ skill trả phí (không phải registry mở). 617 skill tại thời điểm thẩm tra (Video 359 / Web 115 / Image 82 / Slides 61, Free 40). Giá: $9.99/tháng hoặc $169 lifetime; free từng skill lẻ.
- Phương thức hoạt động chung: mỗi skill = thư mục `SKILL.md` + templates/scripts, do team Skillry thiết kế và test kèm preview kết quả thật; agent đọc `description` để trigger, chạy workflow trong skill để ra output (video MP4, trang HTML, deck PPTX, ảnh OG).
- Khác biệt vận hành theo usecase: video (render qua pipeline HyperFrames/Remotion/Seedance) khác image (gọi GPT Image) khác slides (xuất HTML/PPTX, có narration HeyGen/ElevenLabs) khác web (HTML tĩnh). Cài đặt giống nhau (CLI/ZIP/prompt), khác ở engine chạy ra output.

### Định vị khác biệt (đã đối chiếu skills.sh leaderboard ngày 2026-10-29)
- Skillry KHÔNG thắng ở capability: engine video (HyperFrames/Remotion), deck (PptxGenJS), OG (Satori/Playwright) đều có bản free mở, installs lớn hơn Skillry hàng nghìn lần. Skillry thắng ở taste đóng gói sẵn + curation + workflow hướng dẫn + preview trước khi cài.
- Bảng đối thủ free đã xác minh (lệnh cài + installs):
| Việc | Đối thủ free (lệnh) | Installs |
|---|---|---|
| Video launch | `heygen-com/hyperframes` → `npx skills add heygen-com/hyperframes` (skill `product-launch-video`) | ~538.9K |
| Deck PPTX | `anthropics/skills` → `npx skills add anthropics/skills --skill pptx` (PptxGenJS, official) | ~244.5K |
| OG image | repo mở kiểu Satori/Playwright (deterministic, không méo chữ như diffusion) | theo repo |
| Landing mẫu | nhiều builder free (shadcn/ui 271.1K, vercel-labs/agent-skills 32.3k★ collection) | theo repo |
- So với skills.sh/Vercel (registry mở, miễn phí: CLI `vercel-labs/skills` 35.4k★, MIT, 75+ agent): chọn Skillry khi cần đúng 1 taste có sẵn (Manus 2.0, Notion OG...) + quy trình hướng dẫn + preview, chấp nhận trả phí + tạo tài khoản + lock-in; chọn free khi tự ráp được và chỉ cần engine/output.
- So với `../hallmark/` (1 skill sâu, gates máy): Skillry rộng 4 loại output nhưng nông — không có system, tokens, gates, review. Quyết định: cần 1 món trình bày chạy ngay → Skillry; cần system pass gates đo được (contrast 4.5:1, fold 1280x800) → Hallmark.
- Break-even trung thực: trả phí hợp lý khi cần lặp lại nhiều output đúng taste đóng gói; làm 1 lần lẻ → free + engine đủ, đừng trả.
- So với `../reactbits/` (bricks code React sở hữu source): Skillry phủ cả video/slides/image/OG, không chỉ code React. Quyết định: cần motion film/deck/OG image → Skillry; cần component React → React Bits.

### Bản đồ phủ usecase (quét hết 617 skill 29/10/2026 — ★ mạnh nhất đầu)
- ★ Launch video phong cách đóng gói (Manus 2.0, Pixel Promo, LaunchMotion — Video 359, installs 200-518 cao nhất Dot Avatar 518/27, Plush Crew 380-384): xem Usecase 1.
- ★ Landing mẫu (Web 115: Mint Noir free, Cadence 342/16, Harbor): xem Usecase 2 — phần web dùng CHO UI (`../../domains/ui/using-skillry.md`).
- ★ Slide deck + narrated report (Slides 61: Field Notes 287/8, Mint Marker, Starlit): xem Usecase 3.
- ★ OG image/avatar (Image 82: Notion OG 222/7, GrokBot 307/14, Dot Avatar 518/27): xem Usecase 4 — ảnh qua GPT Image.
- Trung bình: các skill web/slides/image còn lại trong catalog (xem preview + installs từng skill, đa số 1–45 installs).
- KHÔNG hỗ trợ → thay thế: review code/PR, data/bảng tính → skills.sh + Anthropic official; UI pass gates → Hallmark (`../hallmark/`); bricks React → React Bits (`../reactbits/`); offline/cấm vendor trả phí → free engine (HyperFrames/Remotion, pptx official, Satori/Playwright).

### Hồ sơ quyết định
- Việc DÙNG: 1. launch video phong cách Manus/Linear (dùng skill video + HyperFrames); 2. landing/saaS site mẫu (Mint Noir, Cadence); 3. slide deck + narrated report (Field Notes, audio report deck); 4. OG image/avatar theo phong cách brand (Notion-style OG, GrokBot avatar).
- Việc KHÔNG DÙNG: 1. review code/PR → dùng skill pr-review hệ mở; 2. xử lý data/bảng tính → dùng skill chính chủ Anthropic (xlsx/csv); 3. UI cần pass gates contrast/focus → dùng Hallmark.
- Free / tổng + giá: 40 free / 617 tổng (~6.5%) tại thời điểm đo 2026-10-29 (xem danh sách Free bên dưới — catalog trôi theo thời gian, kiểm tra lại bằng filter Free trên /skills trước khi quyết định, không mặc định chỉ có từng này). Premium $9.99/tháng, Yearly $79, Lifetime $169 một lần (không hoàn lại). Nguồn số: trang /skills (filter Free) + /pricing ngày 2026-10-29. Lưu ý: free VẪN cần tài khoản (verify entitlement); giá Skillry CHƯA gồm phí model ngoài (GPT Image/HeyGen/ElevenLabs tự trả theo trang skill — kiểm tra trước khi budget).
- Danh sách Free tại thời điểm đo (không đầy đủ vĩnh viễn — ví dụ để bắt đầu 0đ, đối chiếu lại nhãn Free/Premium trên từng trang skill):
  - Video (10): `bs-plush-crew-launch-video`, `bs-paper-cutout-story-video`, `bs-launchmotion-prompt-find-crumbles-ink`, `bs-launchmotion-cta-brush-wipe-sunset`, `bs-launchmotion-data-copper-device-orbits`, `bs-launchmotion-flow-galaxy-collapses-black`, `bs-launchmotion-reveal-laptop-phone-terminal`, `bs-launchmotion-type-demonstrate-parameter-system`, `bs-launchmotion-grid-angle-moodboards-hard`, `bs-launchmotion-ui-agent-shortlists-influencers`.
  - Web (10): `bs-mint-noir-saas-site`, `bs-ember-ebike-store`, `bs-green-pharmacy-storefront`, `bs-sticker-gifting-app-landing`, `bs-tracklane-devtool-landing`, `bs-lime-frame-designer-portfolio`, `bs-mono-designer-portfolio`, `bs-gridpaper-beverage-brand-site`, `bs-marker-doodle-brand-studio`, `bs-royal-blue-pet-store`.
  - Slides (10): `bs-audio-report-deck`, `bs-mint-marker-deck`, `bs-cobalt-serif-marketing-deck`, `bs-spectrum-brand-strategy-deck`, `bs-blue-block-company-deck`, `bs-tidal-service-playbook-deck`, `bs-cobalt-ribbon-profile-deck`, `bs-lilac-pitch-deck`, `bs-steel-curve-profile-deck`, `bs-lavender-editorial-team-deck`.
  - Image OG (10): `bs-headspace-style-og`, `bs-runway-style-og`, `bs-github-style-og`, `bs-discord-style-og`, `bs-mixpanel-style-og`, `bs-intercom-style-og`, `bs-loom-style-og`, `bs-raycast-style-og`, `bs-ramp-style-og`, `bs-retool-style-og`.
  - Cách dùng: paste `Read https://skillry.dev/skills/<slug>/install.md and follow the instructions to install the skill.` — expect `● Loading skill <slug>`. Cài thử 0đ nên bắt đầu từ `bs-mint-noir-saas-site` (web), `bs-paper-cutout-story-video` (video), `bs-audio-report-deck` (slides + narration), `bs-github-style-og` (OG).
- Quy tắc chọn gói bằng số (tính từ giá đã xác minh): dùng lẻ 1 lần → free/engine, đừng trả; dùng <8 tháng → Monthly; dùng liên tục ≥8 tháng → Yearly (hòa vốn sau ~8 tháng: 79/9.99); dùng >~2 năm → Lifetime (~17 tháng Monthly / ~2.1 năm Yearly). Hết sub: giữ file đã tải (chưa xác minh có chạy tiếp/khóa tải mới không — ghi nhận để kiểm tra Terms).
- Ma sát cài đặt: 3 đường — paste prompt 2 bước (khuyến nghị, mọi OS), CLI (macOS + Node 22+, KHÔNG Linux do lỗi secure storage), ZIP thủ công (cần restart agent). ĐÃ chạy `skillry --help` + `status` (chưa login — lỗi secure storage trên Linux, chưa có tài khoản).
- Đối thủ viral cùng phân khúc: skills.sh/Vercel (CLI `vercel-labs/skills` 35.4k★ + collection `agent-skills` 32.3k★, MIT, 75+ agent) vs Hallmark (Nutlope, 39.5k★, 1 skill sâu). So sánh công bằng là per-skill installs: Manus 2.0 style ~40 vs heygen-com/hyperframes product-launch-video ~538.9K; Notion OG 7 vs og-image mở ~199; Field Notes 8 vs pptx chính chủ (official, không công bố installs).
- Chọn nó khi: cần đúng 1 taste đóng gói sẵn có preview (Manus 2.0, Notion OG...), chấp nhận trả phí + tài khoản + lock-in; HOẶC cần nhiều output cùng taste lặp lại (lúc đó thuê bao rẻ hơn tự ráp từng cái).
- TUYỆT ĐỐI không dùng khi: offline; cấm phụ thuộc vendor trả phí; việc nằm ngoài 4 loại output; hoặc chỉ cần engine/output mà free đã làm tương đương (tự ráp HyperFrames/Remotion, pptx chính chủ, Satori/Playwright) — lúc đó Skillry không hơn gì ngoài cái tên style.

### Usecase con 1: launch video
- Khi dùng: cần video giới thiệu/launch theo phong cách có sẵn (Manus 2.0, Pixel Promo, LaunchMotion).
- Khi bỏ qua: cần motion custom từng keyframe → dùng Motion/GSAP + Remotion trực tiếp.
- Lệnh copy-paste: `npx --yes skillry-cli@latest install bs-manus2-0-style-launch-video --agent opencode` (tên skill lấy đúng từ catalog).
- Ngưỡng số cần đạt: preview khớp phong cách cần; skill có installs > 0 và preview thật (Manus 2.0 style: ~40-45 installs tại thời điểm thẩm tra 2026-10-29).
- Đối thủ free đã xác minh: `heygen-com/hyperframes` (`product-launch-video`, ~538.9K installs) — cùng engine HyperFrames, Skillry chỉ thắng ở style Manus đóng gói sẵn.
- Ví dụ input-output: input “launch video kiểu Manus cho tính năng X” → output MP4 theo workflow skill (render qua HyperFrames/Seedance).
- Pitfalls riêng: nhầm tên skill (slug `bs-...` dài) → luôn copy từ nút install của trang skill, không gõ tay.

### Usecase con 2: landing/portfolio web
- Khi dùng: cần landing mẫu/pholio nhanh phong cách có sẵn (Mint Noir SaaS free, Cadence Marketing, Harbor SaaS Suite).
- Khi bỏ qua: cần system pass gates → Hallmark; cần component React sở hữu source → React Bits.
- Lệnh copy-paste: `Read https://skillry.dev/skills/bs-mint-noir-saas-site/install.md and follow the instructions to install the skill.` (paste vào agent), hoặc `npx --yes skillry-cli@latest install bs-mint-noir-saas-site --agent opencode` (macOS/Windows).
- Ngưỡng số cần đạt: preview đúng ngành/tone; Mint Noir free nên thử tốn 0đ; Cadence Marketing có ~342 views / 16 installs tại thời điểm thẩm tra.
- Đối thủ free đã xác minh: nhiều builder mở (vd shadcn/ui 271.1K installs, vercel-labs/agent-skills collection 32.3k★) — Skillry chỉ thắng khi cần đúng taste Mint/Cadence đóng gói sẵn.
- Ví dụ input-output: input `Build a SaaS landing page` (sau `● Loading skill bs-mint-noir-saas-site`) → output trang HTML theo template skill.
- Pitfalls riêng: output theo taste Skillry, không có tokens/design system riêng — restyle sau bằng Hallmark nếu cần chuẩn.

### Usecase con 3: slide deck + narrated report
- Khi dùng: cần deck thuyết trình hoặc report có narration (Field Notes Deck, audio report deck, Mint Marker, Starlit Deck).
- Khi bỏ qua: cần slide nối CI/data sống → dùng skill chính chủ hoặc code tay.
- Lệnh copy-paste: `Read https://skillry.dev/skills/bs-field-notes-deck/install.md and follow the instructions to install the skill.` (paste vào agent), hoặc CLI `--agent` tương ứng.
- Ngưỡng số cần đạt: deck xuất đúng định dạng yêu cầu — kiểm tra trang skill ghi export HTML/PPTX gì; Field Notes có ~287 views / 8 installs tại thời điểm thẩm tra.
- Đối thủ free đã xác minh: `anthropics/skills --skill pptx` (official, PptxGenJS, ~244.5K installs) — Skillry chỉ thắng khi cần đúng taste deck đóng gói sẵn.
- Ví dụ input-output: input “report deck quý 3 kèm narration” → sau `● Loading skill bs-field-notes-deck` ra deck + audio (HeyGen/ElevenLabs theo skill).
- Pitfalls riêng: narration cần tool ngoài (HeyGen/ElevenLabs) — xác nhận skill có kèm hay phải tự lo tài khoản/trả thêm.

### Usecase con 4: OG image / avatar / minh họa
- Khi dùng: cần ảnh OG/avatar/illustration theo phong cách brand có sẵn (Notion-style OG, GrokBot avatar, Monochrome portrait).
- Khi bỏ qua: cần art direction độc quyền → thuê designer hoặc custom prompt + model ảnh.
- Lệnh copy-paste: `Read https://skillry.dev/skills/bs-notion-style-og/install.md and follow the instructions to install the skill.` (paste vào agent), hoặc CLI `--agent` tương ứng.
- Ngưỡng số cần đạt: preview đúng phong cách brand cần (Notion OG ~222 views / 7 installs; GrokBot avatar ~307 views / 14 installs tại thời điểm thẩm tra 2026-10-29); ảnh qua GPT Image (ghi rõ trong skill).
- Đối thủ free đã xác minh: repo mở kiểu Satori/Playwright (deterministic, không méo chữ như diffusion) — Skillry dùng GPT Image kém hơn cho chữ, chỉ thắng khi cần đúng style đóng gói sẵn.
- Ví dụ input-output: input “OG image kiểu Notion cho bài viết” → output file ảnh đúng tỉ lệ OG.
- Pitfalls riêng: kiểm tra license ảnh output trước khi dùng thương mại.

### Prompt mẫu
- "Đọc https://skillry.dev/skills/bs-mint-noir-saas-site/install.md và cài skill cho OpenCode (free, nhưng vẫn cần đăng nhập tài khoản Skillry), rồi dùng nó build landing cho quán cà phê A: hero + menu 3 món + địa chỉ + giờ mở cửa. Không bịa số liệu, expect `● Loading skill bs-mint-noir-saas-site`."
- "So sánh 2 skill Skillry bs-cadence-marketing-landing (342 views/16 installs) vs bs-harbor-saas-suite (72 views/2 installs) cho landing SaaS: preview, installs, free hay premium, rồi mới cài."
- "Dùng skill Skillry bs-field-notes-deck làm deck giới thiệu nhóm 5 người: xác nhận trang skill ghi export PPTX, kiểm tra narration cần tài khoản HeyGen/ElevenLabs nào, rồi build."

### Các bước chung
1. Chốt việc cần output gì (video/landing/deck/ảnh) → tìm skill khớp trên /skills, xem preview + installs + nhãn Free/Premium.
2. Cài bằng 1 trong 3 đường (CLI có `--agent` đúng / paste prompt / ZIP vào `~/.agents/skills/`); Linux ưu tiên prompt/ZIP vì CLI login lỗi secure storage.
3. Chạy skill theo workflow của nó, kiểm tra output (định dạng, tỉ lệ, license) trước khi dùng.
4. Cần chuẩn riêng (gates/a11y) → sweep lại bằng Hallmark; cần bricks code → thay bằng React Bits.

### Pitfalls
- Gõ tay tên skill (`bs-...`) dễ sai slug → luôn copy từ nút install.
- Tưởng free hết: chỉ 40/617 free — kiểm tra nhãn Free/Premium trước khi lên kế hoạch.
- Install counts thấp (đa số 1–45 lượt; Manus 2.0 style ~40-45 là cao nhất nhóm đã thấy) → đọc preview + review độc lập, đừng tin tuyệt đối.
- CLI login cần browser + OS keychain (macOS/Windows); trên Linux `status` báo lỗi secure storage — headless/CI chuẩn bị prompt/ZIP thay thế.
- Output theo taste Skillry, không có gates như Hallmark — cần chuẩn riêng thì sweep lại bằng Hallmark.

### Tham khảo sử dụng (quyết định được + số có trọng số, chốt 29/10/2026)
- Nhận xét sâu nhất: [AI IDE List 30/09/2026](https://aiidelist.com/blog/skillry-review) *"Skillry is a curated marketplace for Agent Skills, not a conventional prompt library... closer to an app store for agent workflows"* + *"The main tradeoff is scale versus curation"* → khuyên test A/B bằng 1 free skill trước khi trả tiền. 4 limitations: *"Runs in is not the same as tested in"*, outside costs (image/video tooling, API), output lệch kỳ vọng (HTML deck thay vì PPTX), *"Install counters should be treated as an adoption signal, not as a reliable quality score."*
- Verdict cân bằng: [Toolin.ai 07/10/2026](https://toolin.ai/en/tools/skillry) *"genuinely usable, well engineered CLI, clear positioning — not a hollow shell"* nhưng solo indie, không công ty đăng ký, mới live ~1 tháng, zero buzz Reddit/HN, payments non-refundable, 0 review. Nhầm lẫn `skillry.com`/`skillry.ai`/open-source cùng tên → phải đúng `skillry.dev`.
- Đối thủ viết (đọc với bias): [SkillGild 25/10/2026](https://skillgild.dev/learn/skillgild-vs-skillry) đối chiếu giá Monthly $9.99 vs $6.99, Yearly $79 vs $49, Lifetime $169 (SkillGild không có); khác biệt mô hình thật: Skillry trả files vs SkillGild hosted-tools qua MCP.
- Doanh thu Stripe-verified: [TrustMRR 29/10/2026](https://trustmrr.com/startup/skillry) All-time $13,090 / MRR $4,111 / 417 subs (tăng ~3.4× từ $1,191 MRR/121 subs đầu 10/2026); founder 1 người, China, 08/2026. Top installs 200–518 (Dot Avatar 518/27 cao nhất, Plush Crew 380-384, Mint Noir 328, Cadence 342/16, Field Notes 287/8). Catalog trôi nhanh: AI IDE List 30/09 đếm 382 → homepage 29/10 ghi 617.
- Điểm yếu đã xác minh từ nguồn chính chủ: [Terms 17/10/2026](https://skillry.dev/terms) non-refundable + giới hạn 50 downloads/ngày + Lifetime gắn vận hành service; [docs install](https://skillry.dev/learn/install) Linux KHÔNG CLI (macOS/Windows + Node 22+ + OS keychain), free VẪN cần tài khoản. Trust deficit: 0 review Toolin/Uneed, 0 kết quả Reddit/HN/ProductHunt. Tiếng Việt: không tìm thấy review Việt → `chưa xác minh`.
- Mâu thuẫn: testimonial "curation đáng tiền" (Sunilkumar, Able, Celine) vs phe free "trả tiền cho thứ có free trên GitHub" → phán quyết: trả phí chỉ khi cần đúng taste đóng gói + lặp lại nhiều (break-even theo tháng ở Hồ sơ quyết định).

### Tham khảo
- Trang chủ + catalog: https://skillry.dev/skills (617 skill, Web 115 / Slides 61 / Video 359 / Image 82, Free 40 — đọc ngày 2026-10-29)
- Học + cài đặt: https://skillry.dev/learn (SKILL.md, install prompt, CLI, MCP vs skills)
- Skill theo agent (có OpenCode): https://skillry.dev/skills/agent/opencode
- Review độc lập + lệnh CLI: https://aiodelist.com/blog/skillry-review (login/status/install, browser auth, OS keychain; CLI login qua browser)
- Giá: $9.99/tháng, $79/năm, $169 lifetime một lần không hoàn lại (trang /pricing + review độc lập, đọc 2026-10-29; Premium khi sub còn hiệu lực; "1,000+ people supporting us")
- skills.sh đối chứng: https://github.com/vercel-labs/skills (CLI 35.4k★) + https://github.com/vercel-labs/agent-skills (collection 32.3k★), MIT, 75+ agent
- Đã chạy xác minh: `skillry --help` (không cần login, liệt kê login/status/logout/install + 7 agent), `skillry status` trên Linux → lỗi secure storage chỉ macOS/Windows

### Được dùng ở đâu
- Dùng CHO UI (phần web): xem `../../domains/ui/using-skillry.md` — index `../../domains/ui/README.md`.
- Dùng CHO media (video/deck/OG): xem `../../domains/media/using-skillry.md` — index `../../domains/media/README.md`.

### Quay lại index
- Về `../../domains/ui/README.md` (web) + `../../domains/media/README.md` (video/deck/OG) để so hiệu năng/chi phí với `hallmark/`, `reactbits/`.
- Xem thêm item liên quan: `../hallmark/` khi cần system pass gates; `../reactbits/` khi cần bricks React.

---

## English

### When to use
- Need one concrete presentation output fast: launch video, landing page, slide deck, OG image, avatar — without hand-writing the workflow.
- Agent is supported (Claude Code, Codex, Cursor, OpenCode...) and paid skills are acceptable when needed.
- Want to preview real results (preview + installs) before installing.

### When to skip
- Need one deep taste/design system with token control → use `../hallmark/` (Skillry sells outputs, not systems).
- Need owned-source React bricks → use `../reactbits/`.
- Jobs in backend/data/code review/harness — Skillry covers none (all 617 skills are web/video/slides/image).
- Offline or no paid-vendor dependency → use skills.sh, awesome-lists, Anthropic official skills.

### Install (ran `skillry --help` + `status`; not logged in — CLI errors on Linux secure storage)
- Route 1 — paste install prompt (recommended, works on every OS incl. Linux): open the skill page → click Copy install prompt → paste verbatim into the OpenCode chat box (no `/` command needed), e.g. `Read https://skillry.dev/skills/bs-mint-noir-saas-site/install.md and follow the instructions to install the skill.` → if the agent opens the browser asking approval, approve it → assign the job, expect output like `● Loading skill bs-mint-noir-saas-site` then `● Writing ...`.
- NOTE on accounts: free skills STILL need a logged-in Skillry account (the service must verify entitlement before returning the archive) — verified on the install.md page: "Free and premium Skills both require an authenticated account".
- Route 2 — CLI (macOS + Node 22+ only, NOT Linux): `npx --yes skillry-cli@latest login`, then `npx --yes skillry-cli@latest install bs-mint-noir-saas-site` (OpenCode is the default target → `~/.agents/skills/`; other agents add exactly 1 of 8 flags: shared, codex, cursor, gemini-cli, opencode, claude-code, kimi-code, antigravity; token stored only in macOS Keychain/Windows Credential Manager). VERIFIED on Linux: `skillry status` errors `Secure session storage is currently supported on macOS and Windows only` — don't use CLI on Linux.
- Route 3 — manual ZIP: click Download ZIP on the skill page (no Node needed) → run `mkdir -p ~/.agents/skills`, then unzip the just-downloaded file (e.g. `bs-mint-noir-saas-site.zip`) into `~/.agents/skills/` so that `~/.agents/skills/<slug>/SKILL.md` exists (with `assets/`, `scripts/` if shipped) → restart OpenCode (quit fully and reopen) so it loads the new skill.
- Recommended path for OpenCode: `~/.agents/skills/` (default, other agents can read too); per-project: `.agents/skills/` or `.opencode/skills/`.
- Prices verified on /pricing 2026-10-29: Monthly $9.99, Yearly $79, Founding Lifetime $169 one-time (non-refundable); Premium works while subscribed; "1,000+ people supporting us".
- Verify: `ls ~/.agents/skills/<slug>/SKILL.md` exists + agent triggers on matching job descriptions.

### How the item works
- Backing organization: Skillry team, site `skillry.dev`, paid skill marketplace (not an open registry). 617 skills at audit time (Video 359 / Web 115 / Image 82 / Slides 61, 40 Free). Price: $9.99/month or $169 lifetime; single free skills exist.
- Core operating method: each skill = `SKILL.md` folder + templates/scripts, designed and tested by Skillry with real-result previews; agent matches `description` to trigger, runs the skill workflow to output (MP4 video, HTML page, PPTX deck, OG image).
- Per-usecase operating differences: video (renders via HyperFrames/Remotion/Seedance pipelines) vs image (GPT Image calls) vs slides (HTML/PPTX export, HeyGen/ElevenLabs narration) vs web (static HTML). Install routes identical (CLI/ZIP/prompt); the run engines differ per output.

### Differentiating positioning (cross-checked vs skills.sh leaderboard 2026-10-29)
- Skillry does NOT win on capability: video engines (HyperFrames/Remotion), decks (PptxGenJS), OG (Satori/Playwright) all have free open versions with thousands of times more installs. Skillry wins on packaged taste + curation + guided workflow + preview before installing.
- Verified free-opponent table (install command + installs):
| Job | Free opponent (command) | Installs |
|---|---|---|
| Launch video | `heygen-com/hyperframes` → `npx skills add heygen-com/hyperframes` (`product-launch-video` skill) | ~538.9K |
| PPTX deck | `anthropics/skills` → `npx skills add anthropics/skills --skill pptx` (PptxGenJS, official) | ~244.5K |
| OG image | open repos using Satori/Playwright (deterministic, no diffusion-garbled text) | per repo |
| Sample landing | many free builders (shadcn/ui 271.1K, vercel-labs/agent-skills 32.3k-star collection) | per repo |
- Vs skills.sh/Vercel (open free registry: CLI `vercel-labs/skills` 35.4k stars, MIT, 75+ agents): pick Skillry when you need one exact packaged taste (Manus 2.0, Notion OG...) + guided workflow + preview, accepting payment + account + lock-in; pick free when you can assemble it yourself and only need the engine/output.
- Vs `../hallmark/` (one deep skill, machine gates): Skillry is wide across 4 outputs but shallow — no system, tokens, gates, review. Decide: need one presentable artifact now → Skillry; need a system with measurable gates (contrast 4.5:1, 1280x800 fold) → Hallmark.
- Honest break-even: paying makes sense when you repeatedly need outputs in one packaged taste; one-off job → free + engine is enough, don't pay.
- Vs `../reactbits/` (owned-source React bricks): Skillry also covers video/slides/image, not just React code. Decide: need motion film/deck/OG image → Skillry; need owned-source React components → React Bits.

### Decision dossier
- Jobs SERVED: 1. Manus/Linear-style launch video (video skill + HyperFrames); 2. sample landing/SaaS site (Mint Noir, Cadence); 3. slide deck + narrated report (Field Notes, audio report deck); 4. brand-style OG image/avatar (Notion-style OG, GrokBot avatar).
- Jobs NOT served: 1. code/PR review → use open-system pr-review skill; 2. data/spreadsheet work → use Anthropic official skills (xlsx/csv); 3. UI that must pass gates (contrast/focus) → use Hallmark.
- Free / total + price: 40 free / 617 total (~6.5%) at measurement 2026-10-29 (see Free list below — catalog drifts over time, re-check the Free filter on /skills before deciding, never assume this is the full set). Premium $9.99/month, Yearly $79, Lifetime $169 one-time (non-refundable). Number sources: /skills page (Free filter) + /pricing, 2026-10-29. Note: free STILL needs an account (entitlement verification); the price does NOT include external model fees (GPT Image/HeyGen/ElevenLabs billed separately per the skill page — check before budgeting).
- Free list at measurement (not permanently exhaustive — 0-cost starters, re-check each skill's Free/Premium label):
  - Video (10): `bs-plush-crew-launch-video`, `bs-paper-cutout-story-video`, `bs-launchmotion-prompt-find-crumbles-ink`, `bs-launchmotion-cta-brush-wipe-sunset`, `bs-launchmotion-data-copper-device-orbits`, `bs-launchmotion-flow-galaxy-collapses-black`, `bs-launchmotion-reveal-laptop-phone-terminal`, `bs-launchmotion-type-demonstrate-parameter-system`, `bs-launchmotion-grid-angle-moodboards-hard`, `bs-launchmotion-ui-agent-shortlists-influencers`.
  - Web (10): `bs-mint-noir-saas-site`, `bs-ember-ebike-store`, `bs-green-pharmacy-storefront`, `bs-sticker-gifting-app-landing`, `bs-tracklane-devtool-landing`, `bs-lime-frame-designer-portfolio`, `bs-mono-designer-portfolio`, `bs-gridpaper-beverage-brand-site`, `bs-marker-doodle-brand-studio`, `bs-royal-blue-pet-store`.
  - Slides (10): `bs-audio-report-deck`, `bs-mint-marker-deck`, `bs-cobalt-serif-marketing-deck`, `bs-spectrum-brand-strategy-deck`, `bs-blue-block-company-deck`, `bs-tidal-service-playbook-deck`, `bs-cobalt-ribbon-profile-deck`, `bs-lilac-pitch-deck`, `bs-steel-curve-profile-deck`, `bs-lavender-editorial-team-deck`.
  - Image OG (10): `bs-headspace-style-og`, `bs-runway-style-og`, `bs-github-style-og`, `bs-discord-style-og`, `bs-mixpanel-style-og`, `bs-intercom-style-og`, `bs-loom-style-og`, `bs-raycast-style-og`, `bs-ramp-style-og`, `bs-retool-style-og`.
  - Try 0-cost first: `bs-mint-noir-saas-site` (web), `bs-paper-cutout-story-video` (video), `bs-audio-report-deck` (slides + narration), `bs-github-style-og` (OG).
- Package rule by the numbers (arithmetic from verified prices): one-off job → free/engine, don't pay; <8 months of use → Monthly; continuous use ≥8 months → Yearly (breaks even at ~8 months: 79/9.99); >~2 years → Lifetime (~17 months of Monthly / ~2.1 years of Yearly). After sub ends: downloaded files stay (UNVERIFIED whether they keep running/block new downloads — flagged for Terms check).
- Install friction: 3 routes — paste prompt 2 steps (recommended, every OS), CLI (macOS + Node 22+, NOT Linux due to secure-storage error), manual ZIP (needs agent restart). RAN `skillry --help` + `status` (not logged in — Linux secure-storage error, no account yet).
- Viral same-segment opponents: skills.sh/Vercel (CLI `vercel-labs/skills` 35.4k stars + collection `vercel-labs/agent-skills` 32.3k stars, MIT, 75+ agents) vs Hallmark (Nutlope, 39.5k stars, one deep skill). Fair comparison is per-skill installs: Manus 2.0 style ~40 vs heygen-com/hyperframes product-launch-video ~538.9K; Notion OG 7 vs open og-image ~199; Field Notes 8 vs official pptx (official, no published installs).
- Pick it when: you need exactly one packaged taste with preview (Manus 2.0, Notion OG...), accepting payment + account + lock-in; OR you need many repeated outputs in one taste (then subscription beats assembling each).
- NEVER use when: offline; paid-vendor dependency forbidden; job outside the 4 outputs; or you only need the engine/output that free already matches (self-assembled HyperFrames/Remotion, official pptx, Satori/Playwright) — then Skillry adds nothing but the style name.

### Sub-usecase 1: launch video
- When to use: launch/intro video in an existing style (Manus 2.0, Pixel Promo, LaunchMotion).
- When to skip: custom keyframed motion → use Motion/GSAP + Remotion directly.
- Copy-paste command: `npx --yes skillry-cli@latest install bs-manus2-0-style-launch-video --agent opencode` (take the exact slug from the catalog).
- Numeric bar: preview matches the needed style; skill has installs > 0 and a real preview (Manus 2.0 style: ~40-45 installs at audit time 2026-10-29).
- Verified free opponent: `heygen-com/hyperframes` (`product-launch-video`, ~538.9K installs) — same HyperFrames engine, Skillry wins only on packaged Manus style.
- Input-output example: input "Manus-style launch video for feature X" → MP4 output via the skill workflow (HyperFrames/Seedance render).
- Own pitfalls: hand-typing slugs (`bs-...`) is error-prone → always copy from the skill page install button.

### Sub-usecase 2: landing/portfolio web
- When to use: quick sample landing/site in an existing style (free Mint Noir SaaS, Cadence Marketing, Harbor SaaS Suite).
- When to skip: system must pass gates → Hallmark; single owned-source React component needed → React Bits.
- Copy-paste command: `Read https://skillry.dev/skills/bs-mint-noir-saas-site/install.md and follow the instructions to install the skill.` (paste into agent), or `npx --yes skillry-cli@latest install bs-mint-noir-saas-site --agent opencode` (macOS/Windows).
- Numeric bar: preview matches industry/tone; Mint Noir free so trying costs nothing; Cadence Marketing shows ~342 views / 16 installs at audit time.
- Verified free opponent: many open builders (e.g. shadcn/ui 271.1K installs, vercel-labs/agent-skills 32.3k-star collection) — Skillry wins only when the exact Mint/Cadence packaged taste is needed.
- Input-output example: input `Build a SaaS landing page` (after `● Loading skill bs-mint-noir-saas-site`) → HTML page output following the skill template.
- Own pitfalls: output follows Skillry taste, no own tokens/design system — restyle with Hallmark afterwards for a custom standard.

### Sub-usecase 3: slide deck + narrated report
- When to use: presentation deck or narrated report (Field Notes Deck, audio report deck, Mint Marker, Starlit Deck).
- When to skip: slides wired to live CI/data → official skills or hand code.
- Copy-paste command: `Read https://skillry.dev/skills/bs-field-notes-deck/install.md and follow the instructions to install the skill.` (paste into agent), or CLI with matching `--agent`.
- Numeric bar: deck exports the required format — check what the skill page lists; Field Notes shows ~287 views / 8 installs at audit time.
- Verified free opponent: `anthropics/skills --skill pptx` (official, PptxGenJS, ~244.5K installs) — Skillry wins only when the exact packaged deck taste is needed.
- Input-output example: input "Q3 report deck with narration" → after `● Loading skill bs-field-notes-deck`, deck + audio output (HeyGen/ElevenLabs per skill).
- Own pitfalls: narration needs external tools (HeyGen/ElevenLabs) — confirm whether the skill bundles them or you bring/pay accounts.

### Sub-usecase 4: OG image / avatar / illustration
- When to use: brand-style OG image/avatar/illustration from existing styles (Notion-style OG, GrokBot avatar, Monochrome portrait).
- When to skip: exclusive art direction → hire a designer or custom prompt + image model.
- Copy-paste command: `Read https://skillry.dev/skills/bs-notion-style-og/install.md and follow the instructions to install the skill.` (paste into agent), or CLI with matching `--agent`.
- Numeric bar: preview matches the needed brand style (Notion OG ~222 views / 7 installs; GrokBot avatar ~307 views / 14 installs at audit time 2026-10-29); images via GPT Image (stated in skill).
- Verified free opponent: open Satori/Playwright-style repos (deterministic, no diffusion-garbled text) — Skillry using GPT Image is weaker for text, winning only on packaged style.
- Input-output example: input "Notion-style OG image for a post" → image file at OG dimensions.
- Own pitfalls: check output image licensing before commercial use.

### Sample prompts
- "Read https://skillry.dev/skills/bs-mint-noir-saas-site/install.md and install the skill for OpenCode (it is free but still needs a logged-in Skillry account), then use it to build a landing for coffee shop A: hero + 3-item menu + address + opening hours. Do not invent numbers; expect `● Loading skill bs-mint-noir-saas-site`."
- "Compare Skillry skills bs-cadence-marketing-landing (342 views/16 installs) vs bs-harbor-saas-suite (72 views/2 installs) for a SaaS landing: preview, installs, free vs premium, then install."
- "Use Skillry skill bs-field-notes-deck for a 5-person team intro deck: confirm the skill page lists PPTX export, check which HeyGen/ElevenLabs account narration needs, then build."

### Shared steps
1. Fix the needed output (video/landing/deck/image) → find the matching skill on /skills, check preview + installs + Free/Premium label.
2. Install via one of 3 routes (CLI with right `--agent` / paste prompt / ZIP into `~/.agents/skills/`); on Linux prefer prompt/ZIP since CLI login errors on secure storage.
3. Run the skill per its workflow, verify output (format, ratio, license) before use.
4. Need a custom standard (gates/a11y) → re-sweep with Hallmark; need code bricks → swap to React Bits.

### Pitfalls
- Hand-typing skill names (`bs-...`) risks wrong slugs → always copy from the install button.
- Not everything is free: only 40/617 are free — check the Free/Premium label before planning.
- Install counts are low (mostly 1-45; Manus 2.0 style ~40-45 is the highest seen) → read previews + independent reviews, never trust blindly.
- CLI login needs browser + OS keychain (macOS/Windows); on Linux `status` errors on secure storage — prepare prompt/ZIP alternatives for headless/CI.
- Output follows Skillry taste with no gates like Hallmark — re-sweep with Hallmark for a custom standard.

### References
- Home + catalog: https://skillry.dev/skills (617 skills, Web 115 / Slides 61 / Video 359 / Image 82, 40 Free — read 2026-10-29)
- Learn + install: https://skillry.dev/learn (SKILL.md, install prompt, CLI, MCP vs skills)
- Per-agent skills (incl. OpenCode): https://skillry.dev/skills/agent/opencode
- Independent review + CLI commands: https://aiodelist.com/blog/skillry-review (login/status/install, browser auth, OS keychain; browser-based CLI login)
- Price: $9.99/month, $79/year, $169 lifetime one-time non-refundable (/pricing page + independent review, read 2026-10-29; Premium while subscribed; "1,000+ people supporting us")
- skills.sh cross-check: https://github.com/vercel-labs/skills (CLI 35.4k stars) + https://github.com/vercel-labs/agent-skills (collection 32.3k stars), MIT, 75+ agents
- Verified by running: `skillry --help` (no login needed, lists login/status/logout/install + 7 agents), `skillry status` on Linux → secure-storage error (macOS/Windows only)

### Back to index
- Back to `../../domains/ui/README.md` (web) + `../../domains/media/README.md` (video/deck/OG).
- Related items: `../hallmark/` (gated system); `../reactbits/` (React bricks). Where used: `../../domains/ui/using-skillry.md` (web) + `../../domains/media/using-skillry.md` (media).
