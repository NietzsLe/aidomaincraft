# Flow — wireframe-docs

> Flow là kịch bản người dùng đi qua các trang, soạn TAY trong `flows/`,
> play bằng `player.html` do `build-flow.py` sinh ra từ flow + wireframe thật.

## Vị trí

```
<suite>/
  flows/<ten-flow>.md     # nguồn soạn tay (1 file = 1 flow)
  player.html             # sinh ra bằng build-flow.py (không sửa tay)
  <page>/-tree.md|-data.json|-wireframe.html
```

## Khuôn flow.md (bắt buộc để `check-flow.py` đọc được)

```markdown
# Flow: <tên flow>
- Entry: <page> @ <sm|md|lg|xl>
- Pre: <điều kiện trước, tùy chọn>
- Req: REQ-01, REQ-02
- Terminal: success → <mô tả> | cancel → <mô tả>

## Step 1: <tên step>
- Page: <page> | Action: `Kiểu` <nhãn> | Expect: <kết quả thấy được>
- go: <đích>
- Input: <Nhãn field> = <key data>   # chỉ step điền form

## Step 2: <tên step rẽ nhánh>
- If: <điều kiện> → go: <đích>
- Else: <điều kiện khác> → go: <đích>
```

## DSL `go:` (đích đến sau action)

- `go: page:<slug>` — sang trang `<slug>` (thư mục `<slug>/` phải tồn tại).
- `go: dialog:<Nhãn>` / `go: drawer:<Nhãn>` — mở overlay có nhãn đó
  (component `behavior: dialog|drawer` phải tồn tại trong tree trang hiện tại).
- `go: back` — quay lại step trước (duyệt lịch sử, không cần target).
- Mỗi step thường có đúng 1 `go:` (trừ step terminal: không có `go:`).

## DSL `Input:` (step điền form)

- `Input: <Nhãn field> [= <key data>]`: field phải là component trong tree,
  key (mặc định = tên field) phải tồn tại trong data. Player gõ từng chữ
  giá trị vào ô lúc play.
- Thiếu field/key = FAIL. Flow có step `Input:` mà không có nhánh lỗi
  (không If/Else nào nhắc error/invalid) = WARN.

## Luật verify (`check-flow.py`)

- FAIL: target `go:` không tồn tại (page/dialog/drawer); step trỏ component
  không có trong tree; `Input:` thiếu field/key; flow không có `Entry`.
- WARN: trang mồ côi (không flow nào tới); step giữa không có `go:`/`If:`
  (dead-end); destructive (note chứa xóa/hủy) không qua dialog confirm;
  thiếu nhánh lỗi cho form; step không có `Expect`; go: toi page thiếu ghi
  chú deep-link; note tai/load nhung thieu state loading.

## Player

`build-flow.py <suite>/flows/<flow>.md` → nhúng steps + frame markup các
trang liên quan vào `player.html` (1 file, `file://`, JS thuần, không server).
Nhúng trực tiếp (không dùng iframe như viewer) vì play cần gõ chữ vào ô +
đọc DOM từng block — `file://` chặn cross-iframe, chỉ same-document mới làm
được. Chế độ xem: list flow (card + thumbnail live) / detail grid từng step /
play (prev-next-auto + chọn khổ + branch-choice + typing vào field +
nút lún + render kết quả) + panel ràng buộc ⓘ (định nghĩa từ
`constraints.md`). CSS của wireframe được build scope vào khung (`#stage`,
`#page-stage`, `.wf-frame`) nên không lem ra shell: selector `body`/`html`/`:root`
trong wireframe thành vô hiệu (shell giữ chrome trang), class chung như `.box`
cũng không chạm shell. Sửa flow thì build lại player, cấm sửa player tay.
