# Quy ước tree.md + wireframe.html — wireframe-docs (từ v10.4)

> Tree (`tree.md`) chỉ định nghĩa phạm vi cấu trúc để làm rõ, không sinh ra wireframe.
> Wireframe (`wireframe.html`) do người/agent soạn tay theo tree, thể hiện giao diện thật
> (layout, độ lớn, vị trí tương đối, loại component, states, effect) trên 4 khổ màn hình
> trong 1 file. Cặp đôi tree ↔ wireframe phải khớp nhau, kiểm tra bằng
> `scripts/verify-pair.py`; lệch thì báo cho designer quyết, cấm tự sửa ngầm.

## Vai trò 2 artifact (bắt buộc)

1. `*-tree.md`: định nghĩa page → section → component kèm note/states/effect và quy tắc
   responsive. `scripts/check.py` PASS nghĩa là cấu trúc đã rõ, không nghĩa là đã có wireframe.
2. `*-wireframe.html`: soạn tay (HTML/CSS self-contained, không mạng, không build ngoài),
   1 file chứa đúng 4 khung khổ màn hình, mỗi khung vẽ lại toàn bộ trang ở khổ đó.
3. Tên cặp đôi trong `.tmp/wireframes/`: `<slug>-tree.md` đi với `<slug>-wireframe.html`
   (ví dụ `pricing-tree.md` + `pricing-wireframe.html`). Trình review luôn trình cả cặp
   + dòng PASS của `check.py` + dòng PASS của `verify-pair.py`.

## Bốn khổ màn hình khóa cứng

| Mã | Khổ | Rộng tham chiếu |
|---|---|---|
| `sm` | mobile | 360 |
| `md` | tablet | 768 |
| `lg` | desktop thường (laptop) | 1366 |
| `xl` | desktop lớn (PC để bàn) | 1920 |

Không tự đặt mã khổ khác. Mỗi khung trong wireframe gắn `data-wf-breakpoint`
và `data-wf-width` đúng số trên.

## Cú pháp tree (3 loại dòng, còn lại bỏ qua)

```markdown
# Page: <tên trang>
> <ghi chú trang — 1 dòng, tùy chọn>

## Section: <tên section> — layout: <base> | layout-md: <ghi đè> | hide: <khổ...>
- `<KiểuComponent>` **<nhãn hiển thị>** — note: <ghi chú> | states: <state, state> | effect: <effect, effect> | span-md: <số> | hide: <khổ...> 
```

## Quy tắc tree

1. File phải có đúng 1 dòng `# Page:`, sau đó ≥1 `## Section:`, mỗi section ≥1 dòng component `-`.
2. Dòng section: tên sau `## Section:`, phần sau `—` là metadata tùy chọn gồm các cặp
   `key: value` cách nhau bằng `|`:
   - `layout:` base mobile-first cho `sm` (mặc định `stack` khi vắng mặt).
   - `layout-sm/md/lg/xl:` ghi đè layout từ khổ đó trở lên (kế thừa dần lên).
   - `hide:` liệt kê khổ ẩn cả section, cách nhau bằng dấu phẩy (ví dụ `hide: sm`).
   - Kiểu layout cho phép: `stack`, `grid-2`, `grid-3`, `grid-4`, `sidebar-left`, `sidebar-right`.
3. Dòng component: bắt đầu bằng `- `, kiểu trong backtick (`...`), nhãn trong bold (`**...**`).
   Phần sau `—` gồm các cặp `key: value` cách nhau bằng `|`:
   - `note:` ghi chú cho designer/agent (tùy chọn).
   - `states:` danh sách state cách nhau bằng dấu phẩy (mặc định `default`).
   - `effect:` danh sách effect cách nhau bằng dấu phẩy (vắng mặt = không effect).
   - `span:` / `span-sm/md/lg/xl:` số cột chiếm trong lưới (số nguyên ≥1, mặc định 1;
     hậu tố khổ ghi đè dần lên như layout; chỉ có nghĩa trong section dạng lưới).
   - `hide:` liệt kê khổ ẩn component (ví dụ `hide: sm` = có mặt ở md/lg/xl, vắng ở sm).
4. Khóa metadata lạ (sai chính tả, ngoài danh sách trên) là FAIL — `check.py` báo đúng
   dòng để sửa, cấm im lặng bỏ qua vì sẽ gây lệch với wireframe.
5. Giá trị `hide` chỉ gồm `sm`, `md`, `lg`, `xl`; `span*` phải là số nguyên ≥1;
   `layout*` phải thuộc danh sách cho phép — sai đều FAIL.
6. Mọi dòng khác (trống, heading `#` khác, text thường) bị bỏ qua khi parse — dùng tự do
   cho ghi chú dài, nhưng thông tin quan trọng (CTA, states, effect, ẩn/hiện) phải nằm
   trong metadata đúng khóa, cấm để trong dòng tự do.
7. Kiểu component viết PascalCase (`Button`, `TextInput`, `Card`, ...) — `check.py` chỉ
   kiểm tra cú pháp, không giới hạn danh mục.

## Chuẩn wireframe.html soạn tay (bắt buộc để `verify-pair.py` đọc được)

1. Một file, đúng 4 khung, mỗi khung là 1 block gắn `data-wf-breakpoint="<sm|md|lg|xl>"`
   + `data-wf-width="<360|768|1366|1920>"` khớp bảng khổ.
2. Khung gốc (hoặc toàn file) gắn `data-wf-page="<tên page>"` khớp `# Page:` của tree.
3. Trong mỗi khung, mỗi section là 1 block gắn `data-wf-section="<tên section>"` +
   `data-wf-layout="<layout hiệu lực ở khổ đó>"` (layout sau khi áp ghi đè dần lên).
4. Trong mỗi section-khung, mỗi component là 1 block gắn
   `data-wf-component="<nhãn>"` + `data-wf-states="<states cách nhau dấu phẩy>"`
   (khớp tập states của tree, không phân biệt thứ tự) +
   `data-wf-effect="<effects>"` khi tree có khai (vắng mặt = rỗng, phải khớp rỗng).
5. Component bị `hide` ở khổ nào thì vắng mặt đúng ở khung khổ đó; xuất hiện ở khổ bị
   ẩn cũng là lệch.
6. Section/khung thừa ngoài tree, component thừa ngoài tree đều là lệch.
7. Trình bày visual (màu khung, độ lớn chữ, gợi ý hình khối theo Kiểu) do người soạn
   quyết — máy chỉ kiểm tra đối chiếu, cảm quan giao diện thuộc về designer (xem phân công).

## Ví dụ tối thiểu (cặp đôi)

`pricing-tree.md`:

```markdown
# Page: Pricing

## Section: Gói — layout: stack | layout-md: grid-3
- `Card` **Gói Pro** — note: gói đề xuất | states: default, selected | effect: hover-lift
- `Button` **Chọn Pro** — note: CTA duy nhất | states: default, hover, disabled | hide: sm
```

`pricing-wireframe.html`: 1 file, 4 khung `sm/md/lg/xl`; khung `sm` vẽ section Gói dạng
`stack` và vắng nút Chọn Pro; 3 khung còn lại vẽ dạng `grid-3` đủ 2 component;
mọi block gắn đủ `data-wf-*` như mục chuẩn trên.

## Lệch thì sao

Mọi lệch `verify-pair.py` báo ra đều là FAIL, cấm agent tự sửa ngầm. Agent trình nguyên
danh sách lệch cho designer; chỉ khi designer quote câu ok tường minh (giữ nguyên lệch
hoặc chỉ định cách sửa) mới được tiếp tục.
