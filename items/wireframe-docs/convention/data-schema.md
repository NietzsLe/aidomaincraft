# Schema data mẫu — wireframe-docs

> 1 bản wireframe = 3 file cùng thư mục `<suite>/<slug>/`:
> `<slug>-tree.md` (phạm vi) + `<slug>-data.json` (nội dung mẫu) +
> `<slug>-wireframe.html` (thể hiện tay đúng cả 3).

## Định dạng `<slug>-data.json`

```json
{
  "page": "<tên page, khớp # Page: của tree>",
  "values": {
    "<nhãn component>": "<giá trị mẫu hiển thị>",
    "<nhãn khác>": ["<giá trị 1>", "<giá trị 2>"]
  }
}
```

## Quy tắc (verify-pair.py bắt cả 3 chân)

1. File phải tồn tại cạnh tree (`<slug>-tree.md` đi với `<slug>-data.json`; ngoại lệ duy nhất: `examples/tree.md` đi với `examples/data.json` vì tên mẫu không có slug), JSON hợp lệ,
   có `page` khớp tree + `values` là object không rỗng.
2. Mọi nhãn component trong tree phải có key trong `values` (thiếu = FAIL);
   mọi key phải ứng với 1 nhãn trong tree (thừa = FAIL).
3. Mọi giá trị (chuỗi, hoặc từng phần tử mảng) phải xuất hiện nguyên văn
   (sau chuẩn hóa khoảng trắng) trong text của đúng block component đó
   trong HTML (thiếu = FAIL — wireframe không render data thật).

## Ví dụ (`checkout-data.json`)

```json
{
  "page": "Checkout mẫu",
  "values": {
    "Email": "ban@example.com",
    "Địa chỉ": "123 Nguyễn Huệ, Q.1",
    "Đặt hàng": "Đặt hàng",
    "Quay lại giỏ": "Quay lại giỏ hàng"
  }
}
```
