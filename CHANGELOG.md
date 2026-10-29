# CHANGELOG.md — aidomaincraft

## v7 — 2026-10-29 (tái cấu trúc items/domains + nâng chuẩn thẩm tra F6)
- Đổi cấu trúc: `ui/hallmark|reactbits|skillry/` → `items/hallmark|reactbits|skillry/` (kho trung lập domain) + `domains/ui/` (index + `using-hallmark.md`, `using-reactbits.md`, `using-skillry.md` phần web) + `domains/media/` (index + `using-skillry.md` phần video/deck/OG). Xóa `ui/`. Link 3 chiều bắt buộc: index → using-doc → item gốc (đúng section) + ngược lại.
- `CHARTER.md` v6 → v7: tầng items/ + domains/ + using-doc, luật 1 nguồn sự thật (gốc sống ở item, domain chỉ viết phần riêng + link, trùng lặp = FAIL), 1 việc có thể NHIỀU item chính (kèm tiêu chí phân biệt).
- `VERIFY.md`: A (khung v7 + using-doc bắt buộc), C (nhiều chính + bản đồ phủ quét hết catalog, ★ đầu), D (đồng bộ 3 chiều + chống trùng lặp + mọi khẳng định kỹ thuật link về item), F6 mới (phủ đủ usecase + tham khảo sử dụng: review sâu có trọng lượng + số trung bình có trọng số + ngày đo, mâu thuẫn ghi cả hai + phán quyết).
- `templates/`: `item-template.md` lên v7 (bản đồ phủ + tham khảo sử dụng + được dùng ở đâu), `domain-index-template.md` lên v7 (nhiều chính), mới `domain-using-template.md`.
- `AGENTS.md` + root `README.md`: tra cứu 4 bước mới (chọn domain → using-doc → item gốc), 2 luồng tạo mới (item mới vs cặp item-domain).
- Bổ sung ngược cho 3 item hiện có (VERIFY F6): Hallmark (~40.8K★/2.1K forks 29/10, SkillForge 4.7/5-121, Tessl 68, PluginBench 70; review sâu andrew.ooo 18/07, rohitraj 18/07, heatdrop 18/08, HN ~07/2026; VN chưa xác minh); React Bits (50,552★/2,510 forks live 29/10, PkgPulse 25/03 #2 Rising Stars, 21st.dev 21/08, Annnimate compare, Motion interview 08/01; VN chưa xác minh); Skillry (TrustMRR 29/10 $13,090 total/$4,111 MRR/417 subs, top installs 200-518, review AI IDE List 30/09 + Toolin 07/10 + SkillGild 25/10, Terms non-refundable + Linux không CLI; VN chưa có nguồn).
- Self-review v7 vòng 1: A đạt (đủ khung v7 + using-doc 4 file), B đạt (nguồn repo/docs/API + review có ngày), C đạt (nhiều chính có tiêu chí, bản đồ phủ đủ, ★ đầu), D đạt (file link sống 0 gãy; anchor section gần đúng — WARN giữ lại vì slug tiếng Việt, sẽ chuẩn hóa khi có tool check anchor), E lượt 1-3 đạt (case `landing SaaS cần gates → Hallmark` + `1 hero text React → React Bits` + `deck budget 0đ → free pptx` đều chọn được <3 phút).
- Added v7 EN mirrors for all of the above.
- Gap log (F5): thẩm tra 2026-10-28 nông — liệt kê mà không trả lời quyết định (đã sửa bằng F); review đối lập thiếu vai luân phiên (đã sửa bằng Lượt 4+); tái cấu trúc lần này thiếu anchor check tự động (ghi nhận, cần script check anchor tiếng Việt).

## v6 — 2026-10-29 (thêm item skillry, qua review đối lập 2 lượt)
- Thêm `ui/skillry/` (chợ skill trình bày 617 món): Hồ sơ quyết định đủ (việc dùng/không dùng 3+3, free 40/617, giá $9.99/$79/$169, ma sát CLI, đối thủ viral có số), 4 usecase 6 field, Các bước chung, check `skillry --help` thật + phát hiện Linux lỗi secure storage.
- Vòng 1 (Kẻ hoài nghi): FAIL A/B/C/D (thiếu Các bước chung, chưa chạy CLI, thiếu số skills.sh, placeholder lệnh, thiếu CHANGELOG) → đã sửa hết: thêm mục, chạy CLI, đối chiếu 35.4k★/32.3k★, lệnh mẫu `bs-mint-noir-saas-site` free, entry này.
- Vòng 2 (Người vận hành khó tính): FAIL 5 lỗi (CLI fail trên Linux mà index vẫn để mặc định; thiếu nguyên văn prompt + nút bấm; thiếu verify/restart + sai thư mục; usecase 2-4 + prompt mẫu placeholder; số installs stale + thiếu giá lẻ) → đã sửa hết: paste-prompt lên mặc định (kèm câu lệnh nguyên văn + output `● Loading skill` + restart), CLI xuống macOS/Windows, ZIP ghi đủ 3 thư mục global + project, mỗi usecase 1 slug thật + lệnh chạy ngay, cập nhật installs/views từ /skills + /agent/opencode (Manus ~40-45 installs, Mint Noir free 155/3, Cadence 342/16, Field Notes 287/8, Notion OG 222/7, GrokBot 307/14).
- Vòng 3 (Người mới hoàn toàn): FAIL 5 điểm mù (lệnh index cụt `...`/thiếu https; thiếu bối cảnh paste + tài khoản free; prompt mẫu còn placeholder trống; ZIP nhảy cóc thiếu mkdir/unzip/restart; mâu thuẫn 7/8 agent + đã/chưa chạy CLI) → đã sửa hết: lệnh index đầy đủ copy-paste được, prompt mẫu điền ví dụ thật (quán cà phê A), ZIP có đủ 3 lệnh + restart + 3 thư mục global, chốt 8 flag + trạng thái "đã chạy --help/--status, chưa login", free VẪN cần tài khoản (đối chiếu install.md).
- Vòng 4 (Phe đối thủ): FAIL 3 điểm — (1) thiếu đối thủ free cụ thể per-usecase, (2) so stars repo vs installs skill là sai mẫu số, (3) ngưỡng 'installs > 0' rỗng + thiếu break-even — đã sửa hết sau khi đối chiếu skills.sh leaderboard: thêm bảng đối thủ free (hyperframes product-launch-video ~538.9K, pptx official ~244.5K, Satori/Playwright, shadcn 271.1K) vào Định vị + từng usecase; khung 'Skillry thắng ở taste đóng gói, thua ở capability'; break-even: trả phí khi lặp lại nhiều output cùng taste.
- Vòng 5 (Người giữ ngân sách): FAIL 3 điểm (phí engine ngoài chưa chốt tổng bill; hết sub thì sao + Lifetime gồm gì + Yearly/Monthly chưa quy ra số; break-even cảm tính) → đã sửa hết: giá Skillry CHƯA gồm phí model ngoài, quy tắc gói bằng số (1 lần lẻ→free, <8 tháng Monthly, ≥8 Yearly hòa vốn 79/9.99, >2 năm Lifetime ~17 tháng/~2.1 năm), giữ file đã tải (chưa xác minh chạy tiếp/khóa tải mới — ghi nhận kiểm tra Terms), bỏ mọi hàm ý hiệu quả chi phí không số.
- Vòng 6 (Người giữ ngân sách, xác minh): PASS có điều kiện — xác minh 16/16 bản sửa vòng 1-5 có thật trong file; test 3 phút case deck budget 0đ chọn free pptx thay vì Skillry premium (quyết định đúng theo tài liệu).
- Vòng 7 (Kẻ hoài nghi, xác nhận cuối): PASS — đủ 16/16 bản sửa, test 3 phút chọn được ngay, không còn FAIL. Đủ 4 điều kiện dừng: hết FAIL, hết câu chưa trả lời, mọi usecase qua thử thách, test 3 phút đạt.
- Added `ui/skillry/` (617-item presentation marketplace): full Decision dossier (3+3 jobs, 40/617 free, $9.99/$79/$169 pricing, install friction, viral opponents with numbers), 4 six-field usecases, Shared steps, ran `skillry --help` + found Linux secure-storage error.
- Round 1 (Skeptic): FAIL A/B/C/D (missing Shared steps, CLI unrunned, missing skills.sh numbers, placeholder command, no CHANGELOG) → all fixed: section added, CLI ran, 35.4k/32.3k stars cross-checked, free `bs-mint-noir-saas-site` example command, this entry.
- Round 2 (Grumpy Operator): FAIL 5 (CLI fails on Linux yet set as default; missing verbatim prompt + button location; missing verify/restart + wrong folders; usecases 2-4 + prompts are placeholders; stale install numbers, no per-skill pricing) → all fixed: paste-prompt as default (verbatim sentence + `● Loading skill` output + restart), CLI demoted to macOS/Windows, ZIP lists all 3 global + project folders, each usecase gets a real slug + runnable command, installs/views refreshed from /skills + /agent/opencode (Manus ~40-45 installs, Mint Noir free 155/3, Cadence 342/16, Field Notes 287/8, Notion OG 222/7, GrokBot 307/14).
- Round 3 (Total Beginner): FAIL 5 blind spots (truncated `...` index command without https; missing paste context + free-account question; empty placeholder prompts; jumping ZIP steps without mkdir/unzip/restart; 7-vs-8 agent + ran-vs-unran contradictions) → all fixed: full copy-pasteable index command, filled prompt examples (coffee shop A), ZIP with 3 commands + restart + 3 global folders, settled on 8 flags + "ran --help/--status, not logged in", free STILL needs account (install.md verified).
- Round 4 (Opponent Camp): FAIL 3 points — (1) missing concrete free opponents per usecase, (2) repo-stars vs skill-installs is a wrong-denominator comparison, (3) empty 'installs > 0' bar + no break-even — all fixed after cross-checking the skills.sh leaderboard: added free-opponent table (hyperframes product-launch-video ~538.9K, official pptx ~244.5K, Satori/Playwright, shadcn 271.1K) to Positioning + each usecase; frame 'Skillry wins on packaged taste, loses on capability'; break-even: pay when repeating many outputs in one taste.
- Round 5 (Budget Holder): FAIL 3 points (external engine fees leave total bill open; post-sub behavior + Lifetime scope + Yearly/Monthly uncomputed; feel-based break-even) → all fixed: Skillry price EXCLUDES external model fees, package rule by numbers (one-off→free, <8 months Monthly, ≥8 months Yearly at 79/9.99 break-even, >~2 years Lifetime at ~17 months/~2.1 years), downloaded files stay (UNVERIFIED whether they keep running/block new downloads — flagged for Terms check), dropped all numberless cost-efficiency hints.
- Round 6 (Budget Holder, verify): CONDITIONAL PASS — verified 16/16 round-1–5 fixes present; 3-minute test on 0-budget deck picks free pptx over paid Skillry (correct per docs).
- Round 7 (Skeptic, final confirmation): PASS — all 16 fixes present, 3-minute test decides instantly, zero FAIL. All 4 stop conditions met.
- Gap log (F5): thẩm tra Skillry ngày 2026-10-28 bị nông — liệt kê mà không trả lời quyết định (thiếu map việc phủ/không phủ, thiếu số free/total + giá, thiếu luật chọn chợ, thiếu ma sát cài đặt, thiếu bằng chứng installs). Sửa bằng cách thêm mục F vào `VERIFY.md` + ô Hồ sơ quyết định vào `templates/item-template.md`.
- Gap log (F5): Skillry audit on 2026-10-28 was shallow — listed facts without answering decisions (no covered/not-covered job map, no free/total numbers + price, no marketplace-choice rule, no install friction, no install-count evidence). Fixed by adding section F to `VERIFY.md` + Decision dossier block to `templates/item-template.md`.
- Review đối lập không giới hạn: VERIFY mục E thêm Lượt 4+ — mỗi lượt 1 persona khác lượt trước (kẻ hoài nghi / người vận hành / người mới / người giữ ngân sách / phe đối thủ), 3 việc bắt buộc (câu hỏi đối lập mới + kiểm tra bổ sung + phán quyết), 4 điều kiện dừng. Unbounded adversarial review: rotating personas, additional-check proposals, 4 stop conditions.

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
