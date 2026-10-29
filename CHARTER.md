# CHARTER.md — aidomaincraft — v7

## Tiếng Việt

### 1. Mục đích
Tổng hợp kinh nghiệm dùng AI theo lĩnh vực, dưới dạng chỉ dẫn theo usecase để tái dùng khi tạo dự án mới và làm việc với AI agent.

### 2. Phạm vi
- Có: chỉ dẫn usecase, prompt mẫu, pitfalls, tham chiếu tới tool/skill/repo ngoài + đánh giá sử dụng.
- Không: copy nguyên code/tool ngoài vào đây; lưu log, token, dữ liệu khách hàng.

### 3. Tổ chức (v7: tách kho item khỏi hướng dẫn domain)
- Tầng chung (mỏng): root `README.md`, `AGENTS.md`, `CHARTER.md`, `CHANGELOG.md`.
- Tầng `items/`: 1 item = 1 thư mục, kiến thức TRUNG LẬP domain của 1 công cụ/giải pháp. `items/<x>/README.md` chứa: là gì, ai làm, cài đặt mọi OS, cơ chế core, định vị vs đối thủ viral, giá/license, pitfalls chung, bản đồ phủ usecase (mạnh ★ / trung bình / không hỗ trợ + thay thế), tham khảo sử dụng (review sâu + số trung bình có trọng số), được dùng ở domain nào (link ngược).
- Tầng `domains/`: 1 domain = 1 thư mục lĩnh vực (`domains/ui/`, `domains/media/`...). Mỗi domain có `README.md` làm index chọn item theo usecase (cho phép NHIỀU item cùng phục vụ 1 usecase, mỗi cái 1 cách, kèm tiêu chí phân biệt) + 1 file `using-<item>.md` cho MỖI cặp item-domain (usecase trong domain này, lệnh mẫu cụ thể, lưu ý riêng, điểm mạnh cốt lõi của item CHO domain đó, link về đúng section item gốc).
- Không tạo tầng khác trừ khi bump CHARTER.

### 4. Quy ước đặt tên
- Thư mục items/domains viết thường, kebab-case, tiếng Anh.
- Tên item = tên giải pháp (`hallmark`, `reactbits`, `skillry`). Không đặt theo usecase lẻ.
- File domain-usage: `domains/<d>/using-<item>.md`.

### 5. Template item (bắt buộc)
`Dùng khi / Bỏ qua khi / Cài đặt / Cách item hoạt động (3 phần) / Định vị khác biệt / Bản đồ phủ usecase (★ mạnh nhất lên đầu + trung bình + không hỗ trợ) / Các usecase con (mỗi usecase 1 block 6 field) / Các bước chung / Prompt mẫu / Pitfalls / Tham khảo sử dụng (review sâu + số trung bình có trọng số) / Tham khảo / Được dùng ở đâu (link domain) / Quay lại index`, song ngữ VI trước EN sau.
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

### 6. Template index domain (bắt buộc)
`Mục đích 1 dòng / Bảng điều hướng: Việc → item(s) (cho phép nhiều item chính, mỗi cái 1 cách + tiêu chí phân biệt) / Bảng định vị / Ma trận chồng lấn (ô = chính-hỗ trợ-thay thế-không dùng + 1 dòng tiêu chí) / Workflow phối hợp / Danh sách item`, song ngữ.
- Mỗi cặp item-domain PHẢI có `using-<item>.md`. Thiếu = thiếu sót (FAIL theo VERIFY D).
- Mỗi việc có thể có NHIỀU item chính (khác v6 chỉ 1 chính), nhưng bắt buộc cột tiêu chí phân biệt đo được.

### 6b. Template using-doc (bắt buộc, `domains/<d>/using-<x>.md`)
`Usecase trong domain này / Lệnh mẫu cụ thể / Lưu ý riêng cho domain / Điểm mạnh cốt lõi của item CHO domain này / Link về item gốc (đúng section)`, song ngữ tóm tắt (EN có thể ngắn hơn, tối thiểu bảng + link).
- Chỉ viết phần RIÊNG cho domain. Mọi kiến thức gốc (cài đặt, cơ chế, giá) LINK về `../../items/<x>/README.md#section`, không copy. Trùng lặp nguyên đoạn = FAIL.

### 7. Nhất quán + link 3 chiều
- Một nguồn sự thật: lệnh, ngưỡng, steps chi tiết chỉ sống trong `items/<x>/README.md`; `domains/<d>/using-<x>.md` chỉ viết phần riêng + link; `domains/<d>/README.md` chỉ tóm 1 dòng + link.
- Link 3 chiều bắt buộc: domain index → using-doc → item gốc (tới đúng section, vd `../../items/skillry/README.md#co-ban`), và item gốc mục `Được dùng ở đâu` link ngược lại từng using-doc.
- Tên việc/lệnh khớp từng chữ giữa 3 tầng. Sửa 1 bên thì sửa các bên kia trong cùng commit + `CHANGELOG.md`.
- Checklist: không item mồ côi, không link gãy, không trùng lặp, song ngữ VI/EN đồng nội dung.

### 8. Phương pháp duy trì
- Sửa item: giữ template, ghi `CHANGELOG.md`.
- Thêm item mới: copy `templates/item-template.md`. Thêm domain mới: copy `templates/domain-index-template.md`. Thêm cặp item-domain: copy `templates/domain-using-template.md` + cập nhật index 2 đầu.
- Mọi thay đổi qua `VERIFY.md` vòng self-review lặp đến hết FAIL (mục E): 1 FAIL là không merge.
- Đổi cấu trúc: bump `CHARTER.md` lên vN+1 + ghi `CHANGELOG.md`.

---

## English

### 1. Purpose
Collect hands-on AI experience by field as usecase-first guides, reusable when starting new projects with AI agents.

### 2. Scope
- In: usecase guides, sample prompts, pitfalls, references to external tools/skills/repos + usage reviews.
- Out: vendored external code/tools; logs, tokens, customer data.

### 3. Organization (v7: split item store from domain guides)
- Common layer (thin): root `README.md`, `AGENTS.md`, `CHARTER.md`, `CHANGELOG.md`.
- `items/` layer: 1 item = 1 folder, DOMAIN-NEUTRAL knowledge of one tool/solution. `items/<x>/README.md` holds: what it is, who builds it, install on every OS, core mechanism, differentiation vs viral opponents, price/license, shared pitfalls, usecase-coverage map (strong ★ / medium / unsupported + replacement), usage references (deep reviews + weighted averages), where-used backlinks.
- `domains/` layer: 1 domain = 1 field folder (`domains/ui/`, `domains/media/`...). Each domain has an index `README.md` (usecase → item(s), MULTIPLE items may serve one usecase in different ways with a distinguishing rule) + one `using-<item>.md` per item-domain pair (usecases in this domain, concrete commands, domain-specific notes, core strengths FOR this domain, links to the exact item sections).
- No other levels without a CHARTER bump.

### 4. Naming
- Lowercase kebab-case English for item/domain folders.
- Item name = solution name (`hallmark`, `reactbits`, `skillry`).
- Domain-usage file: `domains/<d>/using-<item>.md`.

### 5. Item template (required)
`When to use / When to skip / Install / How it works (3 parts) / Differentiation / Coverage map (★ strongest first + medium + unsupported) / Sub-usecases (one 6-field block each) / Shared steps / Prompts / Pitfalls / Usage references (deep + weighted averages) / References / Where used (domain links) / Back to index`, bilingual VI first EN second.
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

### 6. Domain index template (required)
`1-line purpose / Routing: job → item(s) (multiple primaries allowed, each with a distinguishing rule) / Positioning / Overlap matrix / Combined workflow / Item list`, bilingual.
- Every item-domain pair MUST have `using-<item>.md`. Missing = FAIL per VERIFY D.
- One job may have MULTIPLE primaries (changed from v6 single-primary), but the distinguishing rule column is mandatory.

### 6b. Using-doc template (required, `domains/<d>/using-<x>.md`)
`Usecases in this domain / Concrete commands / Domain-specific notes / Core strengths FOR this domain / Links to item origin (exact sections)`, bilingual summary (EN may be shorter, at minimum tables + links).
- Domain-only content. All origin knowledge LINKS to `../../items/<x>/README.md#section`, never copied. Duplicated paragraphs = FAIL.

### 7. Consistency + 3-way links
- Single source of truth: commands, bars, detailed steps live only in `items/<x>/README.md`; `domains/<d>/using-<x>.md` holds domain-only deltas + links; `domains/<d>/README.md` holds 1-line summaries + links.
- Mandatory 3-way links: domain index → using-doc → item origin (exact section, e.g. `../../items/skillry/README.md#co-ban`), and the item's `Where used` section links back to each using-doc.
- Job/command names match word-for-word across all 3 layers. Change one side and the others in the same commit + `CHANGELOG.md`.
- Pre-done checklist: no orphans, no broken links, no duplication, VI/EN in sync.

### 8. Consistency method
- Edit item: keep template, add `CHANGELOG.md` entry.
- New item: copy `templates/item-template.md`. New domain: copy `templates/domain-index-template.md`. New item-domain pair: copy `templates/domain-using-template.md` + update both indexes.
- Every change passes `VERIFY.md` iterative self-review until zero FAIL (section E): 1 FAIL blocks merge.
- Structural change: bump `CHARTER.md` to vN+1 with a `CHANGELOG.md` entry.
