# Từ điển ràng buộc — wireframe-docs

> Mỗi key metadata trong tree là một ràng buộc có định nghĩa cố định.
> Quy tắc sắt: **khai gì hiện nấy** — mọi giá trị đã khai (states, effect,
> behavior, reduced, hide, visible-on, req, note) phải xuất hiện bằng chữ
> trong block wireframe tương ứng; `verify-pair.py` bắt thiếu = FAIL.

## Định nghĩa từng key

- `note:` ghi chú cho designer/agent (tùy chọn, trừ Avatar/Chart bắt buộc nhắc
  `alt`). Không do máy đối chiếu nội dung — chỉ dùng để đọc.
- `states:` các trạng thái component tồn tại. Interactive (theo mapping role)
  bắt buộc có `focus`. Mọi state phải xuất hiện trong block (chip/state list).
- `effect:` tên trong `animations.md`, HOẶC tên tự đặt + `ref:` URL.
  Không effect = không motion = không cần `reduced`.
- `reduced: instant|none` — cách thể hiện khi user bật giảm chuyển động.
  Bắt buộc khi có effect (trừ `focus-ring`). `instant` = hiện ngay trạng thái
  cuối, `none` = tắt hẳn hiệu ứng.
- `behavior:` hành vi đặc biệt (`dialog/drawer/sheet/popover/menu/menubar/
  tabs/accordion/pagination/carousel/toast/tooltip/dropdown/sticky`).
  Chỉ là tuyên bố — logic thật do wireframe 4 khung thể hiện + flow mô tả.
- `ref:` link nguồn của effect tự đặt (định dạng `http(s)://...`, check hình
  thức, không fetch). Thừa (effect đã có trong catalog) = FAIL.
- `hide: <khổ>` — ẩn cả block ở (các) khổ liệt kê. Block phải vắng mặt đúng
  khung đó; xuất hiện = lệch. Tên khổ phải hiện trong block (vd chip `ẩn: sm`).
- `visible-on: <state>` — chỉ hiện khi ở (các) state liệt kê (vd báo lỗi chỉ
  hiện khi `error`, toast chỉ hiện khi `show`). Block vẫn vẽ đủ 4 khung nhưng
  gắn nhãn điều kiện `chỉ hiện khi: <state>` + `data-wf-visible-on`.
  Khác `hide` (theo khổ màn hình), `visible-on` theo trạng thái.
- `req: REQ-xx` — liên kết tới yêu cầu trong `brief.md` của suite.
  Mã sai định dạng/không tồn tại = FAIL (`check.py` chỉ bắt định dạng;
  tồn tại do `check-suite.py` đối chiếu với brief). Component không cite req
  nào = WARN (có requirement chưa map).
- `span:`, `span-sm/md/lg/xl:`, `layout*` — bố cục lưới, số nguyên ≥1 /
  thuộc danh sách cho phép.
- `go:` *(chỉ trong flow, không phải tree)* — xem `flows.md`.

## Trường hợp dễ sót (checklist bắt buộc khi review suite)

1. Báo lỗi form ẩn-cho-đến-khi-lỗi: phải có `visible-on: error` + text lỗi
   lấy từ data, không hard-code 1 chuỗi chung cho mọi lỗi.
2. Toast notify: `behavior: toast` + `effect` + `reduced` + `note:` ghi trigger
   (sau action nào) và thời gian tự ẩn.
3. Loading/skeleton swap: skeleton (`Skeleton`) và nội dung thật không cùng
   hiện — flow phải có step chuyển (dùng `visible-on` hoặc 2 states).
4. Empty state: danh sách rỗng phải có block riêng, không để khung trắng.
5. Disabled có lý do: nút disabled phải có `note:` nêu điều kiện mở
   (vd "mở khi đã tick đồng ý").
6. Đếm ký tự / giới hạn nhập: `note:` ghi max + cách báo (WARN, không chặn).
7. OTP tự nhảy ô: `note:` ghi hành vi focus-next (InputOTP).
8. Confirm trước destructive: action xóa/hủy phải đi qua dialog confirm
   (flow bắt bằng WARN nếu thiếu).
9. Focus visible: interactive nào cũng cần state `focus` + wireframe thể hiện
   vòng focus (không chỉ đổi màu nhẹ).
10. Reduced-motion: mọi effect (trừ `focus-ring`) phải có `reduced`.
