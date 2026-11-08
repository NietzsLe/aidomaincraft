# domains/lookup/

## Tiếng Việt

Domain lookup — tra cứu đối thủ/license/độ sống của tool khi thẩm tra item mới hoặc chọn hệ. Đọc `using-*.md` tương ứng (phần riêng lookup + link về gốc). Chi tiết gốc sống trong `items/*/README.md`; index này chỉ điều hướng + định vị.

### Bảng điều hướng: việc → item(s)
| Việc cần làm | Item chính (mỗi cái 1 cách) | Item hỗ trợ | Lệnh bắt đầu |
|---|---|---|---|
| Map paid tool → open alternatives + license/stars/activity | `opensourcealternatives` (directory + ranked guides — xem `using-opensourcealternatives.md`) | GitHub API + repo chính chủ (re-verify số/license, ngoài kho item) | mở `https://www.opensourcealternatives.to/alternative-to/<paid-tool>` |
| Đọc ranked guide ra quyết định giữ/bỏ gì | `opensourcealternatives` (10 picks + comparison + migration + Best For — xem `using-opensourcealternatives.md`) | docs chính chủ 1-2 điểm quyết định (ngoài kho item) | đọc `Editorial ranking` → `Decision framework` → `Migration` |
| Track tool viral mới theo tuần | `opensourcealternatives` (trending stars gained + as-of date — xem `using-opensourcealternatives.md`) | GitHub trending/topics (ngoài kho item, khi cần nhiệt thô) | đọc `Trending open source projects this week` + ghi as-of date |
| Verify số/license trước khi quote vào docs | `opensourcealternatives` (quy trình Usecase 4 — xem `using-opensourcealternatives.md`) | GitHub API `curl .../repos/<owner>/<repo>` + `LICENSE` repo (ngoài kho item, gate bắt buộc) | `curl -sL https://api.github.com/repos/<owner>/<repo>` |

Việc map có 1 chính (directory nhanh nhất cho `paid X → open Y`); verify số/license có hỗ trợ bắt buộc là GitHub API (site lag nội bộ đã đo: REA 431.018 vs 442.194 live 08/11/2026).

### Bảng định vị
| Item | Mục đích điển hình | Vận hành tóm tắt 1 câu | Điểm mạnh | Điểm yếu | Dùng chính khi | Tránh khi | Thay thế bởi | Vì sao chọn A thay vì B trong case này |
|---|---|---|---|---|---|---|---|---|
| `opensourcealternatives` — chi tiết lookup ở `using-opensourcealternatives.md`, gốc ở `../../items/opensourcealternatives/README.md` | map paid→open + ranked guides + trending + gate verify | cards (license/stars/activity) + 14 ranked guides + trending stars/tuần + re-check API trước khi quote | map dưới 3 phút, license upfront, guides có Reviewed/Verified, trending bắt tool mới | số lag nội bộ, sponsored lẫn organic, operator + phương pháp Verified mờ, không lệnh cài | cần đối thủ/license/độ sống nhanh có xếp hạng khi thẩm tra | cần quote số (phải qua API), cần lệnh chạy, so sánh proprietary | AlternativeTo.net khi cần proprietary; GitHub API khi cần số tươi; docs chính chủ khi cần lệnh | Chọn opensourcealternatives thay vì GitHub trending khi quyết định phụ thuộc vào map `paid X → open Y` cụ thể + migration notes, không phải nhiệt thô theo ngôn ngữ |

### Ma trận chồng lấn
| Việc | `opensourcealternatives` | Tiêu chí chọn phân biệt |
|---|---|---|
| Map paid→open + license/stars/activity | chính | cần `Alternative to X` + license upfront dưới 3 phút → site; cần vote cộng đồng gồm proprietary → AlternativeTo |
| Ranked guide ra quyết định | chính | cần xếp hạng + migration tiers có ngày → site; cần review sâu single-tool → blog chuyên sâu |
| Trending tool mới | chính | cần stars gained/tuần theo phân khúc → site; cần nhiệt thô đa ngôn ngữ → GitHub trending |
| Quote số/license vào docs | hỗ trợ (đầu mối) + GitHub API bắt buộc (gate) | số quote = số API + ngày đo; lệch >5% lấy API |

### Workflow phối hợp mẫu
Map bằng site (shortlist 2-3, tách sponsored) → quyết định bằng ranked guide (pick theo tiêu chí giữ subscription/config/history) → tươi bằng trending khi cần (ghi as-of) → verify bằng GitHub API + `LICENSE` repo trước mọi quote → ghi URL + ngày + số API.

### Danh sách using-doc
- `using-opensourcealternatives.md` — dùng opensourcealternatives CHO lookup → gốc `../../items/opensourcealternatives/README.md`

---

## English

Lookup domain — opponent/license/vitality research for tools during new-item audits or system selection. Read the matching `using-*.md` (lookup-only deltas + links to origin). Origin details live in `items/*/README.md`; this index only routes + positions.

### Routing: job → item(s)
| Job | Primary item(s) (each a different way) | Supporting item | Starter command |
|---|---|---|---|
| Map paid tool → open alternatives + license/stars/activity | `opensourcealternatives` (directory + ranked guides — see `using-opensourcealternatives.md`) | GitHub API + canonical repos (re-verify numbers/licenses, outside the item store) | open `https://www.opensourcealternatives.to/alternative-to/<paid-tool>` |
| Read a ranked guide to decide what to keep/drop | `opensourcealternatives` (10 picks + comparison + migration + Best For — see `using-opensourcealternatives.md`) | 1-2 decisive canonical docs (outside the item store) | read `Editorial ranking` → `Decision framework` → `Migration` |
| Track newly viral tools weekly | `opensourcealternatives` (stars-gained trending + as-of date — see `using-opensourcealternatives.md`) | GitHub trending/topics (outside the item store, for raw heat) | read `Trending open source projects this week` + record as-of date |
| Verify numbers/licenses before quoting into docs | `opensourcealternatives` (Sub-usecase 4 flow — see `using-opensourcealternatives.md`) | GitHub API `curl .../repos/<owner>/<repo>` + repo `LICENSE` (outside the item store, mandatory gate) | `curl -sL https://api.github.com/repos/<owner>/<repo>` |

Mapping has 1 primary (fastest `paid X → open Y` directory); number/license verification mandatorily supports with the GitHub API (measured internal site lag: REA 431,018 vs 442,194 live 08/11/2026).

### Positioning
| Item | Typical purposes | 1-sentence operating summary | Strengths | Weaknesses | Use as primary when | Avoid when | Replaced by | Why pick A over B in this case |
|---|---|---|---|---|---|---|---|---|
| `opensourcealternatives` — lookup details in `using-opensourcealternatives.md`, origin at `../../items/opensourcealternatives/README.md` | paid→open mapping + ranked guides + trending + verify gate | cards (license/stars/activity) + 14 ranked guides + weekly stars trending + API re-check before quoting | sub-3-minute maps, upfront licensing, dated guides, riser-catching trending | internal metric lag, sponsored/organic mixing, opaque operator + `Verified` method, no install commands | fast ranked opponent/license/vitality data during audits | quoting numbers (must pass API), runnable commands, proprietary comparisons | AlternativeTo.net for proprietary; GitHub API for fresh numbers; canonical docs for commands | Pick opensourcealternatives over GitHub trending when a concrete `paid X → open Y` map + migration notes decide, not raw per-language heat |

### Overlap matrix
| Job | `opensourcealternatives` | Distinguishing selection rule |
|---|---|---|
| Paid→open map + license/stars/activity | primary | sub-3-minute `Alternative to X` + upfront licensing → site; community votes incl. proprietary → AlternativeTo |
| Ranked-guide decision | primary | dated ranking + migration tiers → site; deep single-tool review → specialist blogs |
| New-tool trending | primary | per-segment stars-gained/week → site; raw multi-language heat → GitHub trending |
| Quoting numbers/licenses into docs | supporting (lead) + mandatory GitHub API (gate) | quoted number = API number + date; gaps over ~5% take the API |

### Sample combined workflow
Map via the site (2-3 shortlist, sponsored split) → decide via the ranked guide (pick by keep-subscription/config/history criteria) → freshen via trending when needed (record as-of) → verify via GitHub API + repo `LICENSE` before any quote → record URL + date + API numbers.

### Using-doc list
- `using-opensourcealternatives.md` — use opensourcealternatives FOR lookup → origin `../../items/opensourcealternatives/README.md`
