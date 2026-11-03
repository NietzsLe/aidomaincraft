# Quy ước tree.md + data.json + wireframe.html — wireframe-docs (từ v10.7)

> Tree (`tree.md`) chỉ định nghĩa phạm vi cấu trúc để làm rõ, không sinh ra wireframe.
> Data (`<slug>-data.json`) giữ nội dung mẫu thật render vào wireframe.
> Wireframe (`wireframe.html`) do người/agent soạn tay theo tree + data, thể hiện giao diện thật
> (layout, độ lớn, vị trí tương đối, loại component, states, effect) trên 4 khổ màn hình
> trong 1 file. Bộ ba tree ↔ data ↔ wireframe phải khớp nhau, kiểm tra bằng
> `scripts/verify-pair.py`; lệch thì báo cho designer quyết, cấm tự sửa ngầm.

## Vai trò 3 artifact (bắt buộc)

1. `*-tree.md`: định nghĩa page → section → component kèm note/states/effect/reduced/behavior
   và quy tắc responsive. `scripts/check.py` PASS nghĩa là cấu trúc đã rõ, không nghĩa là đã có wireframe.
2. `*-data.json`: nội dung mẫu theo `convention/data-schema.md` — mọi component
   phải có giá trị hiển thị, wireframe render đúng các giá trị này.
3. `*-wireframe.html`: soạn tay (HTML/CSS self-contained, không mạng, không build ngoài),
   1 file chứa đúng 4 khung khổ màn hình, mỗi khung vẽ lại toàn bộ trang ở khổ đó
   bằng đúng giá trị trong data.
4. Tên bộ ba trong thư mục bản `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<slug>/`:
   `<slug>-tree.md` + `<slug>-data.json` đi với `<slug>-wireframe.html`
   (ví dụ `2026-11-03-1430-pricing/` chứa đủ 3 file). Giờ 24h local; slug
   viết thường-gạch-ngang-không-dấu; trùng phút thì thêm `-v2`, `-v3`.
   Trình review luôn trình cả 3 + dòng PASS của `check.py` + dòng PASS
   của `verify-pair.py` + báo cáo `check-guidelines.py`.

## Bốn khổ màn hình khóa cứng

| Mã | Khổ | Rộng tham chiếu |
|---|---|---|
| `sm` | mobile | 360 |
| `md` | tablet | 768 |
| `lg` | desktop thường (laptop) | 1366 |
| `xl` | desktop lớn (PC để bàn) | 1920 |

Không tự đặt mã khổ khác. Mỗi khung trong wireframe gắn `data-wf-breakpoint`
và `data-wf-width` đúng số trên.

## Biến thể preview theo khổ (cho `templates/viewer.html`)

Rộng chuẩn (in đậm) đúng bảng trên; biến thể là các rộng xem thêm khi review,
không cần soạn khung riêng (nội dung reflow tự nhiên).

| Khổ | Biến thể (px, chuẩn in đậm) |
|---|---|
| `sm` | 320, **360**, 390, 412, 430 |
| `md` | **768**, 800, 834 |
| `lg` | 1280, **1366**, 1440 |
| `xl` | 1600, **1920**, 2560 |

Danh sách này là nguồn sự thật cho viewer; `viewer.html` mirror cứng đúng
các số trên — lệch là FAIL review (kiểm tra ở `tests/test.sh` §14).

## Cú pháp tree (3 loại dòng, còn lại bỏ qua)

```markdown
# Page: <tên trang>
> <ghi chú trang — 1 dòng, tùy chọn>

## Section: <tên section> — layout: <base> | layout-md: <ghi đè> | hide: <khổ...>
- `<KiểuComponent>` **<nhãn hiển thị>** — note: <ghi chú> | states: <state, state> | effect: <effect> | reduced: <instant|none> | behavior: <behavior> | ref: <url> | span-md: <số> | hide: <khổ...>
```

Kiểu + behavior + effect/reduced/ref khóa theo 3 tài liệu sau (không tự bịa):

- Kiểu: thuộc danh sách shadcn pin trong `component-roles.md` (66 component +
  4 layout primitives `Section/Grid/Stack/Container`). Ngoài danh sách = FAIL.
- behavior (tùy chọn): 1 trong `dialog, drawer, sheet, popover, menu, menubar,
  tabs, accordion, pagination, carousel, toast, tooltip, dropdown, sticky`.
  Diễn tả hành vi đặc biệt của component/khung (vd sticky header, dialog mở/đóng).
- effect: tên trong `animations.md`, HOẶC tên tự đặt + bắt buộc `ref:` URL
  nguồn (`http(s)://...`, check hình thức). `ref:` kèm effect trong catalog = FAIL.
- reduced: bắt buộc khi có effect (trừ `focus-ring` là chỉ báo focus, được miễn),
  chỉ nhận `instant|none`.
- Ví dụ: `- \`Dialog\` **Xác nhận xóa** — states: closed, open, focus | effect: fade-scale | reduced: instant | behavior: dialog`

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
   - `note:` ghi chú cho designer/agent (tùy chọn, nhưng `Avatar`/`Chart` bắt buộc
     nhắc `alt` mô tả ảnh — `check-guidelines.py` bắt).
   - `states:` danh sách state cách nhau bằng dấu phẩy (mặc định `default`).
     Component tương tác (xem mapping role ở `component-roles.md`) bắt buộc có
     `focus` (khai báo khả năng focus).
   - `effect:` tên trong `animations.md`, HOẶC tên tự đặt + `ref:` URL nguồn.
     Vắng mặt = không effect.
   - `reduced:` `instant|none`, bắt buộc khi có effect (trừ `focus-ring`).
   - `behavior:` hành vi đặc biệt, thuộc danh sách cho phép ở trên (tùy chọn).
   - `ref:` URL nguồn animation tự đặt (bắt buộc khi effect ngoài catalog).
   - `span:` / `span-sm/md/lg/xl:` số cột chiếm trong lưới (số nguyên ≥1, mặc định 1;
     hậu tố khổ ghi đè dần lên như layout; chỉ có nghĩa trong section dạng lưới).
   - `hide:` liệt kê khổ ẩn component (ví dụ `hide: sm` = có mặt ở md/lg/xl, vắng ở sm).
4. Khóa metadata lạ (sai chính tả, ngoài danh sách trên) là FAIL — `check.py` báo đúng
   dòng để sửa, cấm im lặng bỏ qua vì sẽ gây lệch với wireframe. Kiểu ngoài
   từ vựng shadcn pin, `behavior` ngoài danh sách, `effect` ngoài catalog mà
   thiếu `ref:`, `reduced` sai giá trị — đều FAIL cùng cơ chế.
5. Giá trị `hide` chỉ gồm `sm`, `md`, `lg`, `xl`; `span*` phải là số nguyên ≥1;
   `layout*` phải thuộc danh sách cho phép; `ref:` phải là URL http(s) — sai đều FAIL.
6. Mọi dòng khác (trống, heading `#` khác, text thường) bị bỏ qua khi parse — dùng tự do
   cho ghi chú dài, nhưng thông tin quan trọng (CTA, states, effect, ẩn/hiện, reduced)
   phải nằm trong metadata đúng khóa, cấm để trong dòng tự do.
7. Kiểu component thuộc từ vựng shadcn pin + layout primitives trong
   `component-roles.md` — `check.py` khóa chính xác tên (PascalCase), ngoài danh sách
   là FAIL (kể cả sai chính tả nhỏ). Component mới chỉ vào khi convention cập nhật.
8. Thuộc tính `data-wf-*` nào tree không khai thì HTML để rỗng/vắng — thừa
   thuộc tính không khai cũng là lệch (trừ `data-wf-behavior` tùy chọn).

## Chuẩn wireframe.html soạn tay (bắt buộc để `verify-pair.py` đọc được)

1. Một file, đúng 4 khung, mỗi khung là 1 block gắn `data-wf-breakpoint="<sm|md|lg|xl>"`
   + `data-wf-width="<360|768|1366|1920>"` khớp bảng khổ.
2. Khung gốc (hoặc toàn file) gắn `data-wf-page="<tên page>"` khớp `# Page:` của tree.
3. Trong mỗi khung, mỗi section là 1 block gắn `data-wf-section="<tên section>"` +
   `data-wf-layout="<layout hiệu lực ở khổ đó>"` (layout sau khi áp ghi đè dần lên).
4. Trong mỗi section-khung, mỗi component là 1 block gắn
   `data-wf-component="<nhãn>"` + `data-wf-states="<states cách nhau dấu phẩy>"`
   (khớp tập states của tree, không phân biệt thứ tự) +
   `data-wf-effect="<effects>"` khi tree có khai (vắng mặt = rỗng, phải khớp rỗng) +
   `data-wf-reduced="<instant|none>"` khi tree có khai (vắng mặt = rỗng, phải khớp rỗng).
   `data-wf-behavior` tùy chọn (tree khai thì nên gắn cho đủ, không bắt).
5. Component bị `hide` ở khổ nào thì vắng mặt đúng ở khung khổ đó; xuất hiện ở khổ bị
   ẩn cũng là lệch.
6. Section/khung thừa ngoài tree, component thừa ngoài tree đều là lệch.
7. Trình bày visual (màu khung, độ lớn chữ, gợi ý hình khối theo Kiểu) do người soạn
   quyết — máy chỉ kiểm tra đối chiếu, cảm quan giao diện thuộc về designer (xem phân công).

## Ví dụ tối thiểu (cặp đôi trong `2026-11-03-1430-pricing/`)

`pricing-tree.md`:

```markdown
# Page: Pricing

## Section: Gói — layout: stack | layout-md: grid-3
- `Card` **Gói Pro** — note: gói đề xuất | states: default, selected | effect: hover-lift | reduced: instant
- `Button` **Chọn Pro** — note: CTA duy nhất | states: default, hover, focus, disabled | effect: hover-lift | reduced: instant | hide: sm
```

`pricing-wireframe.html` (cùng thư mục bản): 1 file, 4 khung `sm/md/lg/xl`; khung `sm` vẽ section Gói dạng
`stack` và vắng nút Chọn Pro; 3 khung còn lại vẽ dạng `grid-3` đủ 2 component;
mọi block gắn đủ `data-wf-*` như mục chuẩn trên.

## Lệch thì sao

Mọi lệch `verify-pair.py` báo ra đều là FAIL, cấm agent tự sửa ngầm. Agent trình nguyên
danh sách lệch cho designer; chỉ khi designer quote câu ok tường minh (giữ nguyên lệch
hoặc chỉ định cách sửa) mới được tiếp tục.
