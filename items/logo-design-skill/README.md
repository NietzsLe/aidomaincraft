# logo-design-skill

## Tiếng Việt

### Dùng khi
- Cần logo/brand mark mới (wordmark, monogram, letterform, pictorial, abstract, emblem, mascot, combination) ra file SVG vector production-ready kèm test có số + full kit, mà muốn quy trình kỷ luật (brief → concepts → audit → checkpoint dừng chờ duyệt → kit).
- Có logo sẵn cần critique có scorecard, redesign/refresh giữ equity, hoặc xuất favicon/app-icon/web-icons + bản one-colour từ 1 master SVG.
- Agent hỗ trợ định dạng Agent Skills mở (Claude Code, Gemini CLI, Codex, Cursor, Copilot, OpenCode...) + máy có Python 3.8+; khuyến nghị model xem được ảnh để skill tự render PNG và nhìn lại bản vẽ trước khi trình (không có thì skill vẫn chạy nhưng phải khai báo + vẽ hình học đơn giản hơn).
- Muốn học convention của category + tránh đụng hàng bằng thư viện 1,432 logo SVG thật đã phân loại (không copy).

### Bỏ qua khi
- Chỉ cần ảnh raster nhanh (OG/social/avatar trang trí), không cần master vẽ hình học kèm audit → dùng `../skillry/` (GPT Image, taste đóng gói, xem [Usecase con 4](../../items/skillry/README.md#usecase-con-4-og-image--avatar--minh-hoa)) hoặc generator diffusion (logocreator, cần Together key trả tiền).
- Cần video launch/deck → `../skillry/` + `../awesome-opus5-5-videos/`; cần page system pass gates → `../hallmark/`; cần bricks React → `../reactbits/`.
- Cần cam kết pháp lý về trademark clearance → thuê tra cứu chuyên nghiệp/luật sư (skill nói rõ không đảm bảo, xem [Pitfalls](#pitfalls)).
- Muốn copy/trace logo trong thư viện → cấm tuyệt đối (`TRADEMARKS.md`: MIT của repo KHÔNG áp dụng cho file SVG thư viện).

### Cài đặt (đã clone + chạy thử scripts trên Linux 30/10/2026; chưa cài plugin marketplace vì máy này không có Claude Code)
- Cách 1 — plugin marketplace (Claude Code, khuyến nghị theo README gốc): `/plugin marketplace add kaankiziltug/logo-design-skill` rồi `/plugin install logo-design@logo-design-skill`.
- Cách 2 — thủ công (mọi agent, đã chạy tương đương bằng `git clone`): `git clone https://github.com/kaankiziltug/logo-design-skill.git` rồi copy thư mục skill vào đúng chỗ agent đọc, ví dụ `cp -r logo-design-skill/skills/logo-design ~/.claude/skills/logo-design` (all projects) hoặc `.claude/skills/logo-design` (per project); Gemini CLI: `~/.gemini/skills/logo-design`; Codex CLI: `~/.codex/skills/logo-design`; OpenCode/Cursor/Copilot: thư mục `skills/` của project (bảng đầy đủ trong README gốc). ĐÃ CHẠY 30/10/2026: `git clone --depth 1` thành công, `assets/library/svg/` có 1,432 file, `scripts/*.py` chạy được bằng `python3` (chuẩn, không dependency).
- Yêu cầu: Python 3.8+ (thư viện chuẩn only); Windows dùng `python`/`py -3` thay `python3`. Render PNG/SVG→ICO cần 1 backend của `render_png.py`: cairosvg, rsvg-convert, Inkscape, Chrome/Chromium headless hoặc macOS Quick Look (`--which` liệt kê backend có sẵn).
- Kiểm tra (đã chạy 30/10/2026, output thật): `python3 scripts/search_library.py --industry payments-fintech --summary` → `37 logos match (of 1432)` kèm bảng mark-type/màu/technique; `python3 scripts/svg_audit.py test-logo.svg` (hình tròn đen test) → `production-readiness score: 100/100`; `python3 scripts/export_variants.py test-logo.svg --mono "#0F7C80" --icon-bg "#0F7C80" --out-dir out --title "Test"` → 6 file (`-black/-white/-mono-0f7c80/-square/-favicon/-app-icon.svg`); `python3 scripts/presentation_board.py --list-mockups` → 17 mockups, 12 ngành.

### Cách item hoạt động
- Tổ chức đứng sau: cá nhân `kaankiziltug`, repo `https://github.com/kaankiziltug/logo-design-skill`, license MIT (code + chữ; riêng 1,432 SVG thư viện KHÔNG thuộc MIT — xem `TRADEMARKS.md`), bản 1.4.5, nhịp update 25 commits từ 26/09/2026, đẩy cuối 20/10/2026. Số liệu API GitHub ngày 30/10/2026: 5,320★ / 420 forks / 4 issues mở; tăng +4,841★ trong 34 ngày (Trendshift 25/09–28/10/2026).
- Phương thức hoạt động chung: 1 skill định dạng Agent Skills mở (`SKILL.md` + `references/` 15 file load khi cần + `scripts/` 8 file Python + `assets/library/` + `templates/` 2 file). Agent đọc `description` trong `SKILL.md` để trigger khi user nhắc logo/wordmark/monogram/brand mark/app icon/favicon/rebrand/critique; chạy workflow 7 phase (discovery → research → concepts → build SVG đen trước → test & refine lặp ≥2 vòng → checkpoint DỪNG chờ duyệt → kit); mọi bản vẽ đều render ra PNG và nhìn lại trước khi trình.
- Khác biệt vận hành theo usecase: thiết kế mới (chạy đủ 7 phase + checkpoint bắt buộc, xem [Usecase con 1](#usecase-con-1-thiet-ke-logo-moi--checkpoint--kit)) khác critique/redesign (vào thẳng `references/critique.md`/`redesign.md` + audit file có sẵn, xem [Usecase con 2](#usecase-con-2-critique--redesign-logo-co-san)) khác xuất assets (chỉ chạy `export_variants.py`/`render_png.py` trên master đã duyệt, xem [Usecase con 3](#usecase-con-3-xuat-faviconapp-iconbien-the--render-png)) khác board/guidelines (chạy `presentation_board.py` theo spec JSON + template 1 trang, xem [Usecase con 4](#usecase-con-4-board-trinh-bay--guidelines--identity)).

### Cốt lõi bất biến
- Checkpoint bắt buộc: concepts xong + test xong thì trình đúng 1 ảnh `concept_sheet.py` (greyscale + size thật 64/32/16px + recommendation) rồi DỪNG chờ user pick hướng mới build kit (xem [Usecase con 1](#usecase-con-1-thiet-ke-logo-moi--checkpoint--kit)). Build kit trước duyệt = không còn dùng hệ.
- Brief + research trước build: discovery (tên/audience/3–5 tính từ/đối thủ/clichés off-limits) + `search_library.py --summary` category + word map + thử ít nhất 2 mark types, viết 8–12 one-liners rồi chỉ build 3 (xem [Các bước chung](#cac-buoc-chung)). Vẽ thẳng SVG khi chưa brief/research = FAIL.
- Đen trước màu sau + audit trước trình: canvas symbol `viewBox="0 0 256 256"`, không `<text>` ở file final, chạy `svg_audit.py` + `preview_sheet.py` lặp ≥2 vòng và render PNG nhìn thật (xem [Usecase con 1](#usecase-con-1-thiet-ke-logo-moi--checkpoint--kit)). Trình bản chưa audit/render = FAIL.
- Thư viện chỉ học, cấm copy/trace/imitate (`TRADEMARKS.md` + Red flags trong `SKILL.md`). Dùng form thư viện làm output = FAIL pháp lý.
- Sau khi dùng phải nêu được: concept nào trong shortlist đã qua checkpoint + audit score + giữ/đổi gì; không nêu được = chưa thực sự dùng hệ.

### Phần tùy chỉnh
- Được đổi: brief (tên/ngành/audience/tính từ), mark type trong 8 loại, palette 1–2 màu + màu nền mockup (`tile_color`), typography (tối đa 2 họ), mockups theo ngành (17 loại), concept nào trong shortlist 3, giữ/đổi gì sau critique. Cổng duyệt 2 tầng: (1) artifact nào — trình shortlist 2–3 concept kèm lý do qua question tool, user pick mới build kit (kể cả khi user đã duyệt hướng lớn, kit vẫn chờ duyệt artifact cụ thể); (2) giữ/đổi gì — màu/type/mockup nào đổi phải chốt trước khi build. Waiver duy nhất (bỏ checkpoint khi user nói rõ "don't ask, just deliver everything") phải quote câu ok tường minh của user, không suy diễn. Cấm đưa `must-not` (copy thư viện, hứa trademark clearance) vào danh sách tùy chỉnh.

### Phân công ai làm gì
- Agent chính: discovery/brief + research thư viện (shortlist 2–3 hướng kèm lý do, chờ user pick — cấm tự chốt rồi build), build SVG, chạy audit/preview/render + MỞ PNG nhìn thật, trình concept sheet + recommendation, sau duyệt mới build kit/export/board, verify output (định dạng/file tồn tại/license font).
- Giao cho claude các bước cần browser/tài khoản ngoài: reverse-image search kiểm tra đụng hàng, tra cứu trademark database, xác minh font license cho phép làm logo, mở `preview.html`/`gallery.html`/board trên browser xem thật — kèm file SVG + yêu cầu cụ thể; cấm agent tự bịa kết quả tra cứu. Không render được thì agent phải khai báo + vẽ hình học đơn giản hơn, cấm claim test đã chạy.
- Agent verify: `svg_audit.py` hết WARN chưa lý giải + size ladder 16px đọc được + one-colour/reversed/shelf test đạt + file kit tồn tại (`-black/-white/-mono/-square/-favicon/-app-icon`, web-icons, board, guidelines).

### Định vị khác biệt (số liệu API GitHub ngày 30/10/2026)
- So với `Nutlope/logocreator` (generator logo OSS, 8,898★/829 forks, Flux diffusion trên Together AI, MIT): khác cơ chế ở đầu ra — logocreator render ảnh diffusion trong vài giây rồi export SVG từ ảnh (mục SVG export trong README gốc đã tick [x]), cần `TOGETHER_API_KEY` (trả tiền inference theo giá Together, có hiện giá ước tính) + stack `pnpm install && pnpm dev`; logo-design-skill vẽ SVG bằng code hình học + audit số + checkpoint, chỉ cần Python stdlib, 0 key. Chọn logo-design-skill thay vì logocreator khi cần master vẽ hình học + pass 16px/one-colour/audit đo được (ngưỡng: audit ≥~99 như file recommend trong README gốc vs 76 của file bị loại) mà không muốn key/stack trả phí; chọn logocreator khi cần nhiều option ảnh nhanh + đã có Together key, chấp nhận diffusion (rủi ro méo chữ, test kỷ luật tự lo) + tự chịu check đụng hàng.
- So với skill ảnh của `../skillry/` (GPT Image diffusion, taste đóng gói: Notion OG 222 views/7 installs, GrokBot avatar 307/14 ngày 29/10/2026, trả phí $9.99/tháng + bắt buộc tài khoản): khác ở chất liệu — Skillry ra raster theo taste có sẵn + preview; logo-design-skill ra vector + audit + kit 0đ MIT offline được. Chọn logo-design-skill thay vì Skillry khi quyết định phụ thuộc vào vector master + số audit đo được, không phải taste đóng gói; chọn Skillry khi cần đúng taste OG/avatar có preview + chấp nhận trả phí + raster méo chữ diffusion chấp nhận được.
- Khung trung thực: logo-design-skill thắng ở kỷ luật vector + audit + giá 0đ; thua ở tốc độ (7 phase, checkpoint chờ người) và thua ở art raster trang trí (diffusion đẹp hơn cho ảnh minh họa). Cần 1 món raster chạy ngay → Skillry/logocreator; cần master dùng thập kỷ → logo-design-skill.

### Bản đồ phủ usecase (quét HẾT SKILL.md + 8 scripts + 15 references + 2 templates 30/10/2026 — ★ mạnh nhất đầu)
- ★ Thiết kế logo mới full (Design 7 phase + checkpoint + kit): xem Usecase 1.
- Critique + redesign logo có sẵn (scorecard + equity audit + audit số): xem Usecase 2.
- Xuất favicon/app-icon/biến thể + render PNG (`export_variants.py` + `render_png.py`): xem Usecase 3.
- Trung bình: board trình bày + guidelines/identity (`presentation_board.py` 17 mockups/12 ngành + 2 templates) → dùng khi cần pitch khách hàng, xem Usecase 4.
- Trung bình: tra cứu thư viện độc lập (`search_library.py` mọi filter + `--summary` + `gallery.html`) → dùng khi chỉ cần học convention category/tránh đụng hàng mà chưa design (lệnh đã chạy thật ở [Cài đặt](#cai-dat-da-clone--chay-thu-scripts-tren-linux-30102026-chua-cai-plugin-marketplace-vi-may-nay-khong-co-claude-code)).
- KHÔNG hỗ trợ → thay thế: `build_catalog.py` (maintainer rebuild catalog/gallery) → không dùng; cam kết trademark clearance pháp lý → tra cứu chuyên nghiệp/luật sư; xác minh font license → foundry/chủ font; video/deck/OG raster → `../skillry/`; page system pass gates → `../hallmark/`; bricks React → `../reactbits/`.

### Hồ sơ quyết định
- Việc DÙNG (3+, cụ thể): 1. logo mới SVG từ brief đến kit (8–12 one-liners → build 3 → audit ≥2 vòng → checkpoint greyscale → kit màu/lockup/board/icons/guidelines); 2. critique/redesign logo có sẵn (scorecard + audit số + equity audit); 3. favicon/app-icon/web-icons + bản black/white/mono/square từ 1 master đã duyệt.
- Việc KHÔNG DÙNG (3+, mỗi việc kèm hệ thay thế): 1. ảnh raster/OG/avatar trang trí → dùng `../skillry/` (GPT Image) hoặc logocreator (Flux diffusion, cần Together key); 2. video/deck → dùng `../skillry/` + `../awesome-opus5-5-videos/`; 3. page system cần pass gates → dùng `../hallmark/`; 4. cam kết pháp lý trademark → dùng dịch vụ tra cứu/luật sư.
- Free / tổng + giá: 100% free, 0đ toàn bộ (MIT cho code + chữ; 1,432 SVG thư viện KHÔNG thuộc MIT, chỉ học không copy — nguồn `LICENSE` + `TRADEMARKS.md`, đọc 30/10/2026). Không subscription, không tài khoản, không phí model ngoài (chạy local bằng Python).
- Ma sát cài đặt: 2 bước (marketplace: 2 lệnh `/plugin`; thủ công: `git clone` + `cp -r` 1 lệnh). ĐÃ chạy thử đến bước: clone --depth 1 OK + `search_library --summary` (37/1432) + `svg_audit` (100/100) + `export_variants` (6 file) + `presentation_board --list-mockups` (17/12) — output thật ở [Cài đặt](#cai-dat-da-clone--chay-thu-scripts-tren-linux-30102026-chua-cai-plugin-marketplace-vi-may-nay-khong-co-claude-code). Rào cản: không auth/login/Node/tiền/quyền admin; chỉ cần Python 3.8+; render PNG cần 1 backend (cairosvg/rsvg/Inkscape/Chrome/macOS QL), thiếu thì vẫn design được nhưng phải khai báo chưa nhìn bản render.
- Đối thủ viral cùng phân khúc: `Nutlope/logocreator` (8,898★/829 forks, Flux diffusion + BYO Together key trả tiền inference + stack pnpm/Node, SVG export từ ảnh đã có) vs skill ảnh `../skillry/` (GPT Image raster, Notion OG 222/7, GrokBot 307/14, $9.99/tháng + tài khoản bắt buộc). Số đo API GitHub + README logocreator + trang skillry ngày 29–30/10/2026.
- Chọn nó thay vì đối thủ khi: cần SVG vẽ hình học + audit số (target ~99/100, size ladder 16px, one-colour, reversed, shelf test) + checkpoint có recommendation + kit đầy đủ, với giá 0đ MIT không key. Ví dụ đổi lựa chọn: brief quán cà phê cần logo dập 1 màu lên túi kraft + favicon 16px, không muốn key trả phí → logo-design-skill (SVG + small-size cut + audit); brief cần ảnh OG kiểu Notion cho bài post → Skillry; đã có Together key và cần nhiều option ảnh nhanh → logocreator.
- TUYỆT ĐỐI không dùng khi: cần cam kết pháp lý trademark (skill cấm hứa); muốn copy/trace thư viện (vi phạm trademark); cần art raster diffusion (skill vẽ hình học, không thi vẽ minh họa); máy không có Python 3.8+ và không cài được.

### Usecase con 1: thiết kế logo mới + checkpoint + kit
- Khi dùng: có brief thương hiệu mới (tên/audience/tính từ) và cần đi hết quy trình đến kit đầy đủ.
- Khi bỏ qua: chỉ cần critique file có sẵn → Usecase 2; chỉ cần xuất assets từ master đã duyệt → Usecase 3; cần raster nhanh → Skillry/logocreator.
- Cơ chế khác các usecase khác ở đâu: duy nhất chạy đủ 7 phase + checkpoint DỪNG chờ duyệt; các usecase khác vào thẳng script/reference chuyên biệt không qua checkpoint.
- Lệnh copy-paste (checkpoint, chạy sau khi build + test 3 symbols + lockups — lockup là cách xếp symbol + wordmark thành 1 hàng/dọc): `python3 scripts/concept_sheet.py a-symbol.svg b-symbol.svg c-symbol.svg --lockups a-lockup.svg b-lockup.svg c-lockup.svg --names "Kiln K" "Grin" "Pendant" --notes "Kiln arch in the K leg" "Citrus wedge as a cheeky grin" "Didone M holding an O pendant" --recommend 1 --greyscale -o concepts.png` (nguồn `SKILL.md` Phase 6; chuỗi trước đó: `search_library.py --industry <closest> --summary` → build SVG đen → `svg_audit.py` + `preview_sheet.py` lặp ≥2 vòng).
- Ngưỡng số cần đạt: audit hết WARN chưa lý giải (target ~99/100 như file recommend trong README gốc; file 76/100 bị loại); ý tưởng đọc được ở 16–24px; gaps/strokes đủ lớn; màu chính đạt tương phản (ví dụ trong gốc: sage đánh đậm để đạt 3:1, mint 1.4:1 trên trắng chỉ dùng nền tối); shelf test (đặt logo cạnh logo đối thủ xem có lẫn không) đạt.
- Ví dụ input-output (minh họa, không phải mặc định — chọn concept nào phải qua shortlist + user pick trước): input "Kiln, specialty coffee roaster ở Istanbul, warm/crafted/modern, lên túi/cup/avatar" → output `concepts.png` greyscale (3 concepts + size thật 64/32/16px + recommend "Kiln K": chân K là vòm lò, audit bắt diagonal 60.8° + symbol lệch tâm trước khi trình) → user pick → kit (màu/lockups/board/icons/guidelines).
- Pitfalls riêng: vẽ SVG mù không render (bắt buộc `render_png.py` + mở PNG nhìn thật sau mỗi lần sửa); dùng `<text>` ở file final (phải dựng letterform bằng path); gradient/shadow cứu form yếu; >3 màu không lý do concept.
- Phân công usecase này: agent chính làm brief→build→audit→trình checkpoint (shortlist qua question tool, user pick mới build kit); giao claude reverse-image + trademark-database check; verify bằng audit score + 16px ladder + file kit tồn tại.

### Usecase con 2: critique + redesign logo có sẵn
- Khi dùng: đã có file logo (SVG) cần chấm điểm có scorecard, hoặc modernise/thay logo mà giữ equity (equity = phần nhận diện cũ đáng giữ: màu/chữ/form khách đã nhớ).
- Khi bỏ qua: làm logo từ đầu → Usecase 1; file đã duyệt chỉ cần xuất biến thể → Usecase 3.
- Cơ chế khác các usecase khác ở đâu: không qua concepts/checkpoint; vào thẳng `references/critique.md` (scorecard + fixes) hoặc `references/redesign.md` (equity audit → refresh techniques) rồi mới nối vào phase Design 4–5.
- Lệnh copy-paste: `python3 scripts/svg_audit.py my-logo.svg` và `python3 scripts/preview_sheet.py my-logo.svg --refs-industry developer-tools -o preview.html` (nguồn `SKILL.md` Phase 5 + bảng Tools).
- Ngưỡng số cần đạt: audit liệt kê cụ thể anchors vs median thư viện (75 toàn cục/53 square), near-miss 0.3–3°, tiny <1/48 canvas, số màu/gradient, contrast; critique ra scorecard + 3 fixes đo được; redesign qua equity audit (giữ/bỏ gì) trước khi vẽ lại.
- Ví dụ input-output (thật từ README gốc): input 2 file `a-lockup.svg` + `b-emblem.svg` → output audit `a-lockup` 99/100 (205 anchors, INFO complexity) recommend; `b-emblem` 76/100 (374 anchors >95% mẫu, 8 near-miss, 6 tiny) không recommend.
- Pitfalls riêng: audit là advice not law — override WARN được nhưng phải nói được vì sao; critique chưa phải redesign (thiếu equity audit mà vẽ lại = mất equity).
- Phân công usecase này: agent chính chạy audit/preview + chấm scorecard + đề xuất fixes (chờ duyệt trước khi redraw); giao claude đối chiếu 3–4 file exemplary trong thư viện (`--exemplary --format paths`) + peer test; verify bằng audit sau fix + đọc lại ở 16px/mirror/rotate-180°.

### Usecase con 3: xuất favicon/app-icon/biến thể + render PNG
- Khi dùng: đã có master SVG ĐƯỢC DUYỆT ở checkpoint và cần bộ deliverables (one-colour, square, favicon, app-icon, web-icons, PNG đúng size).
- Khi bỏ qua: chưa có master duyệt → Usecase 1/2 trước; cần board pitch → Usecase 4.
- Cơ chế khác các usecase khác ở đâu: không design không audit ý tưởng; chỉ biến đổi file master đã duyệt bằng `export_variants.py`/`render_png.py`.
- Lệnh copy-paste (đã chạy tương đương 30/10/2026): `python3 scripts/export_variants.py final-symbol.svg --title "Brand logo" --mono "#0F7C80" --icon-bg "#0F7C80" --web-icons --favicon-source final-symbol-small.svg` và `python3 scripts/render_png.py my-logo.svg --size 512 -o my-logo.png` (nguồn `SKILL.md` Phase 7 + bảng Tools).
- Ngưỡng số cần đạt: đủ bộ `-black/-white/-mono-<hex>/-square/-favicon/-app-icon.svg` + `--web-icons` (favicon.ico 16/32/48, PNG 180/192/512, maskable, manifest, head snippet); small-size cut riêng (`--favicon-source`) khi master vỡ ở 16px; PNG đúng size tuyệt đối, nền trong suốt.
- Ví dụ input-output (thật, đã chạy 30/10/2026): input hình tròn đen test + `--mono "#0F7C80" --icon-bg "#0F7C80"` → output 6 file SVG trong `out/` (`test-logo-black/white/mono-0f7c80/square/favicon/app-icon.svg`).
- Pitfalls riêng: thiếu backend render thì PNG/ICO không ra — phải khai báo, cấm claim đã test; cấm gọi `qlmanage` trực tiếp (crop non-square, co file có width/height, mất transparency — dùng `render_png.py`).
- Phân công usecase này: agent chính chạy export/render + đối chiếu file tồn tại + mở PNG kiểm tra; giao claude bước mở board/preview trên browser nếu cần; verify bằng `ls` đủ 6 biến thể + web-icons + PNG đúng size.

### Usecase con 4: board trình bày + guidelines + identity
- Khi dùng: concept đã duyệt cần pitch khách hàng (mockups đúng ngành) + guidelines 1 trang + mở rộng identity (sub-brand/pattern/motion).
- Khi bỏ qua: chưa chốt concept → quay lại checkpoint Usecase 1; chỉ cần file assets → Usecase 3.
- Cơ chế khác các usecase khác ở đâu: không vẽ logo; dựng spec JSON từ `templates/presentation-spec.example.json` rồi chạy `presentation_board.py`, điền `templates/brand-guidelines-template.md`, đọc `references/identity-system.md` khi mở rộng.
- Lệnh copy-paste: copy `templates/presentation-spec.example.json` → đặt `"industry"` (vd `coffee`) hoặc list `"mockups"` explicit → `python3 scripts/presentation_board.py spec.json -o board.html` (+ `--png-dir slides` để xuất ảnh share). Liệt kê mockups: `python3 scripts/presentation_board.py --list-mockups` (đã chạy 30/10/2026: 17 mockups, 12 ngành).
- Ngưỡng số cần đạt: 6 mockups đúng ngành (vd café: cup/bag/signage/business-card/social/tote; dev tool: README/terminal); mark đa màu phải truyền `symbol_on_tile`/`lockup_on_dark` (+ `tile_color` tùy chọn) để mockup giữ màu thay vì ép trắng; guidelines đủ clear-space (từ element logo), min-size, mã màu HEX/RGB/CMYK/Pantone, nền duyệt, misuse.
- Ví dụ input-output (minh họa): input concept Kiln đã duyệt + industry `coffee` → output board (brief + từng concept + rationale + mockups cup/bag/signage + so sánh + recommendation) + guidelines 1 trang.
- Pitfalls riêng: mockup sai ngành (lấy mockup software cho café) → pitch trật; build board trước checkpoint → board của concept bị loại, tốn công.
- Phân công usecase này: agent chính điền spec + chạy board + guidelines (mockup list chờ user chốt khi brief thiếu ngành); giao claude mở board HTML trên browser chụp/check; verify bằng board đủ 6 mockups đúng ngành + guidelines đủ mục checklist `references/process.md` §7.

### Các bước chung
1. Chốt brief (tên/audience/3–5 tính từ/đối thủ/clichés off-limits) + ghi assumptions; ít info thì fast-track (tối đa 5 câu 1 tin nhắn, hoặc nêu assumptions rồi đi thẳng 3 concepts).
2. Research thư viện: `search_library.py --industry <closest> --summary` + xem vài file + liệt kê clichés cấm + word map + chọn ≥2 mark types (đối chiếu `references/mark-types.md` §12).
3. Viết 8–12 one-liners (mỗi câu 1 twist ownable; câu nào mô tả được cả đối thủ thì loại), chấm nhanh, chỉ build 3 khác nhau nhất; search subject/technique tránh làm lại mark có sẵn.
4. Build SVG đen trước (symbol `viewBox="0 0 256 256"`, lockup cao 256, góc chuẩn 0/15/30/45/60/90°, lỗ thật `fill-rule="evenodd"`), lưu iteration (`concept-a-v1.svg`...), render PNG và nhìn thật sau mỗi sửa.
5. Test & refine lặp ≥2 vòng (`svg_audit.py` + `preview_sheet.py`): scale 16–24px, optical corrections (overshoot ~1–3%, bone effect, mỏng ngang, centre quang học), letter test, junctions, peer test vs 3–4 exemplary, literalness.
6. Checkpoint: `concept_sheet.py --greyscale` + recommendation trung thực (kèm 1 risk thật mỗi concept) → DỪNG chờ user pick (waiver duy nhất: user nói rõ "don't ask, just deliver", phải quote).
7. Kit sau duyệt: refine + màu (1–2 màu, one-colour/greyscale vẫn chạy) + typo/lockups + board + export + guidelines + checklist `references/process.md` §7.

### Prompt mẫu
- "Thiết kế logo cho Harbor, app tiết kiệm cho người mới lần đầu: calm + safe. Research payments-fintech trong thư viện + liệt kê clichés cấm, viết 8–12 one-liners, build 3 SVG đen, audit + preview ≥2 vòng, trình concept_sheet greyscale + recommend rồi DỪNG chờ tôi pick mới build kit. Không bịa số liệu, không hứa trademark."
- "Critique file logo.svg theo references/critique.md + chạy svg_audit + preview_sheet (--refs-industry developer-tools): liệt kê WARN + score, đề xuất 3 fixes đo được, peer-test vs 3 file exemplary. Chưa redesign khi tôi chưa duyệt."
- "Từ final-symbol.svg đã duyệt, chạy export_variants (--mono #0F7C80 --icon-bg #0F7C80 --web-icons --favicon-source bản small) + board presentation_board industry coffee + guidelines 1 trang. Thiếu renderer PNG thì nói rõ, không claim test đã chạy."

### Pitfalls
- Build kit trước checkpoint → kit của concept bị loại, tốn phần việc lớn nhất; checkpoint là gate chi phí, không phải thủ tục.
- Vẽ SVG mù (không render + mở PNG nhìn) → lọt notch/sliver/lump ở junctions, chữ biến dạng (K đọc thành h) — skill bắt render sau mỗi sửa.
- Live `<text>`, raster nhúng, filter/mask ở file final → audit structure FAIL, không production-ready.
- Copy/trace/imitate thư viện → vi phạm trademark; MIT repo KHÔNG cover 1,432 SVG (xem `TRADEMARKS.md`); familiarity test thấy quen mà không phải của mình thì bỏ.
- Gradient/shadow cứu form yếu; >3 màu không lý do concept; chi tiết <1/48 canvas; hairline/gap khép ở size nhỏ; near-miss 0.3–3°; quá nhiều anchors (median thư viện 75, square 53).
- Bỏ 16px/one-colour/reversed/shelf test → logo chết ở favicon/avatar/khắc dấu.
- Hứa trademark clearance hoặc font license → skill cấm hứa; phải đề nghị tra cứu chuyên nghiệp + khai báo font giả định.
- Concept cần cả đoạn văn mới hiểu → không phải 1 idea, loại.

### Tham khảo sử dụng (số chốt 30/10/2026; review sâu độc lập: chưa xác minh — không bịa)
- Nhận xét sâu: KHÔNG tìm thấy bài critique sâu độc lập (không có HN/ProductHunt/bài review kỹ thuật; Reddit r/BestGitHubRepos + X chỉ là announcement/khen ngắn) → quyết định dùng dựa vào bằng chứng chạy thật ([Cài đặt](#cai-dat-da-clone--chay-thu-scripts-tren-linux-30102026-chua-cai-plugin-marketplace-vi-may-nay-khong-co-claude-code)) + velocity stars, không dựa lời khen. Ghi `chưa xác minh`, cấm suy diễn chất lượng từ buzz.
- Dấu hiệu độc lập có trọng lượng (không phải review sâu, đọc với biashed): Trendshift 25/09–28/10/2026 +4,841★/34 ngày, top-25 HTML nhiều ngày, tuần đầu ~1,400★ (X @StatevergeCN: "最规范的用AI做Logo设计...完全按照专业设计流程" — khen process kỷ luật); SkillsLLM verified (added 27/09/2026, 4,556★ lúc crawl); badge The New 100 #14. → xác nhận viral nhanh + cài được, lật quyết định "repo 1 tháng tuổi chưa kiểm chứng" thành "đáng thử 0đ cho 1 brief thật".
- Bằng chứng chức năng (first-party, không độc lập): 28 brief hư cấu chạy end-to-end trong README gốc (checkpoint greyscale + size thật + recommendation; 4/28 khách pick khác recommend rồi skill refine đúng ý checkpoint) + audit outputs (99/100 recommend vs 76/100 loại).
- Số trung bình có trọng số: 5,320★ / 420 forks / 4 issues mở (API GitHub 30/10/2026). Trọng số: velocity +4,841★/34d đáng tin hơn con số ★ tĩnh; so cùng phân khúc: logocreator 8,898★/829 forks (lớn hơn nhưng khác cơ chế PNG — không suy ra hơn/kém); Skillry per-skill installs 7–27 (nhỏ hơn hàng trăm lần NHƯNG khác mẫu số repo-vs-skill, chỉ so để định vị raster-vs-vector, không kết luận chất lượng).
- Mâu thuẫn: buzz khen process (X/Reddit) vs thiếu critique độc lập sâu → phán quyết: thử 0đ bằng 1 brief thật + tự audit theo checklist, chưa dùng cho brand tiền lớn khi chưa qua trademark search chuyên nghiệp.
- Tiếng Việt: không tìm thấy review Việt → `chưa xác minh`.

### Tham khảo
- Repo + Install + ví dụ 28 brands + audit outputs: https://github.com/kaankiziltug/logo-design-skill (đọc 30/10/2026; MIT; v1.4.5; tạo 26/09/2026; đẩy cuối 20/10/2026).
- Nguồn đã mở kiểm tra: `skills/logo-design/SKILL.md` (7 phase + checkpoint + red flags), `scripts/{search_library,svg_audit,preview_sheet,concept_sheet,presentation_board,render_png,export_variants,build_catalog}.py`, `assets/library/stats.json` (1,432; median anchors 75/53; median màu 2; gradient 19%), `TRADEMARKS.md`, `.claude-plugin/marketplace.json + plugin.json` (v1.4.5).
- Đã chạy xác minh 30/10/2026: `search_library --industry payments-fintech --summary` (37/1432), `svg_audit` hình tròn test (100/100), `export_variants` (6 file), `presentation_board --list-mockups` (17 mockups/12 ngành).
- Số liệu: API GitHub `kaankiziltug/logo-design-skill` + `Nutlope/logocreator` (30/10/2026); Trendshift momentum 25/09–28/10/2026; SkillsLLM verified listing (added 27/09/2026).
- Đối thủ: https://github.com/Nutlope/logocreator (8,898★, Flux diffusion + Together key, SVG export từ ảnh đã có) + `../skillry/` (GPT Image raster, số installs 29/10/2026).

### Được dùng ở đâu
- Dùng CHO media (logo/brand mark/favicons/board): xem `../../domains/media/using-logo-design-skill.md` — index `../../domains/media/README.md`.

### Quay lại index
- Về `../../domains/media/README.md` (so logo vector vs OG raster vs video/deck khi brief có cả nhận diện + trình bày).
- Xem thêm item liên quan: `../skillry/` khi chỉ cần raster nhanh; `../hallmark/` khi cần sweep page theo logo đã chốt.

---

## English

### When to use
- Need a new logo/brand mark (wordmark, monogram, letterform, pictorial, abstract, emblem, mascot, combination) as production-ready vector SVG with numeric tests + full kit, via a disciplined flow (brief → concepts → audit → checkpoint that stops for approval → kit).
- Have an existing logo needing a scorecard critique, an equity-preserving redesign/refresh, or favicon/app-icon/web-icons + one-colour versions from one master SVG.
- Agent supports the open Agent Skills format (Claude Code, Gemini CLI, Codex, Cursor, Copilot, OpenCode...) + Python 3.8+; an image-capable model is recommended so the skill renders PNGs and inspects its drafts before presenting (without one it still runs but must declare it + draw simpler geometry).
- Want to learn category conventions + avoid look-alikes using the classified 1,432-real-logo SVG library (study only).

### When to skip
- Only fast raster output needed (OG/social/decorative avatar), no geometrically-drawn master with audit → use `../skillry/` (GPT Image, packaged taste, see [Sub-usecase 4](../../items/skillry/README.md#sub-usecase-4-og-image--avatar--illustration)) or a diffusion generator (logocreator, needs a paid Together key).
- Launch video/deck → `../skillry/` + `../awesome-opus5-5-videos/`; gated page system → `../hallmark/`; React bricks → `../reactbits/`.
- Legal trademark-clearance commitment needed → hire a professional search/lawyer (the skill disclaims guarantees, see [Pitfalls](#pitfalls)).
- Want to copy/trace library logos → absolutely forbidden (`TRADEMARKS.md`: repo MIT does NOT cover library SVGs).

### Install (cloned + scripts test-ran on Linux 30/10/2026; marketplace plugin not installed — no Claude Code on this machine)
- Route 1 — plugin marketplace (Claude Code, per origin README): `/plugin marketplace add kaankiziltug/logo-design-skill` then `/plugin install logo-design@logo-design-skill`.
- Route 2 — manual (every agent, equivalently ran via `git clone`): `git clone https://github.com/kaankiziltug/logo-design-skill.git`, then copy the skill folder where the agent reads it, e.g. `cp -r logo-design-skill/skills/logo-design ~/.claude/skills/logo-design` (all projects) or `.claude/skills/logo-design` (per project); Gemini CLI: `~/.gemini/skills/logo-design`; Codex CLI: `~/.codex/skills/logo-design`; OpenCode/Cursor/Copilot: project `skills/` folder (full table in origin README). RAN 30/10/2026: `git clone --depth 1` OK, `assets/library/svg/` holds 1,432 files, `scripts/*.py` run with `python3` (stdlib-only).
- Requirements: Python 3.8+ (standard library only); Windows uses `python`/`py -3` instead of `python3`. PNG/SVG→ICO rendering needs one `render_png.py` backend: cairosvg, rsvg-convert, Inkscape, headless Chrome/Chromium, or macOS Quick Look (`--which` lists available backends).
- Verify (ran 30/10/2026, real outputs): `python3 scripts/search_library.py --industry payments-fintech --summary` → `37 logos match (of 1432)` with mark-type/colour/technique tables; `python3 scripts/svg_audit.py test-logo.svg` (black-circle fixture) → `production-readiness score: 100/100`; `python3 scripts/export_variants.py test-logo.svg --mono "#0F7C80" --icon-bg "#0F7C80" --out-dir out --title "Test"` → 6 files (`-black/-white/-mono-0f7c80/-square/-favicon/-app-icon.svg`); `python3 scripts/presentation_board.py --list-mockups` → 17 mockups, 12 industries.

### How the item works
- Backing organization: individual `kaankiziltug`, repo `https://github.com/kaankiziltug/logo-design-skill`, MIT license (code + prose; the 1,432 library SVGs are NOT MIT — see `TRADEMARKS.md`), version 1.4.5, 25 commits since 26/09/2026, last push 20/10/2026. GitHub API 30/10/2026: 5,320 stars / 420 forks / 4 open issues; +4,841 stars in 34 days (Trendshift 25/09–28/10/2026).
- Core operating method: one open-format Agent Skill (`SKILL.md` + 15 on-demand `references/` + 8 Python `scripts/` + `assets/library/` + 2 `templates/`). The agent matches the `SKILL.md` `description` on logo/wordmark/monogram/brand-mark/app-icon/favicon/rebrand/critique triggers, runs the 7-phase workflow (discovery → research → concepts → black-first SVG build → test & refine ≥2 loops → checkpoint that STOPS for approval → kit); every draft is rendered to PNG and inspected before presenting.
- Per-usecase operating differences: new design (full 7 phases + mandatory checkpoint, see [Sub-usecase 1](#sub-usecase-1-new-logo-design--checkpoint--kit)) vs critique/redesign (straight into `references/critique.md`/`redesign.md` + auditing the existing file, see [Sub-usecase 2](#sub-usecase-2-critique--redesign-an-existing-logo)) vs asset export (only `export_variants.py`/`render_png.py` on the approved master, see [Sub-usecase 3](#sub-usecase-3-faviconapp-iconvariants--png-render)) vs board/guidelines (only `presentation_board.py` from a JSON spec + 1-page template, see [Sub-usecase 4](#sub-usecase-4-presentation-board--guidelines--identity)).

### Invariant core
- Mandatory checkpoint: after concepts + tests, present exactly one `concept_sheet.py` image (greyscale + true 64/32/16 px sizes + recommendation), then STOP for the user's direction pick before building the kit (see [Sub-usecase 1](#sub-usecase-1-new-logo-design--checkpoint--kit)). Building the kit pre-approval = no longer using the system.
- Brief + research before building: discovery (name/audience/3–5 adjectives/competitors/off-limits clichés) + `search_library.py --summary` category research + word map + ≥2 mark types tried, 8–12 one-liners with only 3 built (see [Shared steps](#shared-steps)). Drawing SVG before brief/research = FAIL.
- Black first, colour later + audit before presenting: symbol canvas `viewBox="0 0 256 256"`, no `<text>` in final files, `svg_audit.py` + `preview_sheet.py` looped ≥2 times with real PNG inspection (see [Sub-usecase 1](#sub-usecase-1-new-logo-design--checkpoint--kit)). Presenting unaudited/unrendered work = FAIL.
- Library is study-only; copying/tracing/imitating is forbidden (`TRADEMARKS.md` + `SKILL.md` red flags). Shipping a library-derived form = legal FAIL.
- After use, state: which shortlisted concept passed the checkpoint + audit score + what stayed/changed; unable = the system was not really used.

### Customizable surface
- Tunable: brief (name/industry/audience/adjectives), mark type (8 kinds), palette (1–2 colours + mockup `tile_color`), typography (max 2 families), industry mockups (17 kinds), which of the 3 shortlisted concepts, post-critique keep/change list. Two-level approval gate: (1) which artifact — 2–3-concept shortlist with reasons via the question tool, user picks before any kit build (even after a direction was approved, the kit still waits for the concrete artifact pick); (2) what stays/changes — colour/type/mockup deltas settled pre-build. Sole waiver (skipping the checkpoint on explicit "don't ask, just deliver everything") must quote the user's explicit ok, never infer it. Never list `must-not` items (library copying, trademark promises) here.

### Work split
- Main agent: discovery/brief + library research (shortlist 2–3 directions with reasons, wait for user pick — never self-pick then build), SVG builds, audit/preview/render runs + OPENING the PNGs for real inspection, concept-sheet presentation + recommendation, post-approval kit/export/board only, output verification (format/file existence/font license).
- Hand browser/account-dependent steps to claude: reverse-image look-alike checks, trademark-database searches, font-logo-license verification, viewing `preview.html`/`gallery.html`/boards in a browser — with the SVG file + concrete asks; the agent never invents lookup results. If rendering is impossible, the agent must declare it + draw simpler geometry, never claim tests it did not run.
- Agent verifies: `svg_audit.py` with no unexplained WARNs + 16 px size ladder legible + one-colour/reversed/shelf tests passing + kit files present (`-black/-white/-mono/-square/-favicon/-app-icon`, web-icons, board, guidelines).

### Differentiating positioning (GitHub API numbers, 30/10/2026)
- Vs `Nutlope/logocreator` (OSS logo generator, 8,898 stars/829 forks, Flux diffusion on Together AI, MIT): output-mechanism difference — logocreator renders diffusion images in seconds, then exports SVG from the image (the README's SVG-export item is ticked [x]), needs `TOGETHER_API_KEY` (paid inference at Together prices, with price estimate shown) + a `pnpm install && pnpm dev` stack; logo-design-skill draws geometric-code SVG + numeric audits + checkpoint, needing only stdlib Python, zero keys. Pick logo-design-skill over logocreator when a geometrically-drawn master passing 16 px/one-colour/audit is needed (bar: audit ~99/100 like the origin README's recommended file vs 76 for the rejected one) with no paid key/stack; pick logocreator for many fast image options + an existing Together key, accepting diffusion (garbled-letter risk, self-owned discipline tests) + self-owned look-alike checks.
- Vs `../skillry/` image skills (GPT Image diffusion, packaged taste: Notion OG 222 views/7 installs, GrokBot avatar 307/14 on 29/10/2026, $9.99/month + mandatory account): material difference — Skillry ships raster in a packaged taste + previews; logo-design-skill ships vector + audits + kit at $0 MIT, offline-capable. Pick logo-design-skill over Skillry when the decision hinges on a vector master + measurable audit numbers, not packaged taste; pick Skillry for one exact OG/avatar taste with preview, accepting fees + diffusion-garbled text.
- Honest frame: logo-design-skill wins on vector discipline + audits + $0 price; loses on speed (7 phases, human-gated checkpoint) and on decorative raster art (diffusion wins illustration). One fast raster artifact → Skillry/logocreator; one decade master → logo-design-skill.

### Coverage map (full SKILL.md + 8 scripts + 15 references + 2 templates scanned 30/10/2026 — ★ strongest first)
- ★ New-logo full design (7-phase Design + checkpoint + kit): see Sub-usecase 1.
- Critique + redesign of an existing logo (scorecard + equity audit + numeric audit): see Sub-usecase 2.
- Favicon/app-icon/variant export + PNG render (`export_variants.py` + `render_png.py`): see Sub-usecase 3.
- Medium: presentation board + guidelines/identity (`presentation_board.py`, 17 mockups/12 industries + 2 templates) → use when pitching a client, see Sub-usecase 4.
- Medium: standalone library lookup (`search_library.py` all filters + `--summary` + `gallery.html`) → use when studying category conventions/avoiding look-alikes without designing yet (command really ran in [Install](#install-cloned--scripts-test-ran-on-linux-30102026-marketplace-plugin-not-installed--no-claude-code-on-this-machine)).
- NOT supported → replacements: `build_catalog.py` (maintainer catalog/gallery rebuild) → do not use; legal trademark clearance → professional search/lawyer; font-license verification → foundry/font owner; raster video/deck/OG → `../skillry/`; gated page system → `../hallmark/`; React bricks → `../reactbits/`.

### Decision dossier
- Jobs SERVED (3+, concrete): 1. new SVG logo from brief to kit (8–12 one-liners → build 3 → ≥2 audit loops → greyscale checkpoint → colour/lockup/board/icons/guidelines kit); 2. critique/redesign of an existing logo (scorecard + numeric audit + equity audit); 3. favicon/app-icon/web-icons + black/white/mono/square versions from one approved master.
- Jobs NOT served (3+, each with replacement): 1. raster OG/decorative images → `../skillry/` (GPT Image) or logocreator (Flux diffusion, needs Together key); 2. video/deck → `../skillry/` + `../awesome-opus5-5-videos/`; 3. gated page system → `../hallmark/`; 4. legal trademark commitment → professional search/lawyer.
- Free / total + price: 100% free, $0 everything (MIT for code + prose; the 1,432 library SVGs are NOT MIT — study, never copy — sources `LICENSE` + `TRADEMARKS.md`, read 30/10/2026). No subscription, no account, no external model fees (runs locally on Python).
- Install friction: 2 steps (marketplace: 2 `/plugin` commands; manual: `git clone` + 1 `cp -r`). RAN through: depth-1 clone OK + `search_library --summary` (37/1432) + `svg_audit` (100/100) + `export_variants` (6 files) + `presentation_board --list-mockups` (17/12) — real outputs in [Install](#install-cloned--scripts-test-ran-on-linux-30102026-marketplace-plugin-not-installed--no-claude-code-on-this-machine). Barriers: no auth/login/Node/money/admin rights; only Python 3.8+; PNG rendering needs 1 backend (cairosvg/rsvg/Inkscape/Chrome/macOS QL), without which design still works but the missing render must be declared.
- Viral same-segment opponents: `Nutlope/logocreator` (8,898 stars/829 forks, Flux diffusion + BYO Together key with paid inference + pnpm/Node stack, SVG-from-image export shipped) vs `../skillry/` image (GPT Image raster, Notion OG 222/7, GrokBot 307/14, $9.99/month + mandatory account). Measured via GitHub API + logocreator README + skillry pages, 29–30/10/2026.
- Pick it over opponents when: a geometrically-drawn SVG + numeric audit (target ~99/100, 16 px ladder, one-colour, reversed, shelf test) + checkpoint with recommendation + full kit is needed, at $0 MIT with no keys. Choice-flipping example: café brief needing a 1-colour kraft-bag stamp + 16 px favicon, no paid keys wanted → logo-design-skill (SVG + small-size cut + audit); post needing a Notion-style OG image → Skillry; Together key at hand and many fast image options wanted → logocreator.
- NEVER use when: legal trademark commitment is required (the skill forbids promising it); library copying/tracing is wanted (trademark violation); diffusion raster art is wanted (the skill draws geometry, not illustration); no Python 3.8+ available and none installable.

### Sub-usecase 1: new logo design + checkpoint + kit
- When to use: a new brand brief (name/audience/adjectives) needs the full flow through to a kit.
- When to skip: critiquing an existing file → Sub-usecase 2; exporting variants from an approved master → Sub-usecase 3; fast raster → Skillry/logocreator.
- Mechanism difference: the only flow running all 7 phases + the STOP-and-wait checkpoint; other sub-usecases enter dedicated scripts/references with no checkpoint.
- Copy-paste command (checkpoint, run after building + testing 3 symbols + lockups — a lockup is the symbol + wordmark arranged as one horizontal/stacked unit): `python3 scripts/concept_sheet.py a-symbol.svg b-symbol.svg c-symbol.svg --lockups a-lockup.svg b-lockup.svg c-lockup.svg --names "Kiln K" "Grin" "Pendant" --notes "Kiln arch in the K leg" "Citrus wedge as a cheeky grin" "Didone M holding an O pendant" --recommend 1 --greyscale -o concepts.png` (source `SKILL.md` Phase 6; preceding chain: `search_library.py --industry <closest> --summary` → black SVG builds → `svg_audit.py` + `preview_sheet.py` looped ≥2 times).
- Numeric bar: audit with zero unexplained WARNs (target ~99/100 like the origin README's recommended file; the 76/100 file was rejected); idea legible at 16–24 px; gaps/strokes large enough; primary colours contrast-checked (origin examples: sage darkened to reach 3:1, 1.4:1-on-white mint kept to dark surfaces only); shelf test (logo placed next to competitor logos, must not blend in) passes.
- Input-output example (illustrative, not a default — shortlist + user pick comes first): input "Kiln, Istanbul specialty coffee roaster, warm/crafted/modern, for bags/cups/avatar" → output greyscale `concepts.png` (3 concepts + true 64/32/16 px sizes + "Kiln K" recommendation: K leg as kiln arch, audit caught a 60.8° diagonal + off-centre symbol pre-presentation) → user picks → kit (colour/lockups/board/icons/guidelines).
- Own pitfalls: blind SVG drawing without rendering (`render_png.py` + opening the PNG is mandatory after every edit); `<text>` in final files (letterforms must be constructed paths); gradients/shadows rescuing a weak form; >3 colours without a conceptual reason.
- Work split for this sub-usecase: main agent does brief→build→audit→checkpoint presentation (shortlist via question tool, user picks before any kit build); reverse-image + trademark-database checks go to claude; verify via audit score + 16 px ladder + kit files present.

### Sub-usecase 2: critique + redesign an existing logo
- When to use: an existing SVG logo file needs a scorecard critique, or modernising/replacing a logo while keeping equity (equity = the old identity worth keeping: remembered colours/letters/forms).
- When to skip: designing from scratch → Sub-usecase 1; approved file needing only variants → Sub-usecase 3.
- Mechanism difference: no concepts/checkpoint; straight into `references/critique.md` (scorecard + fixes) or `references/redesign.md` (equity audit → refresh techniques), then rejoining Design phases 4–5.
- Copy-paste command: `python3 scripts/svg_audit.py my-logo.svg` and `python3 scripts/preview_sheet.py my-logo.svg --refs-industry developer-tools -o preview.html` (sources `SKILL.md` Phase 5 + Tools table).
- Numeric bar: audit lists concrete anchors vs library medians (75 overall / 53 square), 0.3–3° near-misses, sub-1/48-canvas tiny details, colour/gradient counts, contrast; critique yields a scorecard + 3 measurable fixes; redesign passes an equity audit (what stays/goes) before redrawing.
- Input-output example (real, from origin README): input two files `a-lockup.svg` + `b-emblem.svg` → output audit `a-lockup` 99/100 (205 anchors, complexity INFO) recommended; `b-emblem` 76/100 (374 anchors above 95% of sample, 8 near-misses, 6 tiny details) not recommended.
- Own pitfalls: the audit is advice, not law — overriding a WARN is allowed but must be justifiable; critique is not redesign (redrawing without an equity audit destroys equity).
- Work split for this sub-usecase: main agent runs audit/preview + scorecard + fix proposals (waits for approval before redrawing); claude cross-checks 3–4 exemplary library files (`--exemplary --format paths`) + peer test; verify via post-fix audit + re-reading at 16 px/mirrored/rotated-180°.

### Sub-usecase 3: favicon/app-icon/variants + PNG render
- When to use: a CHECKPOINT-APPROVED master SVG needs deliverables (one-colour, square, favicon, app-icon, web-icons, exact-size PNGs).
- When to skip: no approved master yet → Sub-usecases 1/2 first; client pitch board needed → Sub-usecase 4.
- Mechanism difference: no designing, no idea audit; pure master-file transformation via `export_variants.py`/`render_png.py`.
- Copy-paste command (equivalently ran 30/10/2026): `python3 scripts/export_variants.py final-symbol.svg --title "Brand logo" --mono "#0F7C80" --icon-bg "#0F7C80" --web-icons --favicon-source final-symbol-small.svg` and `python3 scripts/render_png.py my-logo.svg --size 512 -o my-logo.png` (sources `SKILL.md` Phase 7 + Tools table).
- Numeric bar: full `-black/-white/-mono-<hex>/-square/-favicon/-app-icon.svg` set + `--web-icons` (favicon.ico 16/32/48, PNGs 180/192/512, maskable, manifest, head snippet); dedicated small-size cut (`--favicon-source`) when the master breaks at 16 px; exact-size PNGs, transparent background.
- Input-output example (real, ran 30/10/2026): input black-circle fixture + `--mono "#0F7C80" --icon-bg "#0F7C80"` → output 6 SVGs in `out/` (`test-logo-black/white/mono-0f7c80/square/favicon/app-icon.svg`).
- Own pitfalls: missing render backend means no PNG/ICO — must be declared, never claim tested output; never call `qlmanage` directly (crops non-square SVGs, shrinks width/height files, drops transparency — use `render_png.py`).
- Work split for this sub-usecase: main agent runs export/render + file-existence check + opens PNGs; browser-based board/preview viewing goes to claude if needed; verify via `ls` of all 6 variants + web-icons + correct PNG sizes.

### Sub-usecase 4: presentation board + guidelines + identity
- When to use: an approved concept needs a client pitch (industry-correct mockups) + 1-page guidelines + identity extension (sub-brands/patterns/motion).
- When to skip: concept not settled → back to the Sub-usecase 1 checkpoint; only asset files needed → Sub-usecase 3.
- Mechanism difference: no logo drawing; build a JSON spec from `templates/presentation-spec.example.json`, run `presentation_board.py`, fill `templates/brand-guidelines-template.md`, read `references/identity-system.md` for extension.
- Copy-paste command: copy `templates/presentation-spec.example.json` → set `"industry"` (e.g. `coffee`) or an explicit `"mockups"` list → `python3 scripts/presentation_board.py spec.json -o board.html` (+ `--png-dir slides` for shareable images). Mockup listing: `python3 scripts/presentation_board.py --list-mockups` (ran 30/10/2026: 17 mockups, 12 industries).
- Numeric bar: 6 industry-correct mockups (e.g. café: cup/bag/signage/business-card/social/tote; dev tool: README/terminal); multi-colour marks must pass `symbol_on_tile`/`lockup_on_dark` (optional `tile_color`) so mockups keep colours instead of forcing white; guidelines cover element-derived clear space, minimum sizes, HEX/RGB/CMYK/Pantone codes, approved backgrounds, misuse.
- Input-output example (illustrative): input approved Kiln concept + industry `coffee` → output board (brief + each concept + rationale + cup/bag/signage mockups + comparison + recommendation) + 1-page guidelines.
- Own pitfalls: wrong-industry mockups (software mockups for a café) mistarget the pitch; building the board pre-checkpoint wastes work on rejected concepts.
- Work split for this sub-usecase: main agent fills the spec + runs the board + guidelines (mockup list confirmed with the user when the brief lacks an industry); claude opens the board HTML in a browser to check/capture; verify via 6 industry-correct mockups + full `references/process.md` §7 checklist.

### Shared steps
1. Settle the brief (name/audience/3–5 adjectives/competitors/off-limits clichés) + record assumptions; low-info fast track (max 5 questions in one message, or state assumptions and go straight to 3 concepts).
2. Research the library: `search_library.py --industry <closest> --summary` + read a few files + list forbidden clichés + word map + pick ≥2 mark types (`references/mark-types.md` §12).
3. Write 8–12 one-liners (each with an ownable twist; drop any sentence that could also describe a competitor), score quickly, build only the 3 most different; search subject/technique to avoid rebuilding an existing mark.
4. Build black-first SVG (symbol `viewBox="0 0 256 256"`, lockup height 256, exact 0/15/30/45/60/90° angles, real `fill-rule="evenodd"` holes), version iterations (`concept-a-v1.svg`…), render PNG and inspect after every edit.
5. Test & refine ≥2 loops (`svg_audit.py` + `preview_sheet.py`): 16–24 px scale, optical corrections (~1–3% overshoot, bone effect, thinner horizontals, optical centring), letter test, junctions, peer test vs 3–4 exemplaries, literalness.
6. Checkpoint: `concept_sheet.py --greyscale` + honest recommendation (one real risk per concept) → STOP for the user pick (sole waiver: explicit user "don't ask, just deliver", quoted).
7. Post-approval kit: refine + colour (1–2 colours, one-colour/greyscale must still work) + typography/lockups + board + export + guidelines + `references/process.md` §7 checklist.

### Sample prompts
- "Design a logo for Harbor, a savings app for first-time savers: calm + safe. Research payments-fintech in the library + list forbidden clichés, write 8–12 one-liners, build 3 black SVGs, audit + preview ≥2 loops, present a greyscale concept_sheet + recommendation, then STOP for my pick before any kit. No invented numbers, no trademark promises."
- "Critique logo.svg per references/critique.md + run svg_audit + preview_sheet (--refs-industry developer-tools): list WARNs + score, propose 3 measurable fixes, peer-test vs 3 exemplary files. No redesign until I approve."
- "From approved final-symbol.svg, run export_variants (--mono #0F7C80 --icon-bg #0F7C80 --web-icons --favicon-source the small cut) + a coffee-industry presentation_board + 1-page guidelines. Missing PNG renderer → say so, never claim tests you did not run."

### Pitfalls
- Building the kit pre-checkpoint → kitting a rejected concept wastes the biggest work chunk; the checkpoint is a cost gate, not ceremony.
- Blind SVG drawing (no render + PNG inspection) → junction notches/slivers/lumps and deformed letters (K reading as h) slip through — render after every edit.
- Live `<text>`, embedded rasters, filters/masks in final files → structure audit FAIL, not production-ready.
- Copying/tracing/imitating the library → trademark violation; repo MIT does NOT cover the 1,432 SVGs (see `TRADEMARKS.md`); a familiarity test that feels familiar-but-not-yours means dropping the concept.
- Gradients/shadows rescuing a weak form; >3 colours without a conceptual reason; sub-1/48-canvas details; hairlines/gaps closing at small sizes; 0.3–3° near-misses; excessive anchors (library medians 75, 53 square).
- Skipping 16 px / one-colour / reversed / shelf tests → dead logo at favicon/avatar/emboss sizes.
- Promising trademark clearance or font licensing → forbidden; recommend professional search + declare assumed fonts.
- A concept needing a paragraph to understand → not one idea, drop it.

### Usage references (numbers pinned 30/10/2026; independent deep review: unverified — never guessed)
- Deep review: NO independent in-depth critique found (no HN/ProductHunt/technical review; Reddit r/BestGitHubRepos + X posts are announcements/short praise) → usage decisions rest on first-hand runs ([Install](#install-cloned--scripts-test-ran-on-linux-30102026-marketplace-plugin-not-installed--no-claude-code-on-this-machine)) + star velocity, never on buzz. Recorded as `unverified`; anonymous/unsourced praise excluded.
- Weighty independent signals (not deep reviews, read with bias): Trendshift 25/09–28/10/2026 +4,841 stars/34 days with repeated HTML top-25 ranks, ~1,400 stars in week one (X @StatevergeCN: "the most disciplined AI logo-design flow … fully following the professional process" — short praise, not a critique); SkillsLLM verified listing (added 27/09/2026, 4,556 stars at crawl); The New 100 badge #14. → confirms fast virality + installability, flipping "one-month-old repo, unverified" to "worth a $0 trial on one real brief".
- Functional evidence (first-party, not independent): 28 fictional end-to-end briefs in the origin README (greyscale checkpoint + true sizes + recommendation; clients picked against the recommendation in 4/28 and the skill refined the pick — the checkpoint working as designed) + audit outputs (99/100 recommended vs 76/100 rejected).
- Weighted average: 5,320 stars / 420 forks / 4 open issues (GitHub API 30/10/2026). Weight: +4,841/34d velocity is more trustworthy than the static star count; same-segment comparison: logocreator 8,898 stars/829 forks (bigger but a different PNG mechanism — no better/worse inference); Skillry per-skill installs 7–27 (hundreds of times smaller BUT a repo-vs-skill denominator mismatch — used only for raster-vs-vector positioning, never a quality verdict).
- Conflict: process praise (X/Reddit buzz) vs zero independent deep critique → verdict: trial at $0 on one real brief + self-audit per checklist; no big-money brand use before professional trademark search.
- Vietnamese: no Vietnamese review found → `unverified`.

### References
- Repo + install + 28-brand examples + audit outputs: https://github.com/kaankiziltug/logo-design-skill (read 30/10/2026; MIT; v1.4.5; created 26/09/2026; last push 20/10/2026).
- Sources opened and checked: `skills/logo-design/SKILL.md` (7 phases + checkpoint + red flags), `scripts/{search_library,svg_audit,preview_sheet,concept_sheet,presentation_board,render_png,export_variants,build_catalog}.py`, `assets/library/stats.json` (1,432; median anchors 75/53; median colours 2; 19% gradients), `TRADEMARKS.md`, `.claude-plugin/marketplace.json + plugin.json` (v1.4.5).
- Verification runs 30/10/2026: `search_library --industry payments-fintech --summary` (37/1432), `svg_audit` circle fixture (100/100), `export_variants` (6 files), `presentation_board --list-mockups` (17 mockups/12 industries).
- Numbers: GitHub API `kaankiziltug/logo-design-skill` + `Nutlope/logocreator` (30/10/2026); Trendshift momentum 25/09–28/10/2026; SkillsLLM verified listing (added 27/09/2026).
- Opponents: https://github.com/Nutlope/logocreator (8,898 stars, Flux diffusion + Together key, SVG-from-image export shipped) + `../skillry/` (GPT Image raster, install counts 29/10/2026).

### Where used
- Used in `domains/media/`: see `../../domains/media/using-logo-design-skill.md` (logo/brand-mark/favicons/boards).

### Back to index
- Back to `../../domains/media/README.md` (vector logo vs raster OG vs video/deck when a brief spans identity + presentation).
- Related items: `../skillry/` for fast raster only; `../hallmark/` for sweeping pages to a settled logo.
