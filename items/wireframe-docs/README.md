# wireframe-docs

## Tiếng Việt

### Nguồn gốc
- Tác giả: repo aidomaincraft (định nghĩa nội tại, không nhập từ tool ngoài). Commit khai sinh: commit v10 này.
- Lý do ra đời: cần 1 dạng tài liệu hóa wireframe mà cả designer (đọc markdown/HTML) lẫn agent (parse tree) đều dùng được, tài nguyên sống trong repo thay vì phụ thuộc tool vẽ ngoài.

### Dùng khi
- Cần phác thảo cấu trúc UI (page → section → component) trước khi build, ở dạng designer review được trong 1 file.
- Cần 1 component tree mà agent đọc hiểu trực tiếp để build tiếp, không phải đoán từ ảnh chụp màn hình.
- Muốn review cấu trúc bằng checklist máy (`check.py`) + xem render HTML mà không cần Figma/tài khoản ngoài.

### Bỏ qua khi
- Cần system/design chi tiết pass gates đo được (contrast/focus/fold) → dùng `../hallmark/` (wireframe-docs chỉ vẽ khung xám + nhãn, không sinh tokens/gates).
- Cần hiệu ứng React có sẵn → dùng `../reactbits/`; cần landing taste đóng gói → dùng `../skillry/`.
- Cần vẽ tay tự do, kéo-thả trực quan → dùng tool vẽ ngoài (Figma/Excalidraw); wireframe-docs là tài liệu text-first, không phải canvas vẽ.

### Áp dụng (không cài từ ngoài)
- Điều kiện: Python 3.8+ (thư viện chuẩn only, không dependency).
- Viết tree: copy `examples/tree.md`, sửa theo `convention/tree-format.md` (3 loại dòng: `# Page:`, `## Section:`, `- \`Kiểu\` **Nhãn** — note/states`).
- Kiểm tra: `python3 scripts/check.py <tree.md>` (exit 0 + dòng PASS mới đạt).
- Render: `python3 scripts/build.py <tree.md> -o <trang>.html` rồi mở browser xem.
- Kiểm tra đã chạy 03/11/2026: `check.py examples/tree.md` → `PASS: page 'Checkout mẫu' · 2 sections · 4 components`; `build.py` → `examples/tree.html` (mở được, đủ số thứ tự + states); 3 case lỗi (thiếu section, section rỗng, component trước section) đều exit 1 đúng.

### Cách item hoạt động
- Cơ chế cốt lõi: 1 file `tree.md` markdown là nguồn sự thật duy nhất — designer đọc trực tiếp, `check.py` validate cú pháp, `build.py` render ra HTML wireframe khung xám đánh số. Không canvas, không tài khoản, không mạng.
- Khác biệt vận hành theo usecase: viết tree mới (soạn markdown theo convention, xem [Usecase con 1](#usecase-con-1-viet-treemd-moi)) khác validate (chạy `check.py`, xem [Usecase con 2](#usecase-con-2-validate-treemd)) khác render review (chạy `build.py` + mở browser, xem [Usecase con 3](#usecase-con-3-render-html-review)) khác agent đọc tree để build (parse markdown, xem [Usecase con 4](#usecase-con-4-agent-doc-tree-de-build)).

### Cốt lõi bất biến
- Tree là nguồn sự thật duy nhất: HTML chỉ render từ `tree.md`, cấm sửa HTML render rồi coi là thiết kế (sửa là sửa tree rồi render lại).
- Mọi tree phải qua `check.py` PASS trước khi trình review; không nêu được dòng PASS = chưa thực sự dùng hệ.
- Đúng 3 loại dòng cú pháp (`# Page:` đúng 1, `## Section:` ≥1, component `- \`Kiểu\` **Nhãn**`); dòng lạ parser bỏ qua, cấm trông chờ parser hiểu ghi chú tự do.

### Phần tùy chỉnh
- Được đổi: tên page/sections, kiểu component (PascalCase tự đặt, không giới hạn danh mục), nhãn/note/states theo brief. Cổng duyệt 2 tầng: (1) artifact nào — shortlist cấu trúc tree (mấy section, component nào) kèm lý do qua question tool, user pick mới viết hoặc agent viết rồi trình duyệt; (2) giữ/đổi gì — note/states nào đổi phải chốt. Waiver (bỏ check, trình tree chưa PASS) phải quote câu ok tường minh của user. Cấm đưa `must-not` (sửa HTML render, bịa cú pháp mới) vào đây.

### Phân công ai làm gì
- Agent chính: soạn/sửa `tree.md` theo convention, chạy `check.py` + `build.py`, trình file HTML + dòng PASS, verify số sections/components khớp brief.
- Giao cho claude các bước cần mắt người: nhận xét bố cục/cách đặt nhãn trên HTML render (hợp lý không, thiếu gì) — kèm file HTML + brief; cấm agent tự kết luận "nhìn đẹp".
- Agent verify: `check.py` PASS + HTML mở được + đủ số thứ tự + states hiển thị.

### Định vị khác biệt
- So với vẽ wireframe ngoài (Figma/Excalidraw, miễn phí/có phí): khác ở text-first — tree.md version được bằng git, diff được từng dòng, agent parse trực tiếp; tool vẽ mạnh ở kéo-thả trực quan nhưng agent không đọc được file vẽ. Chọn wireframe-docs khi agent phải build tiếp từ tree; chọn tool vẽ khi cần phác thảo tay nhanh không qua agent.
- So với `../hallmark/` (39,5k★, sinh system + gates): khác tầng — hallmark sinh page chi tiết pass gates; wireframe-docs chỉ làm rõ cấu trúc khung trước đó. Chọn wireframe-docs khi chưa chốt cấu trúc; chọn hallmark khi cấu trúc đã chốt và cần chi tiết đạt chuẩn. 2 hệ nối tiếp nhau: tree chốt → hallmark build.
- Khung trung thực: thắng ở nhẹ (0đ, stdlib, offline) + agent-đọc-được + version bằng git; thua ở trực quan (không kéo-thả, không style đẹp) + không gates đo được.

### Bản đồ phủ usecase (quét hết 3 tài nguyên v0 — ★ mạnh nhất đầu)
- ★ Viết `tree.md` mới theo convention: xem Usecase 1.
- Validate `tree.md` bằng `check.py`: xem Usecase 2.
- Render HTML review bằng `build.py`: xem Usecase 3.
- Trung bình: agent đọc tree để build tiếp (parse markdown, không cần render): xem Usecase 4.
- KHÔNG hỗ trợ → thay thế: style đẹp/tokens/gates → `../hallmark/`; canvas kéo-thả → Figma/Excalidraw; hiệu ứng React → `../reactbits/`.

### Hồ sơ quyết định
- Việc DÙNG (3, cụ thể): 1. chốt cấu trúc UI mới bằng tree text trước khi build; 2. cho agent build tiếp từ tree thay vì đoán từ ảnh; 3. review cấu trúc offline không tài khoản (check + HTML render).
- Việc KHÔNG DÙNG (3, mỗi việc kèm hệ thay thế): 1. page chi tiết pass gates → dùng `../hallmark/`; 2. vẽ tay trực quan → dùng Figma/Excalidraw; 3. bricks React → dùng `../reactbits/`.
- Free / tổng + giá: 0đ toàn bộ (tài nguyên nội bộ, Python stdlib). Không subscription, tài khoản, key, phí model.
- Ma sát: 3 bước (`copy tree mẫu` → `check.py` → `build.py`), hơn chuẩn 1 dòng 2 bước. ĐÃ chạy thử đến render + 3 case lỗi (output thật ở [Áp dụng](#ap-dung-khong-cai-tu-ngoai)). Rào cản: chỉ cần Python 3.8+; parser bỏ qua dòng lạ nên ghi chú tự do không ảnh hưởng check.
- Đối thủ cùng phân khúc: tool vẽ Figma/Excalidraw (trực quan, agent không đọc) vs `../hallmark/` (39,5k★, system + gates).
- Chọn nó thay vì đối thủ khi: cần cấu trúc version-bằng-git mà agent đọc trực tiếp được. Ví dụ đổi lựa chọn: chốt sitemap 5 trang cho agent build → wireframe-docs; phác tay nhanh không qua agent → Excalidraw; build page chi tiết → hallmark.
- TUYỆT ĐỐI không dùng khi: cần đo gates (contrast/focus/fold); cần canvas kéo-thả; sửa HTML render thay vì sửa tree (FAIL cốt lõi).

### Usecase con 1: viết tree.md mới
- Khi dùng: có brief cấu trúc (page/sections/components) cần đóng thành tree.
- Khi bỏ qua: tree đã có chỉ cần check/render → Usecase 2/3; cấu trúc đã chốt cần build chi tiết → hallmark.
- Cơ chế khác các usecase khác ở đâu: duy nhất soạn markdown theo convention, chưa chạy script nào; các usecase khác chạy `check.py`/`build.py` hoặc đọc để build.
- Lệnh copy-paste: `cp items/wireframe-docs/examples/tree.md my-page-tree.md` rồi sửa theo `convention/tree-format.md`.
- Ngưỡng số cần đạt: đúng 1 `# Page:`, ≥1 section, mỗi section ≥1 component đúng cú pháp `- \`Kiểu\` **Nhãn**`.
- Ví dụ input-output (minh họa): input "trang Pricing 3 gói" → output `pricing-tree.md` (`# Page: Pricing` + 2 sections + 5 components có states).
- Pitfalls riêng: dùng heading lạ (`###`) cho section (parser bỏ qua → section mất — phải `## Section:`); quên backtick/bold ở component (dòng bị bỏ qua im lặng).
- Phân công usecase này: agent chính soạn tree (shortlist cấu trúc, user pick mới chốt); chưa cần claude; verify bằng đọc lại + sang Usecase 2.

### Usecase con 2: validate tree.md
- Khi dùng: tree đã soạn cần kiểm tra trước khi trình.
- Khi bỏ qua: chỉ đọc để build (tin tree cũ đã PASS) → Usecase 4.
- Cơ chế khác các usecase khác ở đâu: duy nhất chạy `check.py` lấy PASS/FAIL, không sinh file mới.
- Lệnh copy-paste: `python3 scripts/check.py my-page-tree.md` (chạy trong `items/wireframe-docs/`).
- Ngưỡng số cần đạt: exit 0 + dòng `PASS: page '...' · N sections · M components`; exit 1 = FAIL, sửa theo error rồi chạy lại.
- Ví dụ input-output (minh họa): input `examples/tree.md` → output `PASS: page 'Checkout mẫu' · 2 sections · 4 components · types: Button, Link, TextInput`.
- Pitfalls riêng: tưởng cảnh báo là PASS (chỉ exit 0 mới đạt); check file sai đường dẫn (báo file not found — kiểm tra cwd).
- Phân công usecase này: agent chính chạy + trình dòng PASS; không cần claude; verify bằng exit code.

### Usecase con 3: render HTML review
- Khi dùng: tree đã PASS cần cho designer/mắt người xem.
- Khi bỏ qua: chỉ cần agent đọc → Usecase 4 (không cần render).
- Cơ chế khác các usecase khác ở đâu: duy nhất sinh file HTML từ tree; các usecase khác không sinh file.
- Lệnh copy-paste: `python3 scripts/build.py my-page-tree.md -o my-page.html` rồi mở browser.
- Ngưỡng số cần đạt: file HTML mở được + đủ số thứ tự liên tục + states hiển thị dạng chip + footer đếm đúng sections/components.
- Ví dụ input-output (minh họa): input `examples/tree.md` → output `examples/tree.html` (2 fieldset section, 4 box đánh số 01–04).
- Pitfalls riêng: sửa HTML render thay vì sửa tree (FAIL cốt lõi — render lại là mất); mở file bằng viewer không chạy CSS ngoài (HTML self-contained, không cần server).
- Phân công usecase này: agent chính render + mở kiểm tra kỹ thuật; giao claude nhận xét bố cục/nhãn (kèm file HTML + brief); verify bằng HTML + ý kiến reviewer.

### Usecase con 4: agent đọc tree để build
- Khi dùng: tree đã chốt, agent khác (hoặc lượt sau) build UI chi tiết từ tree.
- Khi bỏ qua: cấu trúc chưa chốt → quay Usecase 1.
- Cơ chế khác các usecase khác ở đâu: không chạy script nào — đọc `tree.md` trực tiếp (markdown là tài liệu agent-đọc-được sẵn).
- Lệnh copy-paste: đọc file `my-page-tree.md` (parser bỏ qua dòng nào thì agent cũng bỏ qua dòng đó).
- Ngưỡng số cần đạt: nêu được page + đủ sections + components kèm states/note; không nêu được = tree thiếu, quay về Usecase 1.
- Ví dụ input-output (minh họa): input `examples/tree.md` → output "page Checkout mẫu, 2 sections, CTA `Button Đặt hàng` states default/hover/disabled" rồi sang hallmark build.
- Pitfalls riêng: đọc HTML render thay vì tree (mất note/states đầy đủ); tree ghi chú mập mờ trong dòng tự do mà agent bỏ qua (thông tin quan trọng phải vào note:/states:).
- Phân công usecase này: agent chính đọc + tóm cấu trúc (user xác nhận trước khi build); giao claude khi cần đối chiếu visual; verify bằng tóm tắt khớp tree.

### Các bước chung
1. Shortlist cấu trúc (page/sections/components) qua question tool, user pick mới viết tree.
2. Viết `tree.md` theo convention → `check.py` tới PASS → `build.py` render (nếu cần mắt người).
3. Trình tree + PASS + HTML; visual giao claude nhận xét.
4. Chốt tree rồi mới sang build chi tiết (hallmark) — tree đổi thì render lại, không sửa HTML.

### Prompt mẫu
- "Viết tree.md cho trang Pricing 3 gói theo wireframe-docs (2 sections, CTA có đủ states), chạy check.py tới PASS."
- "Render examples/tree.md ra HTML và cho biết đủ 4 components đánh số + states không."
- "Đọc my-page-tree.md, tóm cấu trúc (page/sections/CTA/states) để tao xác nhận trước khi build hallmark."
- Ví dụ điền sẵn: "Viết tree cho trang Checkout (Form + Hành động, CTA `Button Đặt hàng` states default/hover/disabled), check PASS rồi render HTML."

### Pitfalls
- Sửa HTML render thay vì sửa tree (render lại là mất — FAIL cốt lõi).
- Section viết `###` thay vì `## Section:` (parser bỏ qua im lặng, section biến mất).
- Component thiếu backtick/bold (dòng bị bỏ qua, check vẫn PASS nhưng thiếu món).
- Thông tin quan trọng để trong dòng tự do (agent + parser đều bỏ qua — phải đưa vào note:/states:).
- Trình tree chưa qua `check.py` (không có dòng PASS = chưa dùng hệ).

### Tham khảo sử dụng (bằng chứng nội bộ — item nội tại v0)
- Relay log session `opencode-261103-071445-d82` (03/11/2026): `check.py` PASS + `build.py` render `examples/tree.html` + 3 case lỗi exit 1 đúng → xác nhận tài nguyên chạy được.
- `tests/test.sh` §13: REGISTRY có dòng wireframe-docs + README có `Nguồn gốc`/`Áp dụng` (sẽ xanh ở commit này).
- Nguồn ngoài: không có (item v0 nội bộ, chưa dùng ở dự án thật) — ghi nhận, bổ sung khi có case dùng thật.

### Tài nguyên trong item
- `scripts/build.py` (render tree.md → HTML, stdlib only) + `scripts/check.py` (validate, exit 0/1).
- `convention/tree-format.md` (chuẩn cú pháp 3 loại dòng).
- `examples/tree.md` + `examples/tree.html` (mẫu chạy được, đã verify).
- Khớp cột `tài nguyên` trong `items/REGISTRY.md`: `scripts/, convention/, examples/`.

### Tham khảo
- Nội bộ: `convention/tree-format.md`, `examples/tree.md`, relay session `opencode-261103-071445-d82`.
- Gốc luật: `../../CHARTER.md` §4b + §5d (khung item nội tại).

### Được dùng ở đâu
- Dùng CHO UI: xem `../../domains/ui/using-wireframe-docs.md` — index `../../domains/ui/README.md`.

### Quay lại index
- Về `../../domains/ui/README.md` để so sánh với `hallmark/` + `reactbits/`.
- Liên quan: `../hallmark/` (build chi tiết từ tree đã chốt).

---

## English

### Origin
- Author: the aidomaincraft repo (intrinsic definition, not imported). Birth commit: this v10 commit.
- Why: a wireframe documentation format readable by both designers (markdown/HTML) and agents (parseable tree), with resources living in-repo instead of an outside drawing tool.

### When to use
- Sketching a UI structure (page → section → component) for review in one file, before building.
- A component tree an agent reads directly to keep building, instead of guessing from screenshots.
- Machine-checked structure review (`check.py`) + HTML render without Figma/accounts.

### When to skip
- Detailed systems needing measured gates → use `../hallmark/` (gray boxes + labels only, no tokens/gates).
- Ready-made React effects → `../reactbits/`; packaged landing taste → `../skillry/`.
- Freehand drawing → outside canvas tools (Figma/Excalidraw); this item is text-first.

### Apply (nothing installed from outside)
- Prerequisite: Python 3.8+ (stdlib only, zero dependencies).
- Write a tree: copy `examples/tree.md`, follow `convention/tree-format.md` (3 line kinds).
- Check: `python3 scripts/check.py <tree.md>` (exit 0 + PASS line bar).
- Render: `python3 scripts/build.py <tree.md> -o <page>.html`, open in a browser.
- Verified 03/11/2026: `check.py` PASS (2 sections, 4 components); `build.py` wrote valid HTML; 3 invalid cases exit 1 correctly.

### How the item works
- Core: one `tree.md` is the single source of truth — designers read it directly, `check.py` validates, `build.py` renders numbered gray-box HTML. No canvas, accounts, or network.
- Per-usecase differences: write a tree ([Sub-usecase 1](#sub-usecase-1-write-a-new-treemd)) vs validate ([Sub-usecase 2](#sub-usecase-2-validate-treemd)) vs render ([Sub-usecase 3](#sub-usecase-3-render-html-for-review)) vs agent-read ([Sub-usecase 4](#sub-usecase-4-agent-reads-the-tree-to-build)).

### Invariant core
- The tree is the only source of truth: HTML renders from `tree.md`; editing rendered HTML as design = off-system.
- Every tree must `check.py`-PASS before review; no PASS line = not really used.
- Exactly 3 line kinds; stray lines are ignored — never rely on the parser reading free prose.

### Customizable surface
- Tunables: page/section names, component types (free PascalCase), labels/notes/states. Two-level approval: (1) shortlist the tree structure via the question tool, user picks; (2) what stays/changes. Waivers (skipping the check) must quote the user's explicit ok. Never list `must-not` items here.

### Work split
- Main agent: writes tree per convention, runs `check.py` + `build.py`, presents HTML + PASS line, verifies counts match the brief.
- Hand visual judgment to claude (layout/label sense on rendered HTML — with file + brief); the agent never asserts "looks good".
- Agent verifies: PASS + openable HTML + continuous numbering + visible states.

### Differentiating positioning
- Vs outside drawing tools (Figma/Excalidraw): text-first — git-versioned, line-diffable, agent-parseable; canvas tools win at freehand but agents can't read their files. Pick wireframe-docs when an agent must keep building from the tree.
- Vs `../hallmark/` (39.5k stars, system + gates): different layer — hallmark generates gated detail; wireframe-docs settles structure first. Structure undecided → wireframe-docs; structure settled → hallmark. Chain: settled tree → hallmark build.
- Honest frame: wins on weight ($0, stdlib, offline) + agent-readability + git; loses on visuals (no drag-drop, no beauty) + no measured gates.

### Coverage map (whole v0 catalog scanned — ★ strongest first)
- ★ Write a new `tree.md`: see Sub-usecase 1.
- Validate with `check.py`: see Sub-usecase 2.
- Render review HTML with `build.py`: see Sub-usecase 3.
- Medium: agent reads the tree to build on: see Sub-usecase 4.
- NOT supported → use instead: beauty/tokens/gates → `../hallmark/`; drag-drop canvas → Figma/Excalidraw; React effects → `../reactbits/`.

### Decision dossier
- Jobs SERVED (3): settle a new UI structure in text; hand agents a readable tree; offline account-free structure review.
- Jobs NOT served (3 + replacements): gated detail pages → `../hallmark/`; freehand drawing → Figma/Excalidraw; React bricks → `../reactbits/`.
- Free / total + price: $0, in-repo resources, stdlib Python. No accounts, keys, or model fees.
- Install friction: 3 steps (copy sample → check → build). Ran through render + 3 error cases ([Apply](#apply-nothing-installed-from-outside)). Only barrier: Python 3.8+.
- Viral opponents: Figma/Excalidraw (visual, agent-unreadable) vs `../hallmark/` (39.5k stars, system + gates).
- Pick it over opponents when a git-versioned, agent-readable structure is needed.
- NEVER use when: gates must be measured; drag-drop needed; rendered HTML edited instead of the tree (core FAIL).

### Sub-usecase 1: write a new tree.md
- When to use: a structure brief needs freezing into a tree. Skip: tree exists → 2/3; structure settled → hallmark.
- Copy-paste: `cp items/wireframe-docs/examples/tree.md my-page-tree.md`, edit per `convention/tree-format.md`.
- Numeric bar: exactly one `# Page:`, ≥1 section, each ≥1 component in ``- `Type` **Label**`` syntax.
- Input-output example (illustrative): "3-tier Pricing page" → `pricing-tree.md` (1 page + 2 sections + 5 stateful components).
- Own pitfalls: `###` headings for sections (silently ignored — must be `## Section:`).
- Work split: main agent drafts (user picks structure); verify by re-read → Sub-usecase 2.

### Sub-usecase 2: validate tree.md
- Copy-paste: `python3 scripts/check.py my-page-tree.md` (inside `items/wireframe-docs/`).
- Numeric bar: exit 0 + `PASS: page '...' · N sections · M components`.
- Example: `examples/tree.md` → `PASS: page 'Checkout mẫu' · 2 sections · 4 components`.
- Own pitfalls: mistaking warnings for PASS (only exit 0 counts).
- Work split: main agent runs + presents; no claude needed.

### Sub-usecase 3: render HTML for review
- Copy-paste: `python3 scripts/build.py my-page-tree.md -o my-page.html`, open in browser.
- Numeric bar: opens + continuous numbering + state chips + correct footer counts.
- Example: `examples/tree.md` → `examples/tree.html` (2 fieldsets, boxes 01–04).
- Own pitfalls: editing rendered HTML instead of the tree (core FAIL — re-renders wipe it).
- Work split: main agent renders + technical check; claude judges layout/labels.

### Sub-usecase 4: agent reads the tree to build
- No scripts run — read `tree.md` directly (stray lines ignored by agents too).
- Numeric bar: state page + sections + components with states/notes; otherwise back to Sub-usecase 1.
- Example: `examples/tree.md` → "Checkout mẫu, 2 sections, CTA `Button Đặt hàng` default/hover/disabled" → hallmark build.
- Own pitfalls: reading rendered HTML instead of the tree (notes/states lost); key info in free prose (must be in note:/states:).
- Work split: main agent reads + summarizes (user confirms before building).

### Shared steps
1. Shortlist structure via question tool; write only after user picks.
2. Write per convention → `check.py` to PASS → `build.py` when human eyes needed.
3. Present tree + PASS + HTML; visuals go to claude.
4. Settle the tree before detail builds; re-render on tree change, never edit HTML.

### Sample prompts
- "Write a tree.md for a 3-tier Pricing page per wireframe-docs, check.py to PASS."
- "Render examples/tree.md and confirm 4 numbered components + states."
- "Read my-page-tree.md, summarize structure for my confirmation before the hallmark build."

### Pitfalls
- Editing rendered HTML instead of the tree (core FAIL).
- `###` sections, backtick/bold-less components (silently skipped lines).
- Key info in free prose (invisible to parser + agents).
- Presenting an unchecked tree (no PASS = not used).

### Usage references (internal evidence — v0 intrinsic item)
- Relay session `opencode-261103-071445-d82` (03/11/2026): PASS + render + 3 invalid cases exit 1 → resources run.
- `tests/test.sh` §13 covers the REGISTRY row + `Nguồn gốc`/`Áp dụng` sections (green in this commit).
- External sources: none yet (internal v0, no real-project use) — recorded, to add with first real case.

### In-item resources
- `scripts/build.py` + `scripts/check.py` (stdlib only). `convention/tree-format.md`. `examples/tree.md` + `examples/tree.html` (verified). Matches REGISTRY `tài nguyên`: `scripts/, convention/, examples/`.

### References
- Internal: `convention/tree-format.md`, `examples/tree.md`, relay `opencode-261103-071445-d82`.
- Law: `../../CHARTER.md` §4b + §5d.

### Where used
- Used FOR UI: see `../../domains/ui/using-wireframe-docs.md` — index `../../domains/ui/README.md`.

### Back to index
- Back to `../../domains/ui/README.md` vs `hallmark/` + `reactbits/`.
- Related: `../hallmark/` (detail build from a settled tree).
