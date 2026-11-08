# using-material-3 CHO UI (CHARTER v12)

> Phần RIÊNG khi dùng material-3 cho UI. Gốc sống ở `../../items/material-3/README.md`; mọi lệnh/ngưỡng dưới đây khớp từng chữ với gốc. Không copy lại toàn bộ cài đặt/cơ chế.

## Tiếng Việt

### Usecase trong domain này
- ★ Build theo MD3 có tokens/components: xem [Usecase con 1](../../items/material-3/README.md#usecase-con-1-build-theo-md3-co-tokens-components--manh-nhat).
- Theme từ seed color + dynamic/dark: xem [Usecase con 2](../../items/material-3/README.md#usecase-con-2-theme-tu-seed-color-dynamic-va-dark).
- Audit MD3 10 hạng mục có scoring: xem [Usecase con 3](../../items/material-3/README.md#usecase-con-3-audit-md3-10-hang-muc-co-scoring).
- Tra tokens/components/Expressive matrix: xem [Usecase con 4](../../items/material-3/README.md#usecase-con-4-tra-tokens-components-va-expressive).

### Lệnh mẫu cụ thể (cho UI)
- Cài 1 lần: `npx --yes skills add hamen/material-3-skill --skill material-3 -y` — xem [Cài đặt](../../items/material-3/README.md#cai-dat).
- Build/scaffold: `/material-3 scaffold Tạo app shell responsive có navigation` (kèm platform đã chốt) — xem [Usecase con 1](../../items/material-3/README.md#usecase-con-1-build-theo-md3-co-tokens-components--manh-nhat).
- Theme: `/material-3 theme Generate a theme from seed color #1A73E8` — xem [Usecase con 2](../../items/material-3/README.md#usecase-con-2-theme-tu-seed-color-dynamic-va-dark).
- Audit: `/material-3 audit [URL hoặc file path]` (nêu stack) — xem [Usecase con 3](../../items/material-3/README.md#usecase-con-3-audit-md3-10-hang-muc-co-scoring).

### Lưu ý riêng cho UI
- Platform phải user pick trước (cấm mặc định Compose khi brief là web); web ghi rõ giới hạn Expressive — nguồn [Cốt lõi](../../items/material-3/README.md#cot-loi-bat-bien).
- Signatures/BOM versions trích từ skill phải check docs chính chủ (skill tự báo drift) — nguồn [Pitfalls](../../items/material-3/README.md#pitfalls).
- Quan hệ với frontend-design khi cùng bật: MD3 thắng tokens/components/structure, frontend-design thắng creative direction, Roboto là exception — nguồn [Phần tùy chỉnh](../../items/material-3/README.md#phan-tuy-chinh).

### Điểm mạnh cốt lõi CHO UI
- Hệ design-system duy nhất trong kho có audit scoring: tokens `md.sys.*` tra được tới mã + 30+ components mapping 3 nền tảng + audit 10 hạng mục 0-10 — quyết định chọn thay vì frontend-design khi cần tuân thủ hệ, không phải direction tự do. Xem [Định vị](../../items/material-3/README.md#dinh-vi-khac-biet-so-lieu-ngay-08112026).
- Platform matrix trung thực (Compose primary/Flutter secondary/Web limited + maintenance mode) — biết trước cái gì web không có.

### Phân công CHO UI này
- Agent chính chốt platform (user pick) → decision tree → tra tokens → build/theme/audit + grep → trình report; bước render thật giao nguyên cục cho claude (browser đo contrast/motion/responsive). Chi tiết: [Phân công gốc](../../items/material-3/README.md#phan-cong-ai-lam-gi).

### Link về item gốc (3 chiều)
- Gốc: `../../items/material-3/README.md` (Cài đặt / Cách hoạt động / Định vị / Bản đồ phủ / Hồ sơ quyết định / Usecase 1-4 / Pitfalls / Tham khảo sử dụng).
- Index domain: `./README.md` (hàng material-3 ở điều hướng + định vị + chồng lấn).
- Được liệt kê ngược tại: `../../items/material-3/README.md#duoc-dung-o-dau`.

---

## English

UI-only deltas for material-3. Origin lives at `../../items/material-3/README.md`; commands/bars below match it word-for-word.

### Usecases in this domain
- ★ MD3 builds with tokens and components: see [Sub-usecase 1](../../items/material-3/README.md#sub-usecase-1-md3-builds-with-tokens-and-components--strongest).
- Seed-color themes, dynamic and dark: see [Sub-usecase 2](../../items/material-3/README.md#sub-usecase-2-seed-color-themes-dynamic-and-dark).
- 10-category scored MD3 audit: see [Sub-usecase 3](../../items/material-3/README.md#sub-usecase-3-10-category-md3-audit-with-scoring).
- Token/component/Expressive-matrix lookup: see [Sub-usecase 4](../../items/material-3/README.md#sub-usecase-4-token-and-component-lookup-with-expressive-matrix).

### Concrete commands (for UI)
- Install once: `npx --yes skills add hamen/material-3-skill --skill material-3 -y`.
- Build/scaffold: `/material-3 scaffold ...` (with settled platform). Theme: `/material-3 theme ...`. Audit: `/material-3 audit [URL or file path]` (state stack).

### Domain-specific notes
- Platform needs user pick first (never default Compose on a web brief); state web Expressive limits. Skill-quoted signatures/BOMs need canonical-doc checks (self-reported drift). With frontend-design co-enabled: MD3 wins tokens/components/structure, frontend-design wins direction, Roboto excepted.

### Core strengths FOR UI
- The repo's only design system with a scored audit: `md.sys.*` tokens down to the code + 30+ components across 3 platforms + 0-10 ten-category audit — pick over frontend-design when system compliance, not free direction, decides.
- Honest platform matrix (Compose primary/Flutter secondary/limited maintenance-mode web) — know upfront what web lacks.

### Work split FOR this UI
- Main agent settles platform (user picks) → decision tree → token lookup → builds/themes/audits + grep → presents report; real rendering goes to claude as a whole. Details: [origin Work split](../../items/material-3/README.md#work-split).

### Links to origin (3-way)
- Origin: `../../items/material-3/README.md`. Index: `./README.md`. Backlisted at origin `#where-used`.
