# Quy ước tree.md — component tree dạng README (markdown) cho wireframe-docs

> File tree.md mô tả cấu trúc UI bằng markdown thuần: designer đọc trực tiếp, agent parse, `scripts/build.py` render ra HTML wireframe. Chuẩn này là nguồn sự thật của cú pháp; `scripts/check.py` validate theo đúng chuẩn này.

## Cú pháp (3 loại dòng, còn lại bỏ qua)

```markdown
# Page: <tên trang>
> <ghi chú trang — 1 dòng, tùy chọn>

## Section: <tên section>
- `<KiểuComponent>` **<nhãn hiển thị>** — note: <ghi chú> | states: <state1, state2>
```

## Quy tắc

1. File phải có đúng 1 dòng `# Page:`, sau đó ≥1 `## Section:`, mỗi section ≥1 dòng component `-`.
2. Dòng component: bắt đầu bằng `- `, kiểu trong backtick (\`...\`), nhãn trong bold (`**...**`).
3. Phần sau `—` (gạch dài) là metadata tùy chọn, gồm các cặp `key: value` cách nhau bằng `|`:
   - `note:` ghi chú cho designer/agent (tùy chọn).
   - `states:` danh sách state cách nhau bằng dấu phẩy, vd `default, hover, disabled` (tùy chọn; mặc định `default`).
4. Mọi dòng khác (trống, `#` heading khác, text thường) bị bỏ qua khi parse — dùng tự do để ghi chú dài.
5. Kiểu component viết PascalCase (`Button`, `TextInput`, `Card`, `Navbar`...), không giới hạn danh mục — `check.py` chỉ kiểm tra cú pháp, không kiểm tra kiểu có tồn tại.

## Ví dụ tối thiểu

```markdown
# Page: Checkout
> Trang thanh toán, 1 action chính là đặt hàng.

## Section: Form
- `TextInput` **Email** — note: validate định dạng | states: default, error
- `Button` **Đặt hàng** — note: CTA duy nhất trang | states: default, hover, disabled
```
