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

**Lượt 4+ — Vòng review đối lập không giới hạn (lặp đến khi tài liệu cụ thể mới dừng):**
- Mỗi lượt là 1 persona khác lượt trước (bốc từ bộ vai bên dưới, cấm 2 lượt liên tiếp cùng vai, cấm hỏi lại câu lượt trước đã trả lời đạt).
- Mỗi lượt phải làm đủ 3 việc: (1) đặt câu hỏi đối lập mới — `khác gì hệ X trong việc A?`, `tại sao phải chọn hệ này trong khi đã có hệ B?`, `bẫy ở đâu (giá, lock-in, giới hạn free)?`, kèm yêu cầu chứng minh bằng số/lệnh/nguồn, không bằng tính từ; (2) đề xuất kiểm tra bổ sung cụ thể (lệnh phải chạy, docs phải mở, số phải đối chiếu); (3) phán quyết pass/fail từng mục.
- Tác giả chạy kiểm tra bổ sung → sửa → lặp lượt mới với vai mới. Mỗi lượt ghi log: vai nào, hỏi gì, kết quả gì.
- Bộ vai xoay vòng (không bao giờ dùng cùng vai 2 lượt liên tiếp): Kẻ hoài nghi (chỉ tin số, luôn hỏi “sao không B”) · Người vận hành khó tính (chỉ quan tâm cài/chạy được trong 10 phút không, thiếu bước nào) · Người mới hoàn toàn (không biết gì, bắt mọi chỗ phải đoán) · Người giữ ngân sách (chỉ hỏi tiền, free/lock-in/tổng sở hữu) · Phe đối thủ (bênh hệ B, bắt item phải thắng bằng tiêu chí đo được).
- Điều kiện dừng (thiếu 1 là lặp tiếp): (1) hết FAIL theo A–F; (2) không còn câu “tại sao không B” nào chưa trả lời bằng số/lệnh/nguồn; (3) mỗi usecase con đã qua ít nhất 1 thử thách “chứng minh đi” và đứng vững; (4) bài kiểm tra 3 phút: người lạ đọc index + item là chọn được.
- Chống lặp vô hạn: câu hỏi trùng lượt cũ tính là lượt không hợp lệ, đổi vai hỏi lại.

### F. Quy trình thẩm tra sâu (bắt buộc cho item mới, chống thẩm tra nông)
Mục này dạy *cách hỏi*, không chỉ *mục cần có*. Áp dụng nguyên văn cho mọi tool mới, không cần ai hướng dẫn thêm.

**F0. Thu thập bằng chứng theo thang (ghi nguồn từng khẳng định):**
1. Mạnh nhất: tự chạy lệnh / đọc file nguồn (`SKILL.md`, `package.json`, script install, output lệnh) — bắt buộc cho mọi lệnh copy-paste và ngưỡng số.
2. Docs chính chủ (repo, trang install, registry) — dùng cho license, giá, tính năng.
3. Review độc lập / số liệu thị trường (stars, installs, bài review) — dùng cho độ viral và so sánh.
4. Marketing của vendor — chỉ để tham khảo, cấm trích làm sự thật. Thiếu số thì ghi `chưa xác minh được`, cấm đoán.

**F1. Bộ 8 câu hỏi quyết định (trả lời đủ 8, cấm chung chung — mỗi câu phải có số/tên/lệnh cụ thể):**
1. Việc gì DÙNG (liệt kê 3+, cụ thể)?
2. Việc gì KHÔNG DÙNG (liệt kê 3+, mỗi việc kèm hệ thay thế)?
3. Free bao nhiêu / tổng bao nhiêu, giá chính xác?
4. Cài mấy bước — đã chạy thử đến bước nào, output gì?
5. Đối thủ cùng phân khúc viral là ai (tên + số stars/installs)?
6. Với cùng 1 việc, chọn nó thay vì đối thủ vì tiêu chí đo được nào?
7. Ma sát: cần auth/login/Node/trả phí gì?
8. Khi nào TUYỆT ĐỐI không dùng?

**F2. Bản đồ việc và ma trận chọn hệ:**
- Bảng việc phủ (việc → usecase con nào gánh) + bảng việc KHÔNG phủ (việc → hệ thay thế).
- Ma trận: hàng là việc, cột là các hệ (item này + 2 đối thủ viral), ô là `chính / hỗ trợ / thay thế / không dùng` + 1 dòng tiêu chí phân biệt đo được.

**F3. Đo ma sát cài đặt:** đếm số bước từ 0 đến chạy được lệnh đầu tiên; liệt kê mọi rào cản (tài khoản, browser auth, Node, tiền, quyền admin). So với 1 dòng lệnh chuẩn (`npx skills add ...`) thì hơn/kém mấy bước?

**F4. Bài kiểm tra bác bỏ:** tự đóng vai người phản biện — nêu 3 việc mà đọc xong tài liệu vẫn KHÔNG rõ có nên dùng item không; nếu có, tài liệu FAIL, viết lại đến khi trả lời được.

**F5. Vòng lặp tự hoàn thiện:** mỗi lần phát hiện thẩm tra nông lọt lưới, ghi gap 1 dòng vào `CHANGELOG.md` + bổ sung câu hỏi hoặc ví dụ tương ứng vào mục F này. Checklist tự dày lên, không phụ thuộc người nhắc.

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

**Round 4+ — Unbounded adversarial review loop (repeat until the docs are concrete):**
- Each round is a different persona from the previous round (draw from the deck below; never the same persona twice in a row, never re-ask a question a prior round already passed).
- Each round must do all 3: (1) ask NEW adversarial questions — `how is this different from system X in job A?`, `why pick this when B exists?`, `where is the catch (price, lock-in, free limits)?` — demanding proof by numbers/commands/sources, never adjectives; (2) propose concrete additional checks (commands to run, docs to open, numbers to cross-check); (3) deliver pass/fail per item.
- Author runs the additional checks → fixes → next round with a new persona. Log every round: which persona, what was asked, what resulted.
- Rotating persona deck (never same persona twice in a row): The Skeptic (trusts only numbers, always asks "why not B") · The Grumpy Operator (only cares: can I install/run this in 10 minutes, which step is missing) · The Total Beginner (knows nothing, flags every guessing point) · The Budget Holder (only asks money: free/lock-in/total cost) · The Opponent Camp (roots for system B, forces the item to win on measurable criteria).
- Stop conditions (miss one and the loop continues): (1) zero FAIL under A–F; (2) no unanswered "why not B" question left without numbers/commands/sources; (3) every sub-usecase survived at least one "prove it" challenge; (4) the 3-minute test: a stranger reads the index + item and can decide.
- Anti-infinite-loop: a repeated question from a prior round makes that round invalid — switch persona and re-ask.

### F. Deep audit procedure (required for new items, prevents shallow audits)
This section teaches *how to ask*, not just *what to include*. Apply verbatim to every new tool, no extra guidance needed.

**F0. Collect evidence on a ladder (source every claim):**
1. Strongest: run commands / read source files yourself (`SKILL.md`, `package.json`, install script, command output) — required for every copy-paste command and numeric bar.
2. Canonical docs (repo, install page, registry) — for license, price, features.
3. Independent reviews / market numbers (stars, installs, reviews) — for virality and comparison.
4. Vendor marketing — reference only, never quote as fact. Missing numbers → write `unverified`, never guess.

**F1. The 8 decision questions (answer all 8, generic answers FAIL — each needs numbers/names/commands):**
1. Which jobs DOES it serve (list 3+, concrete)?
2. Which jobs does it NOT serve (list 3+, each with its replacement)?
3. How many free / total, exact price?
4. How many install steps — how far did you run, with what output?
5. Who are the viral same-segment opponents (names + stars/installs)?
6. For the same job, why pick it over opponents, by which measurable criterion?
7. Friction: what auth/login/Node/payment is required?
8. When must you ABSOLUTELY NOT use it?

**F2. Job map and system-choice matrix:**
- Covered-job table (job → which sub-usecase carries it) + NOT-covered table (job → replacement system).
- Matrix: rows are jobs, columns are the systems (this item + 2 viral opponents), cells are `primary / supporting / replaceable / do-not-use` + 1 measurable distinguishing rule.

**F3. Measure install friction:** count steps from zero to first runnable command; list every barrier (account, browser auth, Node, money, admin rights). How many steps more/fewer than the one-line standard (`npx skills add ...`)?

**F4. Rejection test:** play devil's advocate — name 3 jobs that remain unclear after reading the docs; if any exist, the docs FAIL, rewrite until answerable.

**F5. Self-improvement loop:** every time a shallow audit slips through, log the gap in one `CHANGELOG.md` line + add the corresponding question or example to this section F. The checklist thickens itself, no reminders needed.
