# using-skillry CHO UI — phần web (CHARTER v7)

> Phần web của Skillry KHI DÙNG CHO UI. Gốc ở `../../items/skillry/README.md`. Phần video/deck/OG xem `../media/using-skillry.md`.

## Tiếng Việt

### Usecase trong domain này
- ★ Landing/portfolio web mẫu phong cách có sẵn (Mint Noir SaaS free, Cadence Marketing, Harbor SaaS): xem [Usecase con 2](../../items/skillry/README.md#usecase-con-2-landingportfolio-web).
- Không phủ: system pass gates → dùng Hallmark (`using-hallmark.md`); bricks React → React Bits (`using-reactbits.md`).

### Lệnh mẫu cụ thể (cho UI)
- Paste-prompt (khuyến nghị, mọi OS): `Read https://skillry.dev/skills/bs-mint-noir-saas-site/install.md and follow the instructions to install the skill.` — expect `● Loading skill bs-mint-noir-saas-site`. Các slug web Free khác xem [Hồ sơ quyết định](../../items/skillry/README.md#ho-so-quyet-dinh) (vd `bs-ember-ebike-store`, `bs-tracklane-devtool-landing`) — catalog trôi, đối chiếu nhãn Free/Premium trước khi dùng. Xem [Cài đặt](../../items/skillry/README.md#cai-dat-da-chay-skillry-help--status-chua-login--cli-tren-linux-loi-secure-storage).
- CLI macOS/Windows: `npx --yes skillry-cli@latest install bs-mint-noir-saas-site --agent opencode`. ZIP: `mkdir -p ~/.agents/skills` + unzip sao cho có `~/.agents/skills/<slug>/SKILL.md` + restart OpenCode.
- Prompt mẫu quán cà phê A trong [Prompt mẫu](../../items/skillry/README.md#prompt-mau).

### Lưu ý riêng cho UI
- Output theo taste Skillry, không tokens/design system riêng — restyle sau bằng Hallmark nếu cần chuẩn (`sloplint --render`). Free VẪN cần tài khoản Skillry (verify entitlement).
- Linux KHÔNG dùng CLI (lỗi secure storage macOS/Windows only) — dùng paste-prompt/ZIP.

### Điểm mạnh cốt lõi CHO UI
- Taste landing đóng gói (Mint/Cadence/Harbor) + preview + installs trước khi cài — chọn thay vì tự ráp free khi cần đúng taste + quy trình hướng dẫn. Engine free (shadcn 271.1K, agent-skills 32.3k★) thắng về capability. Xem [Định vị](../../items/skillry/README.md#dinh-vi-khac-biet-da-doi-chieu-skillssh-leaderboard-ngay-2026-10-29).

### Link về item gốc (3 chiều)
- Gốc: `../../items/skillry/README.md` (Usecase 2 / Cài đặt / Định vị / Prompt mẫu / Pitfalls / Tham khảo sử dụng).
- Index domain: `./README.md` (hàng skillry-web).
- Media song sinh: `../media/using-skillry.md` (phần video/deck/OG).
- Ngược tại: `../../items/skillry/README.md#duoc-dung-o-dau`.

---

## English

Web part of Skillry FOR UI. Origin at `../../items/skillry/README.md`. Video/deck/OG part: `../media/using-skillry.md`.

### Usecases in this domain
- ★ Sample landing/site in an existing style (free Mint Noir SaaS, Cadence, Harbor): see origin Sub-usecase 2.

### Concrete commands (for UI)
- Paste-prompt (every OS): `Read https://skillry.dev/skills/bs-mint-noir-saas-site/install.md and follow the instructions to install the skill.` CLI (macOS/Windows) or ZIP + restart otherwise.

### Domain-specific notes
- Output follows Skillry taste, no own tokens — re-sweep with Hallmark for a custom standard. Free still needs an account. No CLI on Linux.

### Core strengths FOR UI
- Packaged landing taste + previews + guided workflow — over free assembly when the exact Mint/Cadence taste decides.

### Links to origin (3-way)
- Origin: `../../items/skillry/README.md`. Index: `./README.md`. Twin: `../media/using-skillry.md`. Backlisted at origin `#where-used`.
