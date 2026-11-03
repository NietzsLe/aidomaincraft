# Page: Checkout mẫu
> Trang thanh toán tối thiểu — 1 hành động chính là đặt hàng. Cây này chỉ định nghĩa phạm vi; wireframe thật nằm ở tree.html (soạn tay, 4 khổ sm/md/lg/xl, kiểm tra bằng verify-pair.py).

Ghi chú dài tự do (parser bỏ qua): cặp tree.md + tree.html này dùng để demo check + verify-pair, không phải thiết kế thật.

## Section: Thông tin — layout: stack | layout-md: grid-2 | layout-lg: grid-2 | layout-xl: grid-2
- `TextInput` **Email** — note: kiểm tra định dạng email | states: default, error | effect: focus-ring
- `TextInput` **Địa chỉ** — note: gợi ý địa chỉ tự động | states: default | span-md: 2 | span-lg: 2 | span-xl: 2

## Section: Hành động — layout: stack
- `Button` **Đặt hàng** — note: CTA duy nhất trang | states: default, hover, disabled | effect: hover-lift
- `Link` **Quay lại giỏ** — note: điều hướng, không phải hành động | states: default | hide: sm
