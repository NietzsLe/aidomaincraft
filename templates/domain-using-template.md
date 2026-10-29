# templates/domain-using-template.md — mẫu điền using-doc (CHARTER v7)

> Copy file này thành `domains/<domain>/using-<item>.md`, điền `[...]`, xóa dòng `>` khi xong. Chỉ viết phần RIÊNG cho domain; mọi kiến thức gốc LINK về `items/<item>/README.md#section`, không copy nguyên đoạn. Trùng lặp = FAIL (VERIFY D).

## Tiếng Việt

### Usecase trong domain này
- [Liệt kê usecase của item KHI DÙNG CHO domain này. Mỗi usecase 1 dòng + link về block 6 field gốc, vd `Xem [Usecase con 1](../../items/<item>/README.md#usecase-con-1)`.]
- ★ [Usecase mạnh nhất CHO domain này — đặt đầu]: [...]

### Lệnh mẫu cụ thể (cho domain này)
- [Lệnh copy-paste chạy ngay trong bối cảnh domain, vd UI: giữ tokens Hallmark; media: export MP4/PPTX. Mỗi lệnh phải khớp lệnh trong item gốc từng chữ, kèm link về section gốc.]

### Lưu ý riêng cho domain
- [Bẫy chỉ gặp khi dùng item Ở domain này, vd UI: vỡ gates; media: narration cần tài khoản ngoài. Mỗi lưu ý link về pitfalls gốc nếu có.]

### Điểm mạnh cốt lõi của item CHO domain này
- [1-3 điểm mạnh riêng cho domain, kèm ngưỡng/ví dụ đo được. Cấm mô tả thưởng thức.]

### Link về item gốc (3 chiều — bắt buộc)
- Gốc: `../../items/<item>/README.md` (các section: [Cài đặt / Cách hoạt động / Định vị / ...]).
- Index domain: `./README.md` (dòng tương ứng trong bảng điều hướng + định vị).
- Được liệt kê ngược tại: `../../items/<item>/README.md#duoc-dung-o-dau`.

---

## English

### Usecases in this domain
- [List the item's usecases WHEN USED FOR this domain. One line each + link to the origin 6-field block, e.g. `See [Sub-usecase 1](../../items/<item>/README.md#sub-usecase-1)`.]
- ★ [Strongest usecase FOR this domain — first]: [...]

### Concrete commands (for this domain)
- [Copy-paste commands runnable in this domain's context. Must match the origin commands word-for-word, with links to origin sections.]

### Domain-specific notes
- [Pitfalls only met when using the item IN this domain, each linking to origin pitfalls where applicable.]

### Core strengths FOR this domain
- [1-3 domain-specific strengths with measurable bars/examples. No appreciation wording.]

### Links to item origin (3-way — required)
- Origin: `../../items/<item>/README.md` (sections: [Install / How it works / Positioning / ...]).
- Domain index: `./README.md` (matching rows in routing + positioning tables).
- Backlisted at: `../../items/<item>/README.md#where-used`.
