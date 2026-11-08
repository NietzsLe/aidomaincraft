# using-opensourcealternatives CHO lookup (CHARTER v12)

> Phần RIÊNG khi dùng opensourcealternatives cho lookup. Gốc sống ở `../../items/opensourcealternatives/README.md`; mọi lệnh/ngưỡng dưới đây khớp từng chữ với gốc. Không copy lại toàn bộ cài đặt/cơ chế.

## Tiếng Việt

### Usecase trong domain này
- ★ Map paid tool → open alternatives + license/stars/activity: xem [Usecase con 1](../../items/opensourcealternatives/README.md#usecase-con-1-map-paid-sang-open-theo-license-stars--manh-nhat).
- Đọc ranked guide ra quyết định giữ/bỏ gì: xem [Usecase con 2](../../items/opensourcealternatives/README.md#usecase-con-2-doc-ranked-guide-ra-quyet-dinh).
- Track tool viral mới theo tuần: xem [Usecase con 3](../../items/opensourcealternatives/README.md#usecase-con-3-track-trending-tuan).
- Verify license + freshness trước khi quote vào docs: xem [Usecase con 4](../../items/opensourcealternatives/README.md#usecase-con-4-verify-license--freshness-truoc-khi-quote).

### Lệnh mẫu cụ thể (cho lookup)
- Map: mở `https://www.opensourcealternatives.to/alternative-to/<paid-tool>` + search tên paid tool, shortlist 2-3 (tách sponsored) — xem [Usecase con 1](../../items/opensourcealternatives/README.md#usecase-con-1-map-paid-sang-open-theo-license-stars--manh-nhat).
- Guide: đọc `Editorial ranking` → `Decision framework` → `Migration` trong guide, chốt pick theo tiêu chí giữ subscription/config/history — xem [Usecase con 2](../../items/opensourcealternatives/README.md#usecase-con-2-doc-ranked-guide-ra-quyet-dinh).
- Trending: đọc `Trending open source projects this week` + ghi as-of date — xem [Usecase con 3](../../items/opensourcealternatives/README.md#usecase-con-3-track-trending-tuan).
- Verify: `curl -sL https://api.github.com/repos/<owner>/<repo>` + mở `LICENSE` repo trước mọi quote — xem [Usecase con 4](../../items/opensourcealternatives/README.md#usecase-con-4-verify-license--freshness-truoc-khi-quote).

### Lưu ý riêng cho lookup
- Mọi số định quote vào `items/*/README.md` phải qua gate Usecase 4 (API + ngày đo); lệch site-API >5% lấy API — nguồn [Usecase con 4](../../items/opensourcealternatives/README.md#usecase-con-4-verify-license--freshness-truoc-khi-quote). Đây là điểm khác mọi domain khác: lookup là đầu mối, không phải verdict.
- Sponsored tách khỏi ranked trước khi shortlist — nguồn [Cốt lõi](../../items/opensourcealternatives/README.md#cot-loi-bat-bien).
- `CustomLicence ... with additional terms` phải mở LICENSE thật, không đọc thành MIT/Apache thuần — nguồn [Pitfalls](../../items/opensourcealternatives/README.md#pitfalls).

### Điểm mạnh cốt lõi CHO lookup
- Map `paid X → open Y` dưới 3 phút kèm license upfront + ranked guides có Reviewed/Verified + trending stars/tuần — thứ GitHub trending (nhiệt thô) và AlternativeTo (thiếu license upfront + guides) đều không gánh cùng lúc. Xem [Định vị](../../items/opensourcealternatives/README.md#dinh-vi-khac-biet-so-lieu-ngay-08112026).
- Gate verify (site → API → LICENSE) cho số quote vào docs đạt chuẩn VERIFY F0 tầng 1.

### Phân công CHO domain này
- Agent chính search → shortlist 2-3 (user pick) → đọc guide → đối chiếu API → trình bảng + khuyến nghị; bước cần browser giao nguyên cục cho claude khi fetch lỗi. Chi tiết: [Phân công gốc](../../items/opensourcealternatives/README.md#phan-cong-ai-lam-gi).

### Link về item gốc (3 chiều)
- Gốc: `../../items/opensourcealternatives/README.md` (Truy cập / Cách hoạt động / Định vị / Bản đồ phủ / Hồ sơ quyết định / Usecase 1-4 / Pitfalls / Tham khảo sử dụng).
- Index domain: `./README.md` (hàng opensourcealternatives ở điều hướng + định vị + chồng lấn).
- Được liệt kê ngược tại: `../../items/opensourcealternatives/README.md#duoc-dung-o-dau`.

---

## English

Lookup-only deltas for opensourcealternatives. Origin lives at `../../items/opensourcealternatives/README.md`; commands/bars below match it word-for-word.

### Usecases in this domain
- ★ Map paid tools → open alternatives + license/stars/activity: see [Sub-usecase 1](../../items/opensourcealternatives/README.md#sub-usecase-1-map-paid-to-open-by-license-stars--strongest).
- Read ranked guides to decide what to keep/drop: see [Sub-usecase 2](../../items/opensourcealternatives/README.md#sub-usecase-2-read-a-ranked-guide-to-decide).
- Track newly viral tools weekly: see [Sub-usecase 3](../../items/opensourcealternatives/README.md#sub-usecase-3-track-weekly-trending).
- Verify licenses + freshness before quoting into docs: see [Sub-usecase 4](../../items/opensourcealternatives/README.md#sub-usecase-4-verify-license--freshness-before-quoting).

### Concrete commands (for lookup)
- Map: open `https://www.opensourcealternatives.to/alternative-to/<paid-tool>` + site-search, 2-3 shortlist (sponsored split).
- Guide: read `Editorial ranking` → `Decision framework` → `Migration`, settle by keep-subscription/config/history criteria.
- Trending: read `Trending open source projects this week` + record as-of date.
- Verify: `curl -sL https://api.github.com/repos/<owner>/<repo>` + repo `LICENSE` before any quote.

### Domain-specific notes
- Every quotable number passes the Sub-usecase 4 gate (API + date); gaps over ~5% take the API. Unlike other domains, lookup is a lead, never the verdict.
- Sponsored split from ranked before shortlisting. `CustomLicence ...` terms require opening the real LICENSE.

### Core strengths FOR lookup
- Sub-3-minute `paid X → open Y` maps with upfront licensing + dated ranked guides + weekly stars trending — neither GitHub trending nor AlternativeTo covers all three at once.
- The verify gate (site → API → LICENSE) makes quoted numbers VERIFY-F0-tier-1 grade.

### Work split FOR this lookup
- Main agent searches → shortlists 2-3 (user picks) → reads the guide → cross-checks the API → presents table + recommendation; browser steps go to claude as a whole on fetch failure. Details: [origin Work split](../../items/opensourcealternatives/README.md#work-split).

### Links to origin (3-way)
- Origin: `../../items/opensourcealternatives/README.md`. Index: `./README.md`. Backlisted at origin `#where-used`.
