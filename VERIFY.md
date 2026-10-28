# VERIFY.md — checklist thẩm tra (FAIL = không merge)

## Tiếng Việt

### A. Tồn tại (thiếu là FAIL)
- [ ] Item đủ khung v6: Dùng khi / Bỏ qua khi / Cài đặt / Cách item hoạt động (3 phần) / Định vị khác biệt / Usecase con 6 field / Bước chung / Prompt mẫu / Pitfalls / Tham khảo / Quay lại index.
- [ ] Index domain đủ: mục đích 1 dòng / điều hướng / định vị (có Vận hành tóm tắt + Vì sao chọn A thay vì B) / chồng lấn / workflow phối hợp / danh sách item.
- [ ] Song ngữ VI trước EN sau, đủ cả 2.

### B. Chính xác có nguồn (thiếu nguồn là FAIL)
- [ ] `Tổ chức đứng sau` có link repo/registry + license + số liệu (stars/installs).
- [ ] Mỗi lệnh copy-paste đã mở docs/source kiểm tra (ghi tên file check: `SKILL.md`, `package.json`, trang install/MCP, script).
- [ ] Mỗi ngưỡng số có nguồn (ví dụ 84px/52px/container 1440/gutter 64 từ `layout.md`; 4 biến thể từ README React Bits; Floor gate có số).
- [ ] Không chép mô tả marketing nguyên văn.

### C. Quyết định (chung chung là FAIL)
- [ ] Mỗi điểm khác biệt kèm ngưỡng/ví dụ đổi lựa chọn + `khi nào dùng sẽ phù hợp`.
- [ ] So sánh đúng hệ viral cùng phân khúc (nêu tên + số liệu), cấm hệ vô danh.
- [ ] Ma trận chồng lấn mỗi việc đúng 1 `chính`, có tiêu chí phân biệt đo được.
- [ ] Pitfalls gắn gate/lỗi cụ thể, cấm `chú ý hiệu năng`.

### D. Đồng bộ (lệch là FAIL)
- [ ] Tên việc/lệnh index khớp từng chữ usecase item.
- [ ] Link 2 chiều sống: index → item, item → index + item liên quan.
- [ ] Không item mồ côi, không link gãy, VI/EN cùng nội dung.
- [ ] Sửa index + item trong cùng commit + `CHANGELOG.md`.

### Thang điểm
- FAIL: 1 ô FAIL là không merge.
- WARN: giữ lại phải ghi lý do 1 dòng trong `CHANGELOG.md`.

### E. Vòng self-review lặp đến khi đạt (bắt buộc)
Lặp 3 lượt dưới đây, sửa hết FAIL rồi chạy lại từ lượt 1. Chỉ dừng khi 1 vòng đầy không còn FAIL mới.

Lượt 1 — Người không biết gì (bắt thiếu sót không rõ ràng):
- [ ] Đọc `Cách item hoạt động` như người mới: có hiểu item là gì, ai làm, chạy bằng cơ chế nào, khác tool thường ở đâu không? FAIL nếu phải đoán (ví dụ: ghi `scaffold tokens` nhưng không nói lệnh nào viết file nào).
- [ ] Mỗi usecase con: input là gì, chạy lệnh/script nào, output ra file/giao diện nào? FAIL nếu thiếu 1 trong 3.
- [ ] Thuật ngữ nào chưa giải thích lần đầu xuất hiện (Floor, sweep, scaffold, variant, MCP registry)? FAIL nếu dùng trước, giải thích sau.
- [ ] Ví dụ có đủ cụ thể để làm theo từng bước không? FAIL nếu ví dụ dùng `<...>` mà không có 1 case điền sẵn.

Lượt 2 — Thẩm tra từng usecase (cơ chế khác nhau):
- [ ] Mỗi usecase con nêu rõ cơ chế khác usecase khác ở đâu (ví dụ Hallmark component bỏ deal theme + hero; React Bits tool web export asset thay vì CLI). FAIL nếu 2 usecase mô tả giống nhau.
- [ ] Lệnh copy-paste chạy được thật trên stack đã nêu (variant, path, flag). FAIL nếu thiếu variant/flag bắt buộc.
- [ ] Ngưỡng đo được (số px, %, số states, checklist gates). FAIL nếu ngưỡng kiểu `đảm bảo đẹp`.
- [ ] Pitfalls gắn đúng usecase đó, không copy chung.

Lượt 3 — Người cần quyết định so sánh (đủ để chọn vs hệ viral không):
- [ ] Với 1 case cụ thể tự đặt (ví dụ `landing SaaS cần pass gates` / `1 hero text React`), chỉ đọc index + 2 item so sánh có chọn được không, mất bao lâu? FAIL nếu quá 3 phút vẫn phân vân.
- [ ] Bảng định vị nêu rõ khi nào chọn A bỏ B bằng tiêu chí đo được (stack/giá/pass gates/LCP/a11y). FAIL nếu lý do kiểu `cũng tốt`.
- [ ] Đối thủ so sánh là hệ viral thật (tên + số liệu), cùng phân khúc. FAIL nếu đối thủ vô danh hoặc khác phân khúc.
- [ ] Ghi lại case đã thử + quyết định + lý do 1 dòng vào `CHANGELOG.md` hoặc handoff review.

---

## English

### A. Existence (missing = FAIL)
- [ ] Item has the full v6 frame: When/skip / Install / How it works (3 parts) / Differentiation / 6-field sub-usecases / Shared steps / Prompts / Pitfalls / References / Back to index.
- [ ] Domain index has: 1-line purpose / routing / positioning (with operating summary + why-A-over-B) / overlap / combined workflow / item list.
- [ ] Bilingual VI first EN second, both present.

### B. Sourced accuracy (unsourced = FAIL)
- [ ] Backing org has repo/registry link + license + numbers (stars/installs).
- [ ] Every copy-paste command checked against docs/source (record which file: `SKILL.md`, `package.json`, install/MCP page, script).
- [ ] Every numeric bar sourced (e.g. 84px/52px/container 1440/gutter 64 from `layout.md`; 4 flavors from React Bits README; numbered Floor gates).
- [ ] No verbatim marketing copy.

### C. Decision impact (generic = FAIL)
- [ ] Every difference carries a threshold/example that flips the choice + `when it fits`.
- [ ] Compared against viral same-segment systems (name + numbers), never anonymous ones.
- [ ] Overlap matrix has exactly 1 `primary` per job with a measurable rule.
- [ ] Pitfalls cite concrete gates/errors, never `watch performance`.

### D. Sync (mismatch = FAIL)
- [ ] Index job/command names match item sub-usecase titles word-for-word.
- [ ] Live 2-way links: index → item, item → index + related items.
- [ ] No orphans, no broken links, VI/EN in sync.
- [ ] Index + item changed in the same commit + `CHANGELOG.md`.

### E. Iterative self-review loop until pass (required)
Loop the 3 passes below, fix all FAILs, then restart at pass 1. Stop only after a full loop with zero FAIL.

Pass 1 — Total beginner (catch unclear omissions):
- [ ] Read `How the item works` as a newcomer: is it clear what the item is, who builds it, which mechanism it runs, how it differs? FAIL if guessing is needed (e.g. `scaffold tokens` without which command writes which file).
- [ ] Each sub-usecase: what input, which command/script, what file/UI output? FAIL if any of the 3 is missing.
- [ ] Every term explained on first use (Floor, sweep, scaffold, variant, MCP registry)? FAIL if used before explained.
- [ ] Examples concrete enough to follow step by step? FAIL if the example uses `<...>` with no filled case.

Pass 2 — Per-usecase mechanism check:
- [ ] Each sub-usecase states how its mechanism differs (e.g. Hallmark component skips theme deal + hero; React Bits web tools export assets instead of CLI). FAIL if 2 usecases read identically.
- [ ] Copy-paste commands truly runnable on the stated stack (variant, path, flag). FAIL if a required variant/flag is missing.
- [ ] Measurable bars (px, %, state counts, gate checklist). FAIL on bars like `ensure beauty`.
- [ ] Pitfalls attached to that exact usecase, not shared generic copy.

Pass 3 — Comparison decision check:
- [ ] With one self-set concrete case (e.g. `SaaS landing must pass gates` / `one React hero text`), can a choice be made from the index + 2 items in under 3 minutes? FAIL if still undecided.
- [ ] Positioning states when to pick A over B with measurable criteria (stack/price/gates/LCP/a11y). FAIL on reasons like `also good`.
- [ ] Opponents are real viral same-segment systems (name + numbers). FAIL on anonymous or off-segment opponents.
- [ ] Record the tried case + decision + 1-line reason in `CHANGELOG.md` or the review handoff.
