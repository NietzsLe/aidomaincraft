# claude-seo

## Tiếng Việt

### Dùng khi
- Cần audit SEO 1 website mình sở hữu/có quyền (hoặc URL công khai để học) ra plan hành động xếp thứ tự: technical, E-E-A-T content, schema, Core Web Vitals, GEO/AEO (AI Overviews/ChatGPT/Perplexity/Gemini), local, e-commerce, international — trong 10–15 phút với Claude Code.
- Cần audit chạy bằng agents song song (tối đa 17 agents) + điểm SEO Health Score 0–100 + file giữ lại (`FULL-AUDIT-REPORT.md`, `ACTION-PLAN.md`, PDF/Excel).
- Cần theo dõi drift SEO theo thời gian (`/seo drift baseline|compare|history`, SQLite) hoặc số liệu Google thật (Search Console, PSI, CrUX 25 tuần, GA4, Keyword Planner) qua lệnh `/seo google`.
- Cần readiness cho AI search/agent: citability (mức AI trích dẫn được), llms.txt + ai-catalog.json (file tóm tắt site cho AI đọc), WebMCP scaffold (chuẩn draft để agent gọi tool web), Lighthouse Agentic Browsing (`/seo geo`, `/seo agentic`).

### Bỏ qua khi
- Cần system/design UI mới pass gates → dùng `../hallmark/` (claude-seo audit content/SEO, không sinh design system).
- Cần rebuild app Next.js 1:1 từ URL sống → dùng `../ai-website-cloner-template/` (claude-seo không build app).
- Cần fix code/content hộ (viết bài, sửa schema vào repo) → dùng `../claude-blog` (tương lai) hoặc tự implement theo plan; claude-seo audit + sinh plan/draft (`agentic fix` chỉ draft robots/llms.txt/ai-catalog để review, không deploy).
- Cần audit site KHÔNG có quyền cào (ToS cấm automated access), phishing/giả mạo, spam SEO (nhồi từ khóa, cloaking, link farm) → cấm tuyệt đối (xem [Cốt lõi bất biến](#cot-loi-bat-bien)).

### Cài đặt (đã clone + đọc source + chạy registry/API trên Linux 02/11/2026; `/seo audit` thật chưa chạy vì máy này không có Claude Code)
- Cách 1 — plugin marketplace (khuyến nghị theo README gốc, cần Claude Code 1.0.33+): chạy 3 lệnh TRONG Claude Code: `/plugin marketplace add AgriciDaniel/claude-seo` rồi `/plugin install claude-seo@agricidaniel-claude-seo` rồi `/seo setup` (dựng Python venv cách ly + headless browser, không chạm hệ thống) + `/seo doctor` kiểm tra.
- Cách 2 — manual (macOS/Linux): `git clone --depth 1 https://github.com/AgriciDaniel/claude-seo && bash claude-seo/install.sh` (đã đọc `install.sh`: yêu cầu `git`, pin `REPO_TAG=v2.5.0`, ghi vào `~/.claude/skills/seo` + `~/.claude/agents`; CI guard bắt tag khớp manifest). Windows: `install.ps1`.
- Yêu cầu: Claude Code 1.0.33+, Python 3.11–3.14 (3.10 EOL 10/2026), Git; Playwright Chromium do `/seo setup`/`install.sh` lo (thất bại không fatal — chỉ mất render SPA + screenshots); Linux/CI thêm system libs.
- Kiểm tra đã chạy 02/11/2026: `git clone --depth 1` OK (26 thư mục `skills/`, 19 file `agents/*.md`, 9 thư mục `extensions/`, 76 file `tests/test_*.py`); `curl GitHub API` → 25.381★/3.344 forks/171 watchers/78 issues, release `v2.5.0` ngày 22/10/2026, push 01/11/2026; đọc `skills/seo/SKILL.md` frontmatter (name `seo`, MIT, triggers, `argument-hint: [command] [url]`); đọc `docs/COMMANDS.md` (bảng Quick Reference 30 lệnh + extension rows); đọc `.claude-plugin/marketplace.json` (category `marketing`, v2.5.0).
- Chưa chạy: `/seo setup`, `/seo doctor`, `/seo audit <url>` thật (máy này không có Claude Code + tránh cào site thật) — ghi rõ WARN.

### Cách item hoạt động
- Tổ chức đứng sau: cá nhân `Agrici Daniel` (AI Workflow Architect, Moldova; cộng đồng AI Marketing Hub: 2.700+ free + 161 pro theo Medium 2026 — nguồn thứ ba), repo `https://github.com/AgriciDaniel/claude-seo`, license MIT, 412 commits (trang repo 02/11/2026), release `v2.5.0` ngày 22/10/2026, tạo 07/02/2026, push 01/11/2026. Số liệu API GitHub ngày 02/11/2026: 25.381★ / 3.344 forks / 171 watchers / 78 issues mở. Họ cùng tác giả: `chatgpt-seo` (895★/123 forks, fix-plan trong ChatGPT), `claude-blog` (2.606★/441 forks, viết bài chuẩn SEO), `banana` (ảnh AI cho SEO).
- Phương thức hoạt động chung: plugin Claude Code = 1 skill hub `seo` (`/seo $1 $2`, SKILL.md) điều phối 25 sub-skills (22 core + 1 framework FLOW + 2 extension mirrors) + 19 sub-agents chuyên môn (`agents/seo-*.md`). Audit full: detect business type (SaaS/local/e-commerce/publisher/agency) → fan-out tối đa 17 agents song song (9 always-on + 8 conditional) → chấm SEO Health Score 0–100 → plan xếp thứ tự (cái gì, dựa vào đâu, phụ thuộc gì, verify bằng gì). Fetch qua script chuẩn `scripts/claude-seo run fetch_page.py <url> --json` (2 đường raw `--render never` vs rendered `--render auto|always`, cùng JSON contract; lỗi fetch vẫn ra JSON + exit 1). Hooks `PostToolUse` (Edit|Write) chạy `validate-schema.py` (timeout 30s). Báo cáo: Markdown giữ lại + PDF qua WeasyPrint/matplotlib (`/seo google report`) + Excel.
- Khác biệt vận hành theo usecase: audit full site (fan-out đa trang, crawl tới 500 pages, xem [Usecase con 1](#usecase-con-1-audit-full-site)) khác audit 1 trang chuyên sâu (depth 1 URL, xem [Usecase con 2](#usecase-con-2-audit-1-trang-chuyen-sau)) khác GEO/agentic readiness (đo citability + file cho AI, không đo rank cổ điển, xem [Usecase con 3](#usecase-con-3-geoaeo--agent-readiness)) khác drift + Google APIs (time-series + số liệu thật + PDF, xem [Usecase con 4](#usecase-con-4-drift--google-apis-report)).

### Cốt lõi bất biến
- Audit trước, evidence trước: mọi finding phải nêu nguồn (DOM fetch/GSC/PSI/API nào + lệnh đã chạy) + cách verify lại; cấm điểm số không kèm bằng chứng. Không nêu được skill/agent/lệnh đã dùng + file report + score = chưa thực sự dùng hệ.
- Hub routing đúng: việc SEO chung chưa rõ workflow → skill hub `seo`; việc đã rõ (schema/backlinks/maps/...) → skill `seo-*` cụ thể (nguyên văn SKILL.md). Gọi hub cho mọi việc nhỏ = sai hệ.
- Quyền + white-hat trước mọi URL: chỉ audit site mình sở hữu/có cho phép/URL công khai để học; tuân thủ ToS + robots.txt + rate limit; cấm spam SEO (nhồi từ khóa, cloaking, link farm, review giả), cấm phishing/giả mạo, cấm dùng output tái tạo thương hiệu người khác. Vi phạm = không còn dùng hệ (FAIL pháp lý). Sau khi dùng phải nêu được quyền gì + ToS/robots đã check.
- Draft ≠ deploy: `agentic fix`/schema/llms.txt sinh ra để review, không tự đẩy production; deploy khi chưa có ok tường minh của user = FAIL.

### Phần tùy chỉnh
- Được đổi: URLs/pages nào in-scope (full site tới 500 pages hay 1 page), business type (saas/local/ecommerce/publisher/agency cho `/seo plan`), workflow/lệnh nào (30 lệnh 6 nhóm + extensions), model agent nào (mặc định 5 agents Opus + còn lại Sonnet — đổi trong file `agents/`, tốn plan khác nhau), format report (Markdown giữ lại/PDF/Excel/`cluster-map.html`), ngưỡng đo (ảnh >200KB flag, sitemap 30/50 location limits, `max-off-token`-style gates), extension nào cắm (9 extensions: API keys/creds riêng — DataForSEO trả theo usage, Ahrefs, SE Ranking, Profound, Bing/IndexNow key, Matomo, Firecrawl, Banana/Gemini, unlighthouse local). Cổng duyệt 2 tầng: (1) artifact nào — shortlist lệnh/scope (audit full vs page vs geo vs drift + URLs + business type) kèm lý do qua question tool, user pick mới chạy (audit full 10–15 phút + tốn token plan + data trả phí của extension — log scope đã duyệt TRƯỚC khi chạy); (2) giữ/đổi gì — findings nào fix, draft nào deploy, key nào cắm. Waiver (dùng API trả phí, audit site nhạy cảm, deploy draft) phải quote câu ok tường minh của user. Cấm đưa `must-not` (spam SEO, cào không quyền, hứa rank/cite cụ thể) vào danh sách tùy chỉnh.

### Phân công ai làm gì
- Agent chính: check quyền/ToS + robots trước mỗi URL + shortlist lệnh/scope (chờ user pick — cấm tự chốt rồi audit) + cài/setup/doctor + chạy lệnh `/seo ...` + trình score + plan + diffs/drift + reports; verify reports tồn tại + score + findings có evidence + exit codes.
- Giao cho claude các bước cần Claude Code/browser ngoài: toàn bộ execution `/seo audit|page|geo|...` (kèm URLs + business type + lệnh cụ thể — vì hệ sống trong Claude Code ≥1.0.33, agent không-Claude-Code cấm tự nhận đã chạy), `--login`/OAuth Google (user tự làm trong terminal của họ), review visual/screenshots mắt người; cấm agent tự bịa findings. Không có Claude Code thì agent phải khai báo + dừng ở mức đọc docs/so sánh, cấm claim đã audit.
- Agent verify: `FULL-AUDIT-REPORT.md` + `ACTION-PLAN.md` (+ PDF/screenshots khi có) tồn tại + Health Score + findings map đúng lệnh/skill/agent + drift baselines (SQLite) khi compare + Google report khớp quotas.

### Định vị khác biệt (số liệu ngày 02/11/2026 trừ khi ghi khác)
- So với `harlan-zw/unlighthouse` (4.929★/182 forks, API 02/11/2026 — "Run Google Lighthouse on your entire site", open-source): khác độ sâu — unlighthouse chạy Lighthouse đa trang (perf/a11y/BP/SEO lab scores), không có content/E-E-A-T/schema/GEO/backlinks/local/plans/drift/reports; claude-seo là bundle audit SEO đầy đủ (26 skills + 19 agents + 30 lệnh + Google APIs + PDF). Chọn claude-seo thay vì unlighthouse khi cần audit SEO toàn diện + plan + GEO + drift (ngưỡng: cần Health Score + ACTION-PLAN + schema/GEO, không chỉ điểm Lighthouse); chọn unlighthouse khi chỉ cần quét Lighthouse hàng loạt nhanh local, không quota API (nó cũng là 1 extension của claude-seo: `/seo unlighthouse`, MIT, Node 18+).
- So với skill `SEO Audit` của Corey Haines (AgenticSkills A-rank, 55.5K installs theo directory 2026 — audit technical/on-page/content 1 gói): khác quy mô — 1 skill đơn vs bundle 26 skills + 19 agents + drift + Google APIs + extensions trả phí + PDF/Excel. Chọn claude-seo thay vì skill đơn khi cần fan-out đa agents + GEO/agentic + drift + reports giữ lại; chọn skill đơn khi cần audit 1 lần gọn nhẹ trong ChatGPT/Claude/Cursor bất kỳ (không bắt buộc Claude Code).
- So với `AgriciDaniel/chatgpt-seo` (895★/123 forks, API 02/11/2026 — cùng tác giả): khác engine — chatgpt-seo biến 1 page/draft/export thành fix-plan có nguồn TRONG ChatGPT; claude-seo audit site sống TRONG Claude Code bằng agents + browser + APIs. Cùng job học/fix 1 page → chatgpt-seo khi đang ở ChatGPT; audit site + CI/drift → claude-seo.
- Khung trung thực: claude-seo thắng ở độ phủ audit SEO cho Claude Code + evidence + plan + tốc độ cộng đồng (+5,7k★/11 ngày: 19.695 ngày 22/10 theo claude-seo.md → 25.381 ngày 02/11); thua ở tính độc lập engine (bắt buộc Claude Code ≥1.0.33 — OpenCode/Cursor phải delegate hoặc làm tay), thua ở phí ẩn (token plan Opus + creds/API ngoài), thua ở tính nguyên bản (audit, không tự lên rank — rank phụ thuộc Google). Cần viết bài mới chuẩn SEO → `claude-blog` (2.606★ cùng tác giả); cần quảng cáo → claude-ads; cần deterministic perf scan → unlighthouse.

### Bản đồ phủ usecase (quét HẾT README + `docs/COMMANDS.md` + SKILL.md + agents/ + extensions/ + hooks/ 02/11/2026 — ★ mạnh nhất đầu)
- ★ Audit full site đa agents (crawl tới 500 pages, Health Score, plan): xem Usecase 1.
- Audit 1 trang chuyên sâu (on-page/E-E-A-T/schema/images/sitemap đơn URL): xem Usecase 2.
- GEO/AEO + agent readiness (citability, llms.txt, WebMCP, Agentic Browsing): xem Usecase 3.
- Drift monitoring + Google APIs reporting (SQLite baselines, GSC/PSI/CrUX/GA4/Planner, PDF): xem Usecase 4.
- Trung bình: strategic planning theo industry (`/seo plan saas|local|ecommerce|publisher|agency` + content calendar + roadmap 4 phases + architecture) → dùng khi cần chiến lược, không chỉ audit.
- Trung bình: topic cluster + SXO + programmatic + hreflang + competitor-pages (`/seo cluster|map`, `/seo sxo`, `/seo programmatic`, `/seo hreflang`, `/seo competitor-pages` + `cluster-map.html`) → dùng khi build architecture/content.
- Trung bình: images + sitemap generate (`/seo images`, `/seo sitemap generate`, local optimize + IPTC) → dùng khi media/sitemap là bottleneck.
- Trung bình: 9 extensions live-data (dataforseo 23 lệnh/9 modules + costs, ahrefs, seranking AI-visibility, profound citations, bing/IndexNow, matomo GA4-alternative, firecrawl crawl/map/scrape/search, banana image-gen, unlighthouse) → dùng khi cần số liệu thật ngoài site.
- KHÔNG hỗ trợ → thay thế: tự động lên rank/cam kết cite (không hệ nào — phụ thuộc Google/LLM) → theo plan + re-audit; deploy fix vào production → user/dev tự làm sau review; viết bài mới → `claude-blog` cùng tác giả; audit ads → claude-ads; spam/black-hat → không hệ nào (cấm); site ToS cấm cào → dừng (không hệ nào).

### Hồ sơ quyết định
- Việc DÙNG (4+, cụ thể): 1. audit full site mình sở hữu ra Health Score + plan 10–15 phút thay vì checklist thủ công; 2. audit 1 page sâu (title/meta/headings/schema/images/CWV) trước publish; 3. đo GEO/agentic readiness (citability, llms.txt, WebMCP); 4. drift baseline/compare/history + Google reports PDF.
- Việc KHÔNG DÙNG (3+, mỗi việc kèm hệ thay thế): 1. system/design UI mới → dùng `../hallmark/`; 2. rebuild app từ URL → dùng `../ai-website-cloner-template/`; 3. viết bài mới → dùng `claude-blog` (2.606★ cùng tác giả); 4. quét Lighthouse hàng loạt thuần túy → dùng `harlan-zw/unlighthouse` (4.929★) hoặc extension `/seo unlighthouse`; 5. fix 1 page trong ChatGPT → dùng `chatgpt-seo` (895★); 6. spam/black-hat/cào không quyền → không hệ nào (cấm).
- Free / tổng + giá: plugin public MIT 0đ (nguồn `LICENSE` + marketplace.json). Bản private early-access cho members Skool Pro (nguồn README "Two versions"). Phí ngoài: token Claude plan (5 agents Opus + còn lại Sonnet — nguồn FAQ) + creds/API của extension tự trả (DataForSEO usage + costs tracking, Ahrefs, SE Ranking, Profound, Google Ads token Tier 3, image providers) + GA4/GSC cần property của user. Không có paid tier cho chính plugin (nguồn claude-seo.md FAQ) — giá Skool Pro tương lai `chưa xác minh`, cấm đoán.
- Ma sát cài đặt: 5 bước (cài Claude Code → 3 lệnh plugin → `/seo setup` → `/seo doctor` → `/seo audit`), hơn chuẩn 1 dòng 4 bước. ĐÃ chạy: clone + đếm (26/19/9/76 test files) + đọc SKILL.md/install.sh/COMMANDS.md/marketplace.json + registry/API. Rào cản: BẮT BUỘC Claude Code ≥1.0.33 (OpenCode/Cursor không chạy `/seo` — phải delegate cho claude hoặc làm tay); Python 3.11–3.14 + Git; Chromium tải riêng (fail không fatal); OAuth Google + keys extension do user tự cắm; audit full tốn token plan hơn page check.
- Đối thủ viral cùng phân khúc: `harlan-zw/unlighthouse` (4.929★/182 forks API 02/11/2026) vs skill `SEO Audit` — Corey Haines (A-rank, 55.5K installs theo AgenticSkills directory 2026).
- Chọn nó thay vì đối thủ khi: cần bundle audit SEO đầy đủ trong Claude Code (26 skills + 19 agents + drift + Google APIs + PDF) với evidence + plan + velocity cộng đồng (+5,7k★/11d). Ví dụ đổi lựa chọn: audit full + drift + GEO → claude-seo; quét Lighthouse hàng loạt nhanh → unlighthouse; audit 1 lần gọn mọi engine → skill SEO Audit đơn.
- TUYỆT ĐỐI không dùng khi: không quyền/ToS cấm cào; spam/black-hat/phishing; hứa rank/cite cụ thể (không hệ nào cam kết được); máy không có Claude Code mà vẫn claim đã audit (observation bịa = FAIL); deploy draft khi chưa có ok tường minh.

### Usecase con 1: audit full site
- Khi dùng: có site (quyền đã xác minh) cần audit toàn diện + Health Score + plan 10–15 phút.
- Khi bỏ qua: 1 page → Usecase 2; chỉ GEO → Usecase 3; theo dõi định kỳ → Usecase 4; cần chiến lược industry → plan (bản đồ phủ).
- Cơ chế khác các usecase khác ở đâu: duy nhất fan-out đa agents song song (9 always-on + 8 conditional, tối đa 17) + crawl tới 500 pages + detect business type + score 0–100; các usecase khác depth-1-URL hoặc time-series/API.
- Lệnh copy-paste: `/seo audit https://example.com` (trong Claude Code đã cài plugin; nguồn `docs/COMMANDS.md`).
- Ngưỡng số cần đạt: crawl tới 500 pages (failed không abort run tương tự crawl); `FULL-AUDIT-REPORT.md` + `ACTION-PLAN.md` tồn tại; Health Score 0–100 + findings xếp thứ tự (cái gì/dựa vào đâu/phụ thuộc gì/verify bằng gì); screenshots/ khi Playwright sẵn.
- Ví dụ input-output (minh họa, không phải mặc định — scope/business type do user pick trước): input "audit full shop của mình (sở hữu đã xác minh), scope toàn site" → output 2 file Markdown + score (vd 64/100) + plan (critical: thiếu Product schema 38 URLs; high: LCP 3,1s mobile; medium: thin category pages) + gaps (GSC chưa cắm nên clicks là ước lượng — nêu rõ).
- Pitfalls riêng: tưởng audit = fix (audit ra plan; fix/deploy là việc khác — `agentic fix` chỉ draft để review); GSC/API chưa cắm mà kết luận traffic chính xác = FAIL (ghi ước lượng + nguồn); site JS nặng hydrate miss — cần rendered path + `--slow`-tương đương, ghi gaps.
- Phân công usecase này: agent chính check quyền/ToS + shortlist scope (user pick — cấm tự chốt rồi audit) + chạy lệnh + trình score/plan; giao claude toàn bộ execution trong Claude Code (kèm URLs + business type) + OAuth user tự làm; verify bằng 2 file + score + evidence map.

### Usecase con 2: audit 1 trang chuyên sâu
- Khi dùng: 1 URL cần soi kỹ trước publish/sau sửa (on-page, E-E-A-T, schema, images, sitemap entry).
- Khi bỏ qua: full site → Usecase 1; GEO → Usecase 3.
- Cơ chế khác các usecase khác ở đâu: depth thay vì breadth — 1 URL qua nhiều lens (title/meta/headings/canonical/robots/OG/schema/alt/sizes/CWV) thay vì fan-out nhiều pages.
- Lệnh copy-paste: `/seo page https://example.com/about` (page); `/seo technical https://example.com`; `/seo content https://example.com/blog/post`; `/seo schema https://example.com`; `/seo images https://example.com`; `/seo sitemap https://example.com/sitemap.xml`.
- Ngưỡng số cần đạt: mỗi lens có verdict + evidence (title length/heading tree/canonical/robots/OG tags/schema types/alt miss + sizes >200KB flag/formats/srcset/lazy/dimensions; sitemap: <50k URLs/file, status, lastmod, no priority/changefreq).
- Ví dụ input-output (minh họa — URL + lens do user pick): input "soi pricing page trước launch" → output verdicts (title 62 chars OK; thiếu FAQ schema — sinh JSON-LD sẵn để review; 3 ảnh >200KB chưa WebP; H2 nhảy cấp) + JSON-LD draft (chưa deploy).
- Pitfalls riêng: schema sinh ra ≠ đã deploy/validate (chạy validate + Google requirements + Rich Results test tay, ghi gaps); ảnh gắn nhãn xong mà quên dimensions → CLS (hook validate-schema chỉ check file sửa, không thay browser test).
- Phân công usecase này: agent chính shortlist lens (user pick) + chạy + trình verdicts/drafts; giao claude execution + review visual; verify bằng verdicts + evidence + drafts chưa deploy.

### Usecase con 3: GEO/AEO + agent readiness
- Khi dùng: cần biết AI (AI Overviews/AI Mode/ChatGPT/Perplexity/Gemini) có cite mình không + agents có dùng được site không.
- Khi bỏ qua: rank cổ điển → Usecase 1/2; theo dõi định kỳ → Usecase 4.
- Cơ chế khác các usecase khác ở đâu: đo citability/agent-access thay vì rank — quotable facts, entity clarity, llms.txt/Markdown delivery/ai-catalog/WebMCP/robots Content-Signal/Lighthouse Agentic score; không đụng GSC rankings.
- Lệnh copy-paste: `/seo geo https://example.com/blog/guide`; `/seo agentic https://example.com` (đo); `/seo agentic fix https://example.com` (chỉ draft robots/llms.txt/ai-catalog/WebMCP để review, nothing deployed); `/seo agentic lighthouse https://example.com`.
- Ngưỡng số cần đạt: citability verdict + structural/entity/authority checklist; Agentic result X-of-N (trừ N/A + informative); robots groups per AI purpose + Content-Signal lines; files draft tồn tại (chưa deploy).
- Ví dụ input-output (minh họa — URL do user pick): input "đo guide mới cho AI cite" → output citability (thiếu số liệu quotable + bảng so sánh) + llms.txt draft + WebMCP scaffold + gaps (Profound/SE Ranking chưa cắm nên citation-rate là ước lượng).
- Pitfalls riêng: tưởng draft = đã triển khai (fix KHÔNG deploy — review + user tự đẩy); citation-rate không extension thì là ước lượng, cấm ghi số tuyệt đối; hứa "AI sẽ cite" = FAIL (không hệ nào cam kết).
- Phân công usecase này: agent chính shortlist (geo vs agentic vs fix) + chạy + trình verdicts/drafts; giao claude execution + user tự cắm extension/deploy; verify bằng files draft + scores + gaps ghi rõ.

### Usecase con 4: drift + Google APIs report
- Khi dùng: đã có baseline/cần số liệu Google thật + report PDF giữ lại, theo dõi định kỳ.
- Khi bỏ qua: audit 1 lần → Usecase 1/2.
- Cơ chế khác các usecase khác ở đâu: duy nhất time-series + API data — SQLite baselines + 17 rules severity (CRITICAL/HIGH/MEDIUM) + 4-tier Google creds + PDF/HTML qua WeasyPrint/matplotlib; các usecase khác snapshot 1 thời điểm.
- Lệnh copy-paste: `/seo drift baseline https://example.com` rồi `/seo drift compare https://example.com` (xem `history`); Google: `/seo google setup` → `/seo google pagespeed <url>` (Tier 0 key), `/seo google gsc <property>` + `inspect` (Tier 1 OAuth/SA), `/seo google ga4` (Tier 2), `/seo google keywords` (Tier 3 Ads token); report: `/seo google report full`.
- Ngưỡng số cần đạt: baseline SQLite tồn tại; compare phân loại đúng 17 rules + severity; quotas hiển thị (`quotas`); PDF/HTML mở được; Tier thiếu thì lệnh báo thiếu creds (không bịa số).
- Ví dụ input-output (minh họa — cadence do user pick): input "gate weekly: title/meta/canonical/schema drift + CWV" → output baseline + compare (CRITICAL: canonical đổi 12 URLs sau deploy; HIGH: LCP p75 2,4→3,8s theo CrUX 25 tuần) + PDF weekly + gaps (GA4 Tier 2 chưa cắm).
- Pitfalls riêng: baseline không commit/version mà so = gate rỗng; Tier 3 (Ads token) thiếu mà kết luận keyword volume chính xác = FAIL; Indexing API chỉ cho JobPosting/BroadcastEvent-in-VideoObject — URL thường phải đi Inspection/sitemap (nguyên văn docs).
- Phân công usecase này: agent chính pin baseline + chạy compare/reports + trình diffs/quotas + xin duyệt fix/deploy; giao claude execution + user tự OAuth/cắm keys; verify bằng baselines + severity đúng rules + PDF + Tier coverage.

### Các bước chung
1. Xác minh quyền + ToS/robots site nguồn → shortlist lệnh/scope/business type qua question tool, user pick mới chạy (log scope TRƯỚC vì audit 10–15 phút + token plan + data trả phí).
2. Setup: Claude Code 1.0.33+ → 3 lệnh plugin → `/seo setup` (venv + Chromium) → `/seo doctor`; manual thì `install.sh` (tag v2.5.0) — đọc `docs/INSTALLATION.md` khi lỗi.
3. Audit (UC1/UC2): chạy lệnh đã duyệt → fan-out agents → thu reports + score + evidence; JS nặng dùng rendered path, ghi gaps.
4. GEO/agentic (UC3): đo citability/agent-access → drafts để review (không deploy) → cắm extension khi cần số thật.
5. Drift + APIs (UC4): pin baseline (versioned) → compare/history → `/seo google` theo Tier creds → PDF reports.
6. Strategize khi cần: `/seo plan <type>` + cluster/sxo/programmatic/hreflang/competitor-pages + images/sitemap-generate.
7. Deliver: lệnh đã chạy + files + score/diffs/quotas + gaps + quyền đã check (sở hữu/cho phép/học).

### Prompt mẫu
- "Audit full site shop của mình (sở hữu đã xác minh, ToS cho phép) — scope toàn site, business ecommerce. Chạy `/seo audit <url>`. Trình Health Score + ACTION-PLAN + evidence trước khi tôi duyệt fix. Không deploy gì."
- "Soi pricing page trước launch (1 URL): `/seo page <url>` + `/seo schema <url>`. Trình verdicts + JSON-LD draft để review. Schemavalidate đúng Google requirements, thiếu thì ghi gaps."
- "Đo GEO guide mới: `/seo geo <url>` + `/seo agentic <url>`. Trình citability + llms.txt/WebMCP drafts (review-only). Không hứa AI sẽ cite. Extension chưa cắm thì ghi ước lượng."
- "Gate weekly drift + CWV: `/seo drift baseline <url>` rồi compare sau deploy; `/seo google crux-history <url>` + report PDF. Trình severity theo 17 rules. Tier thiếu thì báo, không bịa số."

### Pitfalls
- Không Claude Code mà claim đã audit (lệnh `/seo` chỉ sống trong Claude Code ≥1.0.33 — OpenCode/Cursor phải delegate cho claude hoặc làm tay).
- Tưởng audit = fix/deploy (`agentic fix`/schema chỉ draft review; deploy khi chưa ok tường minh = FAIL).
- Số không creds (GSC/GA4/extension chưa cắm) mà ghi tuyệt đối — fix: ghi ước lượng + nguồn + Tier thiếu.
- Hứa rank/cite cụ thể — fix: không hệ nào cam kết, chỉ plan + re-audit.
- Baseline/draft không version mà gate/deploy — fix: commit baseline, review draft trước.
- Cào mass bỏ qua robots/ToS/rate-limit; spam SEO (nhồi/cloaking/link-farm/review giả) — fix: check trước, dừng khi cấm (cố = FAIL pháp lý).
- Indexing API cho URL thường (chỉ JobPosting/BroadcastEvent-in-VideoObject) — fix: đi Inspection/sitemap theo docs.

### Tham khảo sử dụng (số chốt 02/11/2026)
- Nhận xét sâu: AgenticSkills directory 2026 `https://agenticskills.io/skills/claude-seo` — "the most comprehensive single-author SEO skill bundle in the ecosystem" + liệt kê 25 skills/18 agents (snapshot fetch 04/06/2026) + skill liên quan `SEO Audit` — Corey Haines (A-rank, 55.5K installs) → xác nhận vị thế bundle + chỉ ra alternative gọn nhẹ (skill đơn, mọi engine).
- Nhận xét sâu 2: Medium `@jahanzaibai` 2026 `Claude SEO: Free SEO Audit Tool for Claude Code (2026 Guide)` — walkthrough 3 cách cài (plugin/marketplace, curl|bash, PowerShell) + hệ sinh thái tác giả (Skool 2.700+ free/161 pro $79/tháng — số do bên thứ ba nêu, dùng tham khảo) + verdict workflow audit→report→fix→re-audit → xác nhận ma sát cài + mô hình free.
- Số trung bình có trọng số: GitHub API 02/11/2026: 25.381★/3.344 forks/171 watchers/78 issues (tạo 07/02/2026, push 01/11/2026 — release đều tới v2.5.0 ngày 22/10/2026). Velocity: 19.695★ (22/10 theo claude-seo.md) → 25.381★ (02/11) ≈ +5,7k★/11 ngày; directory snapshot 19.223★ (04/10). Trọng số: velocity + issues mở/đóng PR (48 PRs) cho thấy repo sống mạnh hơn stars tĩnh. YouTube demo tác giả 72.278 views (09/02/2026 — vendor, tham khảo). Reddit r/ClaudeAI PSA (11,5k★ tại thời điểm post — tín hiệu cộng đồng độc lập).
- Mâu thuẫn: vendor claim own-site (10.8K GSC clicks/12 tuần + PageSpeed 99) vs độc lập (chưa có case-study bên thứ ba) → phán quyết: own-site là bằng chứng khả năng tối thiểu, không phải guarantee; chờ case độc lập.
- Tiếng Việt: không tìm thấy review Việt → `chưa xác minh`.

### Tham khảo
- Repo + docs đã mở kiểm tra: `https://github.com/AgriciDaniel/claude-seo` (README Install/Commands/Pricing/FAQ/Extensions/Security/Privacy), `docs/COMMANDS.md` (Quick Reference 30 lệnh + extension rows + fetch contract + tiers + Indexing guard), `skills/seo/SKILL.md` (frontmatter + hub routing + canonical launcher), `install.sh` (REPO_TAG v2.5.0, git check, dirs), `.claude-plugin/marketplace.json` (category marketing, v2.5.0), `hooks/hooks.json` (PostToolUse validate-schema 30s).
- Registry/API đã chạy: GitHub API 2 repos chính + 3 đối thủ/liên quan (`harlan-zw/unlighthouse`, `AgriciDaniel/chatgpt-seo`, `AgriciDaniel/claude-blog`); clone `--depth 1` + đếm (26 skills / 19 agents / 9 extensions / 76 test files).
- Chưa chạy: `/seo setup|doctor|audit` (không Claude Code + tránh cào site thật) — đã ghi WARN.
- Độc lập: Medium guide 2026 + AgenticSkills directory + Reddit PSA + YouTube demo (vendor) + claude-seo.md FAQ (no paid tier).

### Được dùng ở đâu
- Dùng CHO SEO (audit/drift/GEO/reports): xem `../../domains/seo/using-claude-seo.md` — index `../../domains/seo/README.md`.

### Quay lại index
- Về `../../domains/seo/README.md` để so với skill đơn/lighthouse khi cần gọn.
- Xem thêm item liên quan: `../ai-website-cloner-template/` khi audit xong cần rebuild app (khác việc).

---

## English

### When to use
- Need an SEO audit of a website you own/have rights to (or a public URL for learning) as a ranked action plan: technical, E-E-A-T content, schema, Core Web Vitals, GEO/AEO (AI Overviews/ChatGPT/Perplexity/Gemini), local, e-commerce, international — in 10–15 minutes with Claude Code.
- Need parallel-agent audits (up to 17 agents) + a 0–100 SEO Health Score + keepable files (`FULL-AUDIT-REPORT.md`, `ACTION-PLAN.md`, PDF/Excel).
- Need SEO drift tracking over time (`/seo drift baseline|compare|history`, SQLite) or real Google numbers (Search Console, PSI, 25-week CrUX, GA4, Keyword Planner) via `/seo google`.
- Need AI-search/agent readiness: citability (how quotable you are to AI), llms.txt + ai-catalog.json (site-summary files for AI readers), WebMCP scaffolds (draft standard letting agents call web tools), Lighthouse Agentic Browsing (`/seo geo`, `/seo agentic`).

### When to skip
- Need a brand-new gated UI system → use `../hallmark/` (claude-seo audits content/SEO; it generates no design system).
- Need a 1:1 Next.js rebuild from a live URL → use `../ai-website-cloner-template/` (claude-seo builds no app).
- Need someone to write/fix for you (articles, schema into the repo) → implement from the plan yourself (or a sibling writing skill); `agentic fix` only drafts robots/llms.txt/ai-catalog for review, never deploys.
- Sites you may not crawl (ToS bans automation), phishing/impersonation, SEO spam (keyword stuffing, cloaking, link farms) → absolutely forbidden (see [Invariant core](#invariant-core)).

### Install
- Option 1 — plugin marketplace (recommended per origin README; needs Claude Code 1.0.33+): run 3 commands INSIDE Claude Code: `/plugin marketplace add AgriciDaniel/claude-seo`, `/plugin install claude-seo@agricidaniel-claude-seo`, `/seo setup` (isolated Python venv + headless browser, touches nothing else) + `/seo doctor`.
- Option 2 — manual (macOS/Linux): `git clone --depth 1 https://github.com/AgriciDaniel/claude-seo && bash claude-seo/install.sh` (read `install.sh`: requires `git`, pins `REPO_TAG=v2.5.0`, writes `~/.claude/skills/seo` + `~/.claude/agents`; CI guards tag-vs-manifest). Windows: `install.ps1`.
- Requires: Claude Code 1.0.33+, Python 3.11–3.14 (3.10 EOL 10/2026), Git; Playwright Chromium via setup/install (non-fatal failure — only SPA rendering + screenshots lost); extra Linux system libs.
- Verified 02/11/2026: `git clone --depth 1` OK (26 `skills/` dirs, 19 `agents/*.md`, 9 `extensions/` dirs, 76 `tests/test_*.py` files); GitHub API → 25,381 stars/3,344 forks/171 watchers/78 issues, release `v2.5.0` 22/10/2026, pushed 01/11/2026; read `skills/seo/SKILL.md` frontmatter; read `docs/COMMANDS.md` (30-command Quick Reference + extension rows); read `.claude-plugin/marketplace.json` (category `marketing`, v2.5.0).
- Not run: real `/seo setup|doctor|audit` (no Claude Code on this machine + no live-site crawling) — recorded as WARN.

### How the item works
- Backing organization: individual `Agrici Daniel` (AI Workflow Architect, Moldova; AI Marketing Hub community); repo `https://github.com/AgriciDaniel/claude-seo`, MIT, 412 commits (repo page 02/11/2026), release `v2.5.0` 22/10/2026, created 07/02/2026, pushed 01/11/2026. GitHub API 02/11/2026: 25,381 stars / 3,344 forks / 171 watchers / 78 open issues. Same-author family: `chatgpt-seo` (895 stars/123 forks, sourced fix-plans inside ChatGPT), `claude-blog` (2,606 stars/441 forks, SEO-first article writing), `banana` (AI images for SEO).
- Core method: a Claude Code plugin = 1 hub skill `seo` (`/seo $1 $2`, SKILL.md) orchestrating 25 sub-skills (22 core + 1 FLOW framework + 2 extension mirrors) + 19 specialist agents (`agents/seo-*.md`). Full audit: detect business type (SaaS/local/e-commerce/publisher/agency) → fan out up to 17 parallel agents (9 always-on + 8 conditional) → 0–100 SEO Health Score → ranked plan (what / based on what / depends on what / how to verify). Fetching via canonical `scripts/claude-seo run fetch_page.py <url> --json` (raw `--render never` vs rendered `--render auto|always` sharing one JSON contract; fetch errors still emit JSON + exit 1). `PostToolUse` hooks (Edit|Write) run `validate-schema.py` (30s timeout). Reports: keepable Markdown + PDF via WeasyPrint/matplotlib (`/seo google report`) + Excel.
- Per-usecase differences: full multi-page audit (parallel fan-out, up to 500 crawled pages, see [Sub-usecase 1](#sub-usecase-1-full-site-audit)) vs deep single-page audit (depth over breadth, see [Sub-usecase 2](#sub-usecase-2-deep-single-page-audit)) vs GEO/agentic readiness (citability + agent-access files, no classic rank measurement, see [Sub-usecase 3](#sub-usecase-3-geoaeo--agent-readiness)) vs drift + Google APIs (time series + real numbers + PDF, see [Sub-usecase 4](#sub-usecase-4-drift--google-apis-reporting)).

### Invariant core
- Audit first, evidence first: every finding states its source (which DOM fetch/GSC/PSI/API + command run) + how to re-verify; scoreless-without-evidence = FAIL. Unable to name the skill/agent/command used + report files + score = the system was not really used.
- Correct hub routing: unclear-SEO-workflow jobs → hub skill `seo`; already-scoped jobs (schema/backlinks/maps/…) → the specific `seo-*` skill (SKILL.md verbatim). Using the hub for every small job = off-system.
- Rights + white-hat before every URL: only owned/permitted/public-for-learning sites; respect ToS + robots.txt + rate limits; no SEO spam (stuffing, cloaking, link farms, fake reviews), no phishing/impersonation, no reproducing others' brands. Violation = no longer using the system (legal FAIL). State the right + ToS/robots check after every use.
- Draft ≠ deploy: `agentic fix`/schema/llms.txt outputs are for review, never self-pushed to production; deploying without the user's explicit ok = FAIL.

### Customizable surface
- Tunable: in-scope URLs/pages (full site up to 500 pages vs 1 page), business type, workflow/command (30 commands in 6 groups + extensions), agent models (default 5 Opus agents + rest Sonnet — change in `agents/` files, different plan cost), report format (keepable Markdown/PDF/Excel/`cluster-map.html`), numeric bars (images >200KB, 30/50 sitemap location limits), which extensions to wire (9 extensions with their own creds — pay-per-use DataForSEO, Ahrefs, SE Ranking, Profound, Bing/IndexNow keys, Matomo, Firecrawl, Banana/Gemini, local unlighthouse). Two-level approval gate: (1) which artifact — shortlist commands/scope (full vs page vs geo vs drift + URLs + business type) with reasons via question tool, run only after the user picks (10–15 min full audits + plan tokens + paid extension data — log approved scope BEFORE running); (2) what stays/changes — which findings to fix, which drafts to deploy, which keys to wire. Waivers (paid APIs, sensitive sites, deploying drafts) must quote the user's explicit ok. Never list `must-not` items here.

### Work split
- Main agent: rights/ToS + robots checks + scope shortlist (wait for user pick — never self-pick then audit) + install/setup/doctor + run `/seo ...` commands + present score/plan/diffs/drift/reports; verify reports exist + score + evidence + exit codes.
- Hand Claude-Code/browser steps to claude: ALL `/seo audit|page|geo|…` execution (with URLs + business type + concrete commands — the system lives in Claude Code ≥1.0.33; a non-Claude-Code agent must never claim it ran them), `--login`/Google OAuth (user does it in their terminal), human visual/screenshot review; never invent findings. No Claude Code → declare + stop at docs/comparison level, never claim an audit.
- Agent verifies: `FULL-AUDIT-REPORT.md` + `ACTION-PLAN.md` (+ PDF/screenshots when present) exist + Health Score + findings mapped to commands/skills/agents + drift baselines (SQLite) on compare + Google reports matching quotas.

### Differentiating positioning (numbers as of 02/11/2026 unless noted)
- Vs `harlan-zw/unlighthouse` (4,929 stars/182 forks, API 02/11/2026 — "Run Google Lighthouse on your entire site", open source): depth differs — unlighthouse runs multi-page Lighthouse (lab perf/a11y/BP/SEO scores), with no content/E-E-A-T/schema/GEO/backlinks/local/plans/drift/reports; claude-seo is the full SEO audit bundle (26 skills + 19 agents + 30 commands + Google APIs + PDF). Pick claude-seo over unlighthouse for full SEO audits + plans + GEO + drift (bar: Health Score + ACTION-PLAN + schema/GEO needed, not just Lighthouse scores); pick unlighthouse for fast local bulk Lighthouse scans with no API quota (it is also a claude-seo extension: `/seo unlighthouse`, MIT, Node 18+).
- Vs `SEO Audit` by Corey Haines (AgenticSkills A-rank, 55.5K installs per directory 2026 — one-package technical/on-page/content audit): scale differs — one skill vs a 26-skill + 19-agent bundle with drift + Google APIs + paid extensions + PDF/Excel. Pick claude-seo for multi-agent fan-out + GEO/agentic + drift + keepable reports; pick the single skill for one-shot audits on any engine (no Claude Code required).
- Vs `AgriciDaniel/chatgpt-seo` (895 stars/123 forks, API 02/11/2026 — same author): engine differs — chatgpt-seo turns one page/draft/export into a sourced fix-plan INSIDE ChatGPT; claude-seo audits live sites INSIDE Claude Code with agents + browser + APIs. Same single-page learn/fix job → chatgpt-seo when already in ChatGPT; site audit + CI/drift → claude-seo.
- Honest frame: claude-seo wins on SEO-audit coverage for Claude Code + evidence + plans + community velocity (+5.7k stars/11 days: 19,695 on 22/10 per claude-seo.md → 25,381 on 02/11); loses on engine independence (Claude Code ≥1.0.33 required — OpenCode/Cursor must delegate or hand-roll), on hidden costs (Opus plan tokens + external creds/APIs), on originality (it audits; it does not rank you — ranking belongs to Google). New SEO-first articles → `claude-blog` (2,606 stars, same author); ads → claude-ads; deterministic perf scans → unlighthouse.

### Coverage map (scanned ALL of README + docs/COMMANDS.md + SKILL.md + agents/ + extensions/ + hooks/ 02/11/2026 — ★ strongest first)
- ★ Full multi-agent site audit (up to 500 crawled pages, Health Score, plan): see Sub-usecase 1.
- Deep single-page audit (on-page/E-E-A-T/schema/images/sitemap for one URL): see Sub-usecase 2.
- GEO/AEO + agent readiness (citability, llms.txt, WebMCP, Agentic Browsing): see Sub-usecase 3.
- Drift monitoring + Google APIs reporting (SQLite baselines, GSC/PSI/CrUX/GA4/Planner, PDF): see Sub-usecase 4.
- Medium: per-industry strategic planning (`/seo plan saas|local|ecommerce|publisher|agency` + calendar + 4-phase roadmap + architecture) → use for strategy, not just audits.
- Medium: cluster + SXO + programmatic + hreflang + competitor-pages (`/seo cluster|map`, `/seo sxo`, `/seo programmatic`, `/seo hreflang`, `/seo competitor-pages` + `cluster-map.html`) → use when building architecture/content.
- Medium: images + sitemap generation (`/seo images`, `/seo sitemap generate`, local optimize + IPTC) → use when media/sitemap is the bottleneck.
- Medium: 9 live-data extensions (dataforseo 23 commands/9 modules + costs, ahrefs, seranking AI-visibility, profound citations, bing/IndexNow, matomo GA4-alternative, firecrawl crawl/map/scrape/search, banana image-gen, unlighthouse) → use when real numbers beyond the site are needed.
- NOT supported → replacement: automatic ranking/citation guarantees (no system — Google/LLM dependent) → follow the plan + re-audit; deploying fixes to production → user/dev after review; new articles → `claude-blog` (same author); ads audits → claude-ads; spam/black-hat → no system (forbidden); ToS-banned crawling → stop (no system).

### Decision dossier
- Jobs SERVED (4+): 1. full owned-site audits to Health Score + plan in 10–15 minutes instead of manual checklists; 2. deep single-page audits (title/meta/headings/schema/images/CWV) pre-publish; 3. GEO/agentic readiness measurement (citability, llms.txt, WebMCP); 4. drift baselines/compares/history + Google PDF reports.
- Jobs NOT served (each with replacement): 1. new gated UI systems → use `../hallmark/`; 2. runnable Next.js rebuilds from URLs → use `../ai-website-cloner-template/`; 3. new articles → use `claude-blog` (2,606 stars, same author); 4. pure bulk Lighthouse scans → use `harlan-zw/unlighthouse` (4,929 stars) or the `/seo unlighthouse` extension; 5. single-page fixes in ChatGPT → use `chatgpt-seo` (895 stars); 6. spam/black-hat/unpermitted crawling → no system (forbidden).
- Free / total + price: public plugin MIT $0 (sources: `LICENSE` + marketplace.json). Private early-access build for Skool Pro members (source: README "Two versions"). External costs: Claude plan tokens (5 Opus agents + rest Sonnet — source: FAQ) + self-paid extension creds (DataForSEO usage with cost tracking, Ahrefs, SE Ranking, Profound, Google Ads Tier-3 token, image providers) + user's own GA4/GSC properties. No paid tier for the plugin itself (source: claude-seo.md FAQ) — future Skool Pro pricing `unverified`, never guessed.
- Install friction: 5 steps (install Claude Code → 3 plugin commands → `/seo setup` → `/seo doctor` → `/seo audit`), 4 more than the one-line standard. RAN: clone + counts (26/19/9/76 test files) + read SKILL.md/install.sh/COMMANDS.md/marketplace.json + registry/API. Barriers: Claude Code ≥1.0.33 MANDATORY (OpenCode/Cursor cannot run `/seo` — delegate to claude or hand-roll); Python 3.11–3.14 + Git; separately downloaded Chromium (non-fatal failure); Google OAuth + extension keys wired by the user; full audits cost more plan tokens than page checks.
- Viral same-segment opponents: `harlan-zw/unlighthouse` (4,929 stars/182 forks, API 02/11/2026) vs `SEO Audit` — Corey Haines (A-rank, 55.5K installs per AgenticSkills directory 2026).
- Pick it over opponents when: a full SEO audit bundle inside Claude Code (26 skills + 19 agents + drift + Google APIs + PDF) with evidence + plans + community velocity (+5.7k stars/11 days) matters. Choice-flipping example: full audit + drift + GEO → claude-seo; fast bulk Lighthouse → unlighthouse; one-shot audit on any engine → single SEO Audit skill.
- NEVER use when: no rights/ToS-banned crawling; spam/black-hat/phishing; specific rank/citation promises (no system can promise); no Claude Code on the machine while claiming an audit (invented observation = FAIL); deploying drafts without explicit ok.

### Sub-usecase 1: full site audit
- When to use: an owned (rights-verified) site needs a full audit + Health Score + plan in 10–15 minutes.
- When to skip: 1 page → 2; GEO only → 3; periodic tracking → 4; industry strategy → plan (coverage map).
- How its mechanism differs: the only parallel fan-out (9 always-on + 8 conditional agents, up to 17) + up to 500 crawled pages + business-type detection + 0–100 score; others are single-URL depth or time-series/API.
- Copy-paste: `/seo audit https://example.com` (inside Claude Code with the plugin installed; source: `docs/COMMANDS.md`).
- Numeric bar: up to 500 crawled pages (failures never abort, same crawl contract); `FULL-AUDIT-REPORT.md` + `ACTION-PLAN.md` exist; 0–100 Health Score + ranked findings (what/based-on/depends-on/how-to-verify); `screenshots/` when Playwright is ready.
- Input-output example: owned shop, whole-site scope → 2 Markdown files + score (e.g. 64/100) + plan (critical: Product schema missing on 38 URLs; high: mobile LCP 3.1s; medium: thin category pages) + gaps (GSC not wired so click numbers are estimates — stated).
- Own pitfalls: audit ≠ fix (audits produce plans; fixing/deploying is separate — `agentic fix` drafts for review only); unwired GSC/API numbers stated as exact = FAIL (state estimates + source); heavy-JS hydration misses need the rendered path, record gaps.
- Work split: main agent rights/ToS-checks + scope shortlist (user picks — never self-pick then audit) + runs command + presents score/plan; ALL execution in Claude Code goes to claude (with URLs + business type) + OAuth done by the user; verify via 2 files + score + evidence map.

### Sub-usecase 2: deep single-page audit
- When to use: 1 URL needs a close look pre-publish/post-fix (on-page, E-E-A-T, schema, images, sitemap entry).
- When to skip: full site → 1; GEO → 3.
- How its mechanism differs: depth over breadth — one URL through many lenses instead of fanning out over pages.
- Copy-paste: `/seo page https://example.com/about` (page); `/seo technical https://example.com`; `/seo content https://example.com/blog/post`; `/seo schema https://example.com`; `/seo images https://example.com`; `/seo sitemap https://example.com/sitemap.xml`.
- Numeric bar: each lens has a verdict + evidence (title length/heading tree/canonical/robots/OG/schema types/alt gaps + >200KB sizes/formats/srcset/lazy/dimensions; sitemap: <50k URLs/file, statuses, lastmod, no priority/changefreq).
- Input-output example: pre-launch pricing page → verdicts (title 62 chars OK; FAQ schema missing — JSON-LD drafted for review; 3 images >200KB not WebP; skipped H2 level) + JSON-LD draft (not deployed).
- Own pitfalls: generated schema ≠ deployed/validated (validate against Google requirements + Rich Results test by hand, record gaps); labeled images without dimensions → CLS (validate-schema hook only checks edited files, no substitute for browser tests).
- Work split: main agent shortlists lenses (user picks) + runs + presents verdicts/drafts; execution + visual review to claude; verify via verdicts + evidence + undeployed drafts.

### Sub-usecase 3: GEO/AEO + agent readiness
- When to use: need to know whether AI (AI Overviews/AI Mode/ChatGPT/Perplexity/Gemini) will cite the site, and whether agents can use it.
- When to skip: classic rank work → 1/2; periodic tracking → 4.
- How its mechanism differs: measures citability/agent-access instead of rank — quotable facts, entity clarity, llms.txt/Markdown delivery/ai-catalog/WebMCP/robots Content-Signal/Agentic score; no GSC rankings touched.
- Copy-paste: `/seo geo https://example.com/blog/guide`; `/seo agentic https://example.com` (measure); `/seo agentic fix https://example.com` (drafts robots/llms.txt/ai-catalog/WebMCP for review only, nothing deployed); `/seo agentic lighthouse https://example.com`.
- Numeric bar: citability verdict + structural/entity/authority checklist; Agentic X-of-N result (N/A + informative excluded); per-AI-purpose robots groups + Content-Signal lines; draft files exist (undeployed).
- Input-output example: new guide for AI citation → citability gaps (no quotable stats + comparison table) + llms.txt draft + WebMCP scaffold + gaps (Profound/SE Ranking unwired so citation-rate is estimated).
- Own pitfalls: draft ≠ deployed (`fix` never deploys — review + user pushes); extension-less citation rates are estimates, never absolute; promising "AI will cite you" = FAIL (no system can promise).
- Work split: main agent shortlists (geo vs agentic vs fix) + runs + presents verdicts/drafts; execution to claude + user wires extensions/deploys; verify via draft files + scores + explicit gaps.

### Sub-usecase 4: drift + Google APIs reporting
- When to use: baselines exist/real Google numbers + keepable PDF reports needed, tracked periodically.
- When to skip: one-off audits → 1/2.
- How its mechanism differs: the only time-series + API-data path — SQLite baselines + 17 severity rules (CRITICAL/HIGH/MEDIUM) + 4-tier Google creds + WeasyPrint/matplotlib PDFs; others are single-point snapshots.
- Copy-paste: `/seo drift baseline https://example.com` then `/seo drift compare https://example.com` (see `history`); Google: `/seo google setup` → `/seo google pagespeed <url>` (Tier-0 key), `/seo google gsc <property>` + `inspect` (Tier-1 OAuth/SA), `/seo google ga4` (Tier-2), `/seo google keywords` (Tier-3 Ads token); reports: `/seo google report full`.
- Numeric bar: versioned SQLite baseline exists; compares classified by the 17 rules + severity; quotas shown (`quotas`); openable PDF/HTML; missing tiers report missing creds (never invented numbers).
- Input-output example: weekly gate on title/meta/canonical/schema drift + CWV → baseline + compare (CRITICAL: canonical changed on 12 URLs post-deploy; HIGH: CrUX p75 LCP 2.4→3.8s over 25 weeks) + weekly PDF + gaps (GA4 Tier-2 unwired).
- Own pitfalls: unversioned baselines = empty gates; missing Tier-3 (Ads token) with exact volume claims = FAIL; Indexing API is JobPosting/BroadcastEvent-in-VideoObject only — ordinary URLs go via Inspection/sitemaps (docs verbatim).
- Work split: main agent pins baselines + runs compares/reports + presents diffs/quotas + requests fix/deploy approval; execution to claude + user does OAuth/keys; verify via baselines + rule-correct severity + PDF + tier coverage.

### Shared steps
1. Rights + ToS/robots check → shortlist commands/scope/business type via question tool, run only after user pick (log scope FIRST: 10–15 min audits + plan tokens + paid data).
2. Setup: Claude Code 1.0.33+ → 3 plugin commands → `/seo setup` (venv + Chromium) → `/seo doctor`; manual via `install.sh` (tag v2.5.0) — read `docs/INSTALLATION.md` on failure.
3. Audit (1/2): run approved commands → agent fan-out → collect reports + score + evidence; heavy JS uses the rendered path, record gaps.
4. GEO/agentic (3): measure citability/agent-access → review-only drafts (never deploy) → wire extensions for real numbers.
5. Drift + APIs (4): pin versioned baselines → compare/history → `/seo google` per credential tier → PDF reports.
6. Strategize when needed: `/seo plan <type>` + cluster/sxo/programmatic/hreflang/competitor-pages + images/sitemap-generate.
7. Deliver: commands run + files + score/diffs/quotas + gaps + rights statement (owned/permitted/learning).

### Sample prompts
- "Full-audit my owned shop (rights verified, ToS allows) — whole site, ecommerce business. Run `/seo audit <url>`. Present Health Score + ACTION-PLAN + evidence before I approve any fix. Deploy nothing."
- "Deep-check the pricing page pre-launch (1 URL): `/seo page <url>` + `/seo schema <url>`. Present verdicts + JSON-LD draft for review. Validate schema against Google requirements; record gaps instead of guessing."
- "Measure GEO for the new guide: `/seo geo <url>` + `/seo agentic <url>`. Present citability + llms.txt/WebMCP drafts (review-only). Never promise AI will cite. Unwired extensions mean estimates."
- "Weekly drift gate + CWV: `/seo drift baseline <url>` then compare post-deploy; `/seo google crux-history <url>` + PDF report. Present severity per the 17 rules. Missing tiers get reported, never invented."

### Pitfalls
- No Claude Code while claiming an audit (`/seo` commands live only in Claude Code ≥1.0.33 — OpenCode/Cursor must delegate to claude or hand-roll).
- Audit mistaken for fix/deploy (`agentic fix`/schema output is review-only drafts; deploying without explicit ok = FAIL).
- Credential-less numbers stated as absolute (unwired GSC/GA4/extensions) — state estimates + source + missing tier.
- Rank/citation promises — no system can promise; plan + re-audit only.
- Unversioned baselines/drafts used for gating/deploying — version baselines, review drafts first.
- Mass crawling ignoring robots/ToS/rate limits; SEO spam (stuffing/cloaking/link-farms/fake reviews) — check first, stop when banned (forcing = legal FAIL).
- Indexing API for ordinary URLs (JobPosting/BroadcastEvent-in-VideoObject only) — use Inspection/sitemaps per docs.

### Usage references (pinned 02/11/2026)
- Deep review: AgenticSkills directory 2026 `https://agenticskills.io/skills/claude-seo` — "the most comprehensive single-author SEO skill bundle in the ecosystem" + 25 skills/18 agents at 04/06/2026 snapshot + related single `SEO Audit` — Corey Haines (A-rank, 55.5K installs) → confirms bundle positioning + points at the leaner alternative (single skill, any engine).
- Deep review 2: Medium `@jahanzaibai` 2026 `Claude SEO: Free SEO Audit Tool for Claude Code (2026 Guide)` — 3 install paths (plugin/marketplace, curl|bash, PowerShell) + author ecosystem (Skool 2,700+ free/161 pro $79/mo — third-party numbers, reference only) + audit→report→fix→re-audit workflow verdict → confirms install friction + free model.
- Weighted averages: GitHub API 02/11/2026: 25,381 stars/3,344 forks/171 watchers/78 issues (created 07/02/2026, pushed 01/11/2026 — steady releases to v2.5.0 on 22/10/2026). Velocity: 19,695 stars (22/10 per claude-seo.md) → 25,381 (02/11) ≈ +5.7k stars/11 days; directory snapshot 19,223 (04/10). Weight: velocity + open issues/PRs (48 PRs) show a livelier repo than static stars. Author YouTube demo 72,278 views (09/02/2026 — vendor, reference only). Reddit r/ClaudeAI PSA (11.5k stars at post time — independent community signal).
- Conflict: vendor own-site claim (10.8K GSC clicks/12 weeks + PageSpeed 99) vs no third-party case study → verdict: own-site proves minimum capability, not a guarantee; third-party cases pending.
- Vietnamese: no VI review found → `unverified`.

### References
- Checked repos/docs: `https://github.com/AgriciDaniel/claude-seo` (README Install/Commands/Pricing/FAQ/Extensions/Security/Privacy), `docs/COMMANDS.md` (30-command Quick Reference + extension rows + fetch contract + tiers + Indexing guard), `skills/seo/SKILL.md` (frontmatter + hub routing + canonical launcher), `install.sh` (REPO_TAG v2.5.0, git check, dirs), `.claude-plugin/marketplace.json` (category marketing, v2.5.0), `hooks/hooks.json` (PostToolUse validate-schema 30s).
- Ran registries/APIs: both main GitHub APIs + 3 opponent/related repos (`harlan-zw/unlighthouse`, `AgriciDaniel/chatgpt-seo`, `AgriciDaniel/claude-blog`); `--depth 1` clone + counts (26 skills / 19 agents / 9 extensions / 76 test files).
- Not run: `/seo setup|doctor|audit` (no Claude Code + no live-site crawling) — recorded WARN.
- Independent: Medium 2026 guide + AgenticSkills directory + Reddit PSA + YouTube demo (vendor) + claude-seo.md FAQ (no paid tier).

### Where used
- Used FOR SEO (audits/drift/GEO/reports): see `../../domains/seo/using-claude-seo.md` — index `../../domains/seo/README.md`.

### Back to index
- Back to `../../domains/seo/README.md` for leaner alternatives when needed.
- Related item: `../ai-website-cloner-template/` when an audit calls for an app rebuild (different job).
