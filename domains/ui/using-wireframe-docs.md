# using-wireframe-docs CHO UI (CHARTER v10)

> Phần RIÊNG khi dùng wireframe-docs cho UI. Gốc sống ở `../../items/wireframe-docs/README.md`; mọi lệnh/ngưỡng dưới đây khớp từng chữ với gốc. Item nội tại: tài nguyên trong item, không cài từ ngoài.

## Tiếng Việt

### Usecase trong domain này
- ★ Chốt cấu trúc UI mới bằng tree text trước khi build: xem [Usecase con 1](../../items/wireframe-docs/README.md#usecase-con-1-viet-treemd-moi).
- Validate tree + render HTML cho designer review: xem [Usecase con 2](../../items/wireframe-docs/README.md#usecase-con-2-validate-treemd) + [Usecase con 3](../../items/wireframe-docs/README.md#usecase-con-3-render-html-review).
- Agent đọc tree để build tiếp (sang hallmark): xem [Usecase con 4](../../items/wireframe-docs/README.md#usecase-con-4-agent-doc-tree-de-build).

### Lệnh mẫu cụ thể (cho UI)
- Viết tree: `mkdir -p .tmp/wireframes && cp items/wireframe-docs/examples/tree.md .tmp/wireframes/my-page-tree.md` rồi sửa theo `convention/tree-format.md` — xem [Usecase con 1](../../items/wireframe-docs/README.md#usecase-con-1-viet-treemd-moi).
- Đảm bảo ignored: kiểm tra `.gitignore` đã có dòng `.tmp/` chưa (thiếu thì thêm), verify bằng `git check-ignore -v .tmp/wireframes/my-page-tree.md`.
- Validate + render (chạy trong `items/wireframe-docs/`): `python3 scripts/check.py .tmp/wireframes/my-page-tree.md` rồi `python3 scripts/build.py .tmp/wireframes/my-page-tree.md -o .tmp/wireframes/my-page.html` — xem [Usecase con 2](../../items/wireframe-docs/README.md#usecase-con-2-validate-treemd).

### Lưu ý riêng cho UI
- Tree chốt rồi mới sang hallmark build chi tiết; tree đổi thì render lại, cấm sửa HTML render. Nguồn: [Cốt lõi](../../items/wireframe-docs/README.md#cot-loi-bat-bien).
- Mọi tree/HTML nháp giữ trong `.tmp/wireframes/` đã ignored; cấm viết ra root. Nguồn: [Áp dụng](../../items/wireframe-docs/README.md#ap-dung-khong-cai-tu-ngoai).
- Thông tin quan trọng (CTA, states, note) phải nằm trong cú pháp `note:/states:`, cấm để trong dòng tự do (parser + agent đều bỏ qua). Nguồn: [Pitfalls](../../items/wireframe-docs/README.md#pitfalls).
- Nhận xét bố cục/nhãn trên HTML render là việc của mắt người — giao claude, agent không tự kết luận. Nguồn: [Phân công](../../items/wireframe-docs/README.md#phan-cong-ai-lam-gi).

### Điểm mạnh cốt lõi CHO UI
- Cấu trúc version-bằng-git, agent đọc trực tiếp: tree.md là spec để hallmark build tiếp, không đoán từ ảnh.
- Nhẹ tuyệt đối: Python stdlib, 0đ, offline — chốt cấu trúc trong vài phút trước khi tốn công build chi tiết.

### Phân công CHO UI này
- Agent chính soạn tree + check + render + trình PASS/HTML; bước nhận xét visual giao nguyên cục cho claude (mở HTML + brief). Chi tiết: [Phân công gốc](../../items/wireframe-docs/README.md#phan-cong-ai-lam-gi).

### Link về item gốc (3 chiều)
- Gốc: `../../items/wireframe-docs/README.md` (Nguồn gốc / Áp dụng / Cốt lõi / Usecase 1-4 / Pitfalls / Tài nguyên).
- Index domain: `./README.md` (hàng wireframe-docs ở điều hướng + định vị + chồng lấn).
- Được liệt kê ngược tại: `../../items/wireframe-docs/README.md#duoc-dung-o-dau`.

---

## English

UI-only deltas for wireframe-docs. Origin lives at `../../items/wireframe-docs/README.md`; commands/bars below match it word-for-word. Intrinsic item: resources in-item, nothing installed.

### Usecases in this domain
- ★ Settle a new UI structure in text before building: see [Sub-usecase 1](../../items/wireframe-docs/README.md#sub-usecase-1-write-a-new-treemd).
- Validate + render HTML for designer review: see [Sub-usecases 2–3](../../items/wireframe-docs/README.md#sub-usecase-2-validate-treemd).
- Agent reads the tree to keep building (into hallmark): see [Sub-usecase 4](../../items/wireframe-docs/README.md#sub-usecase-4-agent-reads-the-tree-to-build).

### Concrete commands (for UI)
- Write: `mkdir -p .tmp/wireframes && cp items/wireframe-docs/examples/tree.md .tmp/wireframes/my-page-tree.md`, edit per `convention/tree-format.md`.
- Ensure ignored: check `.gitignore` already lists `.tmp/` (add when missing), verify with `git check-ignore -v .tmp/wireframes/my-page-tree.md`.
- Validate + render (inside `items/wireframe-docs/`): `python3 scripts/check.py .tmp/wireframes/my-page-tree.md` then `python3 scripts/build.py .tmp/wireframes/my-page-tree.md -o .tmp/wireframes/my-page.html`.

### Domain-specific notes
- Settle the tree before the hallmark detail build; re-render on change, never edit rendered HTML. Keep every draft tree/HTML under ignored `.tmp/wireframes/`, never at the root. Visual judgment on rendered HTML goes to claude. Key info (CTA, states, notes) must be in `note:/states:` syntax, never free prose.

### Core strengths FOR UI
- Git-versioned structure agents read directly: tree.md is the spec hallmark builds from. Absolute lightness: stdlib Python, $0, offline.

### Work split FOR this UI
- Main agent drafts + checks + renders + presents PASS/HTML; visual review goes to claude as a whole. Details: [origin Work split](../../items/wireframe-docs/README.md#work-split).

### Links to origin (3-way)
- Origin: `../../items/wireframe-docs/README.md`. Index: `./README.md`. Backlisted at origin `#where-used`.
