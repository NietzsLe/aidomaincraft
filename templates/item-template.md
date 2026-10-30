# templates/item-template.md — mẫu điền item (CHARTER v8, khung item giữ nguyên v7)

> Copy file này thành `items/<solution>/README.md`, điền vào chỗ `[...]`, xóa dòng hướng dẫn `>` khi xong. Giữ song ngữ VI trước EN sau. Chi tiết gốc sống ở đây; domain chỉ link về, không copy.

## Tiếng Việt

### Dùng khi
- [Điều kiện cụ thể, không chung chung]

### Bỏ qua khi
- [Điều kiện cụ thể + trỏ việc thay thế]

### Cài đặt
- [Lệnh copy-paste đã kiểm tra từ docs/source. Ghi nguồn đã mở: ...]
- Yêu cầu: [...]
- Kiểm tra: [...]

### Cách item hoạt động
- Tổ chức đứng sau: [ai làm | repo/registry link | license | nhịp update | số liệu stars/installs]
- Phương thức hoạt động chung: [cơ chế cốt lõi 2-3 câu. Đạt: `Hallmark chạy gates + scaffold + sweep qua sloplint --render`. Không đạt: `công cụ AI mạnh`.]
- Khác biệt vận hành theo usecase: [mỗi usecase con 1 dòng: input nào → script/lệnh nào → output gì]

### Định vị khác biệt
- So với [tên hệ viral cùng phân khúc + số liệu]: [khác gì + ngưỡng/ví dụ + khi nào chọn nó / khi nào bỏ].
- So với [tên hệ viral thứ 2 + số liệu]: [tương tự].
- Đạt: `Chọn Hallmark thay vì v0 khi phải pass gates contrast 4.5:1/fold 1280x800`. Không đạt: `Hallmark cũng tốt, nổi tiếng`.

### Bản đồ phủ usecase (bắt buộc — quét HẾT catalog, cấm chọn lọc)
- ★ [Usecase mạnh nhất — đặt đầu, có prompt mẫu đầy đủ ở dưới]: [...]
- [Usecase trung bình]: [...] → dùng khi [...]
- KHÔNG hỗ trợ: [...] → dùng [...] thay.
- Đạt: mọi tính năng trong catalog đều xuất hiện ở 1 trong 3 nhóm trên. Không đạt: liệt kê 2-3 usecase dễ mà bỏ phần khó.

### Hồ sơ quyết định (bắt buộc — trả lời đủ, cấm chung chung)
- Việc DÙNG (3+, cụ thể): 1. [...] 2. [...] 3. [...]
- Việc KHÔNG DÙNG (3+, mỗi việc kèm hệ thay thế): 1. [...] → dùng [...] thay. 2. [...] 3. [...]
- Free / tổng + giá: [... free / ... tổng, giá ...]. Nguồn số + ngày đo: [...]
- Ma sát cài đặt: [... bước từ 0 đến lệnh đầu chạy được; đã chạy thử đến bước ..., output ...]. Rào cản: [auth/login/Node/tiền/quyền ...].
- Đối thủ viral cùng phân khúc: [tên + stars/installs] vs [tên + stars/installs].
- Chọn nó thay vì đối thủ khi: [tiêu chí đo được, ví dụ đổi lựa chọn].
- TUYỆT ĐỐI không dùng khi: [...]

### Usecase con 1: [tên khớp từng chữ với index + using-doc]
- Khi dùng: [...]
- Khi bỏ qua: [...]
- Lệnh copy-paste: `[...]`
- Ngưỡng số cần đạt: [...]
- Ví dụ input-output: [input thật] → [output thật]
- Pitfalls riêng: [gắn gate/lỗi cụ thể]

### Các bước chung
1. [...]

### Prompt mẫu
- "[...]"

### Pitfalls
- [Gắn gate/lỗi cụ thể]

### Tham khảo sử dụng (bắt buộc từ v7 — review sâu + số trung bình có trọng số)
- Nhận xét sâu: [nguồn URL + ngày] "trích 1-2 câu đắt nhất" → lật/xác nhận quyết định [gì].
- Số trung bình: [điểm + số lượng reviews/installs + ngày đo, vd 4.7/5 (121 ratings, 29/10/2026)]. Trọng số: [vì sao số này đáng tin hơn số kia].
- Mâu thuẫn (nếu có): [review sâu nói X, số đông nói Y] → phán quyết: [...].
- Không tìm được thì ghi `chưa xác minh`, cấm bịa. Review ẩn danh/không nguồn = loại.

### Tham khảo
- [link repo/docs/source đã mở kiểm tra]

### Được dùng ở đâu (link ngược 3 chiều — bắt buộc)
- Dùng cho `domains/ui/`: xem `../../domains/ui/using-<item>.md` (usecase UI).
- Dùng cho `domains/media/`: xem `../../domains/media/using-<item>.md` (usecase media).
- [Thêm domain khác nếu có.]

### Quay lại index
- Về `../../domains/ui/README.md` [...]
- Xem thêm item liên quan: `../<item>/` [...]

---

## English

### When to use
- [...]

### When to skip
- [...]

### Install
- [Checked copy-paste command. Sources opened: ...]

### How the item works
- Backing organization: [...]
- Core operating method: [Good: `...`. Bad: `powerful AI tool`.]
- Per-usecase operating differences: [...]

### Differentiating positioning
- Vs [viral same-segment name + numbers]: [difference + threshold/example + when to pick/drop].
- Good: `Pick X over Y when ... 4.5:1 ...`. Bad: `X is also good and popular`.

### Coverage map (required — scan the WHOLE catalog, no cherry-picking)
- ★ [Strongest usecase — first, full prompt example below]: [...]
- [Medium usecase]: [...] → use when [...]
- NOT supported: [...] → use [...] instead.

### Decision dossier (required — answer fully, no generic wording)
- Jobs SERVED (3+, concrete): 1. [...] 2. [...] 3. [...]
- Jobs NOT served (3+, each with its replacement): 1. [...] → use [...] instead. 2. [...] 3. [...]
- Free / total + price: [... free / ... total, price ...]. Number sources + date: [...]
- Install friction: [... steps from zero to first runnable command; ran up to step ..., output ...]. Barriers: [...]
- Viral same-segment opponents: [name + stars/installs] vs [name + stars/installs].
- Pick it over opponents when: [measurable criterion, choice-flipping example].
- NEVER use when: [...]

### Sub-usecase 1: [title word-for-word matching the index + using-doc]
- When to use: [...]
- When to skip: [...]
- Copy-paste command: `[...]`
- Numeric bar: [...]
- Input-output example: [...] → [...]
- Own pitfalls: [concrete gate/error]

### Shared steps
1. [...]

### Sample prompts
- "[...]"

### Pitfalls
- [concrete gate/error]

### Usage references (required since v7 — deep + weighted averages)
- Deep review: [source URL + date] "1-2 best quotes" → flips/confirms [which decision].
- Weighted average: [score + review/install counts + date, e.g. 4.7/5 (121 ratings, 29/10/2026)]. Weight: [why this number is more trustworthy].
- Conflict (if any): [deep says X, crowd says Y] → verdict: [...].
- Missing → write `unverified`, never guess. Anonymous/unsourced = excluded.

### References
- [checked repo/docs/source links]

### Where used (3-way backlinks — required)
- Used in `domains/ui/`: see `../../domains/ui/using-<item>.md` (UI usecases).
- Used in `domains/media/`: see `../../domains/media/using-<item>.md` (media usecases).

### Back to index
- Back to `../../domains/ui/README.md` [...]
- Related item: `../<item>/` [...]
