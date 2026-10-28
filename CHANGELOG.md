# CHANGELOG.md — aidomaincraft

## v6 — 2026-10-28
- Nâng `CHARTER.md` lên v6: mọi thay đổi phải qua vòng self-review lặp đến khi hết FAIL (`VERIFY.md` mục E).
- `VERIFY.md` thêm mục E: lượt 1 người không biết gì (bắt thiếu input/lệnh/output, thuật ngữ chưa giải thích, ví dụ `<...>` trống), lượt 2 từng usecase (cơ chế khác nhau ở đâu, lệnh chạy thật không, ngưỡng đo được không), lượt 3 quyết định so sánh (1 case cụ thể chọn được trong 3 phút vs hệ viral không + ghi case vào CHANGELOG/handoff).
- `AGENTS.md` cập nhật workflow tạo mới 6 bước có vòng lặp review + ghi case đã thử.
- Self-review vòng 1 trên docs hiện có: lượt 1 đạt (cơ chế + thuật ngữ đã nêu), lượt 2 WARN (usecase `hallmark/`/`reactbits/` vẫn dạng bảng, chưa tách block 6 field — giữ lại vì nội dung đã đủ lệnh + ngưỡng, sẽ refactor khi thêm usecase mới), lượt 3 đạt với case `landing SaaS cần pass gates → Hallmark chính` và `1 hero text React → React Bits chính`.
- Bumped `CHARTER.md` to v6: iterative self-review loop until zero FAIL (`VERIFY.md` section E).
- `VERIFY.md` adds section E (beginner / per-usecase / comparison-decision passes). `AGENTS.md` adds the loop + tried-case log.
- Self-review loop 1 on current docs: pass 1 pass, pass 2 WARN (item sub-usecases still tables, not 6-field blocks — kept since commands + bars exist, refactor on next usecase add), pass 3 pass (`gated SaaS landing → Hallmark`, `one React hero text → React Bits`).
- Verify đầy đủ A-E ngày 2026-10-28 vòng 2: A đạt (đủ khung v6, song ngữ), B đạt (nguồn repo/docs/số liệu stars, lệnh đã kiểm), C đạt (điểm khác biệt có ngưỡng + khi nào dùng, đối thủ viral nêu tên + số), D FAIL đã sửa (index còn ghi `CHARTER v5` → sửa lên v6, khớp AGENTS v6), E lượt 1 FAIL đã sửa (prompt mẫu chỉ có `<...>` → thêm 1 ví dụ điền sẵn mỗi item), lượt 2 WARN giữ lại (bảng usecase chưa tách block 6 field), lượt 3 đạt (2 case 3 phút chọn được). Chạy lại từ lượt 1 sau sửa: hết FAIL.
- Full A-E verify 2026-10-28 loop 2: A pass (v6 frame, bilingual), B pass (sourced), C pass (decision thresholds + named viral opponents), D FAIL fixed (`CHARTER v5` refs → v6), E pass-1 FAIL fixed (added 1 filled prompt example per item), pass-2 WARN kept (tables vs 6-field blocks), pass-3 pass (2 cases decidable). Re-ran from pass 1 after fixes: zero FAIL.

## v5 — 2026-10-28
- Nâng `CHARTER.md` lên v5: item bắt buộc mục `Cách item hoạt động` (tổ chức đứng sau + phương thức chung + khác biệt vận hành theo usecase, có thẩm tra nguồn, cấm chép marketing); index thêm cột `Vận hành tóm tắt 1 câu`; mọi thay đổi qua `templates/` + `VERIFY.md`.
- Viết lại `AGENTS.md`: workflow tra cứu 4 bước + tạo mới 6 bước (copy template → thẩm tra nguồn → viết đủ khung → cập nhật index cùng commit → tự chấm VERIFY → ghi CHANGELOG).
- Thêm `VERIFY.md` (checklist Tồn tại/Chính xác/Quyết định/Đồng bộ, FAIL = không merge) + `templates/item-template.md` + `templates/domain-index-template.md` (điền chỗ trống + ví dụ đạt/không đạt).
- Thêm `Cách item hoạt động / How the item works` cho `hallmark/` + `reactbits/`; thêm cột vận hành tóm tắt ở `ui/README.md`.
- Bumped `CHARTER.md` to v5: required `How the item works` (backing org + core method + per-usecase differences, sourced, no marketing copy); index adds operating-summary column; all changes via `templates/` + `VERIFY.md`.
- Rewrote `AGENTS.md` (4-step lookup + 6-step authoring). Added `VERIFY.md` + 2 templates. Added operation sections to both items.

## v4 — 2026-10-28
- Nâng `CHARTER.md` lên v4: mục `Định vị khác biệt` bắt buộc trong item (so 1-2 hệ cùng phân khúc viral có số liệu, bảng tiêu chí quyết định, khi nào chọn/bỏ, cấm mô tả thưởng thức); index thêm cột `Vì sao chọn A thay vì B`.
- Viết lại `ui/README.md` theo chuẩn v4 (định vị + ma trận có tiêu chí phân biệt, workflow phối hợp).
- Thêm `Định vị khác biệt / Differentiating positioning` cho `hallmark/` (vs generator viral v0/Lovable + lib viral shadcn/ui) và `reactbits/` (vs engine viral Motion/GSAP + collection viral Magic UI/Aceternity UI).
- Bumped `CHARTER.md` to v4: required `Differentiating positioning` in items (1-2 same-segment viral systems with numbers, decision-criteria table, when to pick/drop, no appreciation wording); index adds `Why pick A over B` column.
- Rewrote `ui/README.md` to v4. Added differentiation to both items.

## v3 — 2026-10-28
- Nâng `CHARTER.md` lên v3: usecase con là block 6 field (tên/khi dùng/khi bỏ qua/lệnh copy-paste/ngưỡng/ví dụ+pitfalls), cấm động từ mơ hồ, mỗi usecase 1 lệnh chạy được + 1 ví dụ thật, pitfalls gắn gate cụ thể.
- Chuẩn index domain: bảng điều hướng (việc-item chính-hỗ trợ-lệnh), bảng định vị (mạnh/yếu/dùng chính/tránh/thay thế bởi), ma trận chồng lấn (chính-hỗ trợ-thay thế-không dùng + tiêu chí chọn), workflow phối hợp mẫu.
- Luật nhất quán index ↔ item: chi tiết chỉ sống trong item, index chỉ tóm + link; link 2 chiều; tên khớp từng chữ; sửa cùng commit; checklist mồ côi/link/viết song ngữ.
- Viết lại `ui/README.md` theo chuẩn index v3 (định vị Hallmark vs React Bits, ma trận chồng lấn, workflow phối hợp).
- Thêm `Quay lại index / Back to index` 2 chiều cho `hallmark/` + `reactbits/`.
- Bumped `CHARTER.md` to v3: 6-field sub-usecase blocks, no vague verbs, 1 runnable command + 1 real example per usecase, pitfalls cite concrete gates.
- Domain index standard: routing table, positioning table, overlap matrix, combined workflow.
- Index ↔ item consistency: single source in item, index summarizes + links; 2-way links; word-for-word names; same-commit change; orphan/link/bilingual checklist.
- Rewrote `ui/README.md` to v3 index standard. Added 2-way backlinks to both items.

## v2 — 2026-10-28 (cập nhật)
- Đổi nguyên tắc: 1 công cụ/giải pháp = 1 item. Tên item = tên giải pháp (`hallmark`). Usecase con nằm trong `README.md` của item.
- Nâng `CHARTER.md` lên v2, cập nhật `README.md`, `AGENTS.md`, `ui/README.md`.
- Thêm item đầu tiên `ui/hallmark/` với bảng usecase con, cách cài OpenCode, pitfalls.
- Viết lại `ui/hallmark/README.md` chi tiết từ SKILL.md + anatomy/flow/redesign/gates/layout/imagery/craft/patterns: lệnh copy-paste, ngưỡng số, Floor checklist, pre-flight/deal/scaffold/sweep, component/app-screen/redesign-audit, export tokens.
- Thêm item `ui/reactbits/`: React Bits là gì (215+ component React source-owned, 4 biến thể JS/TS+CSS/TW, 5 nhóm), cài 3 đường (shadcn CLI/jsrepo/copy tay) + MCP registry, bảng usecase, pitfalls giao thoa Hallmark.
- Changed rule: 1 tool/solution = 1 item. Item name = solution name (`hallmark`). Sub-usecases live inside the item README.
- Bumped `CHARTER.md` to v2, updated `README.md`, `AGENTS.md`, `ui/README.md`.
- Added first item `ui/hallmark/` with sub-usecase table, OpenCode install, pitfalls.
- Rewrote `ui/hallmark/README.md` in detail from SKILL.md + anatomy/flow/redesign/gates/layout/imagery/craft/patterns: copy-paste commands, numeric budgets, Floor checklist, pre-flight/deal/scaffold/sweep, component/app-screen/redesign-audit, token export.
- Added `ui/reactbits/` item: what React Bits is (215+ owned-source React components, 4 JS/TS+CSS/TW flavors, 5 groups), 3 install routes (shadcn CLI/jsrepo/hand) + MCP registry, usecase table, Hallmark-overlap pitfalls.

## v1 — 2026-10-28
- Khởi tạo khung: `README.md`, `AGENTS.md`, `CHARTER.md v1`.
- Thêm domain đầu tiên `ui/` (trống, chờ người dùng tự thêm item).
- Init skeleton: `README.md`, `AGENTS.md`, `CHARTER.md v1`.
- Added first empty domain `ui/` (items to be added by owner).
