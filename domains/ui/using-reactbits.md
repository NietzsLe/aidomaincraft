# using-reactbits CHO UI (CHARTER v7)

> Phần RIÊNG khi dùng React Bits cho UI. Gốc ở `../../items/reactbits/README.md`; lệnh/ngưỡng khớp từng chữ với gốc.

## Tiếng Việt

### Usecase trong domain này
- ★ Headline cần chuyển động chữ, hero/section cần nền động, card/nav/carousel/gallery, nút/toggle/indicator, cursor/hover/border/ảnh: xem [Bảng usecase](../../items/reactbits/README.md#bang-usecase-con-cach-dung) (Text 33 / Backgrounds 63 / Components 48 / Micro 34 / Animations 38).
- Tool asset nhanh (Background Studio, Center Stage, Shape Magic, Texture Lab, Sound Lab): cùng link trên — chạy trên web rồi export, không qua CLI component.

### Lệnh mẫu cụ thể (cho UI)
- Headline: `npx shadcn@latest add @react-bits/SplitText-TS-TW` (đổi tên + đuôi variant `-TS-TW`/`-JS-CSS`) — xem [Cài đặt](../../items/reactbits/README.md#cai-dat).
- MCP agent: thêm `{ "registries": { "@react-bits": "https://reactbits.dev/r/{name}.json" } }` vào `components.json` rồi `npx shadcn@latest mcp init --client claude` — cùng link cài đặt.
- Gắn vào layout Hallmark có sẵn: giữ tokens, motion chỉ `transform/opacity`, reduced-motion fallback, LCP <2MB. Prompt mẫu điền sẵn trong [Prompt mẫu](../../items/reactbits/README.md#prompt-mau).

### Lưu ý riêng cho UI
- Chỉ lắp 1-2 effect/page; 3-4 effect cùng lúc → rối + vỡ Hallmark gate 8/9/11. Lắp xong sweep lại Hallmark (`sloplint --render`).
- Quên đuôi variant (`-TS-TW` vs `-JS-CSS`) → sai stack. Nền động đè chữ → scrim 35-65% + contrast 4.5:1. Loop >5s phải có pause (WCAG 2.2.2 + gate 18). Xem [Pitfalls](../../items/reactbits/README.md#pitfalls).
- Không dùng React Bits thay design system: không tokens/gates/review.

### Điểm mạnh cốt lõi CHO UI
- Bricks sở hữu source + demo xem trước + variant khớp stack + MCP lắp nhanh — chọn thay vì Motion/GSAP thuần khi cần component chạy ngay. Xem [Định vị](../../items/reactbits/README.md#dinh-vi-khac-biet).
- Được `PkgPulse 25/03/2026` xác nhận `#2 JS Rising Stars 2025 (+32.8K/năm, 37.1K)` + `Annnimate` thừa nhận *"free, community-backed catalog... easy yes for React-only"* — xem [Tham khảo sử dụng](../../items/reactbits/README.md#tham-khao-su-dung).

### Link về item gốc (3 chiều)
- Gốc: `../../items/reactbits/README.md` (Cài đặt / Cách hoạt động / Định vị / Bảng usecase / Prompt / Pitfalls / Tham khảo sử dụng).
- Index domain: `./README.md`.
- Ngược tại: `../../items/reactbits/README.md#duoc-dung-o-dau`.

---

## English

UI-only deltas for React Bits. Origin at `../../items/reactbits/README.md`.

### Usecases in this domain
- ★ Animated headline, animated hero/section background, ready card/nav/carousel/gallery, micro-interactions, cursor/hover/border effects + 5 web asset tools: see origin usecase table.

### Concrete commands (for UI)
- `npx shadcn@latest add @react-bits/SplitText-TS-TW` (swap name + variant suffix); MCP via `@react-bits` registry. Fit into Hallmark layout (tokens kept, transform/opacity only, reduced-motion fallback).

### Domain-specific notes
- Max 1-2 effects/page; re-sweep with Hallmark afterwards. Wrong variant suffix → stack mismatch; animated background under text needs 35-65% scrim + 4.5:1.

### Core strengths FOR UI
- Owned-source bricks + live demos + stack-matching variants + MCP install — over raw Motion/GSAP when a ready component decides.

### Links to origin (3-way)
- Origin: `../../items/reactbits/README.md`. Index: `./README.md`. Backlisted at origin `#where-used`.
