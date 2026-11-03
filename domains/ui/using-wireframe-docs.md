# using-wireframe-docs CHO UI (CHARTER v10)

> Phần RIÊNG khi dùng wireframe-docs cho UI. Gốc sống ở `../../items/wireframe-docs/README.md`; mọi lệnh/ngưỡng dưới đây khớp từng chữ với gốc. Item nội tại: tài nguyên trong item, không cài từ ngoài.

## Tiếng Việt

### Usecase trong domain này
- ★ Chốt phạm vi cấu trúc UI bằng tree text: xem [Usecase con 1](../../items/wireframe-docs/README.md#usecase-con-1-viet-treemd-data-mau).
- ★ Soạn wireframe tay 4 khổ (`sm/md/lg/xl`) theo tree: xem [Usecase con 3](../../items/wireframe-docs/README.md#usecase-con-3-soan-wireframe-tay-4-kho).
- Validate tree + kiểm tra bộ ba + đánh giá guidelines cho designer quyết: xem [Usecase con 2](../../items/wireframe-docs/README.md#usecase-con-2-validate-treemd) + [Usecase con 4](../../items/wireframe-docs/README.md#usecase-con-4-kiem-tra-bo-ba-tree-data-wireframe) + [Usecase con 7](../../items/wireframe-docs/README.md#usecase-con-7-danh-gia-theo-chuan-web-interface-guidelines).
- Agent đọc bộ ba để build tiếp (sang hallmark): xem [Usecase con 5](../../items/wireframe-docs/README.md#usecase-con-5-agent-doc-bo-ba-de-build).
- Review nhanh nhiều khổ/biến thể bằng viewer: xem [Usecase con 6](../../items/wireframe-docs/README.md#usecase-con-6-review-nhanh-bang-viewer).
- Soạn + play flow như video: xem [Usecase con 8](../../items/wireframe-docs/README.md#usecase-con-8-soan-va-play-flow).
- Rà soát suite trước khi chốt (DoD): xem [Usecase con 9](../../items/wireframe-docs/README.md#usecase-con-9-ra-soat-suite-truoc-khi-trinhchot).

### Lệnh mẫu cụ thể (cho UI)
- Viết brief + tree + data: copy `convention/brief-template.md` thành `.aidomaincraft/.tmp/wireframes/<suite>/brief.md` rồi điền REQ-xxx; `mkdir -p .aidomaincraft/.tmp/wireframes/<suite>/my-page && cp items/wireframe-docs/examples/tree.md .aidomaincraft/.tmp/wireframes/<suite>/my-page/my-page-tree.md` rồi sửa theo `convention/tree-format.md` (Kiểu thuộc vocab shadcn pin ở `component-roles.md`; behavior/effect/reduced/ref theo danh sách cho phép) + viết `my-page-data.json` theo `convention/data-schema.md` — xem [Usecase con 1](../../items/wireframe-docs/README.md#usecase-con-1-viet-treemd-data-mau).
- Đảm bảo ignored: kiểm tra `.gitignore` đã có dòng `.aidomaincraft/` chưa (thiếu thì thêm), verify bằng `git check-ignore -v .aidomaincraft/.tmp/wireframes/<suite>/my-page/my-page-tree.md`.
- Validate tree (chạy trong `items/wireframe-docs/`): `python3 scripts/check.py .aidomaincraft/.tmp/wireframes/<suite>/my-page/my-page-tree.md` — xem [Usecase con 2](../../items/wireframe-docs/README.md#usecase-con-2-validate-treemd).
- Đánh giá guidelines: `python3 scripts/check-guidelines.py .aidomaincraft/.tmp/wireframes/<suite>/my-page/my-page-tree.md` (tự tìm data; báo cáo từng rule + SCORE) — xem [Usecase con 7](../../items/wireframe-docs/README.md#usecase-con-7-danh-gia-theo-chuan-web-interface-guidelines).
- Soạn wireframe 4 khổ theo tree rồi kiểm tra cặp: copy `examples/tree.html` thành `.aidomaincraft/.tmp/wireframes/<suite>/my-page/my-page-wireframe.html` làm khung xương, sửa tay theo tree, rồi `python3 scripts/verify-pair.py .aidomaincraft/.tmp/wireframes/<suite>/my-page/my-page-tree.md .aidomaincraft/.tmp/wireframes/<suite>/my-page/my-page-wireframe.html` — xem [Usecase con 3](../../items/wireframe-docs/README.md#usecase-con-3-soan-wireframe-tay-4-kho) + [Usecase con 4](../../items/wireframe-docs/README.md#usecase-con-4-kiem-tra-bo-ba-tree-data-wireframe).
- Review nhanh: copy `templates/viewer.html` vào cùng thư mục bản, mở `viewer.html?file=my-page-wireframe.html` (frame ảo thu vừa màn hình, caption ghi rộng thật + % thu; click component xem card) — xem [Usecase con 6](../../items/wireframe-docs/README.md#usecase-con-6-review-nhanh-bang-viewer).
- Xem mọi trang không theo flow: mở `player.html` → nút `▦ Pages` (lưới toàn trang thu nhỏ, bấm vào xem chi tiết từng khổ) — xem [Usecase con 8](../../items/wireframe-docs/README.md#usecase-con-8-soan-va-play-flow).
- Soạn + play flow: viết `flows/<ten>.md` theo khuôn + `Entry:` + `go:`/`Input:`/`If:`/`Else:` (`convention/flows.md`), rồi `python3 scripts/check-flow.py .aidomaincraft/.tmp/wireframes/<suite>` + `python3 scripts/build-flow.py .aidomaincraft/.tmp/wireframes/<suite>` → mở `player.html` (list/detail/play toàn trang khung vuông đúng W×H + chọn khổ + rẽ nhánh + gõ Input + panel ràng buộc; dialog render đúng block + nút icon xem meta; tab `▦ Pages` xem mọi trang độc lập flow; badge/Ctrl+Click xem card) — xem [Usecase con 8](../../items/wireframe-docs/README.md#usecase-con-8-soan-va-play-flow).
- Rà soát suite: `python3 scripts/check-suite.py .aidomaincraft/.tmp/wireframes/<suite>` (brief + mọi trang + mọi flow + REQ + player tươi; exit 0 = DoD đạt) — xem [Usecase con 9](../../items/wireframe-docs/README.md#usecase-con-9-ra-soat-suite-truoc-khi-trinhchot).

### Lưu ý riêng cho UI
- Bộ ba tree + data + wireframe chốt rồi mới sang hallmark build chi tiết; bên nào đổi thì các bên còn lại sửa cho khớp và chạy lại `verify-pair.py`, cấm coi một bên là khớp. Nguồn: [Cốt lõi](../../items/wireframe-docs/README.md#cot-loi-bat-bien).
- Mọi tree/data/HTML nháp giữ trong thư mục bản `.aidomaincraft/.tmp/wireframes/<suite>/<tên-trang>/` đã ignored; cấm viết ra root. Nguồn: [Áp dụng](../../items/wireframe-docs/README.md#ap-dung-khong-cai-tu-ngoai).
- Mọi lệch máy đã báo thuộc về designer quyết; agent và claude không tự sửa ngầm. Nguồn: [Usecase con 4](../../items/wireframe-docs/README.md#usecase-con-4-kiem-tra-bo-ba-tree-data-wireframe).
- Thông tin quan trọng (CTA, states, effect, behavior, reduced, ref, ẩn/hiện) phải nằm trong cú pháp `note:/states:/effect:/behavior:/reduced:/ref:/hide:` và block `data-wf-*`, cấm để trong dòng tự do (parser + agent đều bỏ qua). Kiểu component phải thuộc vocab shadcn pin (`component-roles.md`), không tự bịa. Nguồn: [Pitfalls](../../items/wireframe-docs/README.md#pitfalls).
- Nhận xét bố cục/độ lớn/vị trí/nhãn trên wireframe 4 khổ là việc của mắt người — giao claude, agent không tự kết luận. Nguồn: [Phân công](../../items/wireframe-docs/README.md#phan-cong-ai-lam-gi).
- Review nhanh bằng viewer (bấm loại → biến thể trên frame ảo thu vừa màn hình, lưới 4 khung, click component xem card) thay cho resize Chrome thủ công; mở viewer thiếu `?file=` thì thêm vào, không phải lỗi. Nguồn: [Usecase con 6](../../items/wireframe-docs/README.md#usecase-con-6-review-nhanh-bang-viewer).

### Điểm mạnh cốt lõi CHO UI
- Cặp tree + wireframe kiểm tra được bằng máy: tree.md version-bằng-git định nghĩa phạm vi, wireframe tay thể hiện đủ 4 khổ, `verify-pair.py` bắt mọi lệch cho designer quyết.
- Nhẹ tuyệt đối: Python stdlib, 0đ, offline — chốt cấu trúc và bố cục trước khi tốn công build chi tiết.

### Phân công CHO UI này
- Agent chính soạn brief/tree + check + soạn wireframe + kiểm tra bộ ba + đánh giá guidelines + soạn flow + build/play player + rà soát suite, trình to-do còn lại trước khi chốt; bước nhận xét visual giao nguyên cục cho claude (mở HTML/player + brief), mọi lệch + WARN giao designer quyết. Chi tiết: [Phân công gốc](../../items/wireframe-docs/README.md#phan-cong-ai-lam-gi).

### Link về item gốc (3 chiều)
- Gốc: `../../items/wireframe-docs/README.md` (Nguồn gốc / Áp dụng / Cốt lõi / Usecase 1-9 / Pitfalls / Tài nguyên).
- Index domain: `./README.md` (hàng wireframe-docs ở điều hướng + định vị + chồng lấn).
- Được liệt kê ngược tại: `../../items/wireframe-docs/README.md#duoc-dung-o-dau`.

### Tái tạo trên runtime khác
- Mọi thao tác đều trung lập runtime: `git` CLI + Python stdlib + mở file HTML bằng browser (`file://`, offline); `node --check` là tùy chọn (có node mới chạy).
- Muốn làm lại đúng kết quả ở runtime khác (OpenCode/Claude Code/Cursor/Copilot...): cài cùng skill + version ghi trong CHANGELOG, đọc quyết định đã ghi (Picks/stamp/commit message — không nằm trong log local `.relay/` vốn bị git-ignore), chạy `tests/test.sh` phải `fail=0`.
- Verify mắt người: runtime nào cũng làm được — mở `viewer.html`/`player.html` build từ demo và đối chiếu checklist trong CHANGELOG; không phụ thuộc tool điều khiển browser riêng.

---

## English

UI-only deltas for wireframe-docs. Origin lives at `../../items/wireframe-docs/README.md`; commands/bars below match it word-for-word. Intrinsic item: resources in-item, nothing installed.

### Usecases in this domain
- ★ Settle UI scope with a text tree: see [Sub-usecase 1](../../items/wireframe-docs/README.md#sub-usecase-1-write-a-new-treemd-datajson).
- ★ Hand-author the 4-breakpoint (`sm/md/lg/xl`) wireframe per the tree: see [Sub-usecase 3](../../items/wireframe-docs/README.md#sub-usecase-3-hand-author-the-4-frame-wireframe).
- Validate the tree + check the trio + evaluate against the guidelines for the designer to rule on: see [Sub-usecase 2](../../items/wireframe-docs/README.md#sub-usecase-2-validate-treemd) + [Sub-usecase 4](../../items/wireframe-docs/README.md#sub-usecase-4-verify-the-tree-data-wireframe-trio) + [Sub-usecase 7](../../items/wireframe-docs/README.md#sub-usecase-7-evaluate-against-the-guidelines).
- Agent reads the trio to keep building (into hallmark): see [Sub-usecase 5](../../items/wireframe-docs/README.md#sub-usecase-5-agent-reads-the-trio-to-build).
- Quick multi-width/variant review with the viewer: see [Sub-usecase 6](../../items/wireframe-docs/README.md#sub-usecase-6-quick-review-with-the-viewer).
- Author + play flows like video: see [Sub-usecase 8](../../items/wireframe-docs/README.md#sub-usecase-8-author-and-play-flows).
- Suite review gate (DoD): see [Sub-usecase 9](../../items/wireframe-docs/README.md#sub-usecase-9-suite-review-gate).

### Concrete commands (for UI)
- Write brief + tree + data: copy `convention/brief-template.md` to `.aidomaincraft/.tmp/wireframes/<suite>/brief.md` and fill REQ-xxx; `mkdir -p .aidomaincraft/.tmp/wireframes/<suite>/my-page && cp items/wireframe-docs/examples/tree.md .aidomaincraft/.tmp/wireframes/<suite>/my-page/my-page-tree.md`, edit per `convention/tree-format.md` (Kiểu from the pinned shadcn vocab in `component-roles.md`; behavior/effect/reduced/ref per the allowlists) + write `my-page-data.json` per `convention/data-schema.md`.
- Ensure ignored: check `.gitignore` already lists `.aidomaincraft/` (add when missing), verify with `git check-ignore -v .aidomaincraft/.tmp/wireframes/<suite>/my-page/my-page-tree.md`.
- Validate the tree (inside `items/wireframe-docs/`): `python3 scripts/check.py .aidomaincraft/.tmp/wireframes/<suite>/my-page/my-page-tree.md`.
- Evaluate against the guidelines: `python3 scripts/check-guidelines.py .aidomaincraft/.tmp/wireframes/<suite>/my-page/my-page-tree.md` (auto-finds data; per-rule report + SCORE).
- Author the 4-frame wireframe per the tree, then check the pair: copy `examples/tree.html` to `.aidomaincraft/.tmp/wireframes/<suite>/my-page/my-page-wireframe.html` as a skeleton, hand-edit per the tree, then `python3 scripts/verify-pair.py .aidomaincraft/.tmp/wireframes/<suite>/my-page/my-page-tree.md .aidomaincraft/.tmp/wireframes/<suite>/my-page/my-page-wireframe.html`.
- Quick review: copy `templates/viewer.html` into the same version folder, open `viewer.html?file=my-page-wireframe.html` (scaled-to-fit virtual frame, caption shows real width + scale %; click a component for its card) — see [Sub-usecase 6](../../items/wireframe-docs/README.md#sub-usecase-6-quick-review-with-the-viewer).
- Browse every page outside flows: open `player.html` → `▦ Pages` button (thumbnail grid, click through per-breakpoint detail) — see [Sub-usecase 8](../../items/wireframe-docs/README.md#sub-usecase-8-author-and-play-flows).
- Author + play flows: write `flows/<name>.md` per the `convention/flows.md` schema (`Entry:` + `## Step:` with `Page/Action/go:/Input:/If:/Else:`), then `python3 scripts/check-flow.py .aidomaincraft/.tmp/wireframes/<suite>` + `python3 scripts/build-flow.py .aidomaincraft/.tmp/wireframes/<suite>` → open `player.html` (square full-page list/detail/play at canonical W×H + breakpoint picker + branch choices + typing + constraints panel; dialog renders the real block + icon button for meta; `▦ Pages` tab browses every page outside flows; badge/Ctrl+Click shows cards) — see [Sub-usecase 8](../../items/wireframe-docs/README.md#sub-usecase-8-author-and-play-flows).
- Gate the suite: `python3 scripts/check-suite.py .aidomaincraft/.tmp/wireframes/<suite>` (brief + every page + every flow + REQ cross-check + player freshness; exit 0 = DoD met) — see [Sub-usecase 9](../../items/wireframe-docs/README.md#sub-usecase-9-suite-review-gate).

### Domain-specific notes
- Settle the tree + data + wireframe trio before the hallmark detail build; on any-side change fix the other sides and re-run `verify-pair.py`, never treat one side as matching. Keep every draft tree/data/HTML under the ignored version folder `.aidomaincraft/.tmp/wireframes/<suite>/<page>/`, never at the root. Reported drifts belong to the designer; agent and claude never fix them silently. Visual judgment on the 4-frame wireframe goes to claude. Key info (CTA, states, effects, behavior, reduced, ref, visibility) must be in `note:/states:/effect:/behavior:/reduced:/ref:/hide:` syntax and `data-wf-*` blocks, never free prose. Kiểu must come from the pinned shadcn vocab (`component-roles.md`), never invented. Quick multi-width review uses the viewer (type → variant on a scaled-to-fit virtual frame, 4-frame grid, click-cards) instead of manual Chrome resizing.

### Core strengths FOR UI
- A machine-checked tree + data + wireframe trio: git-versioned tree.md defines scope, the data file holds real sample content, the hand-authored wireframe shows all 4 breakpoints, `verify-pair.py` catches every drift and `check-guidelines.py` scores guidelines compliance for the designer to rule on. Absolute lightness: stdlib Python, $0, offline.

### Work split FOR this UI
- Main agent drafts + checks + authors the wireframe + checks the trio + evaluates guidelines + presents the pair, both PASS lines and SCORE; visual review goes to claude as a whole, every drift goes to the designer. Details: [origin Work split](../../items/wireframe-docs/README.md#work-split).

### Links to origin (3-way)
- Origin: `../../items/wireframe-docs/README.md`. Index: `./README.md`. Backlisted at origin `#where-used`.

### Reproduce on another runtime
- Everything is runtime-neutral: `git` CLI + stdlib Python + opening HTML files in a browser (`file://`, offline); `node --check` is optional (runs only when node exists).
- To redo the same result on another runtime (OpenCode/Claude Code/Cursor/Copilot...): install the same skill + version recorded in CHANGELOG, read the recorded decisions (Picks/stamp/commit message — never the local `.relay/` log, which is git-ignored), run `tests/test.sh` until `fail=0`.
- Human visual check works on any runtime: open the demo-built `viewer.html`/`player.html` and compare against the checklist in CHANGELOG; no dependency on any browser-driving tool.
