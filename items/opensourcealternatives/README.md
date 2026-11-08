# opensourcealternatives

## Tiếng Việt

### Dùng khi
- Cần map `paid X → open Y nào` trong dưới 3 phút khi thẩm tra item mới hoặc chọn hệ (tìm đối thủ cùng phân khúc + license + stars sơ bộ).
- Cần lọc nhanh license + độ sống: card ghi license + stars + `Active this week`/`Last commit`, guide ghi ngày review/verify.
- Cần ranked guide có sẵn để ra quyết định: 10 picks xếp hạng, mỗi pick đủ Key Features/Pros/Cons/License & Hosting/Best For + bảng so sánh + migration tiers (vd guide Claude Code: Reviewed Sep 15 2026, Verified Oct 24 2026).
- Cần bắt tool đang lên: trending tuần theo stars gained (số stars tăng thêm trong tuần, chốt tại as-of date — vd as of 8 Nov, REA +25.464/tuần).

### Bỏ qua khi
- Cần quote stars/license vào `items/*/README.md` mà lười re-check: site có refresh lag (card REA 431.018 vs trending 441.320 vs API live 442.194 ngày 08/11/2026) → bắt buộc đối chiếu GitHub API, không quote trực tiếp.
- Cần lệnh cài/cấu hình/verify chạy được → đọc docs chính chủ + repo + chạy thử (site không cho lệnh nào).
- Cần audit sâu 1 tool (cơ chế, gates, pitfalls) → thẩm tra theo VERIFY F (site chỉ là đầu mối tầng 3).
- Cần so sánh gồm cả proprietary → dùng AlternativeTo.net (site này chỉ phủ open-source).

### Cài đặt
- Truy cập (0 bước, không cài đặt, không tài khoản để đọc): mở `https://www.opensourcealternatives.to/` (+ `/alternative-to/<paid-tool>`, `/item/<project>`, `/categories`).
- Newsletter cần email (free, unsubscribe được). Submit/advertise cần email + repo GitHub public (giá tiền cụ thể chưa xác minh).
- Kiểm tra (đã chạy 08/11/2026): fetch homepage + `/alternative-to/claude-code` + `/advertise` (đọc full text); GitHub API đối chiếu 7 repo (hallmark 50.558 vs site 50.351; n8n 209.805 vs 209.760; AppFlowy 78.442 vs 78.217; openclaw 394.173 vs 394.144; rea 442.194 vs 431.018/441.320; impeccable 105.856 vs header 106k; OpenCode 225.393 vs guide 224.587); websearch tìm guide + bài nhắc tới site. Chưa chạy: submit form thật, đo lại sau 1 tuần để tính lag trung bình (ghi WARN).

### Cách item hoạt động
- Tổ chức đứng sau: `chưa xác minh` — footer chỉ ghi `Company` + `© 2026 Open Source Alternatives`; guides ký tên Suraj (vd `By Suraj`); trang advertise dẫn testimonials của sponsors (Elie/Inbox Zero, Stefan/Windshift) + traffic tự báo (166.023 visitors/30d, 66% Google, đo bằng Umami). Không thấy tên pháp nhân/mã nguồn site trong bản fetch 08/11/2026.
- Phương thức hoạt động chung: directory thủ công (1.173 projects/21 categories) — card `Alternative to X + stars + license tag` + trending theo stars gained/tuần + 14 ranked guides (xếp hạng + bảng so sánh + migration notes + `Best For` từng pick) + item pages + search + blog + newsletter; kiếm tiền bằng sponsor cards (`Sponsored`, 7/30 ngày) + form submit/advertise.
- Khác biệt vận hành theo usecase: map nhanh paid→open bằng cards/search (xem [Usecase con 1](#usecase-con-1-map-paid-sang-open-theo-license-stars--manh-nhat)) khác đọc ranked guide ra quyết định (xem [Usecase con 2](#usecase-con-2-doc-ranked-guide-ra-quyet-dinh)) khác track trending tuần (xem [Usecase con 3](#usecase-con-3-track-trending-tuan)) khác verify trước khi quote (re-check API + repo, xem [Usecase con 4](#usecase-con-4-verify-license--freshness-truoc-khi-quote)).

### Cốt lõi bất biến
- Site là đầu mối, không phải verdict: mọi số (stars/license/`Last commit`) quote vào docs phải re-verify qua GitHub API + repo chính chủ ngày đó; quote trực tiếp = FAIL.
- Sponsored ≠ ranked: card `Sponsored` (Windshift, Nuphos, rakazo...) là quảng cáo, không phải pick xếp hạng — lẫn hai loại = FAIL.
- Mọi nhận định dùng được phải gắn ngày đo (stars trôi theo tuần, guide có Reviewed/Verified riêng).
- Sau khi dùng phải nêu được: URL đã mở + ngày + số đã re-check qua API (nguồn nào, ngày nào); không nêu được = chưa thực sự dùng hệ.

### Phần tùy chỉnh
- Được đổi: paid tool target (`/alternative-to/<x>`), category (21 mục), cửa sổ trending (tuần hiện tại), ngưỡng lọc (license MIT/Apache-2.0 vs AGPL/GPL, stars tối thiểu, `Active this week`). Cổng duyệt 2 tầng: (1) shortlist 2-3 ứng viên kèm lý do (license + stars + độ sống) qua question tool, user pick mới đọc sâu guide/repo; (2) quote số nào vào docs thì re-check API trước, ghi ngày đo. Waiver (dùng số site không re-check vì offline/API chặn) phải quote câu ok tường minh của user + ghi `chưa xác minh` cạnh số đó.

### Phân công ai làm gì
- Agent chính: search/category → shortlist cards (user pick) → đọc guide ranked + item pages → đối chiếu GitHub API từng số định quote → trình bảng + khuyến nghị + link.
- Giao cho claude các bước cần browser/người thật: trang JS-heavy không fetch được, verify visual/license badge khi nghi ngờ render sai — kèm URL + field cần lấy + output mong đợi; các URL đã thử 08/11/2026 fetch thẳng được nên mặc định agent tự làm.
- Agent verify: mọi số trong bảng có nguồn API + ngày; license khớp SPDX repo (mã license chuẩn do GitHub nhận diện — vd MIT, AGPL-3.0); sponsored đã tách khỏi ranked.

### Định vị khác biệt (số liệu ngày 08/11/2026)
- So với AlternativeTo.net (viral, crowd, phủ cả proprietary, cần login để vote): khác phạm vi — site này chỉ open-source + tự biên ranked guides có ngày + license/stars hiện ngay trên card. Chọn opensourcealternatives thay vì AlternativeTo khi cần map nhanh `paid X → open Y` kèm license nhìn một phát, không cần proprietary.
- So với GitHub trending/topics + awesome lists (vd awesome-selfhosted): khác curation — trending cho độ nóng thô theo ngôn ngữ, awesome cho list dài không xếp hạng; site này cho `Alternative to X` + bảng so sánh + migration tiers + `Verified` date. Chọn site này thay vì trending/topics khi cần quyết định thay thế cụ thể (giữ subscription/config nào, xem guide Claude Code), không phải lướt xu hướng chung.
- Khung trung thực: thắng ở tốc độ map + license upfront + guides có ngày + trending theo stars gained; thua ở số liệu lag (sections khác nhịp), sponsored lẫn organic, operator + phương pháp `Verified` chưa rõ, không có lệnh cài/audit sâu.

### Bản đồ phủ usecase (quét hết homepage + guide + advertise 08/11/2026 — ★ mạnh nhất đầu)
- ★ Map paid tool → open alternatives + license/stars/activity (search + cards + categories 21 mục): xem Usecase 1.
- Đọc ranked guide ra quyết định (10 picks + comparison + migration + Best For, 14 guides có Reviewed/Verified): xem Usecase 2.
- Trung bình: track trending tuần (stars gained, as-of date) bắt tool đang lên: xem Usecase 3.
- Trung bình: verify trước khi quote (item page + re-check API + repo chính chủ): xem Usecase 4.
- Trung bình: blog + newsletter theo dõi tool mới (vd `Best Open Source AI Video Generators 2026`).
- KHÔNG hỗ trợ → thay thế: lệnh cài/config/audit sâu → docs chính chủ + repo + chạy thử (VERIFY F0); so sánh proprietary → AlternativeTo.net; số stars real-time → GitHub API trực tiếp; review sâu single-tool → blog chuyên sâu (ssdnodes/uichemy).

### Hồ sơ quyết định
- Việc DÙNG (4, cụ thể): 1. map `paid X → open Y` + license/stars sơ bộ khi thẩm tra item mới; 2. đọc ranked guide (pros/cons/migration/Best For) để shortlist đối thủ; 3. track trending tuần bắt tool viral mới; 4. check nhanh license + `Last commit` trước khi đào sâu repo.
- Việc KHÔNG DÙNG (4, mỗi việc kèm hệ thay thế): 1. quote số vào docs → dùng GitHub API trực tiếp; 2. lấy lệnh cài → dùng docs chính chủ; 3. audit sâu → dùng VERIFY F (đọc repo + chạy thử); 4. so sánh proprietary → dùng AlternativeTo.net.
- Free / tổng + giá: đọc web + newsletter 0đ (nguồn `/advertise` fetch 08/11/2026). Tổng sở hữu tra cứu = 0đ + tiền mạng. Submit/advertise/sponsor: giá tiền cụ thể `chưa xác minh`.
- Ma sát cài đặt: 0 bước tới tra cứu đầu (mở URL là đọc). ĐÃ chạy 08/11/2026: fetch 3 URL + API 7 repo + websearch. Chưa chạy: submit form thật + đo lag sau 1 tuần (ghi WARN). Rào cản duy nhất: mạng + email (newsletter/submit).
- Đối thủ viral cùng phân khúc: AlternativeTo.net (crowd, cả proprietary) vs GitHub trending/topics + awesome lists (nóng thô/list dài).
- Chọn nó thay vì đối thủ khi: cần map `paid X → open Y + license + độ sống` dưới 3 phút kèm guide xếp hạng có ngày. Ví dụ đổi lựa chọn: tìm đối thủ cho skill design → site (map + license upfront); vote cộng đồng gồm proprietary → AlternativeTo; xu hướng thô theo ngôn ngữ → GitHub trending.
- TUYỆT ĐỐI không dùng khi: cần số để quote mà offline/API chặn (ghi `chưa xác minh` hoặc bỏ); cần lệnh chạy được; coi sponsored là ranked.

### Usecase con 1: map paid sang open theo license stars (★ mạnh nhất)
- Khi dùng: có 1 paid tool (sở hữu/được phép thay) cần tìm open thay thế khi thẩm tra hoặc chọn hệ.
- Khi bỏ qua: đã có shortlist (sang Usecase 2); cần tool đang lên nói chung (sang Usecase 3); cần quote số (sang Usecase 4).
- Cơ chế khác các usecase khác ở đâu: duy nhất search/category → cards (không xếp hạng sâu); các usecase khác đọc guide, track tuần, hoặc re-check API.
- Lệnh copy-paste: mở `https://www.opensourcealternatives.to/alternative-to/<paid-tool>` (vd `claude-code`) + search site tên paid tool.
- Ngưỡng số cần đạt: shortlist 2-3 ứng viên, mỗi ứng viên đủ 3 field (license SPDX + stars + activity `Active this week`/`Last commit`); tách sponsored khỏi organic.
- Ví dụ input-output (minh họa, số 08/11/2026): input "thay Jira" → output Windshift (sponsored, AGPL-3.0, 404★) tách riêng + OpenProject (17.089★) + Plane (62.127★) + Taiga (385★) để đọc tiếp ở Usecase 2.
- Pitfalls riêng: lấy card đầu tiên làm đáp án (có thể là sponsored); card cũ (stars card ≠ trending — vd REA 431.018 vs 441.320) mà quote luôn.
- Phân công usecase này: agent chính search + shortlist (user pick 2-3) → đọc guide; không cần claude (fetch thẳng được).

### Usecase con 2: đọc ranked guide ra quyết định
- Khi dùng: đã có shortlist 2-3, cầnai thắng theo tiêu chí (giữ subscription/config/history nào).
- Khi bỏ qua: chỉ cần map nhanh (sang Usecase 1); cần số tươi (sang Usecase 4).
- Cơ chế khác các usecase khác ở đâu: duy nhất đọc sâu editorial (ranked + comparison table + migration tiers + Best For từng pick); các usecase khác quét cards/số.
- Lệnh copy-paste: mở guide `/alternative-to/<x>` + đọc 3 mục `Editorial ranking` → `Decision framework` → `Migration`.
- Ngưỡng số cần đạt: quyết định nêu được pick + tiêu chí đo được (vd "giữ Claude subscription + config không rebuild → oh-my-pi; provider freedom từ zero → OpenCode") + ngày Reviewed/Verified của guide.
- Ví dụ input-output (minh họa): input "thay Claude Code, giữ subscription + CLAUDE.md" → output oh-my-pi (auto-discovery config + Anthropic OAuth) thay vì OpenCode (phải rename CLAUDE.md → AGENTS.md), nguồn guide Reviewed Sep 15/Verified Oct 24 2026.
- Pitfalls riêng: `Verified` nghĩa gì không công bố — coi là ngày check lại, không phải chứng nhận độc lập; guide cũ (>3 tháng) mà treat như tươi.
- Phân công usecase này: agent chính đọc + đối chiếu docs chính chủ 1-2 điểm quyết định; giao claude khi guide render thiếu (chưa gặp ở URL đã thử).

### Usecase con 3: track trending tuần
- Khi dùng: cần bắt tool viral mới trong phân khúc (đầu vào cho thẩm tra item mới).
- Khi bỏ qua: đã biết tool cần tra (sang Usecase 1/2).
- Cơ chế khác các usecase khác ở đâu: duy nhất đọc bảng trending (stars gained/tuần + as-of date); không xếp hạng, không verify.
- Lệnh copy-paste: mở homepage mục `Trending open source projects this week` + ghi as-of date.
- Ngưỡng số cần đạt: mỗi ứng viên ghi `+X stars/tuần + as-of date` (vd REA +25.464, as of 8 Nov 2026); trending chỉ là tín hiệu vào, quyết định vẫn qua Usecase 2 + 4.
- Ví dụ input-output (minh họa): input "tool agent tuần này" → output REA (+25.464), T3 Code (+15.602), Agent Desktop (+14.472) + as-of 8 Nov → shortlist đọc tiếp.
- Pitfalls riêng: stars tăng ≠ chất lượng/maintain (phải check `Last commit` + issues ở Usecase 4); as-of date cũ mà tưởng tuần này.
- Phân công usecase này: agent chính quét + shortlist; verify ở Usecase 4.

### Usecase con 4: verify license + freshness trước khi quote
- Khi dùng: bất kỳ số/nhận định nào định đưa vào docs (`items/*/README.md`).
- Khi bỏ qua: chỉ đọc tham khảo nội bộ (ghi rõ số site + ngày, không quote).
- Cơ chế khác các usecase khác ở đâu: duy nhất re-check ngoài site (GitHub API + repo + LICENSE); các usecase khác đọc trong site.
- Lệnh copy-paste: `curl -sL https://api.github.com/repos/<owner>/<repo>` (đọc `stargazers_count` + `license.spdx_id` + `pushed_at`) + mở `LICENSE` repo.
- Ngưỡng số cần đạt: số quote = số API + ngày đo (vd `105.856★ API 08/11/2026`); license = SPDX repo (vd AppFlowy AGPL-3.0); lệch site-API >5% thì lấy API + ghi chú lag.
- Ví dụ input-output (đã chạy thật 08/11/2026): input "quote stars hallmark" → `curl .../Nutlope/hallmark` → 50.558 (site 50.351, lệch 0,4% — dùng API) + `Apache-2.0`... (hallmark MIT? — kiểm tra LICENSE repo trước khi ghi; ví dụ này chỉ minh họa flow, số license lấy từ API field).
- Pitfalls riêng: `CustomLicence ... with additional terms` (vd LobeHub, MinerU) đọc lướt thành Apache-2.0/MIT thuần — mở LICENSE thật; owner path cũ redirect (vd `anomalyco/opencode` → repo thật, stars vẫn đúng) — dùng URL redirect cuối.
- Phân công usecase này: agent chính chạy API + đọc LICENSE (user không cần pick — đây là gate máy); claude không cần trừ khi repo chặn fetch.

### Các bước chung (quy trình tra cứu chuẩn)
1. Map: search/category paid tool → shortlist 2-3 cards (tách sponsored), mỗi ứng viên đủ license + stars + activity.
2. Quyết định: mở ranked guide → đọc ranking + comparison + migration + Best For → chốt pick theo tiêu chí đo được (giữ gì: subscription/config/history).
3. Tươi: check trending nếu cần bắt tool mới (ghi as-of date).
4. Verify: mọi số định quote → GitHub API + LICENSE repo + ngày đo; lệch >5% lấy API.
5. Ghi: nêu URL + ngày + số API (core-fidelity của nguồn tra cứu).

### Prompt mẫu
- "Map open alternative cho `<paid-tool>` trên opensourcealternatives.to: shortlist 2-3 (tách sponsored), mỗi ứng viên đủ license + stars + activity."
- "Đọc guide `/alternative-to/<x>`: chốt 1 pick theo tiêu chí (giữ subscription/config/history), nêu Reviewed/Verified date."
- "Quét trending tuần này: liệt kê top tool phân khúc `<y>` kèm +stars/tuần + as-of date, không kết luận vội."
- Ví dụ điền sẵn: "Map open alternative cho Jira (08/11/2026): mở `/alternative-to/jira`, shortlist Windshift/Plane/OpenProject (tách sponsored Windshift), đọc guide rồi chốt theo tiêu chí self-host + AGPL ok, verify stars qua API trước khi quote."

### Pitfalls
- Sponsored đọc thành ranked (card `Sponsored` là quảng cáo — verdict chỉ từ guide ranking + repo).
- Quote stars/license card mà không re-check API (lag nội bộ đã đo: REA 431.018 vs 442.194 live).
- Owner path cũ (`anomalyco/opencode`) tưởng repo khác — redirect còn sống, stars đúng; luôn theo redirect cuối.
- `CustomLicence ... with additional terms` đọc thành MIT/Apache thuần (LobeHub, MinerU, Sherlock) — mở LICENSE thật.
- `Verified <ngày>` hiểu thành chứng nhận độc lập (phương pháp chưa công bố — chỉ là ngày check lại).
- Guide >3 tháng treat như tươi (check Reviewed/Verified trước khi dùng).
- Operator + giá submit/advertise chưa rõ — không claim "miễn phí toàn bộ".

### Tham khảo sử dụng (quyết định được + số có trọng số, chốt 08/11/2026)
- Nhận xét sâu (thẩm tra trực tiếp phiên này): đối chiếu 7 cặp site-vs-API — hallmark 50.351 vs 50.558, n8n 209.760 vs 209.805, AppFlowy 78.217 vs 78.442, openclaw 394.144 vs 394.173, impeccable header 106k vs 105.856, OpenCode guide 224.587 vs 225.393 (đều lệch <1%, drift tuần) + REA lộ lag nội bộ (431.018 vs 441.320 vs 442.194) → xác nhận quyết định: dùng site để map/shortlist, quote phải qua API.
- Nhận xét sâu (đọc guide): [`/alternative-to/claude-code`](https://www.opensourcealternatives.to/alternative-to/claude-code) (By Suraj, Reviewed Sep 15 2026, Verified Oct 24 2026) — 10 ranked + bảng so sánh (license/model choice/subscription reuse/CLAUDE.md/session import) + migration 3 tiers + Best For từng pick → xác nhận quyết định: guide đủ để shortlist đối thủ có tiêu chí, không thay đọc repo/chạy thử.
- Số trung bình có trọng số: 1.173 projects/21 categories (homepage 08/11; trang guide ghi 1.167 — lag nội bộ) + 14 guides + traffic tự báo 166.023 visitors/30d (3.182–9.675/ngày, 66% Google, Umami) + 47.466 visitors/7d (counter homepage). Trọng số: số API re-check đáng tin nhất; traffic/projects do site tự báo, tin ở mức tham khảo.
- Tiếng Việt: truy vấn `opensourcealternatives.to đánh giá` không trả về review Việt độc lập → `chưa xác minh`.
- Mâu thuẫn: số khớp API tốt vs lag nội bộ + sponsored lẫn organic + operator mờ → phán quyết: nguồn discovery hạng tốt, nguồn quote hạng kém — luôn qua gate Usecase 4.

### Tham khảo
- Site: https://www.opensourcealternatives.to/ (+ `/alternative-to/claude-code`, `/advertise`, `/item/*`)
- Đọc theo thứ tự: homepage (cards + trending + categories) → `/alternative-to/<x>` (ranking + comparison + migration) → `/item/<y>` (license/hosting/Best For) → GitHub API + repo `LICENSE` (verify trước khi quote).
- Đã verify 08/11/2026: fetch 3 URL + API 7 repo + websearch. Chưa chạy: submit form thật + đo lag sau 1 tuần (WARN).

### Được dùng ở đâu
- Dùng CHO lookup: xem `../../domains/lookup/using-opensourcealternatives.md` (map + guide + trending + verify) — index `../../domains/lookup/README.md`.

### Quay lại index
- Về `../../domains/lookup/README.md` để xem hướng dẫn tra cứu chung.
- Xem thêm quy trình thẩm tra: `../../VERIFY.md` (mục F — site này là đầu mối tầng 3, không thay tầng 1).

---

## English

### When to use
- Map `paid X → which open Y` in under 3 minutes during new-item audits or system selection (same-segment opponents + license + preliminary stars).
- Fast license + vitality filtering: cards show license + stars + `Active this week`/`Last commit`; guides carry review/verify dates.
- Ranked guides for decisions: 10 ranked picks, each with Key Features/Pros/Cons/License & Hosting/Best For + comparison table + migration tiers.
- Catch rising tools: weekly trending by stars gained (stars added that week, pinned by an as-of date).

### When to skip
- Quoting stars/licenses into `items/*/README.md` without re-checking: the site has refresh lag → always cross-check the GitHub API, never quote directly.
- Runnable install/config/verification commands → canonical docs + repo + trial runs (the site gives no commands).
- Deep single-tool audits (mechanism, gates, pitfalls) → audit per VERIFY F (the site is a tier-3 lead source).
- Comparisons including proprietary tools → AlternativeTo.net (this site is open-source only).

### Install
- Access (0 steps, no install, no account to read): open `https://www.opensourcealternatives.to/` (+ `/alternative-to/<paid-tool>`, `/item/<project>`, `/categories`).
- Newsletter needs email (free, unsubscribable). Submit/advertise needs email + a public GitHub repo (exact pricing `unverified`).
- Verified 08/11/2026: 3 URL fetches + 7-repo GitHub API cross-checks + websearch. NOT run: a real submit + a one-week-later lag re-measurement (WARN).

### How the item works
- Backing organization: `unverified` — footer only says `Company` + `© 2026 Open Source Alternatives`; guides signed Suraj; the advertise page cites sponsor testimonials + self-reported traffic (166,023 visitors/30d, 66% Google, via Umami). No legal entity/site source found in the 08/11/2026 fetch.
- Core operating method: handpicked directory (1,173 projects/21 categories) — cards (`Alternative to X` + stars + license tag) + weekly stars-gained trending + 14 ranked guides (ranking + comparison + migration notes + per-pick `Best For`) + item pages + search + blog + newsletter; monetized via sponsor cards (`Sponsored`, 7/30 days) + submit/advertise forms.
- Per-usecase differences: fast paid→open mapping via cards/search ([Sub-usecase 1](#sub-usecase-1-map-paid-to-open-by-license-stars--strongest)) vs decision-grade ranked guides ([Sub-usecase 2](#sub-usecase-2-read-a-ranked-guide-to-decide)) vs weekly trending ([Sub-usecase 3](#sub-usecase-3-track-weekly-trending)) vs pre-quote verification (API + repo re-check, [Sub-usecase 4](#sub-usecase-4-verify-license--freshness-before-quoting)).

### Invariant core
- The site is a lead, never the verdict: every number (stars/license/`Last commit`) quoted into docs must be re-verified via the GitHub API + canonical repo on that date; direct quoting = FAIL.
- Sponsored ≠ ranked: `Sponsored` cards are ads, not ranked picks — mixing them = FAIL.
- Every usable claim pins its measurement date (stars drift weekly; guides have their own Reviewed/Verified dates).
- After use, state: URLs opened + date + API re-checked numbers (which source, which date); otherwise the system was not really used.

### Customizable surface
- Tunables: paid-tool target (`/alternative-to/<x>`), category (21), trending window (current week), filters (MIT/Apache-2.0 vs AGPL/GPL license, minimum stars, `Active this week`). Two-level approval: (1) shortlist 2-3 candidates with reasons (license + stars + vitality) via the question tool, user picks before deep guide/repo reads; (2) any number quoted into docs gets an API re-check first, with the date recorded. Waivers (using site numbers unchecked due to offline/blocked API) must quote the user's explicit ok + mark the number `unverified`.

### Work split
- Main agent: search/category → shortlist cards (user picks) → read ranked guide + item pages → cross-check every quotable number against the GitHub API → present table + recommendation + links.
- Hand browser/human steps to claude as a whole: JS-heavy pages that fail fetching, visual/license-badge verification on suspected misrenders — with URL + fields to extract + expected output; the URLs tried on 08/11/2026 fetched directly, so the agent does it by default.
- Agent verifies: every tabled number has an API source + date; license matches repo SPDX (the standard license identifier GitHub reports — e.g. MIT, AGPL-3.0); sponsored separated from ranked.

### Differentiating positioning
- Vs AlternativeTo.net (viral, crowd, includes proprietary, login to vote): different scope — this site is open-source-only + self-written dated ranked guides + license/stars upfront on cards. Pick opensourcealternatives over AlternativeTo when a fast `paid X → open Y` map with at-a-glance licensing is needed, not proprietary coverage.
- Vs GitHub trending/topics + awesome lists (e.g. awesome-selfhosted): different curation — trending gives raw per-language heat, awesomes give long unranked lists; this site gives `Alternative to X` + comparison tables + migration tiers + `Verified` dates. Pick this site over trending/topics when a concrete replacement decision is needed (which subscription/config to keep), not general trend-surfing.
- Honest frame: wins on mapping speed + upfront licensing + dated guides + stars-gained trending; loses on metric lag (sections refresh out of sync), sponsored/organic mixing, unclear operator + `Verified` method, no install commands or deep audits.

### Coverage map (whole homepage + guide + advertise scanned 08/11/2026 — ★ strongest first)
- ★ Map paid tools → open alternatives + license/stars/activity (search + cards + 21 categories): see Sub-usecase 1.
- Read ranked guides to decide (10 picks + comparison + migration + Best For, 14 guides with Reviewed/Verified): see Sub-usecase 2.
- Medium: track weekly trending (stars gained, as-of date) to catch risers: see Sub-usecase 3.
- Medium: verify before quoting (item page + API + canonical repo re-check): see Sub-usecase 4.
- Medium: blog + newsletter for new-tool tracking.
- NOT supported → use instead: install/config/deep-audit commands → canonical docs + repo + trial runs (VERIFY F0); proprietary comparisons → AlternativeTo.net; real-time stars → the GitHub API directly; deep single-tool reviews → specialist blogs.

### Decision dossier
- Jobs SERVED (4, concrete): 1. map `paid X → open Y` + preliminary license/stars for new-item audits; 2. read ranked guides (pros/cons/migration/Best For) to shortlist opponents; 3. track weekly trending for newly viral tools; 4. fast license + `Last commit` checks before deep repo dives.
- Jobs NOT served (4, each with its replacement): 1. quoting numbers into docs → the GitHub API directly; 2. install commands → canonical docs; 3. deep audits → VERIFY F (repo reads + trial runs); 4. proprietary comparisons → AlternativeTo.net.
- Free / total + price: $0 to read + newsletter (source: `/advertise` fetched 08/11/2026). Total lookup cost = $0 + bandwidth. Submit/advertise/sponsor pricing: `unverified`.
- Install friction: 0 steps to first lookup (open a URL and read). Ran 08/11/2026: 3 fetches + 7-repo API checks + websearch. NOT run: real submit + one-week-later lag measurement (WARN). Only barriers: network + email (newsletter/submit).
- Viral same-segment opponents: AlternativeTo.net (crowd, incl. proprietary) vs GitHub trending/topics + awesome lists (raw heat/long lists).
- Pick it over opponents when: a sub-3-minute `paid X → open Y + license + vitality` map with dated ranked guides is needed. Choice-flipping example: opponents for a design skill → this site (map + upfront licensing); community votes incl. proprietary → AlternativeTo; raw per-language heat → GitHub trending.
- NEVER use when: numbers are needed for quoting while offline/API-blocked (mark `unverified` or skip); runnable commands are needed; sponsored is mistaken for ranked.

### Sub-usecase 1: map paid to open by license stars (★ strongest)
- When to use: one owned/permitted paid tool needs an open replacement during audits or system selection.
- When to skip: shortlist exists → Sub-usecase 2; general risers wanted → Sub-usecase 3; quoting needed → Sub-usecase 4.
- Copy-paste command: open `https://www.opensourcealternatives.to/alternative-to/<paid-tool>` (e.g. `claude-code`) + site-search the paid tool name.
- Numeric bar: 2-3 candidate shortlist, each with all 3 fields (SPDX license + stars + `Active this week`/`Last commit` activity); sponsored split from organic.
- Input-output example (illustrative, 08/11/2026 numbers): "replace Jira" → Windshift (sponsored, AGPL-3.0, 404★) split aside + OpenProject (17,089★) + Plane (62,127★) + Taiga (385★) for Sub-usecase 2.
- Own pitfalls: taking the first card as the answer (may be sponsored); quoting stale cards (card vs trending mismatch — e.g. REA 431,018 vs 441,320).
- Work split: main agent searches + shortlists (user picks 2-3) → reads the guide; no claude needed (direct fetches work).

### Sub-usecase 2: read a ranked guide to decide
- When to use: 2-3 shortlisted, winner needed by criterion (which subscription/config/history to keep).
- When to skip: fast map suffices → Sub-usecase 1; fresh numbers needed → Sub-usecase 4.
- Copy-paste command: open guide `/alternative-to/<x>` + read `Editorial ranking` → `Decision framework` → `Migration`.
- Numeric bar: decision names the pick + measurable criterion (e.g. "keep Claude subscription + config with zero rebuild → oh-my-pi; provider freedom from zero → OpenCode") + the guide's Reviewed/Verified dates.
- Input-output example (illustrative): "replace Claude Code, keep subscription + CLAUDE.md" → oh-my-pi (config auto-discovery + Anthropic OAuth) over OpenCode (requires renaming CLAUDE.md → AGENTS.md), source guide Reviewed Sep 15/Verified Oct 24 2026.
- Own pitfalls: `Verified` method is undisclosed — treat as a re-check date, not independent certification; guides older than ~3 months treated as fresh.
- Work split: main agent reads + cross-checks 1-2 decisive points against canonical docs; claude when guide rendering breaks (not met on tried URLs).

### Sub-usecase 3: track weekly trending
- When to use: catching newly viral tools in a segment (input to new-item audits).
- When to skip: the tool is known → Sub-usecases 1/2.
- Copy-paste command: open homepage `Trending open source projects this week` + record the as-of date.
- Numeric bar: each candidate recorded as `+X stars/week + as-of date` (e.g. REA +25,464, as of 8 Nov 2026); trending is an entry signal only, decisions still go through Sub-usecases 2 + 4.
- Input-output example (illustrative): "agent tools this week" → REA (+25,464), T3 Code (+15,602), Agent Desktop (+14,472) as of 8 Nov → shortlist for deeper reads.
- Own pitfalls: star velocity ≠ quality/maintenance (check `Last commit` + issues in Sub-usecase 4); stale as-of dates mistaken for this week.
- Work split: main agent scans + shortlists; verification in Sub-usecase 4.

### Sub-usecase 4: verify license + freshness before quoting
- When to use: any number/claim bound for docs (`items/*/README.md`).
- When to skip: internal reference reading only (note site numbers + date, never quote).
- Copy-paste command: `curl -sL https://api.github.com/repos/<owner>/<repo>` (read `stargazers_count` + `license.spdx_id` + `pushed_at`) + open the repo `LICENSE`.
- Numeric bar: quoted number = API number + date (e.g. `105,856 stars API 08/11/2026`); license = repo SPDX; site-API gaps over ~5% take the API value + a lag note.
- Input-output example (actually ran 08/11/2026): "quote hallmark stars" → `curl .../Nutlope/hallmark` → 50,558 (site 50,351, 0.4% gap — use API) + license from the repo `LICENSE` before writing.
- Own pitfalls: `CustomLicence ... with additional terms` skimmed as pure MIT/Apache (LobeHub, MinerU, Sherlock) — open the real LICENSE; stale owner paths that redirect (e.g. `anomalyco/opencode` → the live repo, stars still correct) — follow the final redirect.
- Work split: main agent runs the API + reads LICENSE (no user pick — a machine gate); claude only when a repo blocks fetching.

### Shared steps (standard lookup flow)
1. Map: search/category the paid tool → 2-3-card shortlist (sponsored split), each with license + stars + activity.
2. Decide: open the ranked guide → ranking + comparison + migration + Best For → pick by measurable criterion (what to keep: subscription/config/history).
3. Freshen: check trending for new risers when needed (record as-of date).
4. Verify: every quotable number → GitHub API + repo LICENSE + date; gaps over ~5% take the API.
5. Record: state URL + date + API numbers (lookup-source core-fidelity).

### Sample prompts
- "Map open alternatives for `<paid-tool>` on opensourcealternatives.to: 2-3 shortlist (sponsored split), each with license + stars + activity."
- "Read guide `/alternative-to/<x>`: settle one pick by criterion (keep subscription/config/history), state Reviewed/Verified dates."
- "Scan this week's trending: list top segment-`<y>` tools with +stars/week + as-of date, no premature verdicts."
- Filled example: "Map open alternatives for Jira (08/11/2026): open `/alternative-to/jira`, shortlist Windshift/Plane/OpenProject (Windshift is sponsored — split it), read the guide and settle by self-host + AGPL-ok criteria, API-verify stars before quoting."

### Pitfalls
- Sponsored read as ranked (`Sponsored` cards are ads — verdicts come only from guide rankings + repos).
- Quoting card stars/licenses without API re-checks (measured internal lag: REA 431,018 vs 442,194 live).
- Stale owner paths (`anomalyco/opencode`) mistaken for different repos — redirects alive, stars correct; always follow the final redirect.
- `CustomLicence ... with additional terms` read as pure MIT/Apache (LobeHub, MinerU, Sherlock) — open the real LICENSE.
- `Verified <date>` read as independent certification (method undisclosed — a re-check date only).
- Guides older than ~3 months treated as fresh (check Reviewed/Verified first).
- Unclear operator + submit/advertise pricing — never claim "fully free".

### Usage references (decisive + weighted, pinned 08/11/2026)
- Deep review (direct audit this session): 7 site-vs-API pairs — hallmark 50,351 vs 50,558, n8n 209,760 vs 209,805, AppFlowy 78,217 vs 78,442, openclaw 394,144 vs 394,173, impeccable header 106k vs 105,856, OpenCode guide 224,587 vs 225,393 (all under ~1%, weekly drift) + REA exposing internal lag (431,018 vs 441,320 vs 442,194) → confirms: use the site to map/shortlist, quote only via API.
- Deep read (guide): [`/alternative-to/claude-code`](https://www.opensourcealternatives.to/alternative-to/claude-code) (By Suraj, Reviewed Sep 15 2026, Verified Oct 24 2026) — 10 ranked + comparison table (license/model choice/subscription reuse/CLAUDE.md/session import) + 3-tier migration + per-pick Best For → confirms: guides suffice to shortlist opponents by criterion, never replace repo reads/trial runs.
- Weighted averages: 1,173 projects/21 categories (homepage 08/11; guide page says 1,167 — internal lag) + 14 guides + self-reported traffic 166,023 visitors/30d (3,182–9,675/day, 66% Google, Umami) + 47,466 visitors/7d (homepage counter). Weight: re-checked API numbers most trusted; traffic/project counts are self-reported, reference-grade.
- Vietnamese: query `opensourcealternatives.to đánh giá` returns no independent Vietnamese review → `unverified`.
- Conflict: numbers matching the API well vs internal lag + sponsored/organic mixing + opaque operator → verdict: good-grade discovery source, poor-grade quoting source — always pass gate Sub-usecase 4.

### References
- Site: https://www.opensourcealternatives.to/ (+ `/alternative-to/claude-code`, `/advertise`, `/item/*`)
- Read order: homepage (cards + trending + categories) → `/alternative-to/<x>` (ranking + comparison + migration) → `/item/<y>` (license/hosting/Best For) → GitHub API + repo `LICENSE` (verify before quoting).
- Verified 08/11/2026: 3 URL fetches, 7-repo API checks, websearch. NOT run: a real submit + a one-week-later lag re-measurement (WARN).

### Where used
- Used FOR lookup: see `../../domains/lookup/using-opensourcealternatives.md` (map + guide + trending + verify) — index `../../domains/lookup/README.md`.

### Back to index
- Back to `../../domains/lookup/README.md` for the shared lookup guide.
- See also the audit procedure: `../../VERIFY.md` (section F — this site is a tier-3 lead source, never tier-1).
