# CHARTER.md — aidomaincraft — v10.9

## Tiếng Việt

### 1. Mục đích
Tổng hợp kinh nghiệm dùng AI theo lĩnh vực, dưới dạng chỉ dẫn theo usecase để tái dùng khi tạo dự án mới và làm việc với AI agent.

### 2. Phạm vi
- Có: chỉ dẫn usecase, prompt mẫu, pitfalls, tham chiếu tới tool/skill/repo ngoài + đánh giá sử dụng.
- Không: copy nguyên code/tool ngoài vào đây; lưu log, token, dữ liệu khách hàng.

### 3. Tổ chức (v10: thêm phân loại nguồn gốc item; giữ bộ 3 v9, tooling v8; v10.9: tiếng Việt có dấu bắt buộc)
- Tầng chung (mỏng): root `README.md`, `AGENTS.md`, `CHARTER.md`, `CHANGELOG.md`.
- Tầng `items/`: 1 item = 1 thư mục, kiến thức TRUNG LẬP domain của 1 công cụ/giải pháp. `items/<x>/README.md` chứa: là gì, ai làm, cài đặt mọi OS, cơ chế core, **cốt lõi bất biến / phần tùy chỉnh / phân công ai làm gì (bắt buộc từ v9)**, định vị vs đối thủ viral, giá/license, pitfalls chung, bản đồ phủ usecase (mạnh ★ / trung bình / không hỗ trợ + thay thế), tham khảo sử dụng (review sâu + số trung bình có trọng số), được dùng ở domain nào (link ngược).
- Tầng `domains/`: 1 domain = 1 thư mục lĩnh vực (`domains/ui/`, `domains/media/`...). Mỗi domain có `README.md` làm index chọn item theo usecase (cho phép NHIỀU item cùng phục vụ 1 usecase, mỗi cái 1 cách, kèm tiêu chí phân biệt) + 1 file `using-<item>.md` cho MỖI cặp item-domain (usecase trong domain này, lệnh mẫu cụ thể, lưu ý riêng, điểm mạnh cốt lõi của item CHO domain đó, link về đúng section item gốc).
- Tầng tooling (không phải kiến thức, không tính là tầng nội dung): `scripts/install.sh` + `scripts/uninstall.sh` + `scripts/aidomaincraft_setup.py`, `templates/agents-block.md` + `templates/claude-block.md` + `templates/VERSIONS`, `INSTALL.md` + `UNINSTALL.md`, `tests/test.sh`. Mặc định cài reference-only (chỉ chèn block vào `AGENTS.md`/`CLAUDE.md` của đích); `--vendor` mới copy snapshot vào `.aidomaincraft/` (git-ignored).
- Không tạo tầng kiến thức khác trừ khi bump CHARTER.

### 4. Quy ước đặt tên
- Thư mục items/domains viết thường, kebab-case, tiếng Anh.
- Tên item = tên giải pháp (`hallmark`, `reactbits`, `skillry`). Không đặt theo usecase lẻ.
- File domain-usage: `domains/<d>/using-<item>.md`.

### 4b. Nguồn gốc item (từ v10)
- `ngoại nhập`: mô tả tool/giải pháp có sẵn bên ngoài. Tài nguyên thật (code, skill, script) nằm ở repo ngoài; item chỉ chứa chỉ dẫn dùng (vd 11 item hiện tại).
- `nội tại`: tri thức do repo tự định nghĩa và sở hữu. Tài nguyên thật (scripts/templates/assets/data) sống trong `items/<x>/`, không chỉ README.
- Mọi item khai nguồn gốc ở `items/REGISTRY.md` (nguồn sự thật của phân loại). Item nội tại theo khung ánh xạ ở §5d.
- Quy tắc tài nguyên nội tại: tự sở hữu (cấm copy code ngoài vào, giữ luật §2) + verify được (chạy thử/`--help`/test) + gọn nhẹ (chỉ giữ lõi; tài nguyên lớn tách repo riêng).

### 5. Template item (bắt buộc)
`Dùng khi / Bỏ qua khi / Cài đặt / Cách item hoạt động (3 phần) / Cốt lõi bất biến / Phần tùy chỉnh / Phân công ai làm gì (3 mục bắt buộc từ v9) / Định vị khác biệt / Bản đồ phủ usecase (★ mạnh nhất lên đầu + trung bình + không hỗ trợ) / Các usecase con (mỗi usecase 1 block 6 field) / Các bước chung / Prompt mẫu / Pitfalls / Tham khảo sử dụng (review sâu + số trung bình có trọng số) / Tham khảo / Được dùng ở đâu (link domain) / Quay lại index`, song ngữ VI trước EN sau; tiếng Việt có dấu đầy đủ trong mọi nội dung đọc được (docs, CHANGELOG, prompt mẫu, PR, commit message) — chỉ code/lệnh/slug anchor/tên file giữ ASCII.
- Cấm động từ mơ hồ nếu không kèm lệnh + ngưỡng đo được.
- Mỗi usecase con: 1 lệnh copy-paste chạy được + 1 ví dụ input-output thật.
- Pitfalls gắn gate/lỗi cụ thể.
- Bản đồ phủ: quét HẾT catalog/tính năng, không chọn lọc. Usecase mạnh nhất gắn ★, đặt đầu, có prompt mẫu đầy đủ. Usecase yếu ghi 1 dòng + hướng thay thế.
- Tham khảo sử dụng (bắt buộc, xem VERIFY F6): trích review sâu quyết định được (nguồn + ngày + kết luận lật/xác nhận gì) + số trung bình có trọng số (điểm + số lượng reviews/installs + ngày đo). Review ẩn danh/không nguồn = loại. Mâu thuẫn review sâu vs số đông thì ghi cả hai + phán quyết.

### 5b. Cách item hoạt động (bắt buộc, có thẩm tra)
- 3 phần: `Tổ chức đứng sau` (ai làm, repo/registry chính, license, nhịp update, link + số liệu) / `Phương thức chung` (cơ chế cốt lõi) / `Khác biệt vận hành theo usecase` (mỗi usecase chạy khác gì).
- Mỗi khẳng định có nguồn (link file/dòng docs hoặc lệnh đã chạy). Cấm chép marketing.

### 5a. Định vị khác biệt (bắt buộc)
- So thẳng 1-2 hệ cùng phân khúc, viral, có số stars/installs. Bảng chỉ gồm tiêu chí quyết định (usecase, stack, giá/license, chất lượng, chi phí học-cài, bảo trì). Mỗi dòng kết bằng `Khi nào chọn nó / khi nào bỏ`. Cấm mô tả thưởng thức.

### 5c. Cốt lõi / tùy chỉnh / phân công (bắt buộc từ v9, chống dùng sai hệ)
- `Cốt lõi bất biến`: 2-4 gạch đầu dòng việc BẮT BUỘC tái dùng của hệ (artifact cụ thể: slug prompt, variant, gates...). Vi phạm = không còn gọi là dùng hệ (FAIL khai báo sai). Đạt: `awesome-list: luôn xuất phát từ 1 prompt có sẵn (lọc → chọn → copy nguyên văn), cấm viết mới hoàn toàn`. Không đạt: `dùng prompt cho video`.
- `Phần tùy chỉnh`: liệt kê tham số được đổi (subject/timing/style/route...) + cổng duyệt 2 tầng (hỏi user trước khi đổi; chọn artifact nào trong catalog cũng phải duyệt như đổi tham số — trình shortlist 2-3 ứng viên kèm lý do qua question tool, user pick mới làm). Waiver (đổi engine/model/thiếu điều kiện) phải quote câu ok tường minh của user, không suy diễn. Cấm đưa `must-not` vào danh sách tùy chỉnh.
- `Phân công ai làm gì`: agent chính làm [...] → giao nguyên cục cho claude bằng lệnh delegate nào → agent verify gì. Handoff format cố định: đầu vào + lệnh delegate + output mong đợi + cách verify. Bước thuộc claude mà agent tự làm = FAIL.
- Mỗi khẳng định link về section gốc của item (cơ chế/usecase/pitfalls).

### 5d. Khung item nội tại (từ v10, được trích nguồn ngoài khi so sánh)
- `Nguồn gốc` thay `Tổ chức đứng sau`: tác giả + commit khai sinh + lý do ra đời, link về chính repo này.
- `Áp dụng` thay `Cài đặt`: điều kiện + các bước chạy tài nguyên trong `items/<x>/` (không cài từ ngoài).
- Giữ nguyên: cốt lõi / tùy chỉnh / phân công / định vị / bản đồ phủ / usecase 6 field / bước chung / prompt mẫu / pitfalls / tham khảo (bằng chứng nội bộ: relay log, CHANGELOG, `test.sh` — được trích nguồn ngoài khi so sánh) / 3 chiều link / song ngữ.
- VERIFY B cho item nội tại ghi `N/A` cho stars/installs kèm lý do 1 dòng, không tính FAIL.

### 6. Template index domain (bắt buộc)
`Mục đích 1 dòng / Bảng điều hướng: Việc → item(s) (cho phép nhiều item chính, mỗi cái 1 cách + tiêu chí phân biệt) / Bảng định vị / Ma trận chồng lấn (ô = chính-hỗ trợ-thay thế-không dùng + 1 dòng tiêu chí) / Workflow phối hợp / Danh sách item`, song ngữ; tiếng Việt có dấu đầy đủ.
- Mỗi cặp item-domain PHẢI có `using-<item>.md`. Thiếu = thiếu sót (FAIL theo VERIFY D).
- Mỗi việc có thể có NHIỀU item chính (khác v6 chỉ 1 chính), nhưng bắt buộc cột tiêu chí phân biệt đo được.

### 6b. Template using-doc (bắt buộc, `domains/<d>/using-<x>.md`)
`Usecase trong domain này / Lệnh mẫu cụ thể / Lưu ý riêng cho domain / Điểm mạnh cốt lõi của item CHO domain này / Phân công CHO domain này (agent chính vs claude + link về mục Phân công gốc) / Link về item gốc (đúng section)`, song ngữ tóm tắt (EN có thể ngắn hơn, tối thiểu bảng + link); tiếng Việt có dấu đầy đủ.
- Chỉ viết phần RIÊNG cho domain. Mọi kiến thức gốc (cài đặt, cơ chế, giá) LINK về `../../items/<x>/README.md#section`, không copy. Trùng lặp nguyên đoạn = FAIL.

### 7. Nhất quán + link 3 chiều
- Một nguồn sự thật: lệnh, ngưỡng, steps chi tiết chỉ sống trong `items/<x>/README.md`; `domains/<d>/using-<x>.md` chỉ viết phần riêng + link; `domains/<d>/README.md` chỉ tóm 1 dòng + link.
- Link 3 chiều bắt buộc: domain index → using-doc → item gốc (tới đúng section, vd `../../items/skillry/README.md#co-ban`), và item gốc mục `Được dùng ở đâu` link ngược lại từng using-doc.
- Tên việc/lệnh khớp từng chữ giữa 3 tầng. Sửa 1 bên thì sửa các bên kia trong cùng commit + `CHANGELOG.md`.
- Checklist: không item mồ côi, không link gãy, không trùng lặp, song ngữ VI/EN đồng nội dung, tiếng Việt có dấu đầy đủ (kể cả commit message; chỉ code/lệnh/slug anchor/tên file giữ ASCII).

### 8. Phương pháp duy trì
- Sửa item: giữ template, ghi `CHANGELOG.md`.
- Thêm item mới: copy `templates/item-template.md`. Thêm domain mới: copy `templates/domain-index-template.md`. Thêm cặp item-domain: copy `templates/domain-using-template.md` + cập nhật index 2 đầu.
- Sửa block cài đặt: sửa `templates/agents-block.md` / `templates/claude-block.md`, chạy `python3 scripts/aidomaincraft_setup.py bump-blocks --to vN` (đồng bộ stamp + `templates/VERSIONS`), chạy `./tests/test.sh`, ghi `CHANGELOG.md`.
- Mọi thay đổi qua `VERIFY.md` vòng self-review lặp đến hết FAIL (mục E): 1 FAIL là không merge.
- Đổi cấu trúc: bump `CHARTER.md` lên vN+1 + ghi `CHANGELOG.md`.

---

## English

### 1. Purpose
Collect hands-on AI experience by field as usecase-first guides, reusable when starting new projects with AI agents.

### 2. Scope
- In: usecase guides, sample prompts, pitfalls, references to external tools/skills/repos + usage reviews.
- Out: vendored external code/tools; logs, tokens, customer data.

### 3. Organization (v10: item origin classification added; v9 triad kept, tooling stays v8; v10.9: Vietnamese accents required)
- Common layer (thin): root `README.md`, `AGENTS.md`, `CHARTER.md`, `CHANGELOG.md`.
- `items/` layer: 1 item = 1 folder, DOMAIN-NEUTRAL knowledge of one tool/solution. `items/<x>/README.md` holds: what it is, who builds it, install on every OS, core mechanism, **invariant core / customizable surface / work split (required since v9)**, differentiation vs viral opponents, price/license, shared pitfalls, usecase-coverage map (strong ★ / medium / unsupported + replacement), usage references (deep reviews + weighted averages), where-used backlinks.
- `domains/` layer: 1 domain = 1 field folder (`domains/ui/`, `domains/media/`...). Each domain has an index `README.md` (usecase → item(s), MULTIPLE items may serve one usecase in different ways with a distinguishing rule) + one `using-<item>.md` per item-domain pair (usecases in this domain, concrete commands, domain-specific notes, core strengths FOR this domain, links to the exact item sections).
- Tooling layer (not knowledge): `scripts/install.sh` + `scripts/uninstall.sh` + `scripts/aidomaincraft_setup.py`, `templates/agents-block.md` + `templates/claude-block.md` + `templates/VERSIONS`, `INSTALL.md` + `UNINSTALL.md`, `tests/test.sh`. Default install is reference-only (blocks in target `AGENTS.md`/`CLAUDE.md`); `--vendor` copies a git-ignored `.aidomaincraft/` snapshot.
- No other knowledge levels without a CHARTER bump.

### 4. Naming
- Lowercase kebab-case English for item/domain folders.
- Item name = solution name (`hallmark`, `reactbits`, `skillry`).
- Domain-usage file: `domains/<d>/using-<item>.md`.

### 4b. Item origin (since v10)
- `imported`: documents an existing external tool/solution. Real resources (code, skill, scripts) live in the outside repo; the item holds usage guidance only.
- `intrinsic`: knowledge defined and owned by this repo. Real resources (scripts/templates/assets/data) live inside `items/<x>/`, not just the README.
- Every item declares its origin in `items/REGISTRY.md` (source of truth for the classification). Intrinsic items follow the mapped frame in §5d.
- Intrinsic resource rules: self-owned (never copy outside code in, per §2) + verifiable (test run/`--help`/tests) + lightweight (core only; large resources get their own repo).

### 5. Item template (required)
`When to use / When to skip / Install / How it works (3 parts) / Invariant core / Customizable surface / Work split (3 blocks required since v9) / Differentiation / Coverage map (★ strongest first + medium + unsupported) / Sub-usecases (one 6-field block each) / Shared steps / Prompts / Pitfalls / Usage references (deep + weighted averages) / References / Where used (domain links) / Back to index`, bilingual VI first EN second; Vietnamese must be fully accented in all readable content (docs, CHANGELOG, sample prompts, PRs, commit messages) — only code/commands/slug anchors/file names stay ASCII.
- Vague verbs banned without runnable command + measurable bar.
- Each sub-usecase: 1 runnable command + 1 real input-output example.
- Pitfalls cite concrete gates/errors.
- Coverage map: scan the WHOLE catalog/features, no cherry-picking. Strongest usecase gets ★, goes first, full prompt example. Weak ones get 1 line + replacement.
- Usage references (required, see VERIFY F6): decisive deep reviews (source + date + what decision it flips/confirms) + weighted averages (score + review/install counts + measurement date). Anonymous/unsourced reviews excluded. Deep-vs-crowd conflicts record both + verdict.

### 5b. How the item works (required, verified)
- 3 parts: `Backing organization` / `Core method` / `Per-usecase differences`.
- Every claim sourced (doc file/line link or executed command). No marketing copy.

### 5a. Differentiation (required)
- Direct comparison vs 1-2 same-segment viral systems with stars/installs. Decision-only criteria. Each row ends `When to pick / drop`. No appreciation wording.

### 5c. Invariant core / customizable surface / work split (required since v9, prevents off-system use)
- `Invariant core`: 2-4 bullets of what MUST be reused (concrete artifact: prompt slug, variant, gates...). Violating = no longer using the system (false-claim FAIL). Good: `awesome-list: always start from one existing prompt (filter → pick → copy verbatim), never author from scratch`. Bad: `use prompts for video`.
- `Customizable surface`: tunable parameters (subject/timing/style/route...) + two-level approval gate (ask the user before changing; picking which catalog artifact also needs approval like a parameter change — present a 2-3 candidate shortlist with reasons via the question tool, proceed only after the user picks). Waivers (engine/model swap, missing precondition) must quote the user's explicit ok, never infer it. Never list `must-not` items here.
- `Work split`: main agent does [...] → hands the whole job to claude via which delegate command → agent verifies what. Fixed handoff format: inputs + delegate command + expected output + verify method. A claude-owned step done by the agent = FAIL.
- Every claim links to the item's origin sections (mechanism/usecases/pitfalls).

### 5d. Intrinsic item frame (since v10, external sources allowed when comparing)
- `Origin` replaces `Backing organization`: author + birth commit + why it exists, linking back to this repo.
- `Apply` replaces `Install`: prerequisites + steps to run the resources inside `items/<x>/` (nothing installed from outside).
- Unchanged: core / surface / split / positioning / coverage map / 6-field sub-usecases / shared steps / prompts / pitfalls / references (internal evidence: relay logs, CHANGELOG, `test.sh` — external sources allowed when comparing) / 3-way links / bilingual.
- VERIFY B lets intrinsic items record `N/A` for stars/installs with a 1-line reason, not a FAIL.

### 6. Domain index template (required)
`1-line purpose / Routing: job → item(s) (multiple primaries allowed, each with a distinguishing rule) / Positioning / Overlap matrix / Combined workflow / Item list`, bilingual; Vietnamese fully accented.
- Every item-domain pair MUST have `using-<item>.md`. Missing = FAIL per VERIFY D.
- One job may have MULTIPLE primaries (changed from v6 single-primary), but the distinguishing rule column is mandatory.

### 6b. Using-doc template (required, `domains/<d>/using-<x>.md`)
`Usecases in this domain / Concrete commands / Domain-specific notes / Core strengths FOR this domain / Work split FOR this domain (main agent vs claude + link to origin Work split) / Links to item origin (exact sections)`, bilingual summary (EN may be shorter, at minimum tables + links); Vietnamese fully accented.
- Domain-only content. All origin knowledge LINKS to `../../items/<x>/README.md#section`, never copied. Duplicated paragraphs = FAIL.

### 7. Consistency + 3-way links
- Single source of truth: commands, bars, detailed steps live only in `items/<x>/README.md`; `domains/<d>/using-<x>.md` holds domain-only deltas + links; `domains/<d>/README.md` holds 1-line summaries + links.
- Mandatory 3-way links: domain index → using-doc → item origin (exact section, e.g. `../../items/skillry/README.md#co-ban`), and the item's `Where used` section links back to each using-doc.
- Job/command names match word-for-word across all 3 layers. Change one side and the others in the same commit + `CHANGELOG.md`.
- Pre-done checklist: no orphans, no broken links, no duplication, VI/EN in sync, Vietnamese fully accented (including commit messages; only code/commands/slug anchors/file names stay ASCII).

### 8. Consistency method
- Edit item: keep template, add `CHANGELOG.md` entry.
- New item: copy `templates/item-template.md`. New domain: copy `templates/domain-index-template.md`. New item-domain pair: copy `templates/domain-using-template.md` + update both indexes.
- Edit install blocks: edit `templates/agents-block.md` / `templates/claude-block.md`, run `python3 scripts/aidomaincraft_setup.py bump-blocks --to vN` (syncs stamps + `templates/VERSIONS`), run `./tests/test.sh`, add a `CHANGELOG.md` entry.
- Every change passes `VERIFY.md` iterative self-review until zero FAIL (section E): 1 FAIL blocks merge.
- Structural change: bump `CHARTER.md` to vN+1 with a `CHANGELOG.md` entry.
