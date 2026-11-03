# templates/intrinsic-item-template.md — mẫu điền item NỘI TẠI (CHARTER v10 §5d)

> Copy file này thành `items/<solution>/README.md`, điền vào chỗ `[...]`, xóa dòng hướng dẫn `>` khi xong. Giữ song ngữ VI trước EN sau. Item nội tại: tri thức + tài nguyên do repo tự định nghĩa và sở hữu, sống trong `items/<x>/` (README + scripts/templates/assets/data). Được trích nguồn ngoài khi so sánh. Khai nguồn gốc ở `items/REGISTRY.md` trong cùng commit.

## Tiếng Việt

### Nguồn gốc
- Tác giả: [...] — Commit khai sinh: [...] — Lý do ra đời: [...]

### Dùng khi
- [Điều kiện cụ thể, không chung chung]

### Bỏ qua khi
- [Điều kiện cụ thể + trỏ việc thay thế]

### Áp dụng (thay Cài đặt — không cài từ ngoài)
- Điều kiện: [...]
- Lệnh copy-paste chạy tài nguyên trong `items/<x>/`: `[...]`
- Kiểm tra: [...] (output ...)

### Cách item hoạt động
- Cơ chế cốt lõi: [2-3 câu, cấm chung chung]
- Khác biệt vận hành theo usecase: [mỗi usecase con 1 dòng]

### Cốt lõi bất biến
- [2-4 gạch: việc BẮT BUỘC tái dùng + artifact cụ thể. Vi phạm = không còn gọi là dùng hệ.]

### Phần tùy chỉnh
- [Tham số được đổi + cổng duyệt 2 tầng (shortlist qua question tool, user pick mới làm). Cấm liệt kê `must-not`.]

### Phân công ai làm gì
- [Agent chính làm gì → giao cho claude bước nào + lệnh delegate → agent verify gì.]

### Định vị khác biệt
- So với [cách làm cũ trong repo hoặc hệ ngoài + số liệu]: [khác + ngưỡng + khi nào chọn/bỏ].

### Bản đồ phủ usecase (★ mạnh nhất đầu + trung bình + không hỗ trợ)
- ★ [...]: [...]
- KHÔNG hỗ trợ: [...] → dùng [...] thay.

### Hồ sơ quyết định
- Việc DÙNG (3+): [...] — Việc KHÔNG DÙNG (3+ kèm thay thế): [...]
- Giá: 0đ nội bộ (ghi phí ngoài nếu có: ...) — Ma sát: [... bước; đã chạy tới ...]
- TUYỆT ĐỐI không dùng khi: [...]

### Usecase con 1: [tên]
- Khi dùng / Khi bỏ qua / Lệnh copy-paste / Ngưỡng số / Ví dụ input-output (gắn nhãn minh họa) / Pitfalls riêng / Phân công usecase này

### Các bước chung
1. [...]

### Prompt mẫu
- "[...]"

### Pitfalls
- [Gắn gate/lỗi cụ thể]

### Tham khảo sử dụng (bằng chứng nội bộ)
- Relay log / CHANGELOG / `test.sh`: [nguồn nội bộ + ngày + kết luận]
- Nguồn ngoài (nếu có, khi so sánh): [URL + ngày]

### Tài nguyên trong item
- [Liệt kê thư mục con: scripts/ (chạy được), templates/, assets/, data/ — khớp cột `tài nguyên` trong `items/REGISTRY.md`]

### Tham khảo
- [Link nội bộ (file/section) + nguồn ngoài đã mở (nếu có)]

### Được dùng ở đâu (link ngược 3 chiều — bắt buộc)
- Dùng cho `domains/<d>/`: xem `../../domains/<d>/using-<item>.md`.

### Quay lại index
- Về `../../domains/<d>/README.md` [...]

---

## English

> Same frame in English: Origin (author + birth commit + why) / When to use / When to skip / Apply (prerequisites + commands running in-repo resources) / How it works / Invariant core / Customizable surface / Work split / Differentiating positioning / Coverage map / Decision dossier / Sub-usecases (6 fields each) / Shared steps / Sample prompts / Pitfalls / Usage references (internal evidence: relay logs, CHANGELOG, `test.sh`; external sources when comparing) / In-item resources (match the `tài nguyên` column in `items/REGISTRY.md`) / References / Where used / Back to index. Bilingual VI first EN second.
