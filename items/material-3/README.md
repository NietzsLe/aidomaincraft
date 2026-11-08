# material-3

## Tiếng Việt

### Dùng khi
- Build app/screen đúng 1 hệ design-system (Material Design 3) có tokens chuẩn: Compose primary (`MaterialTheme`, adaptive, edge-to-edge/insets — vẽ tràn viền + né thanh hệ thống/IME), Flutter secondary (`useMaterial3`, `ColorScheme.fromSeed`), web limited (`@material/web` + CSS custom properties).
- Generate theme từ seed color (1 màu gốc sinh cả scheme) + dynamic color (Android 12+) + dark mode + 3 contrast levels.
- Audit MD3 compliance có scoring: 10 hạng mục chấm 0-10 ra report (Critical/Warnings/Passing + fixes theo thứ tự) + quick grep checks (`Color(0x`, hex cứng, `@material/mdc-`).
- Tra tokens/components chuẩn khi implement: namespace `md.sys.*` (không gian tên token chuẩn của MD3), 30+ components kèm mapping 3 nền tảng, Expressive platform matrix (Compose/Flutter/Web khác nhau cái gì).

### Bỏ qua khi
- Cần taste tự do không theo hệ → dùng `../frontend-design/` (skill này bắt tuân thủ MD3).
- Cần gates merge số cứng ngoài MD3 (fold/word budget/sweep render) → dùng `../hallmark/`.
- Cần detector máy/hook/CI/Live compare → dùng `../impeccable/`.
- Cần M3 Expressive đầy đủ trên web React/Vue/Svelte → không hệ nào tồn tại (web maintenance-only, Expressive không có trên web — phải custom CSS tay, xem `references/` của skill).
- Cần 1 pass checklist `file:line` chung (không riêng MD3) → dùng `../web-interface-guidelines/`.

### Cài đặt
- Đường 1 (khuyến nghị, `npx`): `npx --yes skills add hamen/material-3-skill --skill material-3 -y` (nguồn README, đã đọc 08/11/2026).
- Đường 2 (Claude Code plugin): `/plugin marketplace add hamen/material-3-skill` rồi `/plugin install material-3@material-3-skill` (hoặc `claude plugin ...` từ shell).
- Đường 3 (Codex/manual): `git clone https://github.com/hamen/material-3-skill.git` rồi symlink `skills/material-3` vào thư mục skills (nguồn README).
- Yêu cầu: Node cho đường 1; Claude Code cho đường 2; git cho đường 3.
- Kiểm tra (đã chạy 08/11/2026): fetch README full + `SKILL.md` full (~31KB) + `LICENSE` (MIT, CWTI Ltd 2026) + skills.sh 2 trang (repo: 1 skill, 3.6K installs; skill: 3.6K installs, 1.6K★, First Seen Apr 12 2026, audits Trust Hub Pass/Socket Pass/**Snyk Warn**). GitHub API 504 liên tục → stars/forks `chưa đối chiếu API`. Chưa chạy: install + dùng thật trên project mẫu (ghi WARN).

### Cách item hoạt động
- Tổ chức đứng sau: Ivan (`@hamen`, Android dev — nguồn README mục Made by) / repo `https://github.com/hamen/material-3-skill`, MIT (`LICENSE` root), skill v1.1.1 (29/06/2026, releases 1.1.1/1.1.0/1.0.0), nhịp update theo releases + `CONTRIBUTING.md` giữ Compose-first.
- Phương thức hoạt động chung: 1 skill nhiều file (`SKILL.md` + 6 references + marketplace/plugin manifests) — decision tree chọn platform → tokens/components theo bảng → patterns → anti-patterns → audit 10 hạng mục có scoring. Tự nhận là *distillation* (đúc kết lại từ nhiều nguồn) *best-effort, có thể drift* (nguồn README mục accuracy) — signatures/BOM (chữ ký API/Bill of Materials) phải check docs chính chủ.
- Khác biệt vận hành theo usecase: build theo MD3 (decision tree platform + component catalog, xem [Usecase con 1](#usecase-con-1-build-theo-md3-co-tokens-components--manh-nhat)) khác theme từ seed (theming + dynamic color, xem [Usecase con 2](#usecase-con-2-theme-tu-seed-color-dynamic-va-dark)) khác audit scoring (procedure + report + grep, xem [Usecase con 3](#usecase-con-3-audit-md3-10-hang-muc-co-scoring)) khác tra tokens (lookup tables + Expressive matrix, xem [Usecase con 4](#usecase-con-4-tra-tokens-components-va-expressive)).

### Cốt lõi bất biến
- Mọi output MD3 qua tokens (`md.sys.*` / `MaterialTheme` / `ThemeData`), cấm hex cứng, cấm `border-radius` tay (dùng shape tokens), cấm trộn MD2+MD3, cấm barrel import `@material/web` (nguyên văn Anti-Patterns). Vi phạm = không còn gọi là dùng hệ.
- Tôn trọng platform matrix: Compose-first cho Expressive/adaptive mới; web maintenance-only, Expressive không có trên web — claim parity web là FAIL.
- Audit theo procedure: đủ 10 hạng mục 0-10 + report đúng format (Critical/Warnings/Passing + fixes theo thứ tự) + ngưỡng pass ≥7/warn 4-6/fail ≤3.
- Sau khi dùng phải nêu được: platform target + tokens/components đã dùng + điểm audit (nếu có); không nêu được = chưa thực sự dùng hệ.

### Phần tùy chỉnh
- Được đổi: seed color, brand colors, dynamic/static, light/dark, contrast level, typeface (Roboto/Roboto Flex là default MD3 — thay khi chủ ý custom type scale), shape/motion trong tokens, component variants, canonical layout theo size class (lớp kích thước màn hình). Cổng duyệt 2 tầng: (1) platform nào — shortlist Compose/Flutter/web kèm lý do qua question tool, user pick mới build (web Expressive phải duyệt custom tay vì thiếu parity); (2) giữ/đổi gì — tokens nào giữ, cái nào custom, version nào waive. Waiver (dùng hex cứng cho case one-off, bỏ qua audit 1 hạng mục) phải quote câu ok tường minh của user + ghi lý do.
- Quan hệ với frontend-design khi cùng bật (nguyên văn SKILL.md): MD3 cho system (tokens/components/layout), frontend-design cho creative direction trong giới hạn; MD3 thắng về component structure + token usage; Roboto là exception hợp lệ. Cấm suy diễn ngược (lấy taste đè tokens).

### Phân công ai làm gì
- Agent chính: xác nhận platform (user pick — cấm mặc định Compose khi brief là web), decision tree, tra tokens/components, build/theme theo bảng, chạy audit + grep, trình report + fixes.
- Giao cho claude các bước cần browser/người thật: verify visual render thật (dynamic color, dark mode, foldables, responsive 5 size classes, motion) + đo contrast + screenshot — kèm URL/mã nguồn + checklist 10 hạng mục + output mong đợi; cấm agent tự kết luận đạt khi không render thật.
- Agent verify: tokens đúng namespace + không hex cứng/`@material/mdc-`/barrel import + audit đủ 10 hạng mục + fixes theo thứ tự.

### Định vị khác biệt (số liệu ngày 08/11/2026)
- So với `../frontend-design/` (Anthropic, 1.1M installs, repo 189k★): khác trục — frontend-design cho direction tự do KHÔNG hệ; skill này cho tuân thủ 1 hệ CÓ scoring. Chọn material-3 thay vì frontend-design khi cần build/audit đúng chuẩn MD3 (tokens + components + audit 0-10); chọn frontend-design khi cần taste lạ ngoài mọi hệ. Quan hệ 2 chiều đã do SKILL.md này định nghĩa (system vs direction + Roboto exception).
- So với `../hallmark/` (50.558★, system + gates máy + sweep): khác enforce — hallmark SINH system mới có gates đo được rồi sweep; skill này ÁP 1 hệ có sẵn (MD3) bằng tra cứu + audit do model chạy, không gate máy. Chọn material-3 thay vì hallmark khi hệ đã chốt là MD3 và cần đúng spec + audit scoring; chọn hallmark khi cần system mới pass gates merge.
- Khung trung thực: thắng ở hệ duy nhất có audit scoring trong kho + tokens/components tra được tới mã + platform matrix trung thực (web thiếu gì nói đó) + tự nhận drift; thua ở enforce máy (audit do model chạy), web Expressive thiếu, Snyk Warn 1/3, GitHub API 504 chưa đối chiếu số, lịch sử ngắn (v1.x từ 06/2026).

### Bản đồ phủ usecase (quét HẾT README + SKILL.md 08/11/2026 — ★ mạnh nhất đầu)
- ★ Build theo MD3 có tokens/components (decision tree platform + component catalog + patterns Compose/Flutter/web): xem Usecase 1.
- Theme từ seed color + dynamic/dark (theming reference + Material Theme Builder flow): xem Usecase 2.
- Trung bình: audit MD3 10 hạng mục có scoring (procedure + report + grep + scoring guide, Compose/Kotlin-Flutter-web): xem Usecase 3.
- Trung bình: tra tokens/components/Expressive matrix (color/type/shape/elevation/motion + mapping 3 nền tảng): xem Usecase 4.
- KHÔNG hỗ trợ → thay thế: taste tự do → `../frontend-design/`; gates merge/sweep → `../hallmark/`; detector/hook/CI/Live → `../impeccable/`; checklist `file:line` chung → `../web-interface-guidelines/`; bricks React → `../reactbits/`; Expressive web đầy đủ → custom CSS tay (không hệ nào có).

### Hồ sơ quyết định
- Việc DÙNG (4, cụ thể): 1. build app/screen đúng MD3 (nhất là Compose/Flutter); 2. theme từ seed + dynamic/dark; 3. audit compliance 10 hạng mục có scoring; 4. tra tokens/components/motion chuẩn khi implement.
- Việc KHÔNG DÙNG (5, mỗi việc kèm hệ thay thế): 1. taste tự do → dùng `../frontend-design/`; 2. gates merge → dùng `../hallmark/`; 3. detector/Live → dùng `../impeccable/`; 4. checklist chung → dùng `../web-interface-guidelines/`; 5. Expressive web đầy đủ → custom tay (skill đã báo thiếu parity).
- Free / tổng + giá: 0đ toàn bộ, MIT (`LICENSE` root, CWTI Ltd 2026, fetch 08/11/2026). Tổng sở hữu = 0đ + tiền model.
- Ma sát cài đặt: 1 dòng tới skill (đường `npx`) = chuẩn; marketplace 2 lệnh; manual 3 bước. ĐÃ chạy 08/11/2026: fetch README + SKILL.md + LICENSE + skills.sh 2 trang. Chưa chạy: install + dùng thật (ghi WARN). Rào cản: Node/git/Claude Code tùy đường; GitHub API 504 (số chưa đối chiếu); Snyk Warn chưa đọc chi tiết; skill tự báo drift (signatures/BOM check docs chính chủ).
- Đối thủ viral cùng phân khúc: `../frontend-design/` (1.1M installs, taste tự do chính chủ Anthropic) vs docs chính chủ `m3.material.io` + repo `material-web` (nguồn sự thật, free).
- Chọn nó thay vì đối thủ khi: cần build/audit đúng 1 hệ MD3 có scoring trong thời gian ngắn. Ví dụ đổi lựa chọn: app Compose cần MaterialTheme + audit → material-3; landing cần direction lạ → frontend-design; output pass gates merge → Hallmark.
- TUYỆT ĐỐI không dùng khi: cần Expressive đầy đủ trên web (không tồn tại); cần enforce bằng máy (audit do model chạy); trích signatures/BOM mà không check docs chính chủ (skill tự cảnh báo drift).

### Usecase con 1: build theo MD3 có tokens components (★ mạnh nhất)
- Khi dùng: có platform target (Compose/Flutter/web) + cần UI đúng spec MD3.
- Khi bỏ qua: cần taste tự do (sang `../frontend-design/`); cần gates merge (sang `../hallmark/`).
- Cơ chế khác các usecase khác ở đâu: duy nhất decision tree platform → component catalog → patterns rồi build; các usecase khác theme/audit/lookup.
- Lệnh copy-paste: `npx --yes skills add hamen/material-3-skill --skill material-3 -y` (cài 1 lần) rồi prompt agent `/material-3 scaffold Tạo app shell responsive có navigation` (kèm platform target).
- Ngưỡng số cần đạt: platform đã chốt (user pick); components đúng mapping nền tảng (Compose `Button`/`Scaffold`, web `md-*-*` đã verify trong catalog); tokens namespace `md.sys.*`; không hex cứng/`@material/mdc-`/barrel import; web ghi rõ giới hạn Expressive.
- Ví dụ input-output (minh họa, không phải mặc định — platform do user pick trước): input "Compose app shell + nav rail adaptive" → output `Scaffold` + `NavigationBar`/`rail` theo size class + `MaterialTheme` + edge-to-edge insets.
- Pitfalls riêng: mặc định Compose khi brief là web (platform phải user pick — FAIL core); web mà claim Expressive parity (skill đã báo không có); import cả `@material/web`.
- Phân công usecase này: agent chính xác nhận platform → decision tree → build; giao claude verify render thật (5 size classes, foldables); verify bằng tokens + screenshot.

### Usecase con 2: theme từ seed color dynamic và dark
- Khi dùng: có seed/brand color, cần light/dark/dynamic schemes + contrast levels.
- Khi bỏ qua: theme có sẵn (sang Usecase 1 build thẳng); chỉ cần check (sang Usecase 3).
- Cơ chế khác các usecase khác ở đâu: duy nhất sinh schemes (theming reference + Theme Builder flow); các usecase khác build/audit/lookup.
- Lệnh copy-paste: `/material-3 theme Generate a theme from seed color #1A73E8` (ghi rõ dynamic hay static + contrast level).
- Ngưỡng số cần đạt: scheme đủ light/dark (+ dynamic khi Android 12+ API 31+ và user bật); tonal pairing đúng (`onX` trên `X`); contrast UI components 3:1 text lớn/borders, 4.5:1 text thường (audit sẽ đo lại ở Usecase 3).
- Ví dụ input-output (minh họa): input seed `#1A73E8` + dynamic + dark → output light/dark schemes + `dynamicLightColorScheme`/`dynamicDarkColorScheme` (API 31+) hoặc static fallback.
- Pitfalls riêng: dynamic color mà không check API 31+/user setting (crash/mất màu — check `Build.VERSION.SDK_INT`); tonal pairing tùy tiện (vỡ contrast ở high-contrast mode).
- Phân công usecase này: agent chính sinh schemes; giao claude đo contrast thật + screenshot light/dark; verify bằng schemes + số đo.

### Usecase con 3: audit MD3 10 hạng mục có scoring
- Khi dùng: có URL/file paths/app chạy được cần chấm compliance trước ship.
- Khi bỏ qua: chỉ cần checklist UI chung (sang guidelines); cần gates merge số cứng khác (sang `../hallmark/`).
- Cơ chế khác các usecase khác ở đâu: duy nhất chấm điểm (procedure + report + grep + scoring guide); các usecase khác sinh/tra.
- Lệnh copy-paste: `/material-3 audit [URL hoặc file path]` (nêu rõ stack: Compose-Kotlin/Flutter/web).
- Ngưỡng số cần đạt: đủ 10 hạng mục 0-10 + report đúng format (Critical 0-3 có `file:line` + fix, Warnings 4-6, Passing 7-10, fixes theo thứ tự); ngưỡng pass ≥7/warn 4-6/fail ≤3; grep checks đã chạy (`Color(0x`, hex cứng, `@material/mdc-`).
- Ví dụ input-output (minh họa): input audit web app → output report 82/100 + Critical (hex cứng 3 chỗ có file:line) + fix theo thứ tự.
- Pitfalls riêng: audit bằng đọc code mà không render (contrast/focus phải đo thật — giao claude); MD3 roles tưởng đủ a11y (SKILL.md bắt verify contrast riêng).
- Phân công usecase này: agent chính inspect + grep + trình report; giao claude đo render (contrast, focus, motion, responsive); verify bằng report đủ 10 + số đo.

### Usecase con 4: tra tokens components và Expressive
- Khi dùng: đang implement cần tra nhanh token/component/motion/platform parity.
- Khi bỏ qua: đã thuộc bảng (không tra cho có); cần quyết định build (sang Usecase 1).
- Cơ chế khác các usecase khác ở đâu: duy nhất lookup (tables + matrix), không sinh không chấm.
- Lệnh copy-paste: mở `skills/material-3/references/<color-system|component-catalog|typography-and-shape|layout-and-responsive>` theo câu hỏi (decision tree trong SKILL.md chỉ file).
- Ngưỡng số cần đạt: token đúng namespace + vai (`--md-sys-color-primary` cho fills, `outline-variant` cho dividers không phải `outline`); component đúng variant; platform parity check qua Expressive matrix trước khi claim (web thiếu gì ghi đó).
- Ví dụ input-output (minh họa): input "divider dùng token nào" → output `outline-variant` (không phải `outline`) + lý do (outline dành cho borders quan trọng như text field).
- Pitfalls riêng: `outline` cho dividers; `border-radius` tay; shadows thay tonal elevation; SSR với `@material/web` mà quên hydration (custom elements cần JS).
- Phân công usecase này: agent chính tra + áp; không cần claude trừ khi render lạ.

### Các bước chung
1. Cài 1 lần (đường nào user chọn — `npx` nhanh nhất).
2. Chốt platform (Compose/Flutter/web — user pick, cấm mặc định; web ghi rõ giới hạn Expressive).
3. Decision tree → tra tokens/components → build/theme theo bảng.
4. Audit 10 hạng mục + grep → report + fixes theo thứ tự.
5. Re-verify số đo render (contrast/focus/responsive) bằng claude khi cần.
6. Nêu platform/tokens/audit-score (core-fidelity).

### Prompt mẫu
- "Dùng material-3 build `<component/app>` cho `<platform>`: chốt platform trước, tra tokens/components đúng namespace, không hex cứng, không trộn MD2."
- "Dùng material-3 theme từ seed `<hex>`: dynamic/static + light/dark + contrast level, tonal pairing đúng, check API 31+ nếu dynamic."
- "Dùng material-3 audit `<URL|paths>` (stack ...): đủ 10 hạng mục + report format + grep checks, Critical kèm file:line."
- Ví dụ điền sẵn: "Dùng material-3 build login form Compose (đã chốt platform, không phải web): email + password fields, `MaterialTheme` + tonal pairing đúng, audit 10 hạng mục sau build."

### Pitfalls
- Build/audit mà chưa chốt platform (brief web mặc định Compose — FAIL core).
- Hex cứng/`Color(0x…)`/`border-radius` tay (FAIL tokens — audit bắt bằng grep).
- Trộn `@material/mdc-*` (MD2) với `@material/web` (API không tương thích).
- Barrel import `@material/web` (nổ bundle — import từng module).
- `outline` cho dividers (phải `outline-variant`).
- Shadows thay tonal elevation (MD3 = tonal surface, shadow chỉ khi nền bận).
- Claim Expressive parity trên web (skill đã báo không có — FAIL).
- Quên SSR/hydration với `@material/web` (custom elements cần JS).
- Phone-only, content tràn hinge foldable, text full-width ở 1200dp+ (canonical layouts + max-width 840-1040dp).
- Trích BOM/signatures mà không check docs chính chủ (skill tự báo drift).
- Quote installs/stars cũ (trôi theo tuần — ghi ngày đo; API 504 nên ghi rõ nguồn skills.sh).

### Tham khảo sử dụng (quyết định được + số có trọng số, chốt 08/11/2026)
- Nhận xét sâu: [README repo](https://github.com/hamen/material-3-skill) (fetch full 08/11/2026) — install 3 đường đã test qua các issue (#8 marketplace fix ở v1.1.1) + platform matrix trung thực (Compose primary/Flutter secondary/Web limited + maintenance mode) + mục accuracy tự nhận best-effort drift → xác nhận quyết định: cài theo README, web chỉ làm tới maintenance, signatures check docs chính chủ.
- Nhận xét sâu: [SKILL.md raw ~31KB](https://raw.githubusercontent.com/hamen/material-3-skill/master/skills/material-3/SKILL.md) (fetch full 08/11/2026) — decision tree + token tables + 30+ components + audit procedure/report/grep/scoring + quan hệ frontend-design (system vs direction + Roboto exception) → xác nhận: đủ chi tiết để build/audit thật, không phải stub.
- Nhận xét sâu: [skills.sh 2 trang](https://www.skills.sh/hamen/material-3-skill) (fetch 08/11/2026) — repo 1 skill/3.6K installs + skill 3.6K installs/1.6K★/First Seen Apr 12 2026 + audits Trust Hub Pass/Socket Pass/**Snyk Warn** → xác nhận: scope nhỏ thật (1 skill), Snyk Warn phải đọc chi tiết trước khi cài team-wide.
- Số trung bình có trọng số: 3.6K installs + 1.6K★ (skills.sh 08/11/2026); GitHub API 504 liên tục → `chưa đối chiếu` (ghi rõ). Trọng số: installs hành vi thật > stars hiển thị; cả hai đều thua repo mẹ anomalies (frontend-design 189k★) vì khác quy mô phân phối.
- Tiếng Việt: truy vấn `material 3 skill hamen đánh giá` không trả về review Việt độc lập → `chưa xác minh`.
- Mâu thuẫn: chi tiết kỹ thuật tốt + honesty cao vs installs nhỏ + Snyk Warn + API 504 → phán quyết: dùng build/audit MD3 khi hệ đã chốt, không dùng làm bằng chứng phổ biến; team-wide đợi đọc Snyk Warn + install thử.

### Tham khảo
- Repo: https://github.com/hamen/material-3-skill (README + `skills/material-3/SKILL.md` + 6 references + manifests + `LICENSE` MIT)
- skills.sh: https://www.skills.sh/hamen/material-3-skill (+ `/material-3`)
- Đọc theo thứ tự: README (platform matrix + accuracy + install) → `SKILL.md` (decision tree → tokens → components → platform → patterns → anti-patterns → audit) → references theo câu hỏi → `LICENSE`.
- Đã verify 08/11/2026: fetch README + SKILL.md + LICENSE + skills.sh 2 trang. Chưa chạy thật: install + dùng (WARN); API đối chiếu (504).

### Được dùng ở đâu
- Dùng CHO UI: xem `../../domains/ui/using-material-3.md` (build/theme/audit MD3) — index `../../domains/ui/README.md`.
- Liên quan: taste tự do → `../frontend-design/`; gates → `../hallmark/`; detector/Live → `../impeccable/`; checklist chung → `../web-interface-guidelines/`.

### Quay lại index
- Về `../../domains/ui/README.md` để so sánh định vị với `frontend-design/` + `hallmark/` + `impeccable/`.
- Xem thêm item liên quan: `../frontend-design/` (direction tự do) + `../hallmark/` (gates).

---

## English

### When to use
- Apps/screens in one design system (Material Design 3) with standard tokens: Compose primary (`MaterialTheme`, adaptive, edge-to-edge/insets — full-bleed drawing avoiding system bars/IME), Flutter secondary (`useMaterial3`, `ColorScheme.fromSeed`), limited web (`@material/web` + CSS custom properties).
- Seed-color themes (one seed generating the whole scheme) + dynamic color (Android 12+) + dark mode + 3 contrast levels.
- Scored MD3 compliance audits: 10 categories at 0-10 with reports (Critical/Warnings/Passing + ordered fixes) + quick grep checks.
- Standard token/component lookup while implementing: `md.sys.*` namespace (the standard MD3 token namespace), 30+ components with 3-platform mapping, Expressive platform matrix.

### When to skip
- Free taste outside any system → use `../frontend-design/` (this skill enforces MD3 compliance).
- Hard numeric merge gates beyond MD3 → use `../hallmark/`.
- Detector/hooks/CI/visual Live comparison → use `../impeccable/`.
- Full M3 Expressive on web React/Vue/Svelte → nothing exists (limited maintenance-mode web, no Expressive — hand custom CSS per the skill's `references/`).
- Fast generic (non-MD3) `file:line` checklist passes → use `../web-interface-guidelines/`.

### Install
- Route 1 (recommended, `npx`): `npx --yes skills add hamen/material-3-skill --skill material-3 -y` (source: README, read 08/11/2026).
- Route 2 (Claude Code plugin): `/plugin marketplace add hamen/material-3-skill` then `/plugin install material-3@material-3-skill` (or `claude plugin ...` from shell).
- Route 3 (Codex/manual): `git clone https://github.com/hamen/material-3-skill.git` then symlink `skills/material-3` into the skills dir (source: README).
- Requires: Node for route 1; Claude Code for route 2; git for route 3.
- Verified 08/11/2026: full README + full `SKILL.md` (~31KB) + `LICENSE` (MIT, CWTI Ltd 2026) + 2 skills.sh pages (repo: 1 skill, 3.6K installs; skill: 3.6K installs, 1.6K stars, First Seen Apr 12 2026, Trust Hub Pass/Socket Pass/**Snyk Warn**). GitHub API 504 repeatedly → stars/forks `not cross-checked`. NOT run: real install + use on a sample project (WARN).

### How the item works
- Backing organization: Ivan (`@hamen`, Android dev — source: README Made-by) / repo `https://github.com/hamen/material-3-skill`, MIT (`LICENSE` root), skill v1.1.1 (29/06/2026, releases 1.1.1/1.1.0/1.0.0), release-driven cadence + `CONTRIBUTING.md` keeping Compose-first.
- Core operating method: one multi-file skill (`SKILL.md` + 6 references + marketplace/plugin manifests) — decision tree by platform → tokens/components by table → patterns → anti-patterns → scored 10-category audit. Self-declared *best-effort distillation* (re-distilled from multiple sources) *that may drift* (source: README accuracy section) — signatures/BOMs (API signatures/Bill of Materials) must be checked against canonical docs.
- Per-usecase differences: MD3 builds (platform decision tree + component catalog, [Sub-usecase 1](#sub-usecase-1-md3-builds-with-tokens-and-components--strongest)) vs seed themes (theming + dynamic color, [Sub-usecase 2](#sub-usecase-2-seed-color-themes-dynamic-and-dark)) vs scored audits (procedure + report + grep, [Sub-usecase 3](#sub-usecase-3-10-category-md3-audit-with-scoring)) vs token lookup (tables + Expressive matrix, [Sub-usecase 4](#sub-usecase-4-token-and-component-lookup-with-expressive-matrix)).

### Invariant core
- Every MD3 output goes through tokens (`md.sys.*` / `MaterialTheme` / `ThemeData`); no hardcoded hex, no hand `border-radius` (shape tokens), no MD2+MD3 mixing, no `@material/web` barrel imports (verbatim Anti-Patterns). Violations = off-system.
- Respect the platform matrix: Compose-first for new Expressive/adaptive; limited maintenance-mode web, no Expressive on web — claiming web parity = FAIL.
- Audit by procedure: all 10 categories at 0-10 + correctly formatted report (Critical/Warnings/Passing + ordered fixes) + pass ≥7/warn 4-6/fail ≤3 bars.
- After use, state: target platform + tokens/components used + audit score (if any); otherwise the system was not really used.

### Customizable surface
- Tunables: seed color, brand colors, dynamic/static, light/dark, contrast level, typeface (Roboto/Roboto Flex is the MD3 default — swap on intentional type-scale customization), shape/motion inside tokens, component variants, canonical layout by size class (screen-size classes). Two-level approval: (1) which platform — shortlist Compose/Flutter/web with reasons via the question tool, user picks before building (web Expressive needs hand-custom approval for missing parity); (2) what stays/changes — kept tokens, customized ones, waived versions. Waivers (one-off hardcoded hex, skipping one audit category) must quote the user's explicit ok + reason.
- Relationship with frontend-design when co-enabled (verbatim SKILL.md): MD3 owns the system (tokens/components/layout), frontend-design owns creative direction within bounds; MD3 wins component structure + token usage; Roboto is a valid exception. Never infer the reverse (taste overriding tokens).

### Work split
- Main agent: confirm platform (user picks — never default to Compose on a web brief), decision tree, token/component lookup, table-driven build/theme, audit + grep, present report + fixes.
- Hand browser/human steps to claude as a whole: real-render verification (dynamic color, dark mode, foldables, responsive across 5 size classes, motion) + contrast measurement + screenshots — with URL/source + 10-category checklist + expected output; the agent never asserts render results without real rendering.
- Agent verifies: tokens in the right namespace + no hardcoded hex/`@material/mdc-`/barrel imports + all 10 audit categories + ordered fixes.

### Differentiating positioning
- Vs `../frontend-design/` (Anthropic, 1.1M installs, 189k-star parent repo): different axis — frontend-design gives system-free direction; this skill gives compliant single-system builds + scoring. Pick material-3 over frontend-design for spec-faithful MD3 builds/audits (tokens + components + 0-10 audit); pick frontend-design for off-system strange taste. The two-way relationship is already defined by this SKILL.md (system vs direction + Roboto exception).
- Vs `../hallmark/` (50,558 stars, system + machine gates + sweep): different enforcement — hallmark GENERATES newly gated systems and sweeps clean; this skill APPLIES one existing system (MD3) via lookup + model-run audit, no machine gates. Pick material-3 over hallmark when the system is settled as MD3 and spec + scoring suffice; pick hallmark for newly gated merge-bar systems.
- Honest frame: wins on the repo's only scored-audit design system + lookup-grade token/component tables + honest platform matrix (states exactly what web lacks) + declared drift; loses on machine enforcement (model-run audit), missing web Expressive, 1/3 Snyk Warn, un-cross-checked GitHub API (504), short history (v1.x since 06/2026).

### Coverage map (whole README + SKILL.md scanned 08/11/2026 — ★ strongest first)
- ★ MD3 builds with tokens/components (platform decision tree + component catalog + Compose/Flutter/web patterns): see Sub-usecase 1.
- Seed-color themes + dynamic/dark (theming reference + Theme Builder flow): see Sub-usecase 2.
- Medium: 10-category scored MD3 audit (procedure + report + grep + scoring guide, Compose/Kotlin-Flutter-web): see Sub-usecase 3.
- Medium: token/component/Expressive-matrix lookup (color/type/shape/elevation/motion + 3-platform mapping): see Sub-usecase 4.
- NOT supported → use instead: free taste → `../frontend-design/`; merge gates/sweep → `../hallmark/`; detector/hooks/CI/Live → `../impeccable/`; generic `file:line` checklist → `../web-interface-guidelines/`; React bricks → `../reactbits/`; full web Expressive → hand CSS (nothing has it).

### Decision dossier
- Jobs SERVED (4, concrete): 1. spec-faithful MD3 apps/screens (especially Compose/Flutter); 2. seed + dynamic/dark themes; 3. 10-category scoring compliance audits; 4. standard token/component/motion lookup while implementing.
- Jobs NOT served (5, each with its replacement): 1. free taste → `../frontend-design/`; 2. merge gates → `../hallmark/`; 3. detector/Live → `../impeccable/`; 4. generic checklist → `../web-interface-guidelines/`; 5. full web Expressive → hand custom (the skill reports the missing parity).
- Free / total + price: $0 everything, MIT (`LICENSE` root, CWTI Ltd 2026, fetched 08/11/2026). Total cost = $0 + model fees.
- Install friction: 1 line to the skill (`npx` route) = standard; marketplace 2 commands; manual 3 steps. Ran 08/11/2026: README + SKILL.md + LICENSE + 2 skills.sh page fetches. NOT run: real install + use (WARN). Barriers: Node/git/Claude Code per route; GitHub API 504 (numbers un-cross-checked); unread Snyk Warn detail; self-reported drift (signatures/BOMs need canonical-doc checks).
- Viral same-segment opponents: `../frontend-design/` (1.1M installs, free Anthropic taste) vs canonical `m3.material.io` docs + `material-web` repo (ground truth, free).
- Pick it over opponents when: short spec-faithful single-system MD3 builds/audits. Choice-flipping example: Compose app needing MaterialTheme + audit → material-3; strange-taste landing → frontend-design; gated-merge output → Hallmark.
- NEVER use when: full web Expressive is required (does not exist); machine enforcement is required (model-run audit); quoting signatures/BOMs without canonical-doc checks (the skill itself warns of drift).

### Sub-usecase 1: MD3 builds with tokens and components (★ strongest)
- When to use: a target platform exists (Compose/Flutter/web) + spec-faithful MD3 UI is needed.
- When to skip: free taste needed (→ `../frontend-design/`); gates needed (→ `../hallmark/`).
- Copy-paste command: `npx --yes skills add hamen/material-3-skill --skill material-3 -y` (install once) then prompt the agent `/material-3 scaffold Create a responsive app shell with navigation` (with platform target).
- Numeric bar: platform settled (user picked); components match platform mapping (Compose `Button`/`Scaffold`, web `md-*-*` verified in catalog); `md.sys.*` token namespace; no hardcoded hex/`@material/mdc-`/barrel imports; web Expressive limits stated.
- Input-output example (illustrative, never the default — platform picked by the user first): "Compose app shell + adaptive nav rail" → `Scaffold` + `NavigationBar`/rail by size class + `MaterialTheme` + edge-to-edge insets.
- Own pitfalls: defaulting to Compose on a web brief (platform needs user pick — core FAIL); claiming web Expressive parity (the skill reports none); importing all of `@material/web`.
- Work split: main agent confirms platform → decision tree → builds; claude verifies real rendering (5 size classes, foldables); verify via tokens + screenshots.

### Sub-usecase 2: seed-color themes, dynamic and dark
- When to use: a seed/brand color exists, light/dark/dynamic schemes + contrast levels needed.
- When to skip: theme exists (build straight in Sub-usecase 1); checks only (Sub-usecase 3).
- Copy-paste command: `/material-3 theme Generate a theme from seed color #1A73E8` (state dynamic vs static + contrast level).
- Numeric bar: complete light/dark schemes (+ dynamic on Android 12+ API 31+ when enabled); correct tonal pairing (`onX` on `X`); component/UI contrast 3:1 large text/borders, 4.5:1 normal text (re-measured in Sub-usecase 3).
- Input-output example (illustrative): seed `#1A73E8` + dynamic + dark → light/dark schemes + `dynamicLightColorScheme`/`dynamicDarkColorScheme` (API 31+) or static fallback.
- Own pitfalls: dynamic color without checking API 31+/user setting (crashes/lost color — check `Build.VERSION.SDK_INT`); arbitrary tonal pairing (breaks contrast in high-contrast mode).
- Work split: main agent generates schemes; claude measures real contrast + light/dark screenshots; verify via schemes + numbers.

### Sub-usecase 3: 10-category MD3 audit with scoring
- When to use: a URL/file paths/runnable app needs a compliance score before ship.
- When to skip: generic UI checklist suffices (guidelines); other hard numeric gates needed (→ `../hallmark/`).
- Copy-paste command: `/material-3 audit [URL or file path]` (state stack: Compose-Kotlin/Flutter/web).
- Numeric bar: all 10 categories at 0-10 + correctly formatted report (Critical 0-3 with `file:line` + fixes, Warnings 4-6, Passing 7-10, ordered fixes); pass ≥7/warn 4-6/fail ≤3 bars; grep checks run (`Color(0x`, hardcoded hex, `@material/mdc-`).
- Input-output example (illustrative): web-app audit → 82/100 report + Critical (3 hardcoded-hex spots with file:line) + ordered fixes.
- Own pitfalls: auditing from code without rendering (contrast/focus need real measurement — hand to claude); assuming MD3 roles suffice for a11y (SKILL.md requires separate contrast verification).
- Work split: main agent inspects + greps + presents the report; claude measures rendering (contrast, focus, motion, responsive); verify via full 10-category report + numbers.

### Sub-usecase 4: token and component lookup with Expressive matrix
- When to use: mid-implementation lookup of a token/component/motion/platform parity question.
- When to skip: tables memorized (no lookup for its own sake); build decisions needed (Sub-usecase 1).
- Copy-paste command: open `skills/material-3/references/<color-system|component-catalog|typography-and-shape|layout-and-responsive>` per the question (the SKILL.md decision tree points at the file).
- Numeric bar: correct-namespace token + role (`--md-sys-color-primary` for fills, `outline-variant` for dividers not `outline`); correct-variant component; platform parity checked via the Expressive matrix before claiming (state what web lacks).
- Input-output example (illustrative): "which token for dividers" → `outline-variant` (not `outline`) + reason (outline is for important boundaries like text-field borders).
- Own pitfalls: `outline` for dividers; hand `border-radius`; shadows instead of tonal elevation; SSR with `@material/web` forgetting hydration (custom elements need JS).
- Work split: main agent looks up + applies; no claude unless rendering looks off.

### Shared steps
1. Install once (whichever route the user picks — `npx` is fastest).
2. Settle the platform (Compose/Flutter/web — user picks, never default; state web Expressive limits).
3. Decision tree → token/component lookup → table-driven build/theme.
4. 10-category audit + grep → report + ordered fixes.
5. Re-verify render numbers (contrast/focus/responsive) via claude when needed.
6. State platform/tokens/audit-score (core-fidelity).

### Sample prompts
- "Use material-3 to build `<component/app>` for `<platform>`: settle the platform first, look up tokens/components in the right namespace, no hardcoded hex, no MD2 mixing."
- "Use material-3 to theme from seed `<hex>`: dynamic/static + light/dark + contrast level, correct tonal pairing, check API 31+ for dynamic."
- "Use material-3 to audit `<URL|paths>` (stack ...): all 10 categories + report format + grep checks, Critical items with file:line."
- Filled example: "Use material-3 to build a Compose login form (platform settled, not web): email + password fields, `MaterialTheme` + correct tonal pairing, 10-category audit after the build."

### Pitfalls
- Building/auditing before settling the platform (web brief defaulted to Compose — core FAIL).
- Hardcoded hex/`Color(0x…)`/hand `border-radius` (token FAIL — the audit greps for these).
- Mixing `@material/mdc-*` (MD2) with `@material/web` (incompatible APIs).
- `@material/web` barrel imports (bundle bloat — import per module).
- `outline` for dividers (must be `outline-variant`).
- Shadows instead of tonal elevation (MD3 = tonal surface; shadow only on busy backgrounds).
- Claiming web Expressive parity (the skill reports none — FAIL).
- Forgetting SSR/hydration with `@material/web` (custom elements need JS).
- Phone-only layouts, hinge-crossing content, full-width text at 1200dp+ (canonical layouts + 840-1040dp max width).
- Quoting BOMs/signatures without canonical-doc checks (self-reported drift).
- Quoting stale installs/stars (weekly drift — date every measurement; API 504 so cite skills.sh explicitly).

### Usage references (decisive + weighted, pinned 08/11/2026)
- Deep review: [repo README](https://github.com/hamen/material-3-skill) (fetched full 08/11/2026) — 3 tested install routes (incl. the issue-#8 marketplace fix in v1.1.1) + honest platform matrix (Compose primary/Flutter secondary/limited maintenance-mode web) + accuracy section declaring best-effort drift → confirms: install per README, web only to maintenance level, signatures need canonical-doc checks.
- Deep review: [SKILL.md raw ~31KB](https://raw.githubusercontent.com/hamen/material-3-skill/master/skills/material-3/SKILL.md) (fetched full 08/11/2026) — decision tree + token tables + 30+ components + audit procedure/report/grep/scoring + frontend-design relationship (system vs direction + Roboto exception) → confirms: detailed enough to build/audit for real, not a stub.
- Deep review: [skills.sh, 2 pages](https://www.skills.sh/hamen/material-3-skill) (fetched 08/11/2026) — repo 1 skill/3.6K installs + skill 3.6K installs/1.6K stars/First Seen Apr 12 2026 + Trust Hub Pass/Socket Pass/**Snyk Warn** → confirms: genuinely small scope (1 skill), Snyk Warn must be read before team-wide installs.
- Weighted averages: 3.6K installs + 1.6K stars (skills.sh 08/11/2026); GitHub API 504 repeatedly → `not cross-checked` (stated). Weight: real-behavior installs > displayed stars; both trail anomaly-scale distribution (frontend-design 189k★ parent) because distribution differs.
- Vietnamese: query `material 3 skill hamen đánh giá` returns no independent Vietnamese review → `unverified`.
- Conflict: good technical detail + high honesty vs small installs + Snyk Warn + API 504 → verdict: use for MD3 builds/audits once the system is settled, never as popularity evidence; team-wide use waits on Snyk Warn reading + trial install.

### References
- Repo: https://github.com/hamen/material-3-skill (README + `skills/material-3/SKILL.md` + 6 references + manifests + `LICENSE` MIT)
- skills.sh: https://www.skills.sh/hamen/material-3-skill (+ `/material-3`)
- Read order: README (platform matrix + accuracy + install) → `SKILL.md` (decision tree → tokens → components → platform → patterns → anti-patterns → audit) → references per question → `LICENSE`.
- Verified 08/11/2026: README + SKILL.md + LICENSE + 2 skills.sh page fetches. NOT run for real: install + use (WARN); API cross-check (504).

### Where used
- Used FOR UI: see `../../domains/ui/using-material-3.md` (MD3 builds/themes/audits) — index `../../domains/ui/README.md`.
- Related: free taste → `../frontend-design/`; gates → `../hallmark/`; detector/Live → `../impeccable/`; generic checklist → `../web-interface-guidelines/`.

### Back to index
- Back to `../../domains/ui/README.md` to compare positioning vs `../frontend-design/` + `../hallmark/` + `../impeccable/`.
- Related items: `../frontend-design/` (free direction) + `../hallmark/` (gates).
