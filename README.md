# aidomaincraft

## Tiếng Việt

**Mục đích:** repo tra cứu theo usecase khi làm dự án cùng AI agent. Mở dự án mới → đọc bảng dưới → vào đúng `domains/<d>/` → đọc `using-<item>.md` → theo link về `items/<x>/` làm theo `README.md` trong đó.

**Nguyên tắc (v8):**
- `items/` = kho item trung lập domain (1 tool = 1 item, vd `items/hallmark/`). Chi tiết gốc sống ở đây.
- `domains/` = hướng dẫn theo lĩnh vực (vd `domains/ui/`, `domains/media/`). Mỗi cặp item-domain có `using-<item>.md` viết phần RIÊNG cho domain + link về item gốc. Một việc có thể có NHIỀU item chính (mỗi cái 1 cách).
- Link 3 chiều bắt buộc: domain index → using-doc → item gốc (đúng section), và ngược lại.
- Luật cấu trúc và version nằm ở `CHARTER.md` (hiện tại v8). Agent và người đều phải tuân thủ.
- Cài sang repo/thư mục khác: `./scripts/install.sh --target /path/to/project --dry-run` rồi `--backup` (xem `INSTALL.md`; gỡ: `UNINSTALL.md`). Mặc định reference-only, agent tự clone nguồn khi cần.

**Bảng chọn:**

| Dự án / nhu cầu | Vào đâu |
|---|---|
| Làm UI (page system, effect React, landing mẫu) | `domains/ui/` |
| Làm media (video launch, deck, OG image) | `domains/media/` |
| Xem gốc 1 tool (cài đặt, cơ chế, giá, review) | `items/<tool>/` |
| Lĩnh vực khác (sau này: hardware, backend...) | thêm thư mục ngang `domains/<mới>/`, không đổi khung |

**Cách dùng cho agent:** xem `AGENTS.md`.

---

## English

**Purpose:** usecase-first lookup repo for building projects with AI agents. New project → check the table → open the matching `domains/<d>/` → read `using-<item>.md` → follow links to `items/<x>/` and follow its `README.md`.

**Rules (v8):**
- `items/` = domain-neutral item store (1 tool = 1 item, e.g. `items/hallmark/`). Origin details live here.
- `domains/` = field guides (e.g. `domains/ui/`, `domains/media/`). Each item-domain pair has `using-<item>.md` with domain-only deltas + links to the item origin. One job may have MULTIPLE primary items (each a different way).
- Mandatory 3-way links: domain index → using-doc → item origin (exact section), and back.
- Structure and versioning rules live in `CHARTER.md` (current v8).
- Install into another repo/dir: `./scripts/install.sh --target /path/to/project --dry-run` then `--backup` (see `INSTALL.md`; remove: `UNINSTALL.md`). Reference-only by default.

**Routing:**

| Project / need | Go to |
|---|---|
| UI work (page system, React effects, sample landing) | `domains/ui/` |
| Media work (launch video, deck, OG image) | `domains/media/` |
| One tool's origin (install, mechanism, price, reviews) | `items/<tool>/` |
| Other domains (later: hardware, backend...) | add a sibling of `domains/<new>/`, do not change the skeleton |

**Agent workflow:** see `AGENTS.md`.
