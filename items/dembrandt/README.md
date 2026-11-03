# dembrandt

## Tiếng Việt

### Dùng khi
- Cần đọc design system thật của 1 website đang sống (mình sở hữu/có cho phép/học nội bộ) ra tokens đo được: colors + vai trò/confidence, typography, spacing, borders, shadows, motion, components, breakpoints — trong vài chục giây, không DevTools thủ công.
- Cần file máy đọc được để agent/build tiếp: JSON, W3C DTCG (Design Tokens Community Group — chuẩn tokens chung) (`--dtcg`), `DESIGN.md`, Tailwind v4 `@theme`, shadcn theme, HTML report, brand-guide PDF, screenshot.
- Cần gate chống drift trong CI: pin baseline JSON, `--compare` exit 1 khi tokens trôi, PR annotations, snapshot timeline trên App.
- Cần audit contrast WCAG trên cặp DOM thật (kể cả hover/focus/disabled), hoặc crawl nhiều trang gộp confidence (`--crawl`, `--sitemap`).

### Bỏ qua khi
- Cần system/design mới pass gates đo được từ 0 (contrast/focus/fold) → dùng `../hallmark/` (dembrandt chỉ đo cái đã render, không sinh system/gates).
- Cần rebuild full app 1:1 thành Next.js editable (routes/components/logic) → dùng `../ai-website-cloner-template/` (dembrandt chỉ ra tokens, không ra app).
- Cần 1 effect/component React lẻ sở hữu source → dùng `../reactbits/`.
- Cần landing taste đóng gói chạy ngay → dùng `../skillry/` (phần web).
- Muốn extract site KHÔNG sở hữu/không được phép, ToS cấm automated access, phishing/giả mạo, bê logo/brand người khác ra sản phẩm → cấm tuyệt đối (xem [Cốt lõi bất biến](#cot-loi-bat-bien)).

### Cài đặt (đã verify registry + `--help` chạy thật trên Linux 02/11/2026; extraction full chưa chạy vì kẹt tải Chromium)
- Cài CLI: `npm i -g dembrandt` (nguồn `docs/getting-started`, README gốc). Yêu cầu Node.js ≥18 (nguồn `registry engines` 02/11/2026: `node >=18.0.0`).
- Bắt buộc 1 lần: `dembrandt install-browser` (mặc định chromium; `dembrandt install-browser firefox` cho site Cloudflare/bot). Lý do: dembrandt phụ thuộc `playwright-core` gọn nhẹ, KHÔNG kèm browser binary — không chạy bước này thì lần extract đầu dừng ở `browser engine not available`. Trên Linux/CI cài thêm system libs: `npx playwright@$(node -p "require('playwright-core/package.json').version") install --with-deps chromium`.
- Kiểm tra đã chạy 02/11/2026: `npm view dembrandt version` → `0.39.2`; `timeout 60 npx -y dembrandt@0.39.2 --help` → exit 0, đủ 3 nhóm flags (Extraction / Output & export / Analysis / Network & auth) khớp từng chữ `docs/usage.md`. Lệnh extract thật `npx -y dembrandt@0.39.2 https://example.com --json-only` đã khởi động (`Starting extraction...`) rồi kẹt ở `Installing Playwright chromium for playwright-core 1.63.0...` quá timeout 60s — đúng ma sát đã document, không phải lỗi lệnh.
- Dùng không cài: `npx dembrandt dembrandt.com` (vẫn phải `npx dembrandt install-browser` trước 1 lần; cache Playwright dùng chung).
- Skills (UX intelligence phủ lên tokens): `npx skills add dembrandt/dembrandt-skills --all` (43/45 skills chạy không cần engine; 2 skills `extract-design` + `generate-ui-from-brand` cần engine ≥0.39.0 — nguồn README skills repo). MCP: `claude mcp add --transport stdio dembrandt -- npx -y dembrandt mcp` hoặc `.mcp.json` (`command: npx`, `args: [-y, dembrandt, mcp]`); server đã list trong MCP Registry là `io.github.dembrandt/dembrandt`.
- CI drift gate: `dembrandt/dembrandt@v0.39.2` (`url` + `baseline: .dembrandt/baseline.json`), fail job khi drift; runner khác dùng exit code: `dembrandt URL --compare baseline.json --json-only` (exit 1 khi drift, exit 2 khi baseline không đọc được).

### Cách item hoạt động
- Tổ chức đứng sau: cá nhân `@dembrandt` (designer + dev 15 năm UX/front-end), repo `https://github.com/dembrandt/dembrandt`, license MIT, 394 commits (trang repo 02/11/2026), 79 versions npm (tạo 23/11/2025 → `0.39.2` ngày 11/10/2026), TypeScript + `playwright-core` + `@modelcontextprotocol/sdk`. Số liệu API GitHub ngày 02/11/2026: 3.902★ / 336 forks / 9 watchers / 4 open issues, push 01/11/2026. Registry npm 02/11/2026: bins `dembrandt` + `dembrandt-mcp`, deps `ora/zod/chalk/commander/playwright-core/@modelcontextprotocol/sdk`, engines `node >=18.0.0`. Repo skills riêng `https://github.com/dembrandt/dembrandt-skills` MIT, 179★/22 forks, 246 commits, push 01/11/2026, 45 skills (verify qua GitHub API `contents/skills` = list 45).
- Phương thức hoạt động chung: mở URL trong browser thật (Chromium/Firefox qua Playwright, viewport mặc định 1920×1080, `--mobile` = 390×844), đọc computed styles + CSS variables của DOM đã render, phân tích usage/confidence (màu dùng ở interactive chính → high, generic → low, lọc khỏi terminal nhưng giữ đủ trong JSON), nhóm typography, phát hiện spacing scale, motion, states; trả tokens + evidence. Không đọc spec/TOKENS có sẵn — đo production đang render, nên bắt được lệch spec-vs-ship. Mỗi run mặc định chỉ in terminal; muốn file phải thêm flag (`--save-output`, `--dtcg`, `--design-md`, `--tailwind`, `--shadcn`, `--html`, `--brand-guide`, `--screenshot`). JSON luôn mang đủ hex/rgb/lch/oklch mọi màu bất kể `--color-format` (flag này chỉ đổi cách in terminal, CLI warn khi kết hợp với export).
- Khác biệt vận hành theo usecase: extract 1 URL (1 pass, terminal/JSON, xem [Usecase con 1](#usecase-con-1-extract-1-url-ra-tokens)) khác crawl nhiều trang (merge + cross-page confidence, xem [Usecase con 2](#usecase-con-2-crawl-nhieu-trang-gop-confidence)) khác drift gate CI (so baseline, exit code, annotations, App snapshots, xem [Usecase con 3](#usecase-con-3-drift-gate-ci)) khác WCAG + export cho agent (đọc cặp DOM thật + ghi theme/DESIGN.md/PDF, xem [Usecase con 4](#usecase-con-4-wcag--export-cho-agent)).

### Cốt lõi bất biến
- Quyền trước URL: chỉ extract site mình sở hữu/có cho phép bằng văn bản/mục đích học nội bộ không ship; site ToS cấm automated access thì dừng; tôn trọng robots.txt + rate limit. Vi phạm = không còn dùng hệ (FAIL pháp lý). Sau khi dùng phải nêu được quyền gì (sở hữu/cho phép/học) + ToS/robots đã check. Không dùng output tái tạo trademark/logo/brand người khác (repo `Intended Use`).
- Observed-only, cấm bịa tokens: mọi token phải từ DOM render đo được (có evidence + confidence); Tailwind/shadcn export CHỈ ghi slots quan sát được, thiếu thì để default + liệt kê trong header, cấm padding shade ramps/scale suy diễn; section không evidence thì lược bỏ (vd elevation khi site không dùng box-shadow), cấm điền default cho đầy. Substitute cùng tên khác metrics = FAIL.
- Baseline-gate cho drift: drift chỉ tính khi so với baseline JSON đã pin (`--compare`); exit 1 = drift, exit 2 = baseline lỗi — cấm kết luận drift bằng mắt. Không nêu được baseline + `changes[]` + exit code = chưa thực sự dùng hệ.

### Phần tùy chỉnh
- Được đổi: URL/paths nào in-scope (`<url> [/pricing /docs]`), crawl mấy trang (`--crawl N`, `--sitemap`, DOM-links vs sitemap), viewport nào (`--mobile` 390×844, `--screen-size`, `--dark-mode`), notation màu in terminal (`--color-format hex|rgb|oklch|lch|source` — oklch là không gian màu mặc định của Tailwind v4), format export (`--dtcg`, `--design-md`, `--tailwind [path]`, `--shadcn [path]`, `--html`, `--brand-guide`, `--screenshot`, `--raw-colors`, `--json-only`/`--save-output`), auth (`--cookie/--cookie-file/--basic-auth/--header`, `--login` + `--save-storage-state`), fingerprint (`--user-agent/--locale/--timezone/--accept-language`), engine (`--browser chromium|firefox`, CDP — Chrome DevTools Protocol qua `BROWSER_CDP_ENDPOINT`, `--no-sandbox`, `--slow`), ngưỡng gate (`--tokens <file> --max-off-token N --tokens-report --annotations github|azure --approve`), AI brand-primary (`--ai`, cần `onnxruntime-node`), cloud sync (`--key dmb_···`). Cổng duyệt 2 tầng: (1) artifact nào — shortlist URLs/paths + format export + multi-page vs single kèm lý do qua question tool, user pick mới chạy (crawl nhiều trang + browser loops tốn thời gian/tiền CI — log scope đã duyệt TRƯỚC khi chạy); (2) giữ/đổi gì — diff nào accept baseline (`--approve`), gap nào giữ lại. Waiver (bỏ compare, ship thẳng; dùng `--stealth` anti-detection; extract site nhạy cảm) phải quote câu ok tường minh của user. Cấm đưa `must-not` (extract không quyền, phishing, hứa tokens đầy đủ khi chưa đo) vào danh sách tùy chỉnh.

### Phân công ai làm gì
- Agent chính: check quyền/ToS + robots trước mỗi URL + shortlist scope/format (chờ user pick — cấm tự chốt URL rồi extract), chạy CLI/MCP (`dembrandt <url> [flags]`, `get_design_tokens` → `job_id` → `get_job_status` → `export_dtcg`/`generate_design_md`), trình tokens + evidence + diff/drift + WCAG, xin duyệt `--approve` khi cần; verify JSON/DTCG files tồn tại + exit code + annotations + App snapshot (khi sync).
- Giao cho claude các bước cần browser ngoài/người thật: `--login` interactive (mở browser visible sign-in, user bấm Enter — CLI-only, agent cấm tự làm), quan sát/chụp visual diff khi cần mắt người, reverse-check đụng trademark khi học — kèm URL + states + yêu cầu cụ thể; cấm agent tự bịa observation. Không có browser/engine thì agent phải khai báo + dừng ở mức docs (cấm claim đã extract).
- Agent verify: file output tồn tại (`output/<domain>/TIMESTAMP.json|.tokens.json|DESIGN.md|theme.css|shadcn.css|*.html|*.pdf`) + nội dung chỉ observed slots + exit code đúng (0 clean / 1 drift / 2 baseline lỗi) + WCAG grades trên cặp DOM thật + routes/pages đã crawl đủ.

### Định vị khác biệt (số liệu ngày 02/11/2026 trừ khi ghi khác)
- So với `Manavarya09/design-extract` (designlang, npm `designlang@13.3.2`): GitHub 4.448★/382 forks (API 02/11/2026) vs dembrandt 3.902★/336 forks — designlang NHIỀU ★ hơn; nhưng npm last-month (30/09–29/10/2026) dembrandt 20.389 vs designlang 4.597 — dembrandt gấp 4,4× installs thật. Khác outputs: designlang ra thêm shadcn theme, Figma variables + plugin, typed React stubs, tokens iOS/Android/Flutter, 4 viewports responsive; dembrandt gọn + mạnh ở drift CI (`--compare` + Action + App snapshot timeline + Slack/Linear alerts) + brand-guide PDF + HTML report. Chọn dembrandt thay vì designlang khi cần tokens Tailwind + drift gate CI + PDF/HTML trong 1 CLI gọn, installs/tháng cao hơn; chọn designlang khi cần shadcn/Figma/mobile-native một pass, chấp nhận command list dài + npm release có thể sau repo (blog 15/09/2026 cảnh báo pin version).
- So với `arvindrk/extract-design-system` (npm `extract-design-system@0.1.11`, 801/tháng 30/09–29/10/2026; 218★ 15/09/2026 theo blog Manav): khác tầng — nó GỌI dembrandt CLI làm extraction (chất lượng extract = dembrandt), cộng thêm normalize + lệnh `audit` check code mình theo tokens + skill-first (`npx skills add`, `audit --fail` gate CI) + MCP. Chỉ đọc public single-page (không login/multi-page như dembrandt cookies/headers + crawl). Chọn dembrandt thay vì extract-design-system khi cần multi-page/auth/browser chọn engine/CDP + exports đầy đủ (DTCG/DESIGN.md/Tailwind/shadcn/PDF/HTML); chọn extract-design-system khi muốn starter `tokens.json` + `tokens.css` drop thẳng vào project + audit code mình, chấp nhận single public page.
- So với `../hallmark/` (system + gates trong repo này): dembrandt ĐO cái đã render (observed tokens + evidence + drift), hallmark SINH system mới pass gates. Quyết định: cần audit/tokens/drift của site có sẵn (có quyền) → dembrandt; cần system mới đạt chuẩn đo được → hallmark; tokens dembrandt extract về muốn thành system chuẩn thì sweep lại bằng hallmark. So với `../ai-website-cloner-template/`: cloner rebuild full app Next.js (Map→Observe→Build→Compare + Opus tokens, chậm/đắt); dembrandt chỉ ra tokens (~10s, 0đ) — cần app chạy được → cloner, cần tokens + gate → dembrandt.
- Khung trung thực: dembrandt thắng ở tốc độ + đo thật + enforce CI + exports chuẩn (DTCG/DESIGN.md/Tailwind/shadcn); thua ở tính đầy đủ outputs so với designlang (không shadcn file riêng đầy đủ? có `--shadcn` observed-slots-only — thua ở Figma/native/stubs), thua ở tính nguyên bản (đo copy, không system/gates như hallmark) + phạm vi pháp lý hẹp (quyền/ToS/robots/trademark) + limits đã document (không auto dark-mode, states từ CSS không phải interaction thật, không canvas/WebGL, site JS nặng cần `--slow`/hydration 8s+4s).

### Bản đồ phủ usecase (quét HẾT README + `docs/usage.md` + `docs/ci.md` + `docs/mcp.md` + `docs/recipes.md` + `docs/FLAGS.md` + skills repo 02/11/2026 — ★ mạnh nhất đầu)
- ★ Extract 1 URL ra tokens quan sát được (JSON/DTCG/DESIGN.md): xem Usecase 1.
- Crawl/sitemap nhiều trang gộp confidence + merge paths: xem Usecase 2.
- Drift gate CI (`--compare`/`--approve`/`--tokens`/`--annotations`, Action, App snapshots): xem Usecase 3.
- WCAG contrast cặp DOM thật + states: xem Usecase 4 (gộp export Tailwind/shadcn/brand-guide/HTML/screenshot cho agent).
- Trung bình: MCP server (`dembrandt mcp`, tools `get_design_tokens/get_color_palette/get_typography/get_component_styles/get_surfaces/get_spacing/get_brand_identity` + pure tools `compute_drift/get_findings/export_dtcg/generate_design_md/render_report` + job tools, registry `io.github.dembrandt/dembrandt`) → dùng khi agent cần gọi extraction như tool thay vì CLI.
- Trung bình: skills `dembrandt-skills` (45 skills: orchestrator 6-stage + `extract-design` pipeline + `generate-ui-from-brand` + 39 UX: hierarchy/a11y/states/polish) → dùng khi cần judgment UX phủ lên tokens (review, palette thuật toán, type scale, density, flows).
- Trung bình: auth pages (`--cookie/--cookie-file/--basic-auth/--header`, `--login` + `--save-storage-state`), fingerprint (`--user-agent/--locale/--timezone/--accept-language`), engine/CDP (`--browser firefox`, `BROWSER_CDP_ENDPOINT`, `--no-sandbox`, `--slow`), `--ai` ML brand-primary (cần `onnxruntime-node`, experimental), `--key` cloud sync App.
- KHÔNG hỗ trợ → thay thế: auto dark-mode (phải `--dark-mode`, không tự detect) → tự chạy 2 lần light/dark; interaction states cần pointer-path/timer (chỉ sample CSS) → test tay; canvas/WebGL (không DOM) → không hệ nào (ghi nhận); content hydrate muộn/dynamic miss → `--slow` + crawl thêm, vẫn miss thì ghi gaps; backend/logic/authz sau site → tự implement; pháp lý/ToS → tự kiểm tra + xin quyền (không hệ nào thay); system mới/gates → `../hallmark/`; rebuild app → `../ai-website-cloner-template/`; bricks React → `../reactbits/`; taste đóng gói → `../skillry/`.

### Hồ sơ quyết định
- Việc DÙNG (4+, cụ thể): 1. audit/extract tokens site mình sở hữu ra JSON/DTCG/DESIGN.md trong ~10s thay vì 1-3h DevTools; 2. pin baseline + `--compare` gate CI/PR annotations + App snapshot timeline + Slack alerts; 3. WCAG audit cặp text/background DOM thật kèm hover/focus/disabled; 4. seed Tailwind v4 `@theme`/shadcn observed-slots/DESIGN.md cho agent build tiếp.
- Việc KHÔNG DÙNG (3+, mỗi việc kèm hệ thay thế): 1. system/design mới pass gates → dùng `../hallmark/`; 2. rebuild app Next.js editable nhiều routes → dùng `../ai-website-cloner-template/`; 3. bricks animated React → dùng `../reactbits/`; 4. landing taste đóng gói nhanh → dùng `../skillry/` (phần web); 5. extract hàng loạt không quan tâm UI → dùng firecrawl/API; 6. extract không quyền/ToS cấm/phishing → không dùng hệ nào (cấm).
- Free / tổng + giá: CLI + skills MIT 0đ toàn bộ (nguồn `LICENSE` 2 repo + `npm view` 02/11/2026). App Beta hiện free (sign-in GitHub, `--key dmb_···` sync; sponsorship nuôi enforcement layer — nguồn README Sponsors). Không subscription cho extract local; phí ngoài duy nhất: infra CI/browser time tự trả + `onnxruntime-node` tùy chọn cho `--ai`. Giá App tương lai `chưa xác minh`, cấm đoán.
- Ma sát cài đặt: 3 bước (`npm i -g dembrandt` → `dembrandt install-browser` → `dembrandt <url>`), hơn chuẩn 1 dòng (`npx skills add ...`) 2 bước. ĐÃ chạy: `npm view` (v0.39.2, engines, bins, 79 versions) + `--help` exit 0 khớp `docs/usage.md` + extract thật khởi động rồi kẹt tải Chromium `playwright-core 1.63.0` (đúng ma sát đã document). Rào cản: Node 18+; browser tải riêng (~trăm MB) + Linux cần `--with-deps`; `--login` cần terminal interactive (CI dùng `--cookie-file` storageState thay); site Cloudflare/bot → `--browser=firefox`; site nặng → `--slow`.
- Đối thủ viral cùng phân khúc: `Manavarya09/design-extract` (4.448★/382 forks API 02/11/2026; npm `designlang@13.3.2` 4.597/tháng) vs `arvindrk/extract-design-system` (npm `0.1.11` 801/tháng; 218★ 15/09/2026). Số npm 30/09–29/10/2026 + GitHub API 02/11/2026.
- Chọn nó thay vì đối thủ khi: cần 1 CLI gọn đo thật + DTCG/DESIGN.md/Tailwind/shadcn/PDF/HTML + drift CI/Action/App trong ~10s, installs/tháng gấp 4,4× designlang. Ví dụ đổi lựa chọn: audit tokens + gate CI cho Tailwind → dembrandt; cần shadcn/Figma variables/stubs React/native một pass → designlang; cần starter tokens drop vào project + audit code mình → extract-design-system.
- TUYỆT ĐỐI không dùng khi: không quyền/ToS cấm/robots cấm; phishing/giả mạo/bê brand-logo người khác; canvas/WebGL-only (không DOM để đọc); cần system mới pass gates mà chỉ extract (đo ≠ sinh); agent không có browser mà vẫn claim đã extract (observation bịa = FAIL).

### Usecase con 1: extract 1 URL ra tokens
- Khi dùng: có 1 URL (quyền đã xác minh) cần tokens quan sát được + evidence trong ~10s.
- Khi bỏ qua: nhiều trang → Usecase 2; gate CI → Usecase 3; cần WCAG/export agent → Usecase 4; cần app chạy được → cloner; cần system mới → hallmark.
- Cơ chế khác các usecase khác ở đâu: duy nhất 1 pass terminal/JSON, không merge cross-page, không baseline, không gate; các usecase khác cộng thêm merge/drift/WCAG-exports.
- Lệnh copy-paste: `dembrandt dembrandt.com --json-only` (in JSON ra stdout, không ghi file; nguồn `docs/usage.md` + `--help` đã chạy). Ghi file: `dembrandt dembrandt.com --save-output` (→ `output/dembrandt.com/<timestamp>.json`); chuẩn W3C: `dembrandt dembrandt.com --dtcg` (→ `*.tokens.json`).
- Ngưỡng số cần đạt: JSON tồn tại + đủ 8 nhóm (colors/typography/spacing/borders/shadows/motion/components/breakpoints) ở mức site có; colors có semantic roles + confidence (high/medium in terminal, full trong JSON); typography có fonts/sizes/weights/sources/file URLs; motion có duration/easing/per-context deltas; unobserved slots lược bỏ có liệt kê, cấm padding bịa.
- Ví dụ input-output (minh họa, không phải mặc định — URL/scope + format do user pick trước): input "audit tokens homepage công ty mình (sở hữu đã xác minh), scope 1 URL, format JSON + DTCG" → output `output/acme/<ts>.json` + `*.tokens.json` + terminal `✓ 10 colors, 44 text styles...` (dạng như getting-started) + list gaps (dark-mode chưa đo, canvas hero bỏ qua — nêu rõ).
- Pitfalls riêng: tưởng terminal đầy đủ = full (terminal chỉ high/medium, JSON mới đủ — mở JSON verify); `--color-format` chỉ đổi cách in, JSON không đổi (CLI warn khi mix với export); `.png` logo có thể là AVIF/raster khác (verify content-type/dimensions); site JS nặng hydrate 8s+4s — miss content thì `--slow` + ghi gaps, cấm claim đủ.
- Phân công usecase này: agent chính check quyền/ToS + shortlist URL/format (user pick — cấm tự chốt rồi extract) + chạy CLI + trình tokens/evidence; giao claude khi cần browser visible/`--login`/visual diff mắt người; verify bằng file JSON/DTCG tồn tại + observed-only + gaps.

### Usecase con 2: crawl nhiều trang gộp confidence
- Khi dùng: 1 trang chưa đủ hệ (tokens theo trang lệch nhau), cần cross-page confidence + phát hiện drift giữa pages.
- Khi bỏ qua: 1 URL đủ → Usecase 1; gate theo thời gian → Usecase 3.
- Cơ chế khác các usecase khác ở đâu: duy nhất merge N pages + confidence theo số trang xuất hiện (token càng nhiều trang càng cao); UC1 single-pass, UC3 so theo thời gian với baseline, UC4 đọc sâu states/exports.
- Lệnh copy-paste: `dembrandt dembrandt.com --crawl 5` (homepage + 4 discover qua DOM links); `dembrandt dembrandt.com --sitemap` (discover qua sitemap.xml + robots.txt, theo sitemapindex); gộp: `dembrandt dembrandt.com --crawl 10 --sitemap`; paths chỉ định: `dembrandt dembrandt.com /pricing /docs`.
- Ngưỡng số cần đạt: mọi page fetch thành công/skipped có log (failed không abort run); output merge 1 bộ + confidence theo count; tokens 1-trang-miss được cross-check; polite delays + tôn trọng robots/rate-limit.
- Ví dụ input-output (minh họa — paths/số trang do user pick): input "audit 5 trang công ty mình (`/`, `/pricing`, 3 docs) gộp 1 bộ" → output 1 JSON merge + per-token pages xuất hiện + diff `/pricing` dùng spacing khác homepage (nêu rõ) + gaps (2 pages login-only chưa cover — hẹn `--cookie-file`).
- Pitfalls riêng: crawl mass không delay/rate-limit = vi phạm ToS (FAIL pháp lý); sitemap stale vs DOM mới — mismatch thì ghi cả hai + phán quyết; dynamic content miss ở 1 page rồi kết luận hệ = FAIL (cross-check pages khác + `--slow`).
- Phân công usecase này: agent chính shortlist pages + discovery mode (DOM vs sitemap) + chạy crawl + trình merge/confidence; giao claude khi cần mắt người đối chiếu visual cross-page; verify bằng JSON merge + per-token counts + failed/skipped log.

### Usecase con 3: drift gate CI
- Khi dùng: đã có baseline chuẩn, cần fail build/PR khi tokens trôi sau mỗi release.
- Khi bỏ qua: chưa có baseline → Usecase 1/2 tạo baseline trước; chỉ audit 1 lần → Usecase 1.
- Cơ chế khác các usecase khác ở đâu: duy nhất so với baseline + exit code máy (0 clean / 1 drift / 2 baseline lỗi) + annotations + App snapshots/timeline; các usecase khác đo hiện tại, không phán quyết trôi.
- Lệnh copy-paste: `dembrandt https://preview.example.com --compare .dembrandt/baseline.json --json-only` (exit 1 khi drift, in `changes[]`); accept baseline mới: thêm `--approve` (overwrite file, pass); check code mình theo tokens: `dembrandt URL --tokens ./tokens.json --max-off-token 5 --tokens-report ./drift.md --annotations github`. Action: `dembrandt/dembrandt@v0.39.2` với `url` + `baseline`.
- Ngưỡng số cần đạt: baseline pin trong repo (`--save-output` lần đầu + commit); mỗi run sau so đúng file đó; drift có per-token before/after + category scores (colors/typography/spacing/radius/shadows); PR hiện annotations cạnh diff; App có snapshot + timestamp + baseline pin (khi `--key`).
- Ví dụ input-output (minh họa — baseline + ngưỡng do user pick): input "gate PR preview: baseline `.dembrandt/baseline.json`, fail khi >5 giá trị off-token" → output exit 1 + `changes[]` (primary `#ea580c` → `#e11d48`, radius 8→12) + annotation GitHub + App snapshot mới + quyết định approve hay fix.
- Pitfalls riêng: baseline không commit mà so local = gate rỗng (FAIL); `--approve` bừa khi chưa review diff = hợp thức hóa drift; notation `--color-format` khác nhau giữa runs làm tưởng drift (JSON stable, terminal không — so bằng JSON).
- Phân công usecase này: agent chính pin baseline + chạy compare + trình changes/exit code + xin duyệt approve; giao claude khi cần review visual diff mắt người; verify bằng exit code + annotations + snapshot tồn tại + baseline versioned.

### Usecase con 4: WCAG + export cho agent
- Khi dùng: cần audit contrast thật + file agent/build đọc được (Tailwind/shadcn/DESIGN.md/PDF/HTML/screenshot).
- Khi bỏ qua: chỉ cần JSON thô → Usecase 1; chỉ cần gate → Usecase 3.
- Cơ chế khác các usecase khác ở đâu: duy nhất đọc cặp text/background trên từng element DOM (kể cả `[hover]/[focus]/[disabled]`) + serialize ra nhiều format observed-only; các usecase khác dừng ở tokens/merge/drift.
- Lệnh copy-paste: `dembrandt dembrandt.com --wcag` (grades AA/AA-Large/AAA + fail, sort theo tần suất); `dembrandt dembrandt.com --tailwind` (→ `output/<domain>/theme.css`, v4 `@theme` observed-only); `dembrandt dembrandt.com --shadcn` (→ `shadcn.css`, slots quan sát được, oklch, thiếu thì liệt kê header); `dembrandt dembrandt.com --design-md` (→ `DESIGN.md` draft Google: YAML front matter + sections, thiếu evidence thì lược); `dembrandt dembrandt.com --html` + `--screenshot <path>` + `--brand-guide` (PDF).
- Ngưỡng số cần đạt: WCAG trên cặp DOM thật (không phải palette checker), có grades + states; Tailwind file chỉ values quan sát (không shade ramps/interpolated, spacing theo base-N rhythm hoặc named steps theo usage-count); shadcn chỉ observed slots; DESIGN.md sections thiếu evidence bị drop (vd elevation khi không box-shadow); PDF/HTML mở được.
- Ví dụ input-output (minh họa — format do user pick): input "audit WCAG homepage + ra theme cho agent" → output WCAG list (body 16px trên bg fail AA — nêu cặp + ratio) + `theme.css` (`--color-primary`, `--text-display`, `--spacing`, `--radius-lg`, `--breakpoint-md` observed) + `DESIGN.md` + gaps (popover/destructive không quan sát được — để default, đã liệt kê).
- Pitfalls riêng: palette checker ngoài vs DOM pairs (số khác nhau là đúng — tin DOM); `--dark-mode` quên chạy mà kết luận đủ (phải 2 runs light/dark); hover/focus từ CSS không cover pointer-path/timer states (ghi gaps, test tay bổ sung).
- Phân công usecase này: agent chính chạy WCAG + exports đã duyệt + trình grades/files; giao claude khi cần kiểm visual states mắt người; verify bằng files tồn tại + observed-only + grades trên DOM + gaps.

### Các bước chung
1. Xác minh quyền + ToS/robots site nguồn (sở hữu/cho phép/học) → shortlist URLs/paths + format export + single vs crawl vs gate qua question tool, user pick mới chạy (log scope TRƯỚC vì tốn browser/CI time).
2. Setup: `npm i -g dembrandt` + `dembrandt install-browser` (1 lần; Node ≥18) + đọc `docs/usage.md` + `docs/FLAGS.md` (interactions/ignored-combos/multi-page propagation).
3. Extract (UC1/UC2): `--json-only`/`--save-output`/`--dtcg`, hoặc `--crawl/--sitemap`/paths; tôn trọng delays + robots; lưu JSON + evidence.
4. Gate (UC3): pin baseline (commit file) → `--compare`/`--tokens --max-off-token` → đọc exit code + `changes[]` + annotations → duyệt `--approve` hoặc fix.
5. Audit + export (UC4): `--wcag` + `--tailwind/--shadcn/--design-md/--html/--screenshot/--brand-guide`; verify observed-only (header liệt kê thiếu, section thiếu bị drop).
6. Agent handoff: MCP (`get_design_tokens` → `job_id` → `get_job_status` → `export_dtcg`/`generate_design_md`) hoặc skills (`extract-design`, `generate-ui-from-brand`, orchestrator `dembrandt` 6-stage); skills `npx skills add dembrandt/dembrandt-skills --all`.
7. Deliver: lệnh đã chạy + files output + exit codes + diff/WCAG + gaps + quyền đã check (sở hữu/cho phép/học).

### Prompt mẫu
- "Audit tokens homepage công ty mình (sở hữu đã xác minh, ToS cho phép) — scope 1 URL, format JSON + DTCG. Chạy `dembrandt <url> --save-output` + `dembrandt <url> --dtcg`. Trình tokens + evidence + gaps (dark-mode/canvas) trước khi tôi duyệt export tiếp. Observed-only, cấm bịa slots."
- "Crawl 5 trang docs của mình (`/`, `/pricing`, 3 docs) gộp 1 bộ: `dembrandt <domain> --crawl 5`. Trình merge + per-token page counts + diff giữa pages. Tôn trọng robots/rate-limit."
- "Gate PR preview theo baseline `.dembrandt/baseline.json`, fail khi drift: `dembrandt <preview-url> --compare .dembrandt/baseline.json --json-only`. Trình exit code + `changes[]` + annotations. Không `--approve` khi chưa có ok tường minh của tôi."
- "WCAG + theme cho agent: `dembrandt <url> --wcag` + `dembrandt <url> --tailwind` + `dembrandt <url> --design-md`. Trình grades cặp DOM + files + slots thiếu đã liệt kê. Quên `--dark-mode` thì chạy bổ sung, không kết luận đủ."

### Pitfalls
- Không chạy `install-browser` mà extract (dừng `browser engine not available`) — fix: chạy 1 lần + Linux thêm `--with-deps`; CI dùng `--no-sandbox`/CDP.
- Tưởng terminal = full (terminal chỉ high/medium confidence) — fix: mở JSON verify đủ palette.
- So drift bằng mắt/khác notation terminal — fix: so JSON + baseline pin, exit code quyết định.
- `--approve` bừa hợp thức hóa drift — fix: review `changes[]` + quote ok tường minh mới approve.
- Quên `--dark-mode`/`--mobile` mà kết luận hệ đủ — fix: chạy 2 runs light/dark + mobile 390×844 khi brief yêu cầu.
- Hover/focus từ CSS miss pointer-path/timer; canvas/WebGL không DOM; site nặng hydrate miss — fix: ghi gaps + `--slow`/Firefox (`--browser=firefox`) + test tay, cấm claim đủ.
- Crawl mass không delay + bỏ qua robots/ToS — fix: polite delays, check robots trước, dừng khi ToS cấm (FAIL pháp lý nếu cố).
- Bê logo/brand người khác ra sản phẩm — fix: chỉ học/phân tích nội bộ, không redistribute (repo `Intended Use`).

### Tham khảo sử dụng (số chốt 02/11/2026)
- Nhận xét sâu: Manav Arya Singh (tác giả đối thủ `designlang`, disclose bias ngay đầu bài) 15/09/2026 `https://www.manavaryasingh.com/blog/designlang-vs-dembrandt-vs-extract-design-system` — "mọi fact từ README/package.json/npm tại thời điểm viết; chỗ nào tool khác tốt hơn thì nói thẳng" + verdict `dembrandt solid cho Tailwind + drift CI; designlang cho shadcn/Figma/mobile; extract-design-system cho starter tokens` → lật quyết định chọn dembrandt cho job tokens-Tailwind + gate CI (và bỏ nó cho job shadcn/Figma-native).
- Số trung bình có trọng số: GitHub API 02/11/2026: 3.902★/336 forks/9 watchers/4 issues (tạo 22/11/2025, push 01/11/2026 — còn sống, release đều 79 versions tới `0.39.2`); npm `api.npmjs.org` last-month 20.389 (30/09–29/10/2026) + last-week 7.444 + cộng dồn all-time 269.355 (23/11/2025–29/10/2026) → khớp claim landing `250.000+` (verified). Trọng số: installs/tháng thực (20.389 vs designlang 4.597, gấp 4,4×) đáng tin hơn stars (designlang 4.448★ > dembrandt 3.902★ — stars đo viral, installs đo dùng thật). Skills repo 179★/22 forks + 45 skills (API contents) — claim `25.000+ skill installs` + `10s/extraction` chưa có nguồn độc lập → `chưa xác minh`.
- Mâu thuẫn: deep review (đối thủ khen dembrandt cho Tailwind/CI) vs stars (designlang cao hơn) → phán quyết: job Tailwind + drift CI → dembrandt; job shadcn/Figma/native một pass → designlang; cả hai đều MIT nên thử dembrandt trước vì installs cao + setup gọn.
- Tiếng Việt: không tìm thấy review Việt → `chưa xác minh`.

### Tham khảo
- Repo + docs đã mở kiểm tra: `https://github.com/dembrandt/dembrandt` (README Install/Flags/CI/MCP/App/Limitations/Intended Use), `https://raw.githubusercontent.com/dembrandt/dembrandt/main/docs/usage.md` (toàn bộ flags + multi-page + browser/CDP + DTCG/DESIGN.md/Tailwind/shadcn/WCAG/motion/AI/PDF/confidence), `https://github.com/dembrandt/dembrandt-skills` (Quick start, 45 skills, engine, MCP).
- Registry đã chạy: `npm view dembrandt version/description/license/homepage/engines/bin` (0.39.2, MIT, Node ≥18) + `api.npmjs.org` (20.389/tháng, 7.444/tuần) + `registry.npmjs.org/dembrandt/latest` (deps/bins) + GitHub API 2 repos (số trên).
- Lệnh đã chạy: `npx -y dembrandt@0.39.2 --help` exit 0 (đủ flags) + `npx -y dembrandt@0.39.2 https://example.com --json-only` khởi động rồi kẹt tải Chromium `playwright-core 1.63.0` (đúng ma sát browser).
- So sánh độc lập: `https://www.manavaryasingh.com/blog/designlang-vs-dembrandt-vs-extract-design-system` (15/09/2026, bảng outputs/coverage/MCP-CI + số stars/npm 3 bên).

### Được dùng ở đâu
- Dùng CHO UI (audit tokens/drift/WCAG/exports): xem `../../domains/ui/using-dembrandt.md` — index `../../domains/ui/README.md`.

### Quay lại index
- Về `../../domains/ui/README.md` để so với `hallmark` (system mới) + `ai-website-cloner-template` (rebuild app) + `skillry`/`reactbits`.
- Xem thêm item liên quan: `../ai-website-cloner-template/` khi cần app chạy được thay vì tokens.

---

## English

### When to use
- Need the real, measured design system of a live website you own/have permission to analyze (or for internal learning): colors + roles/confidence, typography, spacing, borders, shadows, motion, components, breakpoints — in tens of seconds, no manual DevTools.
- Need machine-readable files for an agent/build: JSON, W3C DTCG (Design Tokens Community Group) (`--dtcg`), `DESIGN.md`, Tailwind v4 `@theme`, shadcn theme, HTML report, brand-guide PDF, screenshot.
- Need a CI drift gate: pin a baseline JSON, `--compare` exits 1 on drift, PR annotations, snapshot timeline in the App.
- Need WCAG contrast on real DOM pairs (including hover/focus/disabled), or multi-page crawls merged with confidence (`--crawl`, `--sitemap`).

### When to skip
- Need a brand-new gated system from zero → use `../hallmark/` (dembrandt measures what rendered; it generates no system/gates).
- Need a full 1:1 app rebuild as editable Next.js → use `../ai-website-cloner-template/` (dembrandt outputs tokens, not an app).
- Need one owned React animated brick → use `../reactbits/`.
- Need packaged landing taste now → use `../skillry/` (web part).
- Unowned/unpermitted sites, ToS-banned automated access, phishing/impersonation, or reproducing someone else's logo/brand → absolutely forbidden (see [Invariant core](#invariant-core)).

### Install
- CLI: `npm i -g dembrandt` (source: `docs/getting-started`, origin README). Requires Node.js ≥18 (source: `registry engines`, 02/11/2026).
- Mandatory once: `dembrandt install-browser` (default chromium; `dembrandt install-browser firefox` for Cloudflare/bot sites). Reason: dembrandt depends on lean `playwright-core` with NO bundled browser — skipping stops the first run at `browser engine not available`. On Linux/CI add system libs: `npx playwright@$(node -p "require('playwright-core/package.json').version") install --with-deps chromium`.
- Verified 02/11/2026: `npm view dembrandt version` → `0.39.2`; `npx -y dembrandt@0.39.2 --help` → exit 0 with all flag groups matching `docs/usage.md` word-for-word. Real extraction `https://example.com --json-only` started then stalled downloading Chromium for `playwright-core 1.63.0` past a 60s timeout — the documented friction, not a command error.
- No-install: `npx dembrandt dembrandt.com` (still needs the one-time `install-browser`; shared Playwright cache).
- Skills: `npx skills add dembrandt/dembrandt-skills --all` (43/45 run without the engine; `extract-design` + `generate-ui-from-brand` need engine ≥0.39.0). MCP: `claude mcp add --transport stdio dembrandt -- npx -y dembrandt mcp` or `.mcp.json`; listed in the MCP Registry as `io.github.dembrandt/dembrandt`.
- CI gate: `dembrandt/dembrandt@v0.39.2` (`url` + `baseline`), or exit-code gate: `dembrandt URL --compare baseline.json --json-only` (exit 1 = drift, exit 2 = unreadable baseline).

### How the item works
- Backing organization: `@dembrandt` (15y UX/front-end designer-dev), repo `https://github.com/dembrandt/dembrandt`, MIT, 394 commits (repo page 02/11/2026), 79 npm versions (created 23/11/2025 → `0.39.2` 11/10/2026), TypeScript + `playwright-core` + `@modelcontextprotocol/sdk`. GitHub API 02/11/2026: 3,902 stars / 336 forks / 9 watchers / 4 open issues, pushed 01/11/2026. npm registry 02/11/2026: bins `dembrandt` + `dembrandt-mcp`, engines `node >=18.0.0`. Companion repo `https://github.com/dembrandt/dembrandt-skills` (MIT, 179 stars/22 forks, 246 commits, pushed 01/11/2026, 45 skills verified via API).
- Core method: renders the URL in a real browser (Chromium/Firefox via Playwright, default 1920×1080, `--mobile` = 390×844), reads computed styles + CSS variables off the rendered DOM, analyzes usage/confidence, groups typography, detects spacing/motion/states; returns tokens + evidence. It measures production, not specs, so spec-vs-ship gaps surface. Default prints terminal only; files need flags. JSON always carries full hex/rgb/lch/oklch regardless of `--color-format` (presentation-only, CLI warns on export mixes).
- Per-usecase differences: single-URL extract (one pass, see [Sub-usecase 1](#sub-usecase-1-single-url-token-extraction)) vs multi-page crawl (merged + cross-page confidence, see [Sub-usecase 2](#sub-usecase-2-multi-page-crawl-with-merged-confidence)) vs CI drift gate (baseline comparison + exit codes + annotations + App snapshots, see [Sub-usecase 3](#sub-usecase-3-ci-drift-gate)) vs WCAG + agent exports (real DOM pairs + observed-only themes, see [Sub-usecase 4](#sub-usecase-4-wcag--agent-exports)).

### Invariant core
- Rights before URL: only owned/permitted/internal-learning sites; stop when ToS bans automation; respect robots.txt + rate limits. Violation = no longer using the system (legal FAIL). State the right (owned/permitted/learning) + ToS/robots check after every use. Never reproduce third-party trademarks/logos/brands (repo `Intended Use`).
- Observed-only, never invent tokens: every token comes from measured rendered DOM (evidence + confidence); Tailwind/shadcn exports write ONLY observed slots (missing ones stay default + header-listed); evidence-less sections are dropped, never padded. Same-name-different-metrics substitution = FAIL.
- Baseline-gated drift: drift counts only against a pinned baseline JSON (`--compare`); exit 1 = drift, exit 2 = bad baseline — never call drift by eye. No baseline + `changes[]` + exit code = the system was not really used.

### Customizable surface
- Tunable: in-scope URLs/paths, crawl size/mode (`--crawl N`, `--sitemap`, DOM vs sitemap), viewport (`--mobile`, `--screen-size`, `--dark-mode`), terminal color notation (`--color-format hex|rgb|oklch|lch|source`), export format, auth, fingerprint, engine (CDP — Chrome DevTools Protocol via `BROWSER_CDP_ENDPOINT`, `--no-sandbox`, `--slow`), gate thresholds, AI primary (`--ai`), cloud sync (`--key`). Two-level approval gate: (1) which artifact — shortlist URLs/paths + export format + single vs crawl vs gate with reasons via question tool, run only after the user picks (browser loops + CI time cost — log approved scope BEFORE running); (2) what stays/changes — which diffs to `--approve`, which gaps to keep. Waivers (skip compare, `--stealth`, sensitive sites) must quote the user's explicit ok. Never list `must-not` items here.

### Work split
- Main agent: rights/ToS + robots checks + scope shortlist (wait for user pick — never self-pick then extract) + runs CLI/MCP + presents tokens/evidence/diffs/WCAG + requests `--approve`; verifies output files + exit codes + annotations + snapshots.
- Hand browser-visible/human steps to claude: interactive `--login`, human visual diffs, trademark-collision review — with URLs + states + concrete asks; never invent observations. No browser/engine → declare + stop at docs level, never claim extraction.
- Agent verifies: output files exist with observed-only content + correct exit codes (0/1/2) + DOM-pair WCAG grades + crawled pages complete.

### Differentiating positioning (numbers as of 02/11/2026 unless noted)
- Vs `Manavarya09/design-extract` (designlang, npm `designlang@13.3.2`): 4,448 stars/382 forks vs dembrandt 3,902/336 — designlang leads stars; but npm last-month dembrandt 20,389 vs designlang 4,597 (4.4× real installs). designlang outputs more (shadcn, Figma variables + plugin, typed React stubs, iOS/Android/Flutter, 4 viewports); dembrandt is tighter + stronger on CI drift (compare + Action + App timeline + Slack/Linear) + PDF/HTML. Pick dembrandt for Tailwind tokens + CI drift in one lean CLI with higher monthly installs; pick designlang for shadcn/Figma/native in one pass.
- Vs `arvindrk/extract-design-system` (npm `0.1.11`, 801/month; 218 stars 15/09/2026): it CALLS dembrandt CLI for extraction, adding normalization + `audit` + skill-first flow. Public single-page only. Pick dembrandt for multi-page/auth/engines/full exports; pick extract-design-system for starter `tokens.json` + `tokens.css` dropped into a project.
- Vs `../hallmark/`: dembrandt MEASURES rendered output; hallmark GENERATES new gated systems. Audit/tokens/drift of an existing permitted site → dembrandt; new standard system → hallmark; sweep dembrandt tokens with hallmark to standardize. Vs `../ai-website-cloner-template/`: cloner rebuilds runnable Next.js apps (slow/costly); dembrandt outputs tokens (~10s, $0) — app → cloner, tokens + gates → dembrandt.

### Coverage map (scanned ALL of README + docs/usage + ci + mcp + recipes + FLAGS + skills repo 02/11/2026 — ★ strongest first)
- ★ Single-URL token extraction (JSON/DTCG/DESIGN.md): see Sub-usecase 1.
- Multi-page crawl/sitemap merged confidence: see Sub-usecase 2.
- CI drift gate (compare/approve/tokens/annotations, Action, App): see Sub-usecase 3.
- Real-DOM WCAG + agent exports (Tailwind/shadcn/brand-guide/HTML/screenshot): see Sub-usecase 4.
- Medium: MCP server (job + pure + extraction tools, `io.github.dembrandt/dembrandt`).
- Medium: `dembrandt-skills` (45 skills: 6-stage orchestrator + extract/generate + 39 UX).
- Medium: auth/fingerprint/engine/CDP/slow/AI/cloud-sync flags.
- NOT supported → replacement: auto dark-mode (run `--dark-mode` separately) ; pointer-path/timer states (manual test); canvas/WebGL (no DOM — no system); late-hydration misses (`--slow` + more crawl, else record gaps); backends/authz (implement yourself); legal/ToS (check + permission yourself); new systems/gates → `../hallmark/`; app rebuilds → `../ai-website-cloner-template/`; React bricks → `../reactbits/`; packaged taste → `../skillry/`.

### Decision dossier
- Jobs SERVED (4+): 1. token audit/extract to JSON/DTCG/DESIGN.md in ~10s; 2. pinned-baseline CI/PR drift gates + App timeline + Slack alerts; 3. real-DOM WCAG audits with states; 4. observed-only Tailwind/shadcn seeding for agents.
- Jobs NOT served (each with replacement): 1. new gated systems → `../hallmark/`; 2. runnable app rebuilds → `../ai-website-cloner-template/`; 3. single React bricks → `../reactbits/`; 4. packaged landing taste → `../skillry/`; 5. bulk non-UI extraction → firecrawl/API; 6. unpermitted/ToS-banned/phishing work → no system (forbidden).
- Free / total + price: CLI + skills MIT $0 (sources: both `LICENSE` files + `npm view` 02/11/2026). App Beta currently free (GitHub sign-in, `dmb_···` key sync; sponsorship funds enforcement). No extract-local subscription; external costs only: CI/browser time + optional `onnxruntime-node` for `--ai`. Future App pricing `unverified`, never guessed.
- Install friction: 3 steps (`npm i -g dembrandt` → `install-browser` → `dembrandt <url>`), 2 more than the one-line standard. RAN: `npm view` + `--help` exit 0 + real extract boot stalling at Chromium download (documented friction). Barriers: Node 18+, separate browser download + Linux `--with-deps`, interactive `--login` (CI uses `--cookie-file`), Cloudflare → firefox, heavy sites → `--slow`.
- Viral same-segment opponents: `Manavarya09/design-extract` (4,448 stars/382 forks API 02/11/2026; npm `13.3.2` 4,597/month) vs `arvindrk/extract-design-system` (npm `0.1.11` 801/month; 218 stars 15/09/2026). npm window 30/09–29/10/2026.
- Pick it over opponents when: lean real-measurement CLI + DTCG/DESIGN.md/Tailwind/shadcn/PDF/HTML + CI drift in ~10s with 4.4× monthly installs matters. Choice-flipping example: Tailwind tokens + drift gate → dembrandt; one-pass shadcn/Figma/native → designlang; starter tokens into a project → extract-design-system.
- NEVER use when: no rights/ToS-or-robots ban; phishing/impersonation/brand-logo reproduction; canvas/WebGL-only (nothing to read); gated-system work attempted by extraction alone; browser-less agents claiming extraction (invented observation = FAIL).

### Sub-usecase 1: single-URL token extraction
- When to use: one permitted URL needs observed tokens + evidence in ~10s.
- When to skip: multi-page → 2; CI gate → 3; WCAG/exports → 4; runnable app → cloner; new system → hallmark.
- Copy-paste: `dembrandt dembrandt.com --json-only`. Persist: `dembrandt dembrandt.com --save-output`. W3C: `dembrandt dembrandt.com --dtcg`.
- Numeric bar: JSON exists with all 8 groups the site has; colors carry roles + confidence; typography carries fonts/sizes/weights/sources/URLs; motion carries durations/easings/per-context deltas; unobserved slots listed, never padded.
- Input-output example: permitted company homepage, 1 URL, JSON + DTCG → `output/acme/<ts>.json` + `*.tokens.json` + terminal summary + explicit gaps (dark mode unmeasured, canvas hero skipped).
- Own pitfalls: terminal ≠ full (high/medium only — open JSON); `--color-format` is presentation-only; logos may be AVIF; heavy-JS hydration misses need `--slow` + recorded gaps.
- Work split: main agent rights-checks + shortlists URL/format (user picks — never self-picks) + runs CLI + presents tokens; browser-visible steps go to claude; verify via files + observed-only + gaps.

### Sub-usecase 2: multi-page crawl with merged confidence
- When to use: one page under-covers the system; cross-page confidence + inter-page drift needed.
- Copy-paste: `dembrandt dembrandt.com --crawl 5`; `dembrandt dembrandt.com --sitemap`; `dembrandt dembrandt.com --crawl 10 --sitemap`; explicit paths: `dembrandt dembrandt.com /pricing /docs`.
- Numeric bar: every page logged success/skipped (failures never abort); one merged set + per-token page counts; delays + robots respected.
- Input-output example: 5 own docs pages → one merged JSON + page counts + `/pricing` spacing diff + login-only gaps queued for `--cookie-file`.
- Own pitfalls: undelayed mass crawls = legal FAIL; stale sitemaps recorded both-sides + verdict; single-page misses never generalized.
- Work split: main agent shortlists pages + discovery mode + runs crawl + presents merge; human cross-page visuals to claude; verify via merge + counts + logs.

### Sub-usecase 3: CI drift gate
- When to use: a pinned baseline exists; every release must fail on token drift.
- Copy-paste: `dembrandt https://preview.example.com --compare .dembrandt/baseline.json --json-only`; accept: add `--approve`; code-against-tokens: `dembrandt URL --tokens ./tokens.json --max-off-token 5 --tokens-report ./drift.md --annotations github`. Action: `dembrandt/dembrandt@v0.39.2`.
- Numeric bar: versioned baseline; per-token before/after + category scores; PR annotations; App snapshot + timestamp + pin.
- Input-output example: preview + `max-off-token 5` → exit 1 + `changes[]` (primary `#ea580c` → `#e11d48`, radius 8→12) + annotations + snapshot + approve-or-fix decision.
- Own pitfalls: uncommitted baselines = empty gates; careless `--approve` legalizes drift; notation mixes fake drift (compare JSON, not terminal).
- Work split: main agent pins baseline + runs compare + presents changes/exit code + requests approval; human visual review to claude; verify via exit codes + annotations + snapshots.

### Sub-usecase 4: WCAG + agent exports
- When to use: real contrast audit + agent-readable theme files needed.
- Copy-paste: `dembrandt dembrandt.com --wcag`; `dembrandt dembrandt.com --tailwind`; `dembrandt dembrandt.com --shadcn`; `dembrandt dembrandt.com --design-md`; `dembrandt dembrandt.com --html`; plus `--screenshot <path>` and `--brand-guide`.
- Numeric bar: DOM-pair grades (AA/AA-Large/AAA/fail) with states; observed-only theme files; dropped evidence-less sections; openable PDF/HTML.
- Input-output example: homepage audit + theme → WCAG pair list + `theme.css` + `DESIGN.md` + listed-missing slots.
- Own pitfalls: palette checkers disagree with DOM pairs by design — trust DOM; missing `--dark-mode` run noted, never assumed; CSS-only states supplemented manually.
- Work split: main agent runs WCAG + approved exports + presents grades/files; human state checks to claude; verify via files + grades + gaps.

### Shared steps
1. Rights + ToS/robots check → shortlist URLs/paths + format + single-vs-crawl-vs-gate via question tool, run only after user pick (log scope FIRST).
2. Setup: `npm i -g dembrandt` + `install-browser` (once; Node ≥18) + read `docs/usage.md` + `docs/FLAGS.md`.
3. Extract (1/2): json/save/DTCG or crawl/sitemap/paths; respect delays + robots; keep JSON + evidence.
4. Gate (3): pin + commit baseline → compare/tokens/max-off-token → read exit code + `changes[]` + annotations → approve-or-fix.
5. Audit + export (4): WCAG + tailwind/shadcn/DESIGN.md/HTML/screenshot/brand-guide; verify observed-only.
6. Agent handoff: MCP job flow or `dembrandt-skills` (`extract-design`, `generate-ui-from-brand`, 6-stage `dembrandt`); `npx skills add dembrandt/dembrandt-skills --all`.
7. Deliver: commands run + files + exit codes + diffs/WCAG + gaps + rights statement.

### Sample prompts
- "Audit tokens for my permitted company homepage — 1 URL, JSON + DTCG. Run `dembrandt <url> --save-output` + `--dtcg`. Present tokens + evidence + gaps before I approve further exports. Observed-only, no invented slots."
- "Crawl my 5 docs pages and merge: `dembrandt <domain> --crawl 5`. Present merge + page counts + inter-page diffs. Respect robots/rate limits."
- "Gate the preview PR on `.dembrandt/baseline.json`: `dembrandt <preview-url> --compare .dembrandt/baseline.json --json-only`. Present exit code + `changes[]` + annotations. No `--approve` without my explicit ok."
- "WCAG + agent theme: `dembrandt <url> --wcag` + `--tailwind` + `--design-md`. Present DOM-pair grades + files + listed-missing slots. Run `--dark-mode` separately instead of assuming coverage."

### Pitfalls
- Skipping `install-browser` (`browser engine not available`) — run once + Linux `--with-deps`; CI uses `--no-sandbox`/CDP.
- Mistaking terminal for full output — open JSON for the complete palette.
- Eyeballing drift / mixing notations — compare pinned JSON, decide by exit code.
- Careless `--approve` — review `changes[]` + quote explicit ok first.
- Claiming coverage without `--dark-mode`/`--mobile` — run both when the brief needs them.
- CSS-only states, canvas/WebGL gaps, late hydration — record gaps + `--slow`/firefox + manual tests, never claim full.
- Undelayed mass crawls / ignored robots/ToS — polite delays, pre-check robots, stop when banned (forcing = legal FAIL).
- Reproducing others' logos/brands — internal analysis/learning only, no redistribution (`Intended Use`).

### Usage references (pinned 02/11/2026)
- Deep review: Manav Arya Singh (rival `designlang` author, disclosed bias) 15/09/2026 `https://www.manavaryasingh.com/blog/designlang-vs-dembrandt-vs-extract-design-system` — "every fact from READMEs/package.json/npm; states where rivals win" + verdict `dembrandt solid for Tailwind + CI drift; designlang for shadcn/Figma/mobile; extract-design-system for starters` → flips the Tailwind + CI-gate decision to dembrandt (and away for shadcn/Figma-native).
- Weighted averages: GitHub API 02/11/2026: 3,902 stars/336 forks/9 watchers/4 issues (created 22/11/2025, pushed 01/11/2026 — alive, 79 releases to `0.39.2`); npm `api.npmjs.org` last-month 20,389 (30/09–29/10/2026) + last-week 7,444 + all-time sum 269,355 (23/11/2025–29/10/2026) → matches landing `250,000+` (verified). Weight: monthly installs (20,389 vs designlang 4,597, 4.4×) beat stars for real usage (designlang leads stars 4,448 vs 3,902 — stars measure virality, installs measure use). Skills repo 179 stars/22 forks + 45 skills (API) — landing `25,000+ skill installs` + `10s/extraction` lack independent sources → `unverified`.
- Conflict: rival-praised for Tailwind/CI vs fewer stars → verdict: Tailwind + CI drift → dembrandt; one-pass shadcn/Figma/native → designlang; both MIT so try dembrandt first (higher installs + leaner setup).
- Vietnamese: no VI review found → `unverified`.

### References
- Checked repos/docs: `https://github.com/dembrandt/dembrandt` (README Install/Flags/CI/MCP/App/Limitations/Intended Use), `https://raw.githubusercontent.com/dembrandt/dembrandt/main/docs/usage.md` (all flags + multi-page + browser/CDP + DTCG/DESIGN.md/Tailwind/shadcn/WCAG/motion/AI/PDF/confidence), `https://github.com/dembrandt/dembrandt-skills` (Quick start, 45 skills, engine, MCP).
- Ran registries: `npm view dembrandt` (0.39.2, MIT, Node ≥18) + `api.npmjs.org` (20,389/month, 7,444/week) + `registry.npmjs.org/dembrandt/latest` (deps/bins) + both GitHub APIs (numbers above).
- Ran commands: `npx -y dembrandt@0.39.2 --help` exit 0 (full flags) + `https://example.com --json-only` boot stalling at Chromium download for `playwright-core 1.63.0` (documented friction).
- Independent comparison: `https://www.manavaryasingh.com/blog/designlang-vs-dembrandt-vs-extract-design-system` (15/09/2026, outputs/coverage/MCP-CI tables + 3-way stars/npm).

### Where used
- Used FOR UI (token audit/drift/WCAG/exports): see `../../domains/ui/using-dembrandt.md` — index `../../domains/ui/README.md`.

### Back to index
- Back to `../../domains/ui/README.md` to compare with `hallmark` (new systems) + `ai-website-cloner-template` (app rebuilds) + `skillry`/`reactbits`.
- Related item: `../ai-website-cloner-template/` when a runnable app is needed instead of tokens.
