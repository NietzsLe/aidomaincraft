# Catalog hiệu ứng chung — wireframe-docs

> Tên gọi chung cho animation lặp lại. Tree chỉ dùng tên trong catalog;
> kiểu đặc biệt ngoài catalog bắt buộc kèm `ref:` link nguồn (xem
> [Quy tắc custom](#quy-tac-custom--ref)). `check.py` khóa tên theo đúng
> khối máy đọc dưới đây — sửa catalog thì script tự nhận, không hardcode 2 nơi.

## Quy tắc spec

- Thuộc tính chỉ `transform` / `opacity` (compositor-friendly, theo chuẩn
  web-interface-guidelines). Ngoại lệ duy nhất: `focus-ring` dùng `outline`
  vì là chỉ báo focus bắt buộc, không phải motion trang trí.
- Easing trong tập đóng: `linear`, `ease-out`, `ease-in-out`.
- Duration dạng số + `ms`/`s`.
- `effect: focus-ring` được miễn `reduced:` (chỉ báo focus không phải motion;
  focus phải luôn hiển thị). Mọi effect còn lại bắt buộc `reduced: instant|none`.

## Khối máy đọc (check.py parse — cấm sửa tay sai định dạng)

```anim-catalog
fade: opacity 150ms ease-out on show
fade-scale: opacity+scale 200ms ease-out on open
slide-up: transform 200ms ease-out on open
slide-down: transform 200ms ease-out on open
slide-left: transform 200ms ease-out on open
slide-right: transform 200ms ease-out on open
hover-lift: transform 150ms ease-out on hover
collapse-expand: transform 200ms ease-out on expand
stagger-list: opacity 150ms ease-out on show
focus-ring: outline 150ms ease-out on focus
```

## Quy tắc custom + ref

- Effect ngoài catalog: `effect: <ten-tu-dat> | ref: <url>` — url phải
  `http(s)://...` (check hình thức, không fetch vì repo offline).
  Không kèm `ref:` = FAIL. Tên custom đặt lowercase-gạch-ngang.
- `ref:` kèm effect TRONG catalog = FAIL (thừa, gây nhiễu).
- Thăng cấp: 1 custom `ref:` được dùng ≥3 lần → đề xuất đưa vào catalog
  (ghi quyết định vào CHANGELOG).

## Ví dụ

- `- \`Dialog\` **Xác nhận xóa** — states: closed, open | effect: fade-scale | reduced: instant`
- `- \`Tooltip\` **Giá gồm VAT** — states: default | effect: custom-float | ref: https://easings.net#easeOutBack`
