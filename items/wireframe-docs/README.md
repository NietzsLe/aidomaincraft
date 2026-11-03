# wireframe-docs

## Tiếng Việt

### Nguồn gốc
- Tác giả: repo aidomaincraft (định nghĩa nội tại, không nhập từ tool ngoài). Commit khai sinh: commit v10 này.
- Lý do ra đời: cần 1 dạng tài liệu hóa wireframe mà cả designer (đọc markdown/HTML) lẫn agent (parse tree) đều dùng được, tài nguyên sống trong repo thay vì phụ thuộc tool vẽ ngoài.

### Dùng khi
- Cần chốt cấu trúc UI (page → section → component) bằng tree text, rồi thể hiện giao diện thật bằng wireframe soạn tay trên 4 khổ màn hình trong 1 file HTML.
- Cần 1 cặp tree + wireframe mà agent đọc hiểu trực tiếp để build tiếp, không phải đoán từ ảnh chụp màn hình.
- Muốn review cấu trúc bằng checklist máy (`check.py` cho tree, `verify-pair.py` cho cặp tree ↔ wireframe) mà không cần Figma/tài khoản ngoài.

### Bỏ qua khi
- Cần system/design chi tiết pass gates đo được (contrast/focus/fold) → dùng `../hallmark/` (wireframe-docs chỉ khung soạn tay + spec đọc được, không sinh tokens/gates).
- Cần hiệu ứng React có sẵn → dùng `../reactbits/`; cần landing taste đóng gói → dùng `../skillry/`.
- Cần vẽ tay tự do, kéo-thả trực quan → dùng tool vẽ ngoài (Figma/Excalidraw); wireframe-docs là tài liệu text-first, không phải canvas vẽ.

### Áp dụng (không cài từ ngoài)
- Điều kiện: Python 3.8+ (thư viện chuẩn only, không dependency).
- Vị trí output: mọi tree/HTML nháp viết vào `.tmp/wireframes/` của dự án đích, không viết ra root để tránh commit nhầm. Tạo thư mục + đảm bảo ignored trước khi viết: `mkdir -p .tmp/wireframes`, kiểm tra `.gitignore` đã có dòng `.tmp/` chưa (thiếu thì thêm), verify bằng `git check-ignore -v .tmp/wireframes/<file>`.
- Viết tree: copy `examples/tree.md` vào `.tmp/wireframes/<tên-trang>-tree.md`, sửa theo `convention/tree-format.md` (3 loại dòng: `# Page:`, `## Section:`, `- \`Kiểu\` **Nhãn** — note/states/effect/span/hide; layout/layout-md/lg/xl cho section).
- Kiểm tra tree: `python3 scripts/check.py .tmp/wireframes/<tên-trang>-tree.md` (exit 0 + dòng PASS mới đạt; khóa metadata lạ, layout/span/hide sai đều FAIL).
- Soạn wireframe: viết tay `.tmp/wireframes/<tên-trang>-wireframe.html` theo tree (1 file, đúng 4 khung `sm/md/lg/xl` rộng 360/768/1366/1920, mọi block gắn `data-wf-*`), mở browser xem.
- Kiểm tra cặp: `python3 scripts/verify-pair.py .tmp/wireframes/<tên-trang>-tree.md .tmp/wireframes/<tên-trang>-wireframe.html` (exit 0 + dòng PASS mới đạt; mọi lệch thiếu/thừa/sai states-effect đều FAIL để designer quyết).
- Kiểm tra đã chạy 03/11/2026 (v10.4): `check.py examples/tree.md` → `PASS: page 'Checkout mẫu' · 2 sections · 4 components`; `verify-pair.py examples/tree.md examples/tree.html` → `PASS: pair ... · 4 breakpoints ...`; 3 case cây lỗi (thiếu section, section rỗng, component trước section) + cặp lệch mẫu (thiếu frame, sai layout, sai states) đều exit 1 đúng.

### Cách item hoạt động
- Cơ chế cốt lõi: `tree.md` markdown chỉ định nghĩa phạm vi cấu trúc — designer đọc trực tiếp, `check.py` validate cú pháp; `wireframe.html` soạn tay thể hiện giao diện thật (layout, độ lớn, vị trí tương đối, loại component, states, effect) trên 4 khổ `sm/md/lg/xl` trong 1 file; `verify-pair.py` đối chiếu cặp đôi và báo mọi lệch cho designer quyết. Không canvas, không tài khoản, không mạng, không sinh tự động từ tree.
- Khác biệt vận hành theo usecase: viết tree mới (soạn markdown theo convention, xem [Usecase con 1](#usecase-con-1-viet-treemd-moi)) khác validate tree (chạy `check.py`, xem [Usecase con 2](#usecase-con-2-validate-treemd)) khác soạn wireframe tay (viết HTML 4 khung theo tree, xem [Usecase con 3](#usecase-con-3-soan-wireframe-tay-4-kho)) khác kiểm tra cặp (chạy `verify-pair.py`, xem [Usecase con 4](#usecase-con-4-kiem-tra-cap-tree-wireframe)) khác agent đọc cặp để build (xem [Usecase con 5](#usecase-con-5-agent-doc-cap-de-build)).

### Cốt lõi bất biến
- Tree và wireframe là 2 artifact riêng, luôn đi thành cặp `<slug>-tree.md` + `<slug>-wireframe.html`: tree định nghĩa phạm vi, wireframe thể hiện giao diện; cấm coi output máy là wireframe, cấm trình wireframe không có tree đối chiếu.
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

### Bản đồ phủ usecase (quét hết 4 tài nguyên v10.4 — ★ mạnh nhất đầu)
- ★ Viết `tree.md` mới theo convention: xem Usecase 1.
- ★ Soạn `wireframe.html` tay 4 khổ theo tree: xem Usecase 3.
- Validate `tree.md` bằng `check.py`: xem Usecase 2.
- Kiểm tra cặp bằng `verify-pair.py` (báo lệch cho designer): xem Usecase 4.
- Trung bình: agent đọc cặp để build tiếp (parse tree + đối chiếu wireframe): xem Usecase 5.
- KHÔNG hỗ trợ → thay thế: style đẹp/tokens/gates → `../hallmark/`; canvas kéo-thả → Figma/Excalidraw; hiệu ứng React → `../reactbits/`; sinh HTML tự động từ tree → không hỗ trợ (cấm gen, phải soạn tay).

### Hồ sơ quyết định
- Việc DÙNG (3, cụ thể): 1. chốt cấu trúc UI mới bằng tree text trước khi build; 2. thể hiện bố cục 4 khổ bằng wireframe tay có kiểm tra cặp bằng máy; 3. cho agent build tiếp từ cặp tree + wireframe thay vì đoán từ ảnh.
- Việc KHÔNG DÙNG (3, mỗi việc kèm hệ thay thế): 1. page chi tiết pass gates → dùng `../hallmark/`; 2. vẽ tay trực quan → dùng Figma/Excalidraw; 3. bricks React → dùng `../reactbits/`.
- Free / tổng + giá: 0đ toàn bộ (tài nguyên nội bộ, Python stdlib). Không subscription, tài khoản, key, phí model.
- Ma sát: 4 bước (`copy tree mẫu` → `check.py` → `soạn wireframe 4 khổ` → `verify-pair.py`), hơn chuẩn 1 dòng 2 bước. ĐÃ chạy thử cặp mẫu + 3 case cây lỗi + 3 case cặp lệch (output thật ở [Áp dụng](#ap-dung-khong-cai-tu-ngoai)). Rào cản: chỉ cần Python 3.8+ và công soạn wireframe tay; parser báo FAIL khóa metadata lạ nên ghi chú tự do trong dòng lạ vẫn không ảnh hưởng check.
- Đối thủ cùng phân khúc: tool vẽ Figma/Excalidraw (trực quan, agent không đọc, không kiểm tra cặp) vs `../hallmark/` (39,5k★, system + gates).
- Chọn nó thay vì đối thủ khi: cần cặp tree + wireframe version-bằng-git, agent đọc trực tiếp được và lệch bị máy bắt. Ví dụ đổi lựa chọn: chốt sitemap 5 trang cho agent build → wireframe-docs; phác tay nhanh không qua agent → Excalidraw; build page chi tiết → hallmark.
- TUYỆT ĐỐI không dùng khi: cần đo gates (contrast/focus/fold); cần canvas kéo-thả; muốn sinh HTML tự động từ tree (FAIL cốt lõi — phải soạn tay).

### Usecase con 1: viết tree.md mới
- Khi dùng: có brief cấu trúc (page/sections/components) cần đóng thành tree.
- Khi bỏ qua: tree đã có chỉ cần check/soạn wireframe/kiểm tra cặp → Usecase 2/3/4; cặp đã chốt cần build chi tiết → hallmark.
- Cơ chế khác các usecase khác ở đâu: duy nhất soạn markdown theo convention, chưa chạy script nào; các usecase khác chạy `check.py`/`verify-pair.py` hoặc soạn HTML/wireframe.
- Lệnh copy-paste: `mkdir -p .tmp/wireframes && cp items/wireframe-docs/examples/tree.md .tmp/wireframes/my-page-tree.md` rồi sửa theo `convention/tree-format.md`.
- Ngưỡng số cần đạt: đúng 1 `# Page:`, ≥1 section, mỗi section ≥1 component đúng cú pháp `- \`Kiểu\` **Nhãn**`; layout/span/hide (nếu có) thuộc danh sách cho phép.
- Ví dụ input-output (minh họa): input "trang Pricing 3 gói" → output `.tmp/wireframes/pricing-tree.md` (`# Page: Pricing` + 2 sections + 5 components có states, section Gói `layout-md: grid-3`).
- Pitfalls riêng: dùng heading lạ (`###`) cho section (parser bỏ qua → section mất — phải `## Section:`); quên backtick/bold ở component (dòng bị bỏ qua im lặng); sai chính tả khóa metadata (`layot-md:`) → `check.py` FAIL đúng dòng (không im lặng).
- Phân công usecase này: agent chính soạn tree (shortlist cấu trúc, user pick mới chốt); chưa cần claude; verify bằng đọc lại + sang Usecase 2.

### Usecase con 2: validate tree.md
- Khi dùng: tree đã soạn cần kiểm tra trước khi soạn wireframe.
- Khi bỏ qua: chỉ đọc cặp đã PASS để build (tin cặp cũ vẫn khớp) → Usecase 5.
- Cơ chế khác các usecase khác ở đâu: duy nhất chạy `check.py` lấy PASS/FAIL cho một mình tree, không đụng tới HTML.
- Lệnh copy-paste: `python3 scripts/check.py .tmp/wireframes/my-page-tree.md` (chạy trong `items/wireframe-docs/`).
- Ngưỡng số cần đạt: exit 0 + dòng `PASS: page '...' · N sections · M components`; exit 1 = FAIL, sửa theo error rồi chạy lại.
- Ví dụ input-output (minh họa): input `.tmp/wireframes/my-page-tree.md` (copy từ `examples/tree.md`) → output `PASS: page 'Checkout mẫu' · 2 sections · 4 components · types: Button, Link, TextInput`.
- Pitfalls riêng: tưởng cảnh báo là PASS (chỉ exit 0 mới đạt); check file sai đường dẫn (báo file not found — kiểm tra cwd); viết tree ngoài `.tmp/wireframes/` (rơi vào git — phải chuyển vào `.tmp/wireframes/`); khóa metadata lạ tưởng được bỏ qua (FAIL đúng dòng — sửa chính tả rồi chạy lại).
- Phân công usecase này: agent chính chạy + trình dòng PASS; không cần claude; verify bằng exit code.

### Usecase con 3: soạn wireframe tay 4 khổ
- Khi dùng: tree đã PASS cần thể hiện thành giao diện xem được.
- Khi bỏ qua: chỉ cần agent đọc cặp đã chốt để build → Usecase 5 (không soạn mới).
- Cơ chế khác các usecase khác ở đâu: duy nhất tạo file HTML mới bằng tay theo tree; các usecase khác soạn markdown, chạy script kiểm tra, hoặc đọc để build.
- Lệnh copy-paste: copy `examples/tree.html` thành `.tmp/wireframes/my-page-wireframe.html` làm khung xương rồi sửa theo tree (không chạy script sinh nào — cấm gen).
- Ngưỡng số cần đạt: 1 file duy nhất, đúng 4 khung `sm/md/lg/xl` rộng 360/768/1366/1920; mỗi section/component của tree (trừ `hide`) xuất hiện đủ ở khung được phép; mọi block gắn đủ `data-wf-*` theo convention.
- Ví dụ input-output (minh họa): input tree Checkout mẫu (2 sections, CTA `Button Đặt hàng`) → output `.tmp/wireframes/my-page-wireframe.html` 4 khung, khung `sm` vắng nút Quay lại giỏ (`hide: sm`), 3 khung còn lại đủ 4 component.
- Pitfalls riêng: sinh HTML bằng script từ tree (FAIL cốt lõi — phải soạn tay); thiếu 1 khổ (thiếu frame là FAIL ở Usecase 4); quên `data-wf-*` ở block mới thêm (lệch thừa/thiếu ở Usecase 4); viết HTML ngoài `.tmp/wireframes/` (rơi vào git).
- Phân công usecase này: agent chính soạn HTML + mở kiểm tra kỹ thuật (đủ khung, đúng số đo); giao claude nhận xét bố cục/độ lớn/vị trí/nhãn trên 4 khung (kèm cặp tree + HTML + brief); verify bằng mở browser + sang Usecase 4.

### Usecase con 4: kiểm tra cặp tree-wireframe
- Khi dùng: cặp tree + wireframe đã soạn xong cần đối chiếu trước khi trình.
- Khi bỏ qua: cặp cũ đã PASS và không đổi gì → Usecase 5.
- Cơ chế khác các usecase khác ở đâu: duy nhất chạy `verify-pair.py` để bắt lệch 2 chiều; không soạn thêm, không sửa ngầm.
- Lệnh copy-paste: `python3 scripts/verify-pair.py .tmp/wireframes/my-page-tree.md .tmp/wireframes/my-page-wireframe.html` (chạy trong `items/wireframe-docs/`).
- Ngưỡng số cần đạt: exit 0 + dòng `PASS: pair '...' · 4 breakpoints · N sections · M components`; exit 1 = FAIL kèm từng dòng lệch (thiếu frame/khung sai số đo/thiếu-thừa section-component/sai layout-states-effect).
- Ví dụ input-output (minh họa): input cặp mẫu `examples/tree.md` + `examples/tree.html` → output `PASS: pair 'Checkout mẫu' · 4 breakpoints · 2 sections · 4 components`; input cặp lệch (khung `sm` vẽ thừa nút bị `hide: sm`) → output `FAIL: [sm] ... van xuat hien`, exit 1.
- Pitfalls riêng: tưởng tree PASS là đủ (thiếu PASS cặp = chưa dùng hệ); tự sửa lệch ngầm cho xanh (FAIL quy trình — phải trình designer quyết, waiver quote câu ok tường minh).
- Phân công usecase này: agent chính chạy + trình nguyên danh sách lệch (hoặc dòng PASS); designer quyết giữ/sửa; không cần claude; verify bằng exit code.

### Usecase con 5: agent đọc cặp để build
- Khi dùng: cặp đã chốt (2 dòng PASS), agent khác (hoặc lượt sau) build UI chi tiết từ cặp.
- Khi bỏ qua: cặp chưa PASS cả 2 → quay về Usecase 1/3.
- Cơ chế khác các usecase khác ở đâu: không chạy script nào — đọc `tree.md` lấy phạm vi (note/states/effect/hide) + đối chiếu `wireframe.html` lấy bố cục 4 khổ; cấm đọc HTML thay tree khi cần note đầy đủ và cấm đọc tree thay HTML khi cần bố cục.
- Lệnh copy-paste: đọc cặp `.tmp/wireframes/my-page-tree.md` + `.tmp/wireframes/my-page-wireframe.html` (block nào thiếu `data-wf-*` thì agent cũng coi như thiếu thông tin).
- Ngưỡng số cần đạt: nêu được page + đủ sections + components kèm states/effect/hide + bố cục từng khổ; không nêu được = cặp thiếu, quay về Usecase 1/3.
- Ví dụ input-output (minh họa): input cặp Checkout mẫu → output "page Checkout mẫu, 2 sections, CTA `Button Đặt hàng` states default/hover/disabled effect hover-lift, khung sm vắng Quay lại giỏ, Thông tin grid-2 từ md" rồi sang hallmark build.
- Pitfalls riêng: build từ tree mà bỏ wireframe (mất bố cục 4 khổ); build từ wireframe mà bỏ tree (mất note/states/effect đầy đủ); thông tin quan trọng để trong dòng tự do của tree hoặc block thiếu `data-wf-*` (máy + agent đều bỏ qua).
- Phân công usecase này: agent chính đọc + tóm cặp (user xác nhận trước khi build); giao claude khi cần đối chiếu visual; verify bằng tóm tắt khớp cặp.

### Các bước chung
1. Shortlist cấu trúc (page/sections/components) qua question tool, user pick mới viết tree.
2. Tạo `.tmp/wireframes/` + đảm bảo `.gitignore` đã có `.tmp/` (thiếu thì thêm, verify `git check-ignore -v`), rồi viết `tree.md` theo convention → `check.py` tới PASS → soạn `wireframe.html` 4 khung theo tree → `verify-pair.py` tới PASS.
3. Trình cặp tree + wireframe + 2 dòng PASS; visual và mọi lệch giao designer quyết, claude chỉ nhận xét bố cục.
4. Chốt cặp rồi mới sang build chi tiết (hallmark) — tree đổi thì sửa wireframe cho khớp và chạy lại `verify-pair.py`, cấm sửa một bên rồi coi như khớp.

### Prompt mẫu
- "Viết tree.md cho trang Pricing 3 gói theo wireframe-docs vào `.tmp/wireframes/pricing-tree.md` (2 sections, CTA có đủ states, section Gói layout-md grid-3), chạy check.py tới PASS."
- "Soạn `.tmp/wireframes/pricing-wireframe.html` theo tree vừa chốt (4 khung sm/md/lg/xl, gắn đủ data-wf-*), rồi chạy verify-pair.py tới PASS."
- "Chạy verify-pair.py cho cặp pricing và trình nguyên danh sách lệch (nếu có) để designer quyết."
- "Đọc cặp `.tmp/wireframes/pricing-tree.md` + `.tmp/wireframes/pricing-wireframe.html`, tóm cấu trúc (page/sections/CTA/states/bố cục từng khổ) để tao xác nhận trước khi build hallmark."
- Ví dụ điền sẵn: "Viết tree cho trang Checkout vào `.tmp/wireframes/checkout-tree.md` (Thông tin + Hành động, CTA `Button Đặt hàng` states default/hover/disabled effect hover-lift, nút phụ hide ở sm), check PASS rồi soạn wireframe 4 khung."

### Pitfalls
- Sinh HTML tự động từ tree thay vì soạn tay (FAIL cốt lõi).
- Trình wireframe không kèm tree đối chiếu (không kiểm tra cặp được = chưa dùng hệ).
- Trình tree chưa qua `check.py` hoặc cặp chưa qua `verify-pair.py` (thiếu 1 trong 2 dòng PASS = chưa dùng hệ).
- Tự sửa lệch ngầm cho xanh (FAIL quy trình — lệch thuộc về designer quyết, waiver quote câu ok tường minh).
- Section viết `###` thay vì `## Section:` (parser bỏ qua im lặng, section biến mất).
- Component thiếu backtick/bold (dòng bị bỏ qua, check vẫn PASS nhưng thiếu món).
- Sai chính tả khóa metadata (`layot-md:`, `hied:`) → `check.py` FAIL đúng dòng (sửa rồi chạy lại, cấm trông chờ bỏ qua).
- Quên `data-wf-*` ở block mới thêm (lệch thừa/thiếu ở `verify-pair.py`).
- Thiếu 1 trong 4 khung hoặc sai số đo rộng (FAIL ở `verify-pair.py`).
- Thông tin quan trọng để trong dòng tự do của tree hoặc block thiếu `data-wf-*` (máy + agent đều bỏ qua — phải đưa vào note:/states:/effect:/data-wf-*).
- Viết tree/HTML ngoài `.tmp/wireframes/` hoặc quên kiểm tra `.gitignore` (file nháp rơi vào git — phải giữ trong `.tmp/` đã ignored, verify `git check-ignore -v`).

### Tham khảo sử dụng (bằng chứng nội bộ — item nội tại)
- Relay log session v10.4 (03/11/2026): `check.py` standalone PASS trên `examples/tree.md` (không còn import từ `build.py`) + `verify-pair.py` PASS cặp mẫu 4 khổ + 3 case cây lỗi và 3 case cặp lệch (thiếu frame, sai layout, sai states) đều exit 1 đúng → xác nhận tài nguyên chạy được.
- `tests/test.sh` §13–§15: REGISTRY có dòng wireframe-docs + README có `Nguồn gốc`/`Áp dụng` + cấm tham chiếu `build.py` + cặp mẫu PASS + cặp lệch FAIL đúng.
- Nguồn ngoài: không có (item nội tại, chưa dùng ở dự án thật) — ghi nhận, bổ sung khi có case dùng thật.

### Tài nguyên trong item
- `scripts/check.py` (validate tree.md, standalone, exit 0/1) + `scripts/verify-pair.py` (đối chiếu cặp tree ↔ wireframe, exit 0/1).
- `convention/tree-format.md` (chuẩn cú pháp 3 loại dòng + metadata + chuẩn wireframe 4 khổ + quy tắc cặp đôi).
- `examples/tree.md` + `examples/tree.html` (cặp mẫu soạn tay 4 khổ, đã verify PASS cả 2 script).
- Khớp cột `tài nguyên` trong `items/REGISTRY.md`: `scripts/, convention/, examples/`.

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
- Settling a UI structure with a text tree, then showing the real interface with a hand-authored wireframe across 4 screen sizes in one HTML file.
- A tree + wireframe pair an agent reads directly to keep building, instead of guessing from screenshots.
- Machine-checked reviews (`check.py` for the tree, `verify-pair.py` for the pair) without Figma/accounts.

### When to skip
- Detailed systems needing measured gates → use `../hallmark/` (hand-built frames + readable spec only, no tokens/gates).
- Ready-made React effects → `../reactbits/`; packaged landing taste → `../skillry/`.
- Freehand drawing → outside canvas tools (Figma/Excalidraw); this item is text-first.

### Apply (nothing installed from outside)
- Prerequisite: Python 3.8+ (stdlib only, zero dependencies).
- Output location: write every draft tree/HTML under the target project's `.tmp/wireframes/`, never at the repo root to avoid accidental commits. Create + ensure ignored first: `mkdir -p .tmp/wireframes`, check `.gitignore` already lists `.tmp/` (add it when missing), verify with `git check-ignore -v .tmp/wireframes/<file>`.
- Write a tree: copy `examples/tree.md` to `.tmp/wireframes/<page>-tree.md`, follow `convention/tree-format.md` (3 line kinds + metadata: note/states/effect/span/hide; layout/layout-md/lg/xl per section).
- Check the tree: `python3 scripts/check.py .tmp/wireframes/<page>-tree.md` (exit 0 + PASS line bar; unknown keys and bad layout/span/hide values FAIL).
- Author the wireframe by hand: `.tmp/wireframes/<page>-wireframe.html` per the tree (one file, exactly 4 frames `sm/md/lg/xl` at 360/768/1366/1920, every block carrying `data-wf-*`), open in a browser.
- Check the pair: `python3 scripts/verify-pair.py .tmp/wireframes/<page>-tree.md .tmp/wireframes/<page>-wireframe.html` (exit 0 + PASS line bar; every missing/extra/mismatched item FAILs for the designer to rule on).
- Verified 03/11/2026 (v10.4): standalone `check.py` PASS on `examples/tree.md`; `verify-pair.py` PASS on the 4-frame example pair; 3 invalid trees + 3 drifting pairs exit 1 correctly.

### How the item works
- Core: the `tree.md` markdown only defines scope — designers read it directly, `check.py` validates it; the hand-authored `wireframe.html` shows the real interface (layout, sizes, relative positions, component types, states, effects) across 4 breakpoints `sm/md/lg/xl` in one file; `verify-pair.py` diffs the pair and reports every drift for the designer to rule on. No canvas, accounts, network, or generation from the tree.
- Per-usecase differences: write a tree ([Sub-usecase 1](#sub-usecase-1-write-a-new-treemd)) vs validate the tree ([Sub-usecase 2](#sub-usecase-2-validate-treemd)) vs hand-author the wireframe ([Sub-usecase 3](#sub-usecase-3-hand-author-the-4-frame-wireframe)) vs check the pair ([Sub-usecase 4](#sub-usecase-4-verify-the-tree-wireframe-pair)) vs agent-read the pair to build ([Sub-usecase 5](#sub-usecase-5-agent-reads-the-pair-to-build)).

### Invariant core
- Tree and wireframe are two separate artifacts, always presented as a `<slug>-tree.md` + `<slug>-wireframe.html` pair: the tree defines scope, the wireframe shows the interface. Machine output is never the wireframe; a wireframe without its tree is never a review.
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

### Coverage map (whole v10.4 catalog scanned — ★ strongest first)
- ★ Write a new `tree.md`: see Sub-usecase 1.
- ★ Hand-author the 4-frame `wireframe.html` per the tree: see Sub-usecase 3.
- Validate with `check.py`: see Sub-usecase 2.
- Check the pair with `verify-pair.py` (drifts go to the designer): see Sub-usecase 4.
- Medium: agent reads the pair to build on: see Sub-usecase 5.
- NOT supported → use instead: beauty/tokens/gates → `../hallmark/`; drag-drop canvas → Figma/Excalidraw; React effects → `../reactbits/`; auto-generating HTML from the tree → unsupported (hand-authoring required).

### Decision dossier
- Jobs SERVED (3): settle a new UI structure in text; show a 4-breakpoint layout in a hand-authored wireframe with machine-checked pairing; hand agents a readable pair.
- Jobs NOT served (3 + replacements): gated detail pages → `../hallmark/`; freehand drawing → Figma/Excalidraw; React bricks → `../reactbits/`.
- Free / total + price: $0, in-repo resources, stdlib Python. No accounts, keys, or model fees.
- Install friction: 4 steps (copy sample → check → author 4-frame wireframe → verify pair). Ran the example pair + 3 invalid trees + 3 drifting pairs ([Apply](#apply-nothing-installed-from-outside)). Only barriers: Python 3.8+ and hand-authoring effort; unknown metadata keys FAIL loudly so free prose in stray lines still passes the check.
- Viral opponents: Figma/Excalidraw (visual, agent-unreadable, no pair check) vs `../hallmark/` (39.5k stars, system + gates).
- Pick it over opponents when a git-versioned, agent-readable pair with machine-caught drift is needed.
- NEVER use when: gates must be measured; drag-drop needed; auto-generated HTML from the tree is wanted (core FAIL — hand-author it).

### Sub-usecase 1: write a new tree.md
- When to use: a structure brief needs freezing into a tree. Skip: tree exists → 2/3/4; settled pair → hallmark.
- Copy-paste: `mkdir -p .tmp/wireframes && cp items/wireframe-docs/examples/tree.md .tmp/wireframes/my-page-tree.md`, edit per `convention/tree-format.md`.
- Numeric bar: exactly one `# Page:`, ≥1 section, each ≥1 component in ``- `Type` **Label**`` syntax; any layout/span/hide keys from the allowlist.
- Input-output example (illustrative): "3-tier Pricing page" → `.tmp/wireframes/pricing-tree.md` (1 page + 2 sections + 5 stateful components, pricing section `layout-md: grid-3`).
- Own pitfalls: `###` headings for sections (silently ignored — must be `## Section:`); misspelled metadata keys (`layot-md:`) → `check.py` FAILs on the exact line (never silent).
- Work split: main agent drafts (user picks structure); verify by re-read → Sub-usecase 2.

### Sub-usecase 2: validate tree.md
- Copy-paste: `python3 scripts/check.py .tmp/wireframes/my-page-tree.md` (inside `items/wireframe-docs/`).
- Numeric bar: exit 0 + `PASS: page '...' · N sections · M components`.
- Example: `.tmp/wireframes/my-page-tree.md` (copied from `examples/tree.md`) → `PASS: page 'Checkout mẫu' · 2 sections · 4 components`.
- Own pitfalls: mistaking warnings for PASS (only exit 0 counts); tree written outside `.tmp/wireframes/` (leaks into git); unknown metadata keys assumed ignored (they FAIL — fix the spelling).
- Work split: main agent runs + presents; no claude needed.

### Sub-usecase 3: hand-author the 4-frame wireframe
- When to use: a PASSed tree needs a viewable interface. Skip: reading an already-settled pair to build → Sub-usecase 5 (no new authoring).
- Copy-paste: copy `examples/tree.html` to `.tmp/wireframes/my-page-wireframe.html` as a skeleton, then hand-edit per the tree (no generating script — generation is banned).
- Numeric bar: one file, exactly 4 frames `sm/md/lg/xl` at 360/768/1366/1920; every tree section/component (minus `hide`) present in its allowed frames; every block carrying the right `data-wf-*`.
- Example: Checkout tree (2 sections, CTA `Button Đặt hàng`) → 4-frame wireframe where the `sm` frame hides the back link (`hide: sm`) and the other frames show all 4 components.
- Own pitfalls: generating HTML from the tree (core FAIL — hand-author it); a missing frame or wrong width (FAIL in Sub-usecase 4); a newly added block without `data-wf-*` (drift in Sub-usecase 4); wireframe outside `.tmp/wireframes/` (leaks into git).
- Work split: main agent authors + technical check (frames, widths); claude judges layout/sizes/positions/labels on all 4 frames (pair + brief); verify by opening in a browser → Sub-usecase 4.

### Sub-usecase 4: verify the tree-wireframe pair
- When to use: a finished pair needs diffing before review. Skip: unchanged already-PASSed pair → Sub-usecase 5.
- Copy-paste: `python3 scripts/verify-pair.py .tmp/wireframes/my-page-tree.md .tmp/wireframes/my-page-wireframe.html` (inside `items/wireframe-docs/`).
- Numeric bar: exit 0 + `PASS: pair '...' · 4 breakpoints · N sections · M components`; exit 1 lists each drift (missing frame/wrong width/missing-extra section-component/wrong layout-states-effect).
- Example: `examples/tree.md` + `examples/tree.html` → `PASS: pair 'Checkout mẫu' · 4 breakpoints · 2 sections · 4 components`; a drifting pair (sm frame showing a `hide: sm` button) → `FAIL: [sm] ...` exit 1.
- Own pitfalls: treating a tree PASS as enough (a missing pair PASS = not used); silently fixing drifts to green (process FAIL — present drifts to the designer, waivers quote the explicit ok).
- Work split: main agent runs + presents the full drift list (or PASS); designer rules keep/fix; no claude needed.

### Sub-usecase 5: agent reads the pair to build
- No scripts run — read `.tmp/wireframes/my-page-tree.md` for scope (notes/states/effects/hide) and cross-check `.tmp/wireframes/my-page-wireframe.html` for the 4-breakpoint layout; never read the HTML instead of the tree for full notes, never read the tree instead of the HTML for layout.
- Numeric bar: state page + sections + components with states/effects/hide + per-breakpoint layout; otherwise back to Sub-usecase 1/3.
- Example: the Checkout pair → "Checkout mẫu, 2 sections, CTA `Button Đặt hàng` default/hover/disabled effect hover-lift, sm frame without the back link, Thông tin grid-2 from md up" → hallmark build.
- Own pitfalls: building from the tree alone (loses the 4-breakpoint layout); building from the wireframe alone (loses full notes/states/effects); key info in free prose or blocks without `data-wf-*` (invisible to machines + agents).
- Work split: main agent reads + summarizes (user confirms before building).

### Shared steps
1. Shortlist structure via question tool; write only after user picks.
2. Create `.tmp/wireframes/` + ensure `.gitignore` lists `.tmp/` (add when missing, verify `git check-ignore -v`), then write per convention → `check.py` to PASS → hand-author the 4-frame wireframe per the tree → `verify-pair.py` to PASS.
3. Present pair + both PASS lines; visuals and every drift go to the designer, claude only comments on layout.
4. Settle the pair before detail builds; on tree change fix the wireframe to match and re-run `verify-pair.py`, never treat one side as matching.

### Sample prompts
- "Write a tree.md for a 3-tier Pricing page per wireframe-docs into `.tmp/wireframes/pricing-tree.md`, check.py to PASS."
- "Author `.tmp/wireframes/pricing-wireframe.html` per the settled tree (4 frames sm/md/lg/xl, full data-wf-*), then verify-pair.py to PASS."
- "Run verify-pair.py on the pricing pair and present the full drift list (if any) for the designer to rule on."
- "Read the pair `.tmp/wireframes/pricing-tree.md` + `.tmp/wireframes/pricing-wireframe.html`, summarize structure (page/sections/CTA/states/layout per breakpoint) for my confirmation before the hallmark build."
- Filled example: "Write the tree for a Checkout page into `.tmp/wireframes/checkout-tree.md` (Thông tin + Hành động, CTA `Button Đặt hàng` states default/hover/disabled effect hover-lift, secondary button hidden on sm), check.py PASS, then hand-author the 4-frame wireframe."

### Pitfalls
- Auto-generating HTML from the tree instead of hand-authoring (core FAIL).
- Presenting a wireframe without its tree (no pair check = not used).
- Presenting a tree without `check.py` or a pair without `verify-pair.py` (missing either PASS = not used).
- Silently fixing drifts to green (process FAIL — drifts belong to the designer, waivers quote the explicit ok).
- `###` sections (silently skipped lines).
- Backtick/bold-less components (silently skipped lines, check still PASSes but misses items).
- Misspelled metadata keys (`layot-md:`, `hied:`) → `check.py` FAILs on the exact line (fix and re-run, never expect leniency).
- New blocks without `data-wf-*` (drift in `verify-pair.py`).
- Missing 1 of the 4 frames or wrong frame width (FAIL in `verify-pair.py`).
- Key info in free prose or blocks without `data-wf-*` (invisible to parsers + agents).
- Writing trees/HTML outside `.tmp/wireframes/` or skipping the `.gitignore` check (drafts leak into git — keep them under ignored `.tmp/`, verify `git check-ignore -v`).

### Usage references (internal evidence — intrinsic item)
- Relay session v10.4 (03/11/2026): standalone `check.py` PASS + `verify-pair.py` PASS on the 4-frame example pair + 3 invalid trees and 3 drifting pairs exit 1 correctly → resources run.
- `tests/test.sh` §13–§15 covers the REGISTRY row + `Nguồn gốc`/`Áp dụng` + no `build.py` references + the example pair PASS + a drifting pair FAIL.
- External sources: none yet (intrinsic item, no real-project use) — recorded, to add with first real case.

### In-item resources
- `scripts/check.py` (tree validation, standalone, exit 0/1) + `scripts/verify-pair.py` (pair diff, exit 0/1). `convention/tree-format.md` (3 line kinds + metadata + 4-frame wireframe standard + pair rule). `examples/tree.md` + `examples/tree.html` (hand-authored 4-frame pair, both scripts PASS). Matches REGISTRY `tài nguyên`: `scripts/, convention/, examples/`.

### References
- Internal: `convention/tree-format.md`, `examples/tree.md` + `examples/tree.html`, `scripts/verify-pair.py`, relay v10.4.
- Law: `../../CHARTER.md` §4b + §5d.

### Where used
- Used FOR UI: see `../../domains/ui/using-wireframe-docs.md` — index `../../domains/ui/README.md`.

### Back to index
- Back to `../../domains/ui/README.md` vs `hallmark/` + `reactbits/`.
- Related: `../hallmark/` (detail build from a settled pair).
