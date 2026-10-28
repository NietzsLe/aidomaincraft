# CHARTER.md — aidomaincraft — v6

## Tiếng Việt

### 1. Mục đích
Tổng hợp kinh nghiệm dùng AI theo lĩnh vực (trước mắt: UI), dưới dạng chỉ dẫn theo usecase để tái dùng khi tạo dự án mới và làm việc với AI agent.

### 2. Phạm vi
- Có: chỉ dẫn usecase, prompt mẫu, pitfalls, tham chiếu tới tool/skill/repo ngoài.
- Không: copy nguyên code/tool ngoài vào đây; lưu log, token, dữ liệu khách hàng.

### 3. Tổ chức
- Tầng chung (mỏng): root `README.md`, `AGENTS.md`, `CHARTER.md`, `CHANGELOG.md`.
- Tầng domain: thư mục ngang nhau theo lĩnh vực (`ui/`, sau này `hardware/`...). Mỗi domain có `README.md` làm index + bảng giải pháp → item.
- Tầng item: mỗi công cụ/giải pháp là 1 thư mục con trong domain (1 tool = 1 item), chứa `README.md` chi tiết. Các usecase con của tool đó nằm bên trong file dưới dạng bảng, không tách thành item riêng. Không tạo thêm tầng con trừ khi CHARTER nâng version.

### 4. Quy ước đặt tên
- Tên thư mục domain/item viết thường, kebab-case, tiếng Anh.
- Tên item = tên giải pháp, ví dụ `hallmark`, `relay-logs`. Không đặt theo usecase lẻ.
- Bảng usecase → lệnh dùng ghi bên trong `README.md` của item.

### 5. Template item (bắt buộc trong mỗi item README)
Mỗi usecase con là 1 block riêng với đủ 6 field: `Tên usecase / Khi dùng - điều kiện cụ thể / Khi bỏ qua / Lệnh copy-paste / Ngưỡng số cần đạt / Ví dụ input-output + pitfalls riêng`. Khung file: `Dùng khi / Bỏ qua khi / Cài đặt / Cách item hoạt động / Định vị khác biệt / Các usecase con (mỗi usecase 1 block 6 field) / Các bước chung / Prompt mẫu / Pitfalls / Tham khảo / Quay lại index`, song ngữ Việt trước Anh sau.
- Cấm động từ mơ hồ (`tối ưu`, `nâng cao`, `hiện đại hóa`) nếu không kèm lệnh chạy được + ngưỡng đo được.
- Mỗi usecase con phải có ít nhất 1 lệnh copy-paste chạy được + 1 ví dụ input-output thật.
- Pitfalls phải gắn lỗi/gate cụ thể (ví dụ Hallmark Floor 46a/54/70), cấm ghi chung chung kiểu `chú ý hiệu năng`.

### 5b. Cách item hoạt động (bắt buộc, có thẩm tra)
- Mỗi item phải có mục `Cách item hoạt động` với 3 phần: `Tổ chức đứng sau` (ai làm, repo/registry chính, license, nhịp update, kèm link + số liệu) / `Phương thức hoạt động chung` (cơ chế cốt lõi, ví dụ Hallmark = gates + scaffold + sweep; React Bits = copy source + variant; lib prompts UI = lấy video sẵn + áp style thay vì tự vẽ model/animation) / `Khác biệt vận hành theo usecase` (mỗi usecase con chạy khác gì: input nào, script/lệnh nào, output ra gì).
- Cấm 1 mô tả chung cho mọi usecase. Mỗi khẳng định vận hành phải có nguồn (link file/dòng docs hoặc lệnh đã chạy).
- Agent phải tự thẩm tra: mở repo/docs/registry + ít nhất 1 file nguồn (`SKILL.md`, `package.json`, script install, trang install/MCP) rồi mới ghi, không chép mô tả marketing.

### 5a. Định vị khác biệt trong item (bắt buộc)
- Mỗi item phải có mục `Định vị khác biệt`, so thẳng với 1-2 hệ cùng phân khúc, viral, nhiều người dùng (có số stars/installs làm bằng chứng). Ví dụ: skill chống AI-slop so với skill chống AI-slop viral khác; harness so với harness viral khác; bricks animated so với lib animated viral khác.
- Bảng so sánh chỉ gồm tiêu chí ảnh hưởng quyết định: usecase khớp, stack yêu cầu, giá/license, chất lượng output, chi phí học-cài, bảo trì. Mỗi dòng kết bằng `Khi nào chọn nó / khi nào bỏ`.
- Cấm mô tả thưởng thức (`cũng tốt`, `nổi tiếng`, `mạnh`). Mỗi điểm khác biệt phải kèm ngưỡng hoặc ví dụ khiến người đọc đổi lựa chọn, và nêu rõ `khi nào dùng sẽ phù hợp`.
- Hệ đem ra so sánh phải là hệ viral đã kiểm chứng (nêu tên + số liệu), không so với hệ vô danh.

### 6. Template index domain (bắt buộc trong mỗi domain README)
`Mục đích domain 1 dòng / Bảng điều hướng: Việc cần làm - Item chính - Item hỗ trợ - Lệnh bắt đầu / Bảng định vị: Item - Mục đích điển hình - Vận hành tóm tắt 1 câu - Điểm mạnh - Điểm yếu - Dùng chính khi - Tránh khi - Thay thế bởi - Vì sao chọn A thay vì B trong case này / Ma trận chồng lấn: hàng là việc, ô là chính-hỗ trợ-thay thế-không dùng kèm 1 dòng tiêu chí chọn phân biệt / Workflow phối hợp mẫu / Danh sách item`, song ngữ Việt trước Anh sau.
- Mỗi item phải xuất hiện ít nhất 1 lần trong index; mỗi việc chỉ 1 item chính.
- Mọi overlap phải ghi rõ, cấm 2 item cùng `chính` cho 1 việc mà không có tiêu chí phân biệt. Cột `Vì sao chọn A thay vì B` là bắt buộc, 1 câu gắn tiêu chí quyết định (stack/giá/output/a11y/perf), không ghi thưởng thức.

### 7. Nhất quán index ↔ item
- Một nguồn sự thật: lệnh, ngưỡng, steps chi tiết chỉ sống trong `item/README.md`; `domain/README.md` chỉ tóm 1 dòng + link, cấm copy nguyên đoạn.
- Link 2 chiều bắt buộc: index có link tới từng item; cuối mỗi item có `Quay lại index + Xem thêm item liên quan`.
- Tên việc/lệnh trong index phải khớp từng chữ với tiêu đề usecase trong item. Sửa 1 bên thì sửa bên kia trong cùng commit + ghi `CHANGELOG.md`.
- Checklist trước khi xong việc: không item mồ côi, không link gãy, bảng chồng lấn khớp bảng usecase con, song ngữ VI/EN cùng nội dung.

### 8. Phương pháp duy trì nhất quán
- Sửa nội dung item: giữ template, ghi `CHANGELOG.md`.
- Thêm domain/item: copy `templates/item-template.md`, cập nhật index của domain + root nếu cần.
- Thêm domain mới: copy `templates/domain-index-template.md`.
- Mọi thay đổi phải qua `VERIFY.md` với vòng self-review lặp đến khi hết FAIL (mục E): 1 FAIL là không merge, WARN phải ghi lý do giữ lại.
- Đổi cấu trúc (thêm tầng, đổi quy ước): phải bump `CHARTER.md` lên vN+1 và ghi `CHANGELOG.md`. Không tự ý đổi khung ở version hiện tại.

---

## English

### 1. Purpose
Collect hands-on AI experience by domain (first: UI) as usecase-first guides, reusable when starting new projects with AI agents.

### 2. Scope
- In: usecase guides, sample prompts, pitfalls, references to external tools/skills/repos.
- Out: vendored external code/tools; logs, tokens, customer data.

### 3. Organization
- Common layer (thin): root `README.md`, `AGENTS.md`, `CHARTER.md`, `CHANGELOG.md`.
- Domain layer: sibling folders by field (`ui/`, later `hardware/`...). Each domain has an index `README.md` with a solution → item table.
- Item layer: each tool/solution is one subfolder in a domain (1 tool = 1 item) with a detailed `README.md`. The tool's sub-usecases live inside that file as tables, never as separate items. No deeper nesting unless CHARTER is version-bumped.

### 4. Naming
- Lowercase kebab-case English folder names.
- Item name = solution name, e.g. `hallmark`, `relay-logs`. Never name after a single sub-usecase.
- The usecase → command table lives inside the item's `README.md`.

### 5. Item template (required)
Each sub-usecase is its own block with all 6 fields: `Usecase name / When to use - concrete condition / When to skip / Copy-paste command / Numeric bar to hit / Real input-output example + own pitfalls`. File frame: `When to use / When to skip / Install / How the item works / Differentiating positioning / Sub-usecases (one 6-field block each) / Shared steps / Sample prompts / Pitfalls / References / Back to index`, bilingual VI first EN second.
- Vague verbs (`optimize`, `modernize`, `enhance`) are banned unless paired with a runnable command + measurable bar.
- Each sub-usecase must have at least 1 runnable copy-paste command + 1 real input-output example.
- Pitfalls must cite a concrete gate/error (e.g. Hallmark Floor 46a/54/70), never generic `watch performance`.

### 5b. How the item works (required, verified)
- Each item must have a `How the item works` section with 3 parts: `Backing organization` (who builds it, canonical repo/registry, license, update cadence, with links + numbers) / `Core operating method` (core mechanism, e.g. Hallmark = gates + scaffold + sweep; React Bits = copy owned source + variant; UI prompt library = reuse existing video + apply style instead of drawing models/animations) / `Per-usecase operating differences` (how each sub-usecase runs differently: which input, which script/command, what output).
- One generic description for all usecases is banned. Every operating claim must carry a source (doc file/line link or an executed command).
- The agent must self-verify: open the repo/docs/registry + at least 1 source file (`SKILL.md`, `package.json`, install script, install/MCP page) before writing, never copy marketing copy.

### 5a. Differentiating positioning in item (required)
- Each item must have a `Differentiating positioning` section, compared directly against 1-2 same-segment, viral, widely-used systems (with stars/installs as evidence). Example: anti-AI-slop skill vs another viral anti-AI-slop skill; harness vs another viral harness; animated bricks vs another viral animated lib.
- The comparison table holds only decision-impacting criteria: matching usecase, required stack, price/license, output quality, learn-install cost, maintenance. Each row ends with `When to pick it / when to drop it`.
- Appreciation-only wording (`also good`, `popular`, `powerful`) is banned. Each difference must carry a threshold or example that flips the choice, and state clearly `when it fits`.
- Compared systems must be proven viral (name + numbers), never anonymous systems.

### 6. Domain index template (required in each domain README)
`1-line domain purpose / Routing table: Job - Primary item - Supporting item - Starter command / Positioning table: Item - Typical purposes - 1-sentence operating summary - Strengths - Weaknesses - Use as primary when - Avoid when - Replaced by - Why pick A over B in this case / Overlap matrix: rows are jobs, cells are primary-support-replaceable-do-not-use plus 1-line distinguishing selection rule / Sample combined workflow / Item list`, bilingual VI first EN second.
- Every item must appear at least once in the index; each job has exactly 1 primary item.
- Every overlap must be stated; never 2 primaries for 1 job without a distinguishing rule. The `Why pick A over B` column is required, 1 sentence tied to a decision criterion (stack/price/output/a11y/perf), no appreciation wording.

### 7. Index ↔ item consistency
- Single source of truth: commands, bars, detailed steps live only in `item/README.md`; `domain/README.md` holds a 1-line summary + link, never a full copy.
- Mandatory 2-way links: index links to every item; each item ends with `Back to index + Related items`.
- Job/command names in the index must match sub-usecase titles in items word-for-word. Change one side and the other in the same commit + `CHANGELOG.md` entry.
- Pre-done checklist: no orphan items, no broken links, overlap matrix matches sub-usecase blocks, VI/EN in sync.

### 8. Consistency method
- Edit item content: keep the template, add `CHANGELOG.md` entry.
- Add domain/item: copy `templates/item-template.md`, update domain index (+ root if needed).
- Add a new domain: copy `templates/domain-index-template.md`.
- Every change must pass `VERIFY.md` with an iterative self-review loop until zero FAIL (section E): 1 FAIL blocks merge, WARN must record why it stays.
- Change structure (new levels, new conventions): bump `CHARTER.md` to vN+1 with a `CHANGELOG.md` entry. No ad-hoc skeleton changes at the current version.
