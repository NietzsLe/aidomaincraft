# using-wireframe-docs CHO UI (CHARTER v10)

> Phần RIÊNG khi dùng wireframe-docs cho UI. Gốc sống ở `../../items/wireframe-docs/README.md`; mọi lệnh/ngưỡng dưới đây khớp từng chữ với gốc. Item nội tại: tài nguyên trong item, không cài từ ngoài.

## Tiếng Việt

### Usecase trong domain này
- ★ Chốt phạm vi cấu trúc UI bằng tree text: xem [Usecase con 1](../../items/wireframe-docs/README.md#usecase-con-1-viet-treemd-moi).
- ★ Soạn wireframe tay 4 khổ (`sm/md/lg/xl`) theo tree: xem [Usecase con 3](../../items/wireframe-docs/README.md#usecase-con-3-soan-wireframe-tay-4-kho).
- Validate tree + kiểm tra cặp cho designer quyết: xem [Usecase con 2](../../items/wireframe-docs/README.md#usecase-con-2-validate-treemd) + [Usecase con 4](../../items/wireframe-docs/README.md#usecase-con-4-kiem-tra-cap-tree-wireframe).
- Agent đọc cặp để build tiếp (sang hallmark): xem [Usecase con 5](../../items/wireframe-docs/README.md#usecase-con-5-agent-doc-cap-de-build).
- Review nhanh nhiều khổ/biến thể bằng viewer: xem [Usecase con 6](../../items/wireframe-docs/README.md#usecase-con-6-review-nhanh-bang-viewer).

### Lệnh mẫu cụ thể (cho UI)
- Viết tree: `mkdir -p .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page && cp items/wireframe-docs/examples/tree.md .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-tree.md` rồi sửa theo `convention/tree-format.md` — xem [Usecase con 1](../../items/wireframe-docs/README.md#usecase-con-1-viet-treemd-moi).
- Đảm bảo ignored: kiểm tra `.gitignore` đã có dòng `.aidomaincraft/` chưa (thiếu thì thêm), verify bằng `git check-ignore -v .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-tree.md`.
- Validate tree (chạy trong `items/wireframe-docs/`): `python3 scripts/check.py .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-tree.md` — xem [Usecase con 2](../../items/wireframe-docs/README.md#usecase-con-2-validate-treemd).
- Soạn wireframe 4 khổ theo tree rồi kiểm tra cặp: copy `examples/tree.html` thành `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-wireframe.html` làm khung xương, sửa tay theo tree, rồi `python3 scripts/verify-pair.py .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-tree.md .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-wireframe.html` — xem [Usecase con 3](../../items/wireframe-docs/README.md#usecase-con-3-soan-wireframe-tay-4-kho) + [Usecase con 4](../../items/wireframe-docs/README.md#usecase-con-4-kiem-tra-cap-tree-wireframe).
- Review nhanh: copy `templates/viewer.html` vào cùng thư mục bản, mở `viewer.html?file=my-page-wireframe.html` — xem [Usecase con 6](../../items/wireframe-docs/README.md#usecase-con-6-review-nhanh-bang-viewer).

### Lưu ý riêng cho UI
- Cặp tree + wireframe chốt rồi mới sang hallmark build chi tiết; bên nào đổi thì bên kia sửa cho khớp và chạy lại `verify-pair.py`, cấm coi một bên là khớp. Nguồn: [Cốt lõi](../../items/wireframe-docs/README.md#cot-loi-bat-bien).
- Mọi tree/HTML nháp giữ trong thư mục bản `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<tên-trang>/` đã ignored; cấm viết ra root. Nguồn: [Áp dụng](../../items/wireframe-docs/README.md#ap-dung-khong-cai-tu-ngoai).
- Mọi lệch máy đã báo thuộc về designer quyết; agent và claude không tự sửa ngầm. Nguồn: [Usecase con 4](../../items/wireframe-docs/README.md#usecase-con-4-kiem-tra-cap-tree-wireframe).
- Thông tin quan trọng (CTA, states, effect, ẩn/hiện) phải nằm trong cú pháp `note:/states:/effect:/hide:` và block `data-wf-*`, cấm để trong dòng tự do (parser + agent đều bỏ qua). Nguồn: [Pitfalls](../../items/wireframe-docs/README.md#pitfalls).
- Nhận xét bố cục/độ lớn/vị trí/nhãn trên wireframe 4 khổ là việc của mắt người — giao claude, agent không tự kết luận. Nguồn: [Phân công](../../items/wireframe-docs/README.md#phan-cong-ai-lam-gi).
- Review nhanh bằng viewer (bấm loại → biến thể, gập panel, lưới 4 khung) thay cho resize Chrome thủ công; mở viewer thiếu `?file=` thì thêm vào, không phải lỗi. Nguồn: [Usecase con 6](../../items/wireframe-docs/README.md#usecase-con-6-review-nhanh-bang-viewer).

### Điểm mạnh cốt lõi CHO UI
- Cặp tree + wireframe kiểm tra được bằng máy: tree.md version-bằng-git định nghĩa phạm vi, wireframe tay thể hiện đủ 4 khổ, `verify-pair.py` bắt mọi lệch cho designer quyết.
- Nhẹ tuyệt đối: Python stdlib, 0đ, offline — chốt cấu trúc và bố cục trước khi tốn công build chi tiết.

### Phân công CHO UI này
- Agent chính soạn tree + check + soạn wireframe + kiểm tra cặp + trình cặp và 2 dòng PASS; bước nhận xét visual giao nguyên cục cho claude (mở HTML + brief), mọi lệch giao designer quyết. Chi tiết: [Phân công gốc](../../items/wireframe-docs/README.md#phan-cong-ai-lam-gi).

### Link về item gốc (3 chiều)
- Gốc: `../../items/wireframe-docs/README.md` (Nguồn gốc / Áp dụng / Cốt lõi / Usecase 1-6 / Pitfalls / Tài nguyên).
- Index domain: `./README.md` (hàng wireframe-docs ở điều hướng + định vị + chồng lấn).
- Được liệt kê ngược tại: `../../items/wireframe-docs/README.md#duoc-dung-o-dau`.

---

## English

UI-only deltas for wireframe-docs. Origin lives at `../../items/wireframe-docs/README.md`; commands/bars below match it word-for-word. Intrinsic item: resources in-item, nothing installed.

### Usecases in this domain
- ★ Settle UI scope with a text tree: see [Sub-usecase 1](../../items/wireframe-docs/README.md#sub-usecase-1-write-a-new-treemd).
- ★ Hand-author the 4-breakpoint (`sm/md/lg/xl`) wireframe per the tree: see [Sub-usecase 3](../../items/wireframe-docs/README.md#sub-usecase-3-hand-author-the-4-frame-wireframe).
- Validate the tree + check the pair for the designer to rule on: see [Sub-usecase 2](../../items/wireframe-docs/README.md#sub-usecase-2-validate-treemd) + [Sub-usecase 4](../../items/wireframe-docs/README.md#sub-usecase-4-verify-the-tree-wireframe-pair).
- Agent reads the pair to keep building (into hallmark): see [Sub-usecase 5](../../items/wireframe-docs/README.md#sub-usecase-5-agent-reads-the-pair-to-build).
- Quick multi-width/variant review with the viewer: see [Sub-usecase 6](../../items/wireframe-docs/README.md#sub-usecase-6-quick-review-with-the-viewer).

### Concrete commands (for UI)
- Write: `mkdir -p .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page && cp items/wireframe-docs/examples/tree.md .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-tree.md`, edit per `convention/tree-format.md`.
- Ensure ignored: check `.gitignore` already lists `.aidomaincraft/` (add when missing), verify with `git check-ignore -v .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-tree.md`.
- Validate the tree (inside `items/wireframe-docs/`): `python3 scripts/check.py .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-tree.md`.
- Author the 4-frame wireframe per the tree, then check the pair: copy `examples/tree.html` to `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-wireframe.html` as a skeleton, hand-edit per the tree, then `python3 scripts/verify-pair.py .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-tree.md .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-wireframe.html`.
- Quick review: copy `templates/viewer.html` into the same version folder, open `viewer.html?file=my-page-wireframe.html` — see [Sub-usecase 6](../../items/wireframe-docs/README.md#sub-usecase-6-quick-review-with-the-viewer).

### Domain-specific notes
- Settle the tree + wireframe pair before the hallmark detail build; on either-side change fix the other side and re-run `verify-pair.py`, never treat one side as matching. Keep every draft tree/HTML under the ignored version folder `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<page>/`, never at the root. Reported drifts belong to the designer; agent and claude never fix them silently. Visual judgment on the 4-frame wireframe goes to claude. Key info (CTA, states, effects, visibility) must be in `note:/states:/effect:/hide:` syntax and `data-wf-*` blocks, never free prose. Quick multi-width review uses the viewer (type → variant, collapsible panel, 4-frame grid) instead of manual Chrome resizing.

### Core strengths FOR UI
- A machine-checked tree + wireframe pair: git-versioned tree.md defines scope, the hand-authored wireframe shows all 4 breakpoints, `verify-pair.py` catches every drift for the designer to rule on. Absolute lightness: stdlib Python, $0, offline.

### Work split FOR this UI
- Main agent drafts + checks + authors the wireframe + checks the pair + presents the pair and both PASS lines; visual review goes to claude as a whole, every drift goes to the designer. Details: [origin Work split](../../items/wireframe-docs/README.md#work-split).

### Links to origin (3-way)
- Origin: `../../items/wireframe-docs/README.md`. Index: `./README.md`. Backlisted at origin `#where-used`.
