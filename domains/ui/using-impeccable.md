# using-impeccable CHO UI (CHARTER v12)

> Phần RIÊNG khi dùng Impeccable cho UI. Gốc sống ở `../../items/impeccable/README.md`; mọi lệnh/ngưỡng dưới đây khớp từng chữ với gốc. Không copy lại toàn bộ cài đặt/cơ chế.

## Tiếng Việt

### Usecase trong domain này
- ★ Polish/refine UI có sẵn giữ system (1 lệnh/pass + detector before/after): xem [Usecase con 1](../../items/impeccable/README.md#usecase-con-1-polishrefine-ui-co-san--manh-nhat).
- Build mới qua direction picker + comp-led/code-led: xem [Usecase con 2](../../items/impeccable/README.md#usecase-con-2-build-moi-qua-direction-picker).
- Review xếp hạng `critique`/audit P0-P3: xem [Usecase con 3](../../items/impeccable/README.md#usecase-con-3-review-xep-hang-critiqueaudit).
- Iterate trực quan Live/generate + detector CI/hooks: xem [Usecase con 4](../../items/impeccable/README.md#usecase-con-4-iterate-truc-quan-livegenerate--detector-ci).

### Lệnh mẫu cụ thể (cho UI)
- Polish 1 page: `/impeccable polish the pricing page` (kèm `Keep our colors and the current plan names`) rồi `npx impeccable detect src/` so baseline — xem [Usecase con 1](../../items/impeccable/README.md#usecase-con-1-polishrefine-ui-co-san--manh-nhat).
- Build mới: `/impeccable init` rồi `/impeccable design a signup page for our monthly book club. Help visitors understand the next event and reserve a seat.` — xem [Usecase con 2](../../items/impeccable/README.md#usecase-con-2-build-moi-qua-direction-picker).
- Review: `/impeccable critique the pricing page` + `/impeccable audit site/index.html` — xem [Usecase con 3](../../items/impeccable/README.md#usecase-con-3-review-xep-hang-critiqueaudit).
- Live + CI: `/impeccable live` (trên `http://localhost:3000`) hoặc `/impeccable generate 3 bold variants of the pricing cards`; CI `npx impeccable detect --json .` (exit 2 = findings) — xem [Usecase con 4](../../items/impeccable/README.md#usecase-con-4-iterate-truc-quan-livegenerate--detector-ci).

### Lưu ý riêng cho UI
- Findings mà thuộc về system (thiếu tokens, shape lặp, hero sai fold) thì sửa bằng Hallmark thay vì vá lẻ bằng Impeccable — xem [Định vị](../../items/impeccable/README.md#dinh-vi-khac-biet-so-lieu-ngay-08112026-tru-khi-ghi-khac).
- 1 project UI = 1 skill design: đã bật Impeccable thì disable Hallmark/guidelines ở local scope (ngược lại agent load cả hai, hook chạy đôi). Nguồn: [Cốt lõi](../../items/impeccable/README.md#cot-loi-bat-bien).
- Live chỉ trên checkout local (cấm inject production/CSP yếu); Live Apply bypass approvals khi không poll — review staged edits trước. Nguồn: [Usecase con 4](../../items/impeccable/README.md#usecase-con-4-iterate-truc-quan-livegenerate--detector-ci).
- Exception (`overused-font` cho brand font...) ghi 1 lần bằng `ignores add-value --reason` + commit `.impeccable/config.json`, không cãi với agent mỗi lần. Nguồn: [Pitfalls](../../items/impeccable/README.md#pitfalls).

### Điểm mạnh cốt lõi CHO UI
- Vốn từ 24 lệnh + detector không-LLM + Live pick-compare-accept trên UI có sẵn mà giữ system: quyết định chọn thay vì guidelines khi cần sửa tới nơi + mắt thấy, thay vì list lỗi nhanh. Xem [Định vị](../../items/impeccable/README.md#dinh-vi-khac-biet-so-lieu-ngay-08112026-tru-khi-ghi-khac).
- Review xếp hạng P0-P3 + check drift `DESIGN.md` (font/color/radius/size ngoài system) — thứ guidelines (checklist phẳng) và Hallmark (gates lúc sinh) đều không gánh.

### Phân công CHO UI này
- Agent chính `init` + shortlist 1 lệnh (user pick) → chạy 1 lệnh/pass → review `git diff` + detector before/after; bước visual giao nguyên cục cho claude (mở browser verify focus/contrast/motion/màn hẹp). Chi tiết: [Phân công gốc](../../items/impeccable/README.md#phan-cong-ai-lam-gi).

### Link về item gốc (3 chiều)
- Gốc: `../../items/impeccable/README.md` (Cài đặt / Cách hoạt động / Định vị / Bản đồ phủ / Hồ sơ quyết định / Usecase 1-4 / Pitfalls / Tham khảo sử dụng).
- Index domain: `./README.md` (hàng impeccable ở điều hướng + định vị + chồng lấn).
- Được liệt kê ngược tại: `../../items/impeccable/README.md#duoc-dung-o-dau`.

---

## English

UI-only deltas for Impeccable. Origin lives at `../../items/impeccable/README.md`; commands/bars below match it word-for-word.

### Usecases in this domain
- ★ Polish/refine existing UI in place (one command/pass + detector before/after): see [Sub-usecase 1](../../items/impeccable/README.md#sub-usecase-1-polishrefine-existing-ui--strongest).
- New builds via direction picker + comp-led/code-led: see [Sub-usecase 2](../../items/impeccable/README.md#sub-usecase-2-new-build-via-direction-picker).
- Ranked `critique`/`audit` reviews (P0-P3): see [Sub-usecase 3](../../items/impeccable/README.md#sub-usecase-3-ranked-review-critiqueaudit).
- Visual Live/generate iteration + detector CI/hooks: see [Sub-usecase 4](../../items/impeccable/README.md#sub-usecase-4-visual-iteration-livegenerate--detector-ci).

### Concrete commands (for UI)
- Polish one page: `/impeccable polish the pricing page` (plus `Keep our colors and the current plan names`), then `npx impeccable detect src/` against the baseline.
- New build: `/impeccable init`, then `/impeccable design a signup page for our monthly book club. Help visitors understand the next event and reserve a seat.`
- Review: `/impeccable critique the pricing page` + `/impeccable audit site/index.html`.
- Live + CI: `/impeccable live` (on `http://localhost:3000`) or `/impeccable generate 3 bold variants of the pricing cards`; CI via `npx impeccable detect --json .` (exit 2 = findings).

### Domain-specific notes
- System-level findings (missing tokens, repeated shapes, wrong-fold hero) get fixed with Hallmark, not patched ad hoc. Visual verdicts need claude with a real browser. One design skill per UI project. Live on local checkouts only; review Live Apply staged edits first.

### Core strengths FOR UI
- 24-command vocabulary + model-free detector + Live pick-compare-accept on existing UI while keeping the system — pick over guidelines when fixes must land + be seen, not just listed.
- P0-P3 ranked reviews + `DESIGN.md` drift checks (off-system font/color/radius/size).

### Work split FOR this UI
- Main agent `init`s + shortlists one command (user picks) → runs one command/pass → reviews `git diff` + detector before/after; visual steps go to claude as a whole. Details: [origin Work split](../../items/impeccable/README.md#work-split).

### Links to origin (3-way)
- Origin: `../../items/impeccable/README.md`. Index: `./README.md`. Backlisted at origin `#where-used`.
