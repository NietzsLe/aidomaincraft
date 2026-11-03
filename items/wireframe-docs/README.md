# wireframe-docs

## Tiếng Việt

### Nguồn gốc
- Tác giả: repo aidomaincraft (định nghĩa nội tại, không nhập từ tool ngoài). Commit khai sinh: commit v10 này.
- Lý do ra đời: cần 1 dạng tài liệu hóa wireframe mà cả designer (đọc markdown/HTML) lẫn agent (parse tree) đều dùng được, tài nguyên sống trong repo thay vì phụ thuộc tool vẽ ngoài.

### Dùng khi
- Cần chốt cấu trúc UI (page → section → component) bằng tree text, rồi thể hiện giao diện thật bằng wireframe soạn tay trên 4 khổ màn hình trong 1 file HTML, với nội dung mẫu thật render đúng mọi component.
- Cần 1 bộ ba tree + data + wireframe mà agent đọc hiểu trực tiếp để build tiếp, không phải đoán từ ảnh chụp màn hình.
- Muốn review cấu trúc bằng checklist máy (`check.py` cho tree, `verify-pair.py` cho bộ ba tree ↔ data ↔ wireframe, `check-guidelines.py` đánh giá theo chuẩn web-interface-guidelines) mà không cần Figma/tài khoản ngoài.

### Bỏ qua khi
- Cần system/design chi tiết pass gates đo được (contrast/focus/fold) → dùng `../hallmark/` (wireframe-docs chỉ khung soạn tay + spec đọc được, không sinh tokens/gates).
- Cần hiệu ứng React có sẵn → dùng `../reactbits/`; cần landing taste đóng gói → dùng `../skillry/`.
- Cần vẽ tay tự do, kéo-thả trực quan → dùng tool vẽ ngoài (Figma/Excalidraw); wireframe-docs là tài liệu text-first, không phải canvas vẽ.

### Áp dụng (không cài từ ngoài)
- Điều kiện: Python 3.8+ (thư viện chuẩn only, không dependency).
- Vị trí output: mọi tree/HTML nháp viết vào 1 thư mục bản `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<tên-trang>/` của dự án đích (giờ 24h local, slug thường-gạch-ngang-không-dấu, trùng phút thêm `-v2`), không viết ra root để tránh commit nhầm. Tạo thư mục + đảm bảo ignored trước khi viết: `mkdir -p .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<tên-trang>`, kiểm tra `.gitignore` đã có dòng `.aidomaincraft/` chưa (thiếu thì thêm; target vendor đã có sẵn), verify bằng `git check-ignore -v .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<tên-trang>/<file>`.
- Viết tree + data: copy `examples/tree.md` vào `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<tên-trang>/<tên-trang>-tree.md`, sửa theo `convention/tree-format.md` (3 loại dòng + metadata: note/states/effect/reduced/behavior/ref/span/hide; layout/layout-md/lg/xl cho section). Kiểu thuộc từ vựng shadcn pin (`convention/component-roles.md`); behavior/effect/reduced/ref theo `convention/tree-format.md` + `animations.md` (effect ngoài catalog bắt buộc `ref:` URL). Viết `<tên-trang>-data.json` theo `convention/data-schema.md` (mọi nhãn component phải có giá trị mẫu).
- Kiểm tra tree: `python3 scripts/check.py .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<tên-trang>/<tên-trang>-tree.md` (exit 0 + dòng PASS mới đạt; khóa metadata lạ, Kiểu ngoài vocab, behavior/effect/reduced/ref sai đều FAIL).
- Soạn wireframe: viết tay `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<tên-trang>/<tên-trang>-wireframe.html` theo tree + data (1 file, đúng 4 khung `sm/md/lg/xl` rộng 360/768/1366/1920, mọi block gắn `data-wf-*`, hiển thị đúng giá trị data), mở browser xem.
- Kiểm tra bộ ba: `python3 scripts/verify-pair.py .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<tên-trang>/<tên-trang>-tree.md .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<tên-trang>/<tên-trang>-wireframe.html` (tự tìm `<slug>-data.json` cạnh tree; exit 0 + dòng PASS mới đạt; lệch thiếu/thừa/sai states-effect/reduced/data đều FAIL để designer quyết).
- Đánh giá guidelines: `python3 scripts/check-guidelines.py .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<tên-trang>/<tên-trang>-tree.md` (báo cáo từng rule + `SCORE: X/6`; FAIL chặn, WARN chỉ nhắc) — xem Usecase con 7.
- Review nhanh: copy `templates/viewer.html` vào cùng thư mục bản, mở `viewer.html?file=<tên-trang>-wireframe.html` (chạy `file://`, không cần server) — bấm loại (`sm/md/lg/xl`) rồi biến thể, gập panel để xem, hoặc bật "Lưới 4 khung" so 1 màn hình (bấm khung để drill-down).
- Kiểm tra đã chạy 03/11/2026 (v10.4): `check.py examples/tree.md` → `PASS: page 'Checkout mẫu' · 2 sections · 4 components`; `verify-pair.py examples/tree.md examples/tree.html` → `PASS: pair ... · 4 breakpoints ...`; 3 case cây lỗi (thiếu section, section rỗng, component trước section) + cặp lệch mẫu (thiếu frame, sai layout, sai states) đều exit 1 đúng.

### Cách item hoạt động
- Cơ chế cốt lõi: `tree.md` markdown chỉ định nghĩa phạm vi cấu trúc (Kiểu khóa theo từ vựng shadcn + mapping ARIA) — designer đọc trực tiếp, `check.py` validate cú pháp; `<slug>-data.json` giữ nội dung mẫu thật; `wireframe.html` soạn tay thể hiện giao diện thật (layout, độ lớn, vị trí tương đối, loại component, states, effect) trên 4 khổ `sm/md/lg/xl` trong 1 file bằng đúng giá trị data; `verify-pair.py` đối chiếu bộ ba và báo mọi lệch cho designer quyết; `check-guidelines.py` đánh giá theo chuẩn web-interface-guidelines. Không canvas, không tài khoản, không mạng, không sinh tự động từ tree.
- Khác biệt vận hành theo usecase: viết tree + data mới (soạn markdown + JSON theo convention, xem [Usecase con 1](#usecase-con-1-viet-treemd-data-mau)) khác validate tree (chạy `check.py`, xem [Usecase con 2](#usecase-con-2-validate-treemd)) khác soạn wireframe tay (viết HTML 4 khung theo tree + data, xem [Usecase con 3](#usecase-con-3-soan-wireframe-tay-4-kho)) khác kiểm tra bộ ba (chạy `verify-pair.py`, xem [Usecase con 4](#usecase-con-4-kiem-tra-bo-ba-tree-data-wireframe)) khác agent đọc bộ ba để build (xem [Usecase con 5](#usecase-con-5-agent-doc-bo-ba-de-build)) khác review nhanh bằng viewer (xem [Usecase con 6](#usecase-con-6-review-nhanh-bang-viewer)) khác đánh giá guidelines (xem [Usecase con 7](#usecase-con-7-danh-gia-theo-guidelines)).

### Cốt lõi bất biến
- Tree và wireframe là 2 artifact riêng, luôn đi thành cặp trong 1 thư mục bản `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<slug>/`: `<slug>-tree.md` + `<slug>-wireframe.html`; tree định nghĩa phạm vi, wireframe thể hiện giao diện; cấm coi output máy là wireframe, cấm trình wireframe không có tree đối chiếu.
- Data là chân thứ ba bắt buộc: `<slug>-data.json` đi cùng thư mục bản; mọi nhãn component phải có giá trị mẫu và HTML phải hiển thị đúng — thiếu/thừa/sai giá trị đều FAIL.
- Kiểu component khóa theo từ vựng shadcn pin + layout primitives (`convention/component-roles.md`); behavior/effect/reduced/ref khóa theo convention (`effect` ngoài catalog bắt buộc `ref:` URL; có effect (trừ `focus-ring`) bắt buộc `reduced:`) — ngoài danh sách đều FAIL.
- Bốn số rộng chuẩn (360/768/1366/1920) và danh sách biến thể từng khổ lấy từ `convention/tree-format.md` (nguồn sự thật); `templates/viewer.html` mirror đúng các số đó — lệch là FAIL review.
- Mọi tree phải qua `check.py` PASS và mọi cặp phải qua `verify-pair.py` PASS trước khi trình review; không nêu được cả 2 dòng PASS = chưa thực sự dùng hệ.
- Mọi wireframe là 1 file duy nhất chứa đúng 4 khung `sm/md/lg/xl` (360/768/1366/1920); thiếu khổ là FAIL.
- Mọi lệch `verify-pair.py` báo ra (thiếu/thừa/sai states-effect) đều là FAIL, cấm agent tự sửa ngầm — chỉ designer quote câu ok tường minh mới được tiếp tục.
- Đúng 3 loại dòng cú pháp tree (`# Page:` đúng 1, `## Section:` ≥1, component `- \`Kiểu\` **Nhãn**`); dòng lạ parser bỏ qua, nhưng khóa metadata lạ là FAIL (tránh sai chính tả gây lệch ngầm).

### Phần tùy chỉnh
- Được đổi: tên page/sections, kiểu component (PascalCase tự đặt, không giới hạn danh mục), nhãn/note/states/effect, layout/span theo khổ, danh sách `hide` theo brief. Bốn mã khổ và 4 số đo rộng là khóa cứng, cấm tự đặt mã khác. Cổng duyệt 2 tầng: (1) artifact nào — shortlist cấu trúc tree (mấy section, component nào) kèm lý do qua question tool, user pick mới viết hoặc agent viết rồi trình duyệt; (2) giữ/đổi gì — note/states/effect/layout/hide nào đổi phải chốt. Waiver (bỏ check, trình tree chưa PASS, trình cặp còn lệch) phải quote câu ok tường minh của designer. Cấm đưa `must-not` (trình wireframe không tree, tự sửa lệch ngầm, bịa cú pháp/khóa metadata mới) vào đây.

### Phân công ai làm gì
- Agent chính: soạn/sửa `tree.md` theo convention, chạy `check.py` tới PASS, soạn `wireframe.html` 4 khung theo tree, chạy `verify-pair.py` tới PASS, trình cả cặp + 2 dòng PASS, verify số sections/components và đủ 4 khổ khớp brief.
- Giao cho claude các bước cần mắt người: nhận xét bố cục/độ lớn/vị trí tương đối và cách đặt nhãn trên wireframe (hợp lý không, thiếu gì) — kèm cặp tree + HTML + brief; cấm agent tự kết luận "nhìn đẹp". Mọi lệch máy đã báo thì designer quyết, không giao claude quyết thay.
- Agent verify: `check.py` PASS + `verify-pair.py` PASS + HTML mở được + đủ 4 khung đúng số đo + states/effect hiển thị khớp tree.

### Định vị khác biệt
- So với vẽ wireframe ngoài (Figma/Excalidraw, miễn phí/có phí): khác ở text-first + cặp đôi kiểm tra được bằng máy — tree.md version được bằng git, diff được từng dòng, agent parse trực tiếp, wireframe HTML soạn tay thể hiện đủ 4 khổ và gắn `data-wf-*` để `verify-pair.py` bắt lệch; tool vẽ mạnh ở kéo-thả trực quan nhưng agent không đọc được file vẽ và không có kiểm tra cặp tự động. Chọn wireframe-docs khi agent phải build tiếp từ cặp tree + wireframe; chọn tool vẽ khi cần phác thảo tay nhanh không qua agent.
- So với `../hallmark/` (39,5k★, sinh system + gates): khác tầng — hallmark sinh page chi tiết pass gates; wireframe-docs làm rõ cấu trúc khung + bố cục 4 khổ trước đó. Chọn wireframe-docs khi chưa chốt cấu trúc và bố cục; chọn hallmark khi cặp tree + wireframe đã chốt và cần chi tiết đạt chuẩn. 2 hệ nối tiếp nhau: cặp chốt → hallmark build.
- Khung trung thực: thắng ở nhẹ (0đ, stdlib, offline) + agent-đọc-được + bắt lệch bằng máy; thua ở trực quan (không kéo-thả, không style đẹp) + không gates đo được + wireframe soạn tay tốn công hơn gen tự động.

### Bản đồ phủ usecase (quét hết catalog v10.7 — ★ mạnh nhất đầu)
- ★ Viết `tree.md` + `<slug>-data.json` mới theo convention: xem Usecase 1.
- ★ Soạn `wireframe.html` tay 4 khổ theo tree + data: xem Usecase 3.
- Validate `tree.md` bằng `check.py` (vocab shadcn, behavior, effect/reduced/ref): xem Usecase 2.
- Kiểm tra bộ ba bằng `verify-pair.py` (báo lệch cho designer): xem Usecase 4.
- Đánh giá theo chuẩn web-interface-guidelines bằng `check-guidelines.py`: xem Usecase 7.
- Review nhanh nhiều khổ/biến thể bằng `viewer.html` (gập panel / lưới 4 khung): xem Usecase 6.
- Trung bình: agent đọc bộ ba để build tiếp (parse tree + data + đối chiếu wireframe): xem Usecase 5.
- KHÔNG hỗ trợ → thay thế: style đẹp/tokens/gates → `../hallmark/`; canvas kéo-thả → Figma/Excalidraw; hiệu ứng React → `../reactbits/`; sinh HTML tự động từ tree → không hỗ trợ (cấm gen, phải soạn tay).

### Hồ sơ quyết định
- Việc DÙNG (5, cụ thể): 1. chốt cấu trúc UI mới bằng tree text trước khi build; 2. thể hiện bố cục 4 khổ bằng wireframe tay có kiểm tra 3 chân bằng máy; 3. cho agent build tiếp từ bộ ba tree + data + wireframe thay vì đoán từ ảnh; 4. soạn data mẫu render đúng vào wireframe (mọi component đều có nội dung thật); 5. đánh giá wireframe theo chuẩn web-interface-guidelines có điểm số.
- Việc KHÔNG DÙNG (3, mỗi việc kèm hệ thay thế): 1. page chi tiết pass gates → dùng `../hallmark/`; 2. vẽ tay trực quan → dùng Figma/Excalidraw; 3. bricks React → dùng `../reactbits/`.
- Free / tổng + giá: 0đ toàn bộ (tài nguyên nội bộ, Python stdlib). Không subscription, tài khoản, key, phí model.
- Ma sát: 6 bước (`copy tree mẫu` → soạn tree + data → `check.py` → `soạn wireframe 4 khổ` → `verify-pair.py` → `check-guidelines.py`), hơn chuẩn 1 dòng 3 bước. ĐÃ chạy thử bộ ba mẫu + 3 case cây lỗi + 3 case cặp lệch + check-guidelines 6/6 (output thật ở [Áp dụng](#ap-dung-khong-cai-tu-ngoai)). Rào cản: chỉ cần Python 3.8+ và công soạn wireframe tay; parser báo FAIL khóa metadata lạ/Kiểu ngoài vocab nên ghi chú tự do trong dòng lạ vẫn không ảnh hưởng check.
- Đối thủ cùng phân khúc: tool vẽ Figma/Excalidraw (trực quan, agent không đọc, không kiểm tra cặp) vs `../hallmark/` (39,5k★, system + gates).
- Chọn nó thay vì đối thủ khi: cần cặp tree + wireframe version-bằng-git, agent đọc trực tiếp được và lệch bị máy bắt. Ví dụ đổi lựa chọn: chốt sitemap 5 trang cho agent build → wireframe-docs; phác tay nhanh không qua agent → Excalidraw; build page chi tiết → hallmark.
- TUYỆT ĐỐI không dùng khi: cần đo gates (contrast/focus/fold); cần canvas kéo-thả; muốn sinh HTML tự động từ tree (FAIL cốt lõi — phải soạn tay).

### Usecase con 1: viết tree.md + data mẫu
- Khi dùng: có brief cấu trúc + nội dung (page/sections/components + giá trị mẫu) cần đóng thành tree + data.
- Khi bỏ qua: tree + data đã có chỉ cần check/soạn wireframe/kiểm tra bộ ba/đánh giá → Usecase 2/3/4/7; bộ ba đã chốt cần build chi tiết → hallmark.
- Cơ chế khác các usecase khác ở đâu: duy nhất soạn markdown + JSON theo convention, chưa chạy script nào; các usecase khác chạy `check.py`/`verify-pair.py`/`check-guidelines.py` hoặc soạn HTML/wireframe.
- Lệnh copy-paste: `mkdir -p .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page && cp items/wireframe-docs/examples/tree.md .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-tree.md` rồi sửa theo `convention/tree-format.md` (Kiểu thuộc từ vựng shadcn pin; behavior/effect/reduced/ref theo danh sách cho phép); viết `my-page-data.json` theo `convention/data-schema.md` (mọi nhãn component phải có giá trị mẫu).
- Ngưỡng số cần đạt: đúng 1 `# Page:`, ≥1 section, mỗi section ≥1 component đúng cú pháp `- \`Kiểu\` **Nhãn**`; Kiểu trong vocab, layout/span/hide/behavior/effect/reduced/ref (nếu có) thuộc danh sách cho phép; data có đủ key cho mọi nhãn.
- Ví dụ input-output (minh họa): input "trang Pricing 3 gói" → output `.aidomaincraft/.tmp/wireframes/2026-11-03-1430-pricing/pricing-tree.md` (`# Page: Pricing` + 2 sections + 5 components có states, section Gói `layout-md: grid-3`).
- Pitfalls riêng: dùng heading lạ (`###`) cho section (parser bỏ qua → section mất — phải `## Section:`); quên backtick/bold ở component (dòng bị bỏ qua im lặng); sai chính tả khóa metadata (`layot-md:`) → `check.py` FAIL đúng dòng (không im lặng).
- Phân công usecase này: agent chính soạn tree (shortlist cấu trúc, user pick mới chốt); chưa cần claude; verify bằng đọc lại + sang Usecase 2.

### Usecase con 2: validate tree.md
- Khi dùng: tree đã soạn cần kiểm tra trước khi soạn wireframe.
- Khi bỏ qua: chỉ đọc cặp đã PASS để build (tin cặp cũ vẫn khớp) → Usecase 5.
- Cơ chế khác các usecase khác ở đâu: duy nhất chạy `check.py` lấy PASS/FAIL cho một mình tree, không đụng tới HTML.
- Lệnh copy-paste: `python3 scripts/check.py .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-tree.md` (chạy trong `items/wireframe-docs/`).
- Ngưỡng số cần đạt: exit 0 + dòng `PASS: page '...' · N sections · M components`; exit 1 = FAIL, sửa theo error rồi chạy lại.
- Ví dụ input-output (minh họa): input `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-tree.md` (copy từ `examples/tree.md`) → output `PASS: page 'Checkout mẫu' · 2 sections · 4 components · types: Button, Input`.
- Pitfalls riêng: tưởng cảnh báo là PASS (chỉ exit 0 mới đạt); check file sai đường dẫn (báo file not found — kiểm tra cwd); viết tree ngoài `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<tên-trang>` (rơi vào git — phải chuyển vào `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<tên-trang>`); khóa metadata lạ tưởng được bỏ qua (FAIL đúng dòng — sửa chính tả rồi chạy lại).
- Phân công usecase này: agent chính chạy + trình dòng PASS; không cần claude; verify bằng exit code.

### Usecase con 3: soạn wireframe tay 4 khổ
- Khi dùng: tree đã PASS cần thể hiện thành giao diện xem được.
- Khi bỏ qua: chỉ cần agent đọc cặp đã chốt để build → Usecase 5 (không soạn mới).
- Cơ chế khác các usecase khác ở đâu: duy nhất tạo file HTML mới bằng tay theo tree; các usecase khác soạn markdown, chạy script kiểm tra, hoặc đọc để build.
- Lệnh copy-paste: copy `examples/tree.html` thành `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-wireframe.html` làm khung xương rồi sửa theo tree (không chạy script sinh nào — cấm gen).
- Ngưỡng số cần đạt: 1 file duy nhất, đúng 4 khung `sm/md/lg/xl` rộng 360/768/1366/1920; mỗi section/component của tree (trừ `hide`) xuất hiện đủ ở khung được phép; mọi block gắn đủ `data-wf-*` theo convention.
- Ví dụ input-output (minh họa): input tree Checkout mẫu (2 sections, CTA `Button Đặt hàng`) → output `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-wireframe.html` 4 khung, khung `sm` vắng nút Quay lại giỏ (`hide: sm`), 3 khung còn lại đủ 4 component.
- Pitfalls riêng: sinh HTML bằng script từ tree (FAIL cốt lõi — phải soạn tay); thiếu 1 khổ (thiếu frame là FAIL ở Usecase 4); quên `data-wf-*` ở block mới thêm (lệch thừa/thiếu ở Usecase 4); viết HTML ngoài `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<tên-trang>` (rơi vào git).
- Phân công usecase này: agent chính soạn HTML + mở kiểm tra kỹ thuật (đủ khung, đúng số đo); giao claude nhận xét bố cục/độ lớn/vị trí/nhãn trên 4 khung (kèm cặp tree + HTML + brief); verify bằng mở browser + sang Usecase 4.

### Usecase con 4: kiểm tra bộ ba tree-data-wireframe
- Khi dùng: tree + data + wireframe đã soạn xong cần đối chiếu trước khi trình.
- Khi bỏ qua: bộ ba cũ đã PASS và không đổi gì → Usecase 5/7.
- Cơ chế khác các usecase khác ở đâu: duy nhất chạy `verify-pair.py` để bắt lệch 3 chiều (tree ↔ data ↔ wireframe); không soạn thêm, không sửa ngầm.
- Lệnh copy-paste: `python3 scripts/verify-pair.py .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-tree.md .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-wireframe.html` (chạy trong `items/wireframe-docs/`, tự tìm `my-page-data.json` cạnh tree).
- Ngưỡng số cần đạt: exit 0 + dòng `PASS: pair '...' · 4 breakpoints · N sections · M components (tree<->wireframe<->data khop)`; exit 1 = FAIL kèm từng dòng lệch (thiếu data/key thừa/giá trị không hiển thị/thiếu frame/khung sai số đo/thiếu-thừa section-component/sai layout-states-effect-reduced).
- Ví dụ input-output (minh họa): input cặp mẫu `examples/tree.md` + `examples/tree.html` → output `PASS: pair 'Checkout mẫu' · 4 breakpoints · 2 sections · 4 components (tree<->wireframe<->data khop)`; input cặp lệch (khung `sm` vẽ thừa nút bị `hide: sm`) → output `FAIL: [sm] ... van xuat hien`, exit 1.
- Pitfalls riêng: tưởng tree PASS là đủ (thiếu PASS cặp = chưa dùng hệ); tự sửa lệch ngầm cho xanh (FAIL quy trình — phải trình designer quyết, waiver quote câu ok tường minh).
- Phân công usecase này: agent chính chạy + trình nguyên danh sách lệch (hoặc dòng PASS); designer quyết giữ/sửa; không cần claude; verify bằng exit code.

### Usecase con 5: agent đọc bộ ba để build
- Khi dùng: bộ ba đã chốt (PASS check + PASS verify-pair + guidelines không còn FAIL), agent khác (hoặc lượt sau) build UI chi tiết từ bộ ba.
- Khi bỏ qua: bộ ba chưa PASS đủ → quay về Usecase 1/3/4.
- Cơ chế khác các usecase khác ở đâu: không chạy script nào — đọc `tree.md` + `data.json` lấy phạm vi + nội dung (note/states/effect/hide/behavior) + đối chiếu `wireframe.html` lấy bố cục 4 khổ; cấm đọc HTML thay tree/data khi cần note/giá trị đầy đủ và cấm đọc tree thay HTML khi cần bố cục.
- Lệnh copy-paste: đọc bộ ba `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-tree.md` + `my-page-data.json` + `my-page-wireframe.html` (block nào thiếu `data-wf-*` thì agent cũng coi như thiếu thông tin).
- Ngưỡng số cần đạt: nêu được page + đủ sections + components kèm states/effect/hide/behavior + giá trị data + bố cục từng khổ; không nêu được = bộ ba thiếu, quay về Usecase 1/3.
- Ví dụ input-output (minh họa): input bộ ba Checkout mẫu → output "page Checkout mẫu, 2 sections, CTA `Button Đặt hàng` states default/hover/focus/disabled effect hover-lift reduced instant + giá trị `ban@example.com`/`123 Nguyễn Huệ, Q.1`, khung sm vắng Quay lại giỏ, Thông tin grid-2 từ md" rồi sang hallmark build.
- Pitfalls riêng: build từ tree mà bỏ wireframe/data (mất bố cục 4 khổ + nội dung thật); build từ wireframe mà bỏ tree (mất note/states/effect đầy đủ); thông tin quan trọng để trong dòng tự do của tree hoặc block thiếu `data-wf-*` (máy + agent đều bỏ qua).
- Phân công usecase này: agent chính đọc + tóm cặp (user xác nhận trước khi build); giao claude khi cần đối chiếu visual; verify bằng tóm tắt khớp cặp.

### Usecase con 6: review nhanh bằng viewer
- Khi dùng: cặp đã PASS cần xem nhanh nhiều khổ/biến thể trên máy tính, không resize Chrome.
- Khi bỏ qua: cặp chưa PASS cả 2 → quay Usecase 1/3/4; chỉ cần đọc spec để build → Usecase 5.
- Cơ chế khác các usecase khác ở đâu: duy nhất mở `viewer.html` bấm nút đổi rộng iframe (loại → biến thể, gập panel, lưới 4 khung); không soạn thêm, không chạy script kiểm tra.
- Lệnh copy-paste: `cp items/wireframe-docs/templates/viewer.html .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/` rồi mở `viewer.html?file=my-page-wireframe.html` (chạy `file://`, không cần server).
- Ngưỡng số cần đạt: 4 nút loại đúng số chuẩn + biến thể đúng danh sách convention + gập/mở panel được (✕/Esc/nút) + lưới hiện đủ 4 khung đúng rộng + bấm khung drill-down đúng khổ.
- Ví dụ input-output (minh họa): input cặp checkout `2026-11-03-1430-checkout` → output bấm `lg` → `1440`, iframe rộng 1440px + nhãn `lg · 1440px`; bật lưới → 4 khung scale vừa màn hình; bấm khung `sm` → về xem đơn 360px.
- Pitfalls riêng: mở viewer thiếu `?file=` (hiện trang hướng dẫn, không phải lỗi); sửa số trong viewer mà không sửa convention (drift — FAIL review); kỳ vọng viewer kiểm tra đúng/sai (viewer chỉ đổi rộng hiển thị, đúng/sai do `verify-pair.py`).
- Phân công usecase này: agent chính copy viewer + mở đúng `?file=` + trình các chế độ; giao claude nhận xét visual ở khổ designer cần; verify bằng bấm đủ nút + nhãn px đúng.

### Usecase con 7: đánh giá theo chuẩn web-interface-guidelines
- Khi dùng: bộ ba đã PASS `check.py` + `verify-pair.py`, cần chấm theo checklist guidelines trước khi trình/chốt.
- Khi bỏ qua: còn FAIL ở check/verify → quay Usecase 2/3/4 (guidelines không thay thế kiểm tra cấu trúc).
- Cơ chế khác các usecase khác ở đâu: duy nhất chạy `check-guidelines.py` đọc mapping role ARIA + đánh giá từng rule (PASS/FAIL/WARN/na) + in `SCORE`; không sửa file, không đối chiếu cặp.
- Lệnh copy-paste: `python3 scripts/check-guidelines.py .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-tree.md` (tự tìm `my-page-data.json` cạnh tree; chạy trong `items/wireframe-docs/`).
- Ngưỡng số cần đạt: exit 0 + `SCORE: 6/6` (6 rule FAIL-core: data/label/focus/motion/alt/ellipsis); FAIL rule nào sửa rule đó; WARN (notes/intl/trigger) chỉ nhắc; na có lý do code-level.
- Ví dụ input-output (minh họa): input bộ ba Checkout mẫu → output `SCORE: 6/6 applicable rules pass (0 WARN)`; input tree thiếu `focus` ở Email → output `FAIL: G-focus [Thông tin] 'Email': interactive thiếu state 'focus'`, exit 1.
- Pitfalls riêng: tưởng verify-pair PASS là đủ chuẩn guidelines (verify-pair chỉ bắt khớp 3 chân, không chấm a11y/UX); sửa WARN cho xanh như FAIL (WARN là nhắc, không chặn — chỉ designer mới nâng WARN thành chặn); đòi check rule code-level (contrast/dark-mode/virtualize → na có lý do, sang code thật mới đo).
- Phân công usecase này: agent chính chạy + trình báo cáo từng rule + SCORE; designer quyết giữ/sửa WARN; không cần claude; verify bằng exit code + hết FAIL.

### Các bước chung
1. Shortlist cấu trúc + nội dung (page/sections/components + giá trị mẫu) qua question tool, user pick mới viết tree + data.
2. Tạo thư mục bản `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<tên-trang>/` + đảm bảo `.gitignore` đã có `.aidomaincraft/` (thiếu thì thêm, verify `git check-ignore -v`), rồi viết `tree.md` + `data.json` theo convention → `check.py` tới PASS → soạn `wireframe.html` 4 khung theo tree + data → `verify-pair.py` tới PASS → `check-guidelines.py` tới SCORE 6/6.
3. Trình bộ ba tree + data + wireframe + 2 dòng PASS + SCORE; visual và mọi lệch giao designer quyết, claude chỉ nhận xét bố cục. Review nhanh nhiều khổ: copy `templates/viewer.html` vào thư mục bản, mở `viewer.html?file=<tên-trang>-wireframe.html`.
4. Chốt bộ ba rồi mới sang build chi tiết (hallmark) — tree/data đổi thì sửa wireframe cho khớp và chạy lại `verify-pair.py`, cấm sửa một bên rồi coi như khớp.

### Prompt mẫu
- "Viết tree.md + data.json cho trang Pricing 3 gói theo wireframe-docs vào `.aidomaincraft/.tmp/wireframes/2026-11-03-1430-pricing/` (2 sections, Kiểu thuộc vocab shadcn, CTA đủ states + focus, effect có reduced, mọi nhãn có giá trị data), chạy check.py tới PASS."
- "Soạn `.aidomaincraft/.tmp/wireframes/2026-11-03-1430-pricing/pricing-wireframe.html` theo tree vừa chốt (4 khung sm/md/lg/xl, gắn đủ data-wf-*), rồi chạy verify-pair.py tới PASS."
- "Chạy verify-pair.py cho bộ ba pricing (tự tìm data) và trình nguyên danh sách lệch (nếu có) để designer quyết."
- "Chạy check-guidelines.py cho bộ ba pricing, trình báo cáo từng rule + SCORE (FAIL sửa ngay, WARN designer quyết)."
- "Đọc cặp `.aidomaincraft/.tmp/wireframes/2026-11-03-1430-pricing/pricing-tree.md` + `.aidomaincraft/.tmp/wireframes/2026-11-03-1430-pricing/pricing-wireframe.html`, tóm cấu trúc (page/sections/CTA/states/bố cục từng khổ) để tao xác nhận trước khi build hallmark."
- "Mở viewer cho bản checkout `2026-11-03-1430-checkout`: copy `templates/viewer.html` vào thư mục bản, mở `viewer.html?file=checkout-wireframe.html`, bấm `lg` → `1440` rồi bật lưới 4 khung."
- Ví dụ điền sẵn: "Viết tree + data cho trang Checkout vào `.aidomaincraft/.tmp/wireframes/2026-11-03-1430-checkout/` (Thông tin + Hành động, CTA `Button Đặt hàng` states default/hover/focus/disabled effect hover-lift reduced instant, nút phụ hide ở sm, data đủ 4 nhãn), check PASS → verify-pair 3 chân PASS → check-guidelines SCORE 6/6."

### Pitfalls
- Sinh HTML tự động từ tree thay vì soạn tay (FAIL cốt lõi).
- Trình wireframe không kèm tree + data đối chiếu (không kiểm tra 3 chân được = chưa dùng hệ).
- Trình tree chưa qua `check.py`, bộ ba chưa qua `verify-pair.py`, hoặc còn FAIL ở `check-guidelines.py` (thiếu dòng PASS/SCORE đạt = chưa dùng hệ).
- Tự sửa lệch ngầm cho xanh (FAIL quy trình — lệch thuộc về designer quyết, waiver quote câu ok tường minh).
- Section viết `###` thay vì `## Section:` (parser bỏ qua im lặng, section biến mất).
- Component thiếu backtick/bold (dòng bị bỏ qua, check vẫn PASS nhưng thiếu món).
- Sai chính tả khóa metadata (`layot-md:`, `hied:`) → `check.py` FAIL đúng dòng (sửa rồi chạy lại, cấm trông chờ bỏ qua).
- Quên `data-wf-*` ở block mới thêm (lệch thừa/thiếu ở `verify-pair.py`); tree khai `reduced:`/`behavior:` mà HTML thiếu attr tương ứng (FAIL khớp).
- Thiếu 1 trong 4 khung hoặc sai số đo rộng (FAIL ở `verify-pair.py`).
- Kiểu ngoài vocab shadcn pin, `behavior` ngoài danh sách, `effect` ngoài catalog mà thiếu `ref:` (FAIL `check.py` — tra convention, không bịa).
- Thông tin quan trọng để trong dòng tự do của tree hoặc block thiếu `data-wf-*` (máy + agent đều bỏ qua — phải đưa vào note:/states:/effect:/behavior:/data-wf-*).
- Data thiếu key, thừa key, hoặc giá trị không xuất hiện trong HTML (FAIL 3 chân ở `verify-pair.py` — wireframe phải render đúng data).
- Viết tree/data/HTML ngoài thư mục bản `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<tên-trang>/` hoặc quên kiểm tra `.gitignore` (file nháp rơi vào git — phải giữ trong `.aidomaincraft/` đã ignored, verify `git check-ignore -v`).
- Mở viewer thiếu `?file=` (hiện trang hướng dẫn, không phải lỗi — thêm `?file=<slug>-wireframe.html`).
- Sửa số rộng trong `viewer.html` mà không sửa `convention/tree-format.md` (drift — FAIL review; convention là nguồn sự thật).
- Kỳ vọng viewer kiểm tra đúng/sai (viewer chỉ đổi rộng hiển thị; đúng/sai do `verify-pair.py`).

### Tham khảo sử dụng (bằng chứng nội bộ — item nội tại)
- Relay log session v10.7 (03/11/2026): vocab shadcn pin (66 mục, đối chiếu ui.shadcn.com/docs/components) + mapping ARIA (đối chiếu MDN, dựa trên WAI-ARIA) + `check.py` PASS + `verify-pair.py` PASS 3 chân + `check-guidelines.py` SCORE 6/6 trên bộ ba mẫu → xác nhận tài nguyên chạy/đúng.
- `tests/test.sh` §13–§16: REGISTRY có dòng wireframe-docs + README có `Nguồn gốc`/`Áp dụng` + cấm tham chiếu `build.py` + bộ ba mẫu PASS + cặp lệch FAIL đúng + viewer tồn tại + số chuẩn khớp convention + vocab/mapping/catalog cho máy đọc được.
- Nguồn ngoài: shadcn docs + MDN ARIA (pin từ vựng/mapping, đối chiếu 03/11/2026) + item `web-interface-guidelines` nội bộ (chuẩn đánh giá); chưa có case dùng ở dự án thật — ghi nhận, bổ sung khi có.

### Tài nguyên trong item
- `scripts/check.py` (validate tree.md: vocab shadcn, metadata, effect/reduced/ref, standalone, exit 0/1).
- `scripts/verify-pair.py` (đối chiếu bộ ba tree ↔ data ↔ wireframe, exit 0/1).
- `scripts/check-guidelines.py` (đánh giá theo chuẩn web-interface-guidelines: PASS/FAIL/WARN/na + SCORE, exit 1 khi còn FAIL).
- `convention/tree-format.md` (chuẩn cú pháp 3 loại dòng + metadata + chuẩn wireframe 4 khổ + quy tắc bộ ba) + `convention/component-roles.md` (từ vựng shadcn pin + mapping ARIA) + `convention/animations.md` (catalog tên gọi chung + quy tắc `ref:`) + `convention/references.md` (nguồn tin cậy + thăng cấp) + `convention/data-schema.md` (schema data JSON).
- `examples/tree.md` + `examples/data.json` + `examples/tree.html` (bộ ba mẫu, cả 3 script đều PASS).
- `templates/viewer.html` (xem nhanh 2 tầng loại→biến thể, gập panel, lưới 4 khung; `?file=` + `file://`, JS thuần).
- Khớp cột `tài nguyên` trong `items/REGISTRY.md`: `scripts/, convention/, examples/, templates/`.

### Tham khảo
- Nội bộ: `convention/tree-format.md`, `examples/tree.md` + `examples/tree.html`, `scripts/verify-pair.py`, relay session v10.4.
- Gốc luật: `../../CHARTER.md` §4b + §5d (khung item nội tại).

### Được dùng ở đâu
- Dùng CHO UI: xem `../../domains/ui/using-wireframe-docs.md` — index `../../domains/ui/README.md`.

### Quay lại index
- Về `../../domains/ui/README.md` để so sánh với `hallmark/` + `reactbits/`.
- Liên quan: `../hallmark/` (build chi tiết từ cặp đã chốt).

---

## English

### Origin
- Author: the aidomaincraft repo (intrinsic definition, not imported). Birth commit: this v10 commit.
- Why: a wireframe practice readable by both designers (markdown/hand-written HTML) and agents (parseable tree plus machine-checked pair), with resources living in-repo instead of an outside drawing tool. The tree only defines scope; it never generates the wireframe.

### When to use
- Settling a UI structure with a text tree, then showing the real interface with a hand-authored wireframe across 4 screen sizes in one HTML file, with real sample content rendered in every component.
- A tree + data + wireframe trio an agent reads directly to keep building, instead of guessing from screenshots.
- Machine-checked reviews (`check.py` for the tree, `verify-pair.py` for the tree ↔ data ↔ wireframe trio, `check-guidelines.py` for web-interface-guidelines scoring) without Figma/accounts.

### When to skip
- Detailed systems needing measured gates → use `../hallmark/` (hand-built frames + readable spec only, no tokens/gates).
- Ready-made React effects → `../reactbits/`; packaged landing taste → `../skillry/`.
- Freehand drawing → outside canvas tools (Figma/Excalidraw); this item is text-first.

### Apply (nothing installed from outside)
- Prerequisite: Python 3.8+ (stdlib only, zero dependencies).
- Output location: write every draft tree/HTML under one version folder `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<page>/` of the target project (24h local time; lowercase-hyphen slug, no diacritics; same-minute clash gets `-v2`), never at the repo root to avoid accidental commits. Create + ensure ignored first: `mkdir -p .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<page>`, check `.gitignore` already lists `.aidomaincraft/` (add it when missing; vendor targets already have it), verify with `git check-ignore -v .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<page>/<file>`.
- Write a tree + data: copy `examples/tree.md` to `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<page>/<page>-tree.md`, follow `convention/tree-format.md` (3 line kinds + metadata; Kiểu from the pinned shadcn vocab; behavior/effect/reduced/ref per the allowlists). Write `<page>-data.json` per `convention/data-schema.md` (every label needs a sample value).
- Check the tree: `python3 scripts/check.py .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<page>/<page>-tree.md` (exit 0 + PASS line bar; unknown keys, off-vocab Kiểu, bad layout/span/hide/behavior/effect/reduced/ref values FAIL).
- Author the wireframe by hand: `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<page>/<page>-wireframe.html` per the tree + data (one file, exactly 4 frames `sm/md/lg/xl` at 360/768/1366/1920, every block carrying `data-wf-*`, every sample value shown), open in a browser.
- Check the trio: `python3 scripts/verify-pair.py .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<page>/<page>-tree.md .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<page>/<page>-wireframe.html` (auto-finds `<page>-data.json`; exit 0 + PASS line bar; every missing/extra/mismatched item or data value FAILs for the designer to rule on).
- Evaluate against guidelines: `python3 scripts/check-guidelines.py .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<page>/<page>-tree.md` (per-rule report + `SCORE`; FAIL blocks, WARN only advises) — see [Sub-usecase 7](#sub-usecase-7-evaluate-against-the-guidelines).
- Quick review: copy `templates/viewer.html` into the same version folder, open `viewer.html?file=<page>-wireframe.html` (`file://`, no server) — pick a type (`sm/md/lg/xl`) then a variant, collapse the panel to view, or switch on the "4-frame grid" to compare on one screen (click a frame to drill down).
- Verified 03/11/2026 (v10.7): pinned shadcn vocab (66 items, checked against ui.shadcn.com/docs/components) + ARIA mapping (checked against MDN) + `check.py` PASS + `verify-pair.py` 3-way PASS + `check-guidelines.py` SCORE 6/6 on the example trio.

### How the item works
- Core: the `tree.md` markdown only defines scope (Kiểu from the pinned shadcn vocab + ARIA-mapped) — designers read it directly, `check.py` validates syntax; `<slug>-data.json` holds the real sample content; the hand-authored `wireframe.html` shows the real interface across 4 breakpoints `sm/md/lg/xl` in one file using exactly those values; `verify-pair.py` diffs the trio and reports every drift for the designer to rule on; `check-guidelines.py` evaluates against the web-interface-guidelines standard. No canvas, accounts, network, or generation from the tree.
- Per-usecase differences: write a tree + data ([Sub-usecase 1](#sub-usecase-1-write-a-new-treemd-datajson)) vs validate the tree ([Sub-usecase 2](#sub-usecase-2-validate-treemd)) vs hand-author the wireframe ([Sub-usecase 3](#sub-usecase-3-hand-author-the-4-frame-wireframe)) vs check the trio ([Sub-usecase 4](#sub-usecase-4-verify-the-tree-data-wireframe-trio)) vs agent-read the trio to build ([Sub-usecase 5](#sub-usecase-5-agent-reads-the-trio-to-build)) vs quick review with the viewer ([Sub-usecase 6](#sub-usecase-6-quick-review-with-the-viewer)) vs evaluate against the guidelines ([Sub-usecase 7](#sub-usecase-7-evaluate-against-the-guidelines)).

### Invariant core
- Tree, data, and wireframe are three separate artifacts, always presented as a trio inside one version folder `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<slug>/`: `<slug>-tree.md` + `<slug>-data.json` + `<slug>-wireframe.html`: the tree defines scope, data holds sample content, the wireframe shows the interface. Machine output is never the wireframe; a wireframe without its tree + data is never a review.
- Kiểu follows the pinned shadcn vocab + layout primitives (`convention/component-roles.md`); behavior/effect/reduced/ref follow the allowlists (`convention/tree-format.md` + `animations.md`; off-catalog effects need a `ref:` URL). The 4 canonical widths and per-type variant lists come from `convention/tree-format.md` (source of truth); `templates/viewer.html` mirrors exactly those numbers — drift is a review FAIL.
- The 4 canonical widths (360/768/1366/1920) and per-type variant lists come from `convention/tree-format.md` (source of truth); `templates/viewer.html` mirrors exactly those numbers — drift is a review FAIL.
- Every tree must `check.py`-PASS and every pair must `verify-pair.py`-PASS before review; missing either PASS line = not really used.
- Every wireframe is one file with exactly the 4 frames `sm/md/lg/xl` (360/768/1366/1920); a missing frame is a FAIL.
- Every drift `verify-pair.py` reports (missing/extra/wrong states-effect) is a FAIL, and agents never fix drifts silently — only an explicit quoted designer ok lets work continue.
- Exactly 3 tree line kinds; stray lines are ignored, but unknown metadata keys are a FAIL (no silent typos that drift from the wireframe).

### Customizable surface
- Tunables: page/section names, component types (free PascalCase), labels/notes/states/effects, per-breakpoint layout/span, `hide` lists. The four breakpoint codes and widths are locked, never renamed. Two-level approval: (1) shortlist the tree structure via the question tool, user picks; (2) what stays/changes. Waivers (skipping a check, presenting an unchecked tree or a drifting pair) must quote the designer's explicit ok. Never list `must-not` items here.

### Work split
- Main agent: writes tree per convention, runs `check.py` to PASS, authors the 4-frame `wireframe.html` per the tree, runs `verify-pair.py` to PASS, presents the pair + both PASS lines, verifies counts and all 4 frames match the brief.
- Hand visual judgment to claude (layout/sizes/positions/labels on the wireframe — with pair + brief); the agent never asserts "looks good". Reported drifts belong to the designer, never to claude as a substitute decider.
- Agent verifies: `check.py` PASS + `verify-pair.py` PASS + openable HTML + 4 frames at the right widths + states/effects matching the tree.

### Differentiating positioning
- Vs outside drawing tools (Figma/Excalidraw): text-first + a machine-checked pair — the tree is git-versioned, line-diffable, agent-parseable, the hand-authored wireframe covers all 4 breakpoints with `data-wf-*` hooks so `verify-pair.py` catches drifts; canvas tools win at freehand but agents can't read their files and there is no automatic pair check. Pick wireframe-docs when an agent must keep building from the tree + wireframe pair.
- Vs `../hallmark/` (39.5k stars, system + gates): different layer — hallmark generates gated detail; wireframe-docs settles structure + 4-breakpoint layout first. Structure/layout undecided → wireframe-docs; pair settled → hallmark. Chain: settled pair → hallmark build.
- Honest frame: wins on weight ($0, stdlib, offline) + agent-readability + machine-caught drift; loses on visuals (no drag-drop, no beauty) + no measured gates + hand-authoring costs more than generation.

### Coverage map (whole v10.7 catalog scanned — ★ strongest first)
- ★ Write a new `tree.md` + `<slug>-data.json` per convention: see Sub-usecase 1.
- ★ Hand-author the 4-frame `wireframe.html` per the tree + data: see Sub-usecase 3.
- Validate with `check.py` (shadcn vocab, behavior, effect/reduced/ref): see Sub-usecase 2.
- Check the trio with `verify-pair.py` (drifts go to the designer): see Sub-usecase 4.
- Evaluate against the web-interface-guidelines with `check-guidelines.py`: see Sub-usecase 7.
- Quick-review many widths/variants with `viewer.html` (collapsible panel / 4-frame grid): see Sub-usecase 6.
- Medium: agent reads the trio to build on: see Sub-usecase 5.
- NOT supported → use instead: beauty/tokens/gates → `../hallmark/`; drag-drop canvas → Figma/Excalidraw; React effects → `../reactbits/`; auto-generating HTML from the tree → unsupported (hand-authoring required).

### Decision dossier
- Jobs SERVED (5): settle a new UI structure in text; show a 4-breakpoint layout in a hand-authored wireframe with machine-checked trio; hand agents a readable trio; author sample data rendered into the wireframe; evaluate the wireframe against the web-interface-guidelines with a score.
- Jobs NOT served (3 + replacements): gated detail pages → `../hallmark/`; freehand drawing → Figma/Excalidraw; React bricks → `../reactbits/`.
- Free / total + price: $0, in-repo resources, stdlib Python. No accounts, keys, or model fees.
- Install friction: 6 steps (copy sample → author tree + data → check → author 4-frame wireframe → verify trio → evaluate guidelines). Ran the example trio + 3 invalid trees + 3 drifting pairs + guidelines 6/6 ([Apply](#apply-nothing-installed-from-outside)). Only barriers: Python 3.8+ and hand-authoring effort; unknown metadata keys and off-vocab Kiểu FAIL loudly so free prose in stray lines still passes the check.
- Viral opponents: Figma/Excalidraw (visual, agent-unreadable, no pair check) vs `../hallmark/` (39.5k stars, system + gates).
- Pick it over opponents when a git-versioned, agent-readable pair with machine-caught drift is needed.
- NEVER use when: gates must be measured; drag-drop needed; auto-generated HTML from the tree is wanted (core FAIL — hand-author it).

### Sub-usecase 1: write a new tree.md + data.json
- When to use: a structure + content brief needs freezing into a tree + data. Skip: tree + data exist → 2/3/4/7; settled trio → hallmark.
- Copy-paste: `mkdir -p .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page && cp items/wireframe-docs/examples/tree.md .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-tree.md`, edit per `convention/tree-format.md` (Kiểu from the pinned shadcn vocab; behavior/effect/reduced/ref per the allowlists); write `my-page-data.json` per `convention/data-schema.md` (every label gets a sample value).
- Numeric bar: exactly one `# Page:`, ≥1 section, each ≥1 component in ``- `Type` **Label**`` syntax with Kiểu from the pinned vocab; any layout/span/hide/behavior/effect/reduced/ref keys from the allowlists; data file covers every label.
- Input-output example (illustrative): "3-tier Pricing page" → `.aidomaincraft/.tmp/wireframes/2026-11-03-1430-pricing/pricing-tree.md` (1 page + 2 sections + 5 stateful components, pricing section `layout-md: grid-3`).
- Own pitfalls: `###` headings for sections (silently ignored — must be `## Section:`); misspelled metadata keys (`layot-md:`) → `check.py` FAILs on the exact line (never silent).
- Work split: main agent drafts (user picks structure); verify by re-read → Sub-usecase 2.

### Sub-usecase 2: validate tree.md
- Copy-paste: `python3 scripts/check.py .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-tree.md` (inside `items/wireframe-docs/`).
- Numeric bar: exit 0 + `PASS: page '...' · N sections · M components`.
- Example: `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-tree.md` (copied from `examples/tree.md`) → `PASS: page 'Checkout mẫu' · 2 sections · 4 components`.
- Own pitfalls: mistaking warnings for PASS (only exit 0 counts); tree written outside `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<page>` (leaks into git); unknown metadata keys assumed ignored (they FAIL — fix the spelling).
- Work split: main agent runs + presents; no claude needed.

### Sub-usecase 3: hand-author the 4-frame wireframe
- When to use: a PASSed tree needs a viewable interface. Skip: reading an already-settled trio to build → Sub-usecase 5 (no new authoring).
- Copy-paste: copy `examples/tree.html` to `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-wireframe.html` as a skeleton, then hand-edit per the tree + data (render every sample value; no generating script — generation is banned).
- Numeric bar: one file, exactly 4 frames `sm/md/lg/xl` at 360/768/1366/1920; every tree section/component (minus `hide`) present in its allowed frames; every block carrying the right `data-wf-*`; every data value shown in its component's blocks.
- Example: Checkout tree (2 sections, CTA `Button Đặt hàng`) → 4-frame wireframe where the `sm` frame hides the back link (`hide: sm`) and the other frames show all 4 components.
- Own pitfalls: generating HTML from the tree (core FAIL — hand-author it); a missing frame or wrong width (FAIL in Sub-usecase 4); a newly added block without `data-wf-*` (drift in Sub-usecase 4); wireframe outside `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<page>` (leaks into git).
- Work split: main agent authors + technical check (frames, widths); claude judges layout/sizes/positions/labels on all 4 frames (pair + brief); verify by opening in a browser → Sub-usecase 4.

### Sub-usecase 4: verify the tree-data-wireframe trio
- When to use: a finished tree + data + wireframe need 3-way diffing before review. Skip: unchanged already-PASSed trio → Sub-usecase 5/7.
- Copy-paste: `python3 scripts/verify-pair.py .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-tree.md .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-wireframe.html` (auto-finds `my-page-data.json` beside the tree; inside `items/wireframe-docs/`).
- Numeric bar: exit 0 + `PASS: pair '...' · 4 breakpoints · N sections · M components (tree<->wireframe<->data khop)`; exit 1 lists each drift (missing data/extra key/unshown value/missing frame/wrong width/missing-extra section-component/wrong layout-states-effect-reduced).
- Example: `examples/tree.md` + `examples/tree.html` → `PASS: pair 'Checkout mẫu' · 4 breakpoints · 2 sections · 4 components (tree<->wireframe<->data khop)`; a drifting pair (sm frame showing a `hide: sm` button) → `FAIL: [sm] ...` exit 1.
- Own pitfalls: treating a tree PASS as enough (a missing trio PASS = not used); silently fixing drifts to green (process FAIL — present drifts to the designer, waivers quote the explicit ok).
- Work split: main agent runs + presents the full drift list (or PASS); designer rules keep/fix; no claude needed.

### Sub-usecase 5: agent reads the trio to build
- No scripts run — read `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-tree.md` + `my-page-data.json` for scope + content (notes/states/effects/hide/behavior/values) and cross-check `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-wireframe.html` for the 4-breakpoint layout; never read the HTML instead of the tree/data for full notes/values, never read the tree instead of the HTML for layout.
- Numeric bar: state page + sections + components with states/effects/hide + per-breakpoint layout; otherwise back to Sub-usecase 1/3.
- Example: the Checkout pair → "Checkout mẫu, 2 sections, CTA `Button Đặt hàng` default/hover/disabled effect hover-lift, sm frame without the back link, Thông tin grid-2 from md up" → hallmark build.
- Own pitfalls: building from the tree alone (loses the 4-breakpoint layout); building from the wireframe alone (loses full notes/states/effects); key info in free prose or blocks without `data-wf-*` (invisible to machines + agents).
- Work split: main agent reads + summarizes (user confirms before building).

### Sub-usecase 6: quick review with the viewer
- When to use: a PASSed pair needs fast multi-width/variant viewing on desktop, no Chrome resizing.
- Skip: pair not yet double-PASSed → back to Sub-usecase 1/3/4; spec-only reading to build → Sub-usecase 5.
- Mechanism vs the others: the only one that opens `viewer.html` and clicks to resize the iframe (type → variant, collapse panel, 4-frame grid); no authoring, no check scripts.
- Copy-paste: `cp items/wireframe-docs/templates/viewer.html .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/` then open `viewer.html?file=my-page-wireframe.html` (`file://`, no server).
- Numeric bar: 4 type buttons at canonical widths + variants matching the convention list + panel collapses/reopens (✕/Esc/button) + grid shows all 4 frames at the right widths + clicking a frame drills to the right breakpoint.
- Example (illustrative): the `2026-11-03-1430-checkout` pair → click `lg` → `1440`, 1440px-wide iframe + `lg · 1440px` label; grid on → 4 scaled frames on one screen; click the `sm` frame → single 360px view.
- Own pitfalls: opening the viewer without `?file=` (shows the help page, not an error); editing widths in the viewer without editing the convention (drift — review FAIL); expecting the viewer to judge right/wrong (it only changes display width; `verify-pair.py` judges).
- Work split: main agent copies the viewer + opens the right `?file=` + presents the modes; claude judges visuals at the needed breakpoint; verify by clicking every control + correct px labels.

### Sub-usecase 7: evaluate against the guidelines
- When to use: a `check.py`-PASSed + `verify-pair.py`-PASSed trio needs a web-interface-guidelines ruling before review/settle.
- Skip: tree/data/wireframe still FAILing checks → back to Sub-usecase 1/3/4; guidelines evaluation never replaces structural checks.
- Mechanism vs the others: the only one that runs `check-guidelines.py` (ARIA role mapping + 6 FAIL rules + 2 WARNs + na list + SCORE); no authoring, no pair diffing.
- Copy-paste: `python3 scripts/check-guidelines.py .aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-my-page/my-page-tree.md` (auto-finds `my-page-data.json`; inside `items/wireframe-docs/`).
- Numeric bar: exit 0 + `SCORE: 6/6`; each FAIL names rule + evidence (`G-focus [Thông tin] 'Email'`); WARNs listed, exit stays 0.
- Example (illustrative): the Checkout trio → `SCORE: 6/6 applicable rules pass (0 WARN)`; a tree with an interactive component missing `focus` → `FAIL: G-focus ...`, exit 1.
- Own pitfalls: treating a verify-pair PASS as a guidelines PASS (pair checks only structure/data, not a11y/UX); fixing WARNs to green (WARNs only advise — only the designer promotes one to blocking).
- Work split: main agent runs + presents the report + SCORE; designer rules on WARNs; no claude needed; verify by exit code + zero FAILs.

### Shared steps
1. Shortlist structure + content via question tool; write only after user picks.
2. Create `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<page>/` + ensure `.gitignore` lists `.aidomaincraft/` (add when missing, verify `git check-ignore -v`), then write `tree.md` + `data.json` per convention → `check.py` to PASS → hand-author the 4-frame wireframe per the tree + data → `verify-pair.py` to PASS → `check-guidelines.py` to SCORE 6/6.
3. Present trio + both PASS lines + SCORE; visuals and every drift go to the designer, claude only comments on layout. Quick multi-width review: copy `templates/viewer.html` into the version folder, open `viewer.html?file=<page>-wireframe.html`.
4. Settle the trio before detail builds; on tree/data change fix the wireframe to match and re-run `verify-pair.py`, never treat one side as matching.

### Sample prompts
- "Write a tree.md + data.json for a 3-tier Pricing page per wireframe-docs into `.aidomaincraft/.tmp/wireframes/2026-11-03-1430-pricing/` (2 sections, shadcn-vocab Kiểu, CTA with full states + focus, effects with reduced, every label with a data value), check.py to PASS."
- "Author `.aidomaincraft/.tmp/wireframes/2026-11-03-1430-pricing/pricing-wireframe.html` per the settled tree (4 frames sm/md/lg/xl, full data-wf-*), then verify-pair.py to PASS."
- "Run verify-pair.py on the pricing trio (auto-finds data) and present the full drift list (if any) for the designer to rule on."
- "Run check-guidelines.py on the pricing trio, present the per-rule report + SCORE (fix FAILs now, designer rules on WARNs)."
- "Read the pair `.aidomaincraft/.tmp/wireframes/2026-11-03-1430-pricing/pricing-tree.md` + `.aidomaincraft/.tmp/wireframes/2026-11-03-1430-pricing/pricing-wireframe.html`, summarize structure (page/sections/CTA/states/layout per breakpoint) for my confirmation before the hallmark build."
- Filled example: "Write the tree + data for a Checkout page into `.aidomaincraft/.tmp/wireframes/2026-11-03-1430-checkout/` (Thông tin + Hành động, CTA `Button Đặt hàng` states default/hover/focus/disabled effect hover-lift reduced instant, secondary button hidden on sm, data for all 4 labels), check.py PASS → 3-way verify-pair PASS → check-guidelines SCORE 6/6."
- "Open the viewer for the `2026-11-03-1430-checkout` version: copy `templates/viewer.html` into the version folder, open `viewer.html?file=checkout-wireframe.html`, click `lg` → `1440`, then switch on the 4-frame grid."

### Pitfalls
- Auto-generating HTML from the tree instead of hand-authoring (core FAIL).
- Presenting a wireframe without its tree + data (no 3-way check = not used).
- Presenting a tree without `check.py`, a trio without `verify-pair.py`, or leftover FAILs in `check-guidelines.py` (missing PASS/SCORE = not used).
- Off-vocab Kiểu, off-list `behavior`, off-catalog `effect` without `ref:` (FAIL `check.py` — consult the convention, never invent).
- Silently fixing drifts to green (process FAIL — drifts belong to the designer, waivers quote the explicit ok).
- `###` sections (silently skipped lines).
- Backtick/bold-less components (silently skipped lines, check still PASSes but misses items).
- Misspelled metadata keys (`layot-md:`, `hied:`) → `check.py` FAILs on the exact line (fix and re-run, never expect leniency).
- New blocks without `data-wf-*` (drift in `verify-pair.py`); tree-declared `reduced:`/`behavior:` missing the matching HTML attr (mismatch FAIL).
- Missing 1 of the 4 frames or wrong frame width (FAIL in `verify-pair.py`).
- Missing/extra data keys, or values absent from the HTML (3-way FAIL in `verify-pair.py` — the wireframe must render the data).
- Key info in free prose or blocks without `data-wf-*` (invisible to parsers + agents; notes/states/effects/behavior belong in metadata).
- Writing trees/data/HTML outside `.aidomaincraft/.tmp/wireframes/YYYY-MM-DD-HHmm-<page>/` or skipping the `.gitignore` check (drafts leak into git — keep them under ignored `.aidomaincraft/`, verify `git check-ignore -v`).
- Opening the viewer without `?file=` (shows the help page, not an error — append `?file=<slug>-wireframe.html`).
- Editing widths in `viewer.html` without editing the convention (drift — review FAIL; the convention is the source of truth).
- Expecting the viewer to judge right/wrong (it only changes display width; `verify-pair.py` judges).

### Usage references (internal evidence — intrinsic item)
- Relay session v10.7 (03/11/2026): pinned shadcn vocab (66 items, checked against ui.shadcn.com/docs/components) + ARIA mapping (checked against MDN) + `check.py` PASS + `verify-pair.py` 3-way PASS + `check-guidelines.py` SCORE 6/6 on the example trio → resources run/correct.
- `tests/test.sh` §13–§16 covers the REGISTRY row + `Nguồn gốc`/`Áp dụng` + no `build.py` references + the example trio PASS + a drifting trio FAIL + viewer presence + canonical widths matching the convention + vocab/mapping/catalog machine blocks + the guidelines run.
- External sources: shadcn docs + MDN ARIA (vocab/mapping pinned, checked 03/11/2026) + the in-repo `web-interface-guidelines` item (evaluation standard); no real-project use yet — recorded, to add with the first real case.

### In-item resources
- `scripts/check.py` (tree validation: shadcn vocab, metadata, effect/reduced/ref; standalone, exit 0/1) + `scripts/verify-pair.py` (trio diff tree ↔ data ↔ wireframe, exit 0/1) + `scripts/check-guidelines.py` (guidelines evaluation: PASS/FAIL/WARN/na + SCORE, exit 1 on FAIL). `convention/tree-format.md` (3 line kinds + metadata + 4-frame wireframe standard + trio rule + variant lists) + `convention/component-roles.md` (pinned vocab + ARIA mapping) + `convention/animations.md` (named catalog + `ref:` rule) + `convention/references.md` (trusted sources + promotion) + `convention/data-schema.md` (data JSON schema). `examples/tree.md` + `examples/data.json` + `examples/tree.html` (hand-authored trio, all three scripts PASS). `templates/viewer.html` (2-level quick view, collapsible panel, 4-frame grid). Matches REGISTRY `tài nguyên`: `scripts/, convention/, examples/, templates/`.

### References
- Internal: `convention/tree-format.md`, `convention/component-roles.md`, `convention/animations.md`, `convention/references.md`, `convention/data-schema.md`, `examples/tree.md` + `examples/data.json` + `examples/tree.html`, `scripts/verify-pair.py`, `scripts/check-guidelines.py`, `templates/viewer.html`, relay v10.7.
- Law: `../../CHARTER.md` §4b + §5d.

### Where used
- Used FOR UI: see `../../domains/ui/using-wireframe-docs.md` — index `../../domains/ui/README.md`.

### Back to index
- Back to `../../domains/ui/README.md` vs `hallmark/` + `reactbits/`.
- Related: `../hallmark/` (detail build from a settled pair).
