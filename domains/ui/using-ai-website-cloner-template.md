# using-ai-website-cloner-template CHO UI — rebuild/migrate site 1:1 thành Next.js (CHARTER v9)

> Phần rebuild site của ai-website-cloner-template KHI DÙNG CHO UI. Gốc ở `../../items/ai-website-cloner-template/README.md`.

## Tiếng Việt

### Usecase trong domain này
- ★ Clone 1 URL 1:1 (site có quyền) thành trang Next.js editable: xem [Usecase con 1](../../items/ai-website-cloner-template/README.md#usecase-con-1-clone-1-url-11-tu-template-trong).
- Migrate site nhiều trang mình sở hữu giữ pathnames: xem [Usecase con 2](../../items/ai-website-cloner-template/README.md#usecase-con-2-migrate-site-nhieu-trang-minh-so-huu).
- Thêm trang mới vào clone có sẵn (extend + regression): xem [Usecase con 3](../../items/ai-website-cloner-template/README.md#usecase-con-3-them-trang-moi-vao-clone-co-san).
- Compare/repair + production check (không build mới): xem [Usecase con 4](../../items/ai-website-cloner-template/README.md#usecase-con-4-comparerepair--production-check-tren-clone-co-san).

### Lệnh mẫu cụ thể (cho UI)
- Clone 1 URL (khớp từng chữ lệnh gốc, cần agent có browser): `/clone-website https://example.com`. Nhiều URL: `/clone-website <url1> <url2> ...`. Xem [Usecase con 1](../../items/ai-website-cloner-template/README.md#usecase-con-1-clone-1-url-11-tu-template-trong) + [Usecase con 2](../../items/ai-website-cloner-template/README.md#usecase-con-2-migrate-site-nhieu-trang-minh-so-huu).
- Check sau mọi slice (đã xác minh xanh trên template): `npm run check` (lint + typecheck + build). Xem [Cài đặt](../../items/ai-website-cloner-template/README.md#cai-dat-da-clone--npm-install--npm-run-check-xanh-tren-linux-30102026-chua-chay-clone-website-vi-may-nay-khong-co-browser-agent--tranh-dung-tos-site-that).
- Nối trang mới: `/clone-website <new-url>` trong app đã có clone. Xem [Usecase con 3](../../items/ai-website-cloner-template/README.md#usecase-con-3-them-trang-moi-vao-clone-co-san).

### Lưu ý riêng cho domain
- Phân biệt với Hallmark: brief UI cần giống hệt site sống (có quyền) → cloner chính; cần system mới pass gates → hallmark chính (clone không sinh tokens/gates). Phần custom viết thêm sau clone muốn đạt chuẩn thì sweep lại bằng hallmark. Xem [Định vị](../../items/ai-website-cloner-template/README.md#dinh-vi-khac-biet-so-lieu-api-github-ngay-30102026).
- Quyền/ToS check trước mỗi URL (sở hữu/cho phép/học); out-of-scope giữ trỏ source + disclose. Xem [Cốt lõi bất biến](../../items/ai-website-cloner-template/README.md#cot-loi-bat-bien).
- Token burn theo trang × vòng compare (Opus) — log scope duyệt trước khi chạy; chi phí/clone chưa công bố. Xem [Hồ sơ quyết định](../../items/ai-website-cloner-template/README.md#ho-so-quyet-dinh).

### Điểm mạnh cốt lõi của item CHO domain này
- Tái dựng 1:1 URL sống thành Next.js/shadcn editable: observe đa viewport/state bằng browser thật + route map + compare cùng viewport/state + check xanh — việc hallmark/skillry/reactbits đều không làm. Xem [Usecase con 1](../../items/ai-website-cloner-template/README.md#usecase-con-1-clone-1-url-11-tu-template-trong).
- Migrate giữ pathnames + preserve routes cũ + regression — đúng việc "mất source/chuyển nền tảng" của UI. Xem [Usecase con 2](../../items/ai-website-cloner-template/README.md#usecase-con-2-migrate-site-nhieu-trang-minh-so-huu) + [Usecase con 3](../../items/ai-website-cloner-template/README.md#usecase-con-3-them-trang-moi-vao-clone-co-san).
- Template 0đ MIT, setup 4 bước đã chạy xanh (476 pkgs, Node 24). Xem [Cài đặt](../../items/ai-website-cloner-template/README.md#cai-dat-da-clone--npm-install--npm-run-check-xanh-tren-linux-30102026-chua-chay-clone-website-vi-may-nay-khong-co-browser-agent--tranh-dung-tos-site-that).

### Phân công CHO domain này (1 dòng + link, không copy)
- Agent chính check quyền/scope (user pick URLs + gộp/tách qua question tool) → Map/Observe/Build/Compare + check + trình compare cho chủ site pick diff/gaps; bước browser đa state + chụp compare giao claude; verify bằng check xanh + ảnh cùng viewport/state + routes chạy. Chi tiết: [Phân công gốc](../../items/ai-website-cloner-template/README.md#phan-cong-ai-lam-gi).

### Link về item gốc (3 chiều)
- Gốc: `../../items/ai-website-cloner-template/README.md` (Usecase 1/2/3/4 / Cài đặt / Định vị / Hồ sơ quyết định / Tham khảo sử dụng).
- Index domain: `./README.md`.
- Ngược tại: `../../items/ai-website-cloner-template/README.md#duoc-dung-o-dau`.

---

## English

UI use of ai-website-cloner-template — 1:1 site rebuilds as Next.js. Origin at `../../items/ai-website-cloner-template/README.md`.

### Usecases in this domain
- ★ 1:1 clone of one URL (permitted site) into editable Next.js: see [Sub-usecase 1](../../items/ai-website-cloner-template/README.md#sub-usecase-1-11-clone-of-one-url-from-the-empty-template).
- Multi-page self-owned migration with preserved pathnames: see [Sub-usecase 2](../../items/ai-website-cloner-template/README.md#sub-usecase-2-migrating-a-self-owned-multi-page-site).
- Adding pages to an existing clone (extend + regress): see [Sub-usecase 3](../../items/ai-website-cloner-template/README.md#sub-usecase-3-adding-pages-to-an-existing-clone).
- Compare/repair + production check (no new build): see [Sub-usecase 4](../../items/ai-website-cloner-template/README.md#sub-usecase-4-comparerepair--production-check-on-an-existing-clone).

### Concrete commands (for this domain)
- Clone one URL (word-for-word origin command, browser-capable agent needed): `/clone-website https://example.com`. Multiple URLs: `/clone-website <url1> <url2> ...`. See [Sub-usecase 1](../../items/ai-website-cloner-template/README.md#sub-usecase-1-11-clone-of-one-url-from-the-empty-template) + [Sub-usecase 2](../../items/ai-website-cloner-template/README.md#sub-usecase-2-migrating-a-self-owned-multi-page-site).
- Check after every slice (verified green on the template): `npm run check` (lint + typecheck + build). See [Install](../../items/ai-website-cloner-template/README.md#install-cloned--npm-install--green-npm-run-check-on-linux-30102026-clone-website-not-run--no-browser-agent-on-this-machine--avoiding-real-site-tos-issues).
- Append a page: `/clone-website <new-url>` inside the app holding the clone. See [Sub-usecase 3](../../items/ai-website-cloner-template/README.md#sub-usecase-3-adding-pages-to-an-existing-clone).

### Domain-specific notes
- Vs Hallmark: UI briefs needing an exact match of a live site (with rights) → cloner primary; new gated systems → hallmark primary (clones generate no tokens/gates). Custom post-clone additions can be re-swept with hallmark. See [Positioning](../../items/ai-website-cloner-template/README.md#differentiating-positioning-github-api-numbers-30102026).
- Rights/ToS check before every URL (ownership/permission/learning); out-of-scope stays pointing at source + disclosed. See [Invariant core](../../items/ai-website-cloner-template/README.md#invariant-core).
- Token burn scales with pages × compare loops (Opus) — log the approved scope before running; per-clone cost unpublished. See [Decision dossier](../../items/ai-website-cloner-template/README.md#decision-dossier).

### Core strengths FOR this domain
- 1:1 live-URL rebuilds as editable Next.js/shadcn: real-browser multi-viewport/state observation + route map + matched comparison + green check — a job hallmark/skillry/reactbits all skip. See [Sub-usecase 1](../../items/ai-website-cloner-template/README.md#sub-usecase-1-11-clone-of-one-url-from-the-empty-template).
- Pathname-preserving migration + old-route preservation + regression — exactly the UI "lost source/re-platform" job. See [Sub-usecase 2](../../items/ai-website-cloner-template/README.md#sub-usecase-2-migrating-a-self-owned-multi-page-site) + [Sub-usecase 3](../../items/ai-website-cloner-template/README.md#sub-usecase-3-adding-pages-to-an-existing-clone).
- $0 MIT template, 4-step setup verified green (476 pkgs, Node 24). See [Install](../../items/ai-website-cloner-template/README.md#install-cloned--npm-install--green-npm-run-check-on-linux-30102026-clone-website-not-run--no-browser-agent-on-this-machine--avoiding-real-site-tos-issues).

### Work split FOR this domain (1 line + link, never copied)
- Main agent checks rights/scope (user picks URLs + combine/split via question tool) → Maps/Observes/Builds/Compares + checks + presents comparisons for the site owner to pick diffs/gaps; multi-state browser work + comparison captures go to claude; verify via green check + matched images + running routes. Details: [origin Work split](../../items/ai-website-cloner-template/README.md#work-split).

### Links to origin (3-way)
- Origin: `../../items/ai-website-cloner-template/README.md` (Sub-usecases 1/2/3/4 / Install / Positioning / Decision dossier / Usage references).
- Domain index: `./README.md`.
- Backlisted at: `../../items/ai-website-cloner-template/README.md#where-used`.
