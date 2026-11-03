# using-rea CHO reverse — hiểu app/binary/website có evidence (CHARTER v9)

> Phần reverse của rea KHI DÙNG CHO reverse. Gốc ở `../../items/rea/README.md`.

## Tiếng Việt

### Usecase trong domain này
- ★ Phân tích native qua provider (pseudocode/trace + snapshot): xem [Usecase con 2](../../items/rea/README.md#usecase-con-2-phan-tich-native-qua-provider-co-evidence).
- Phân tích tĩnh JS/Electron không engine: xem [Usecase con 1](../../items/rea/README.md#usecase-con-1-phan-tich-tinh-jselectron-khong-can-engine).
- Quan sát website/runtime 1 flow: xem [Usecase con 3](../../items/rea/README.md#usecase-con-3-quan-sat-website--runtime-hanh-vi).
- Inventory tĩnh offline (managed/APK/firmware/model): xem [Usecase con 4](../../items/rea/README.md#usecase-con-4-inventory-tinh-offline-managedapkfirmwaremodel).

### Lệnh mẫu cụ thể (cho reverse)
- Setup + kiểm tra (khớp từng chữ lệnh gốc): `npx rea-agents setup` rồi `rea doctor --json` (scoped: `rea doctor --provider ghidra --json`). Xem [Cài đặt](../../items/rea/README.md#cai-dat).
- JS/Electron tĩnh: `npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json`. Xem [Usecase con 1](../../items/rea/README.md#usecase-con-1-phan-tich-tinh-jselecron-khong-can-engine).
- Native: `rea providers --json` rồi `rea analyze /absolute/path/to/program --provider ghidra --json` (+ `search`/`function`/`decompile`/`xrefs`/`trace`, snapshot `--snapshot PATH`). Xem [Usecase con 2](../../items/rea/README.md#usecase-con-2-phan-tich-native-qua-provider-co-evidence).
- Web/runtime: `rea capture-browser-scenario` / `rea capture-web-screenshot` / `rea analyze-web-bundle` trong origin scope đã duyệt. Xem [Usecase con 3](../../items/rea/README.md#usecase-con-3-quan-sat-website--runtime-hanh-vi).
- Inventory: `rea inspect-managed-artifact /absolute/path/Assembly.dll --json` (+ `--type` cho members), `rea inspect-go-binary <bin> --json`, `rea inspect-model-artifact model.gguf --json`. Xem [Usecase con 4](../../items/rea/README.md#usecase-con-4-inventory-tinh-offline-managedapkfirmwaremodel).

### Lưu ý riêng cho domain
- Phân biệt với universal-modder: brief reverse cần hiểu 1 feature bất kỳ có evidence → rea chính; cần mod game tới chạy thật + assets + clip + note → universal-modder chính (rea làm bước đọc code thật trong vòng mod). Xem [Định vị](../../items/rea/README.md#dinh-vi-khac-biet-so-lieu-ngay-01112026-tru-khi-ghi-khac).
- Quyền/ToS/license check trước mỗi target (sở hữu/cho phép/học; site cấm automated access thì dừng; Hopper/IDA/JEB tự mua license); terminal chỉ tóm tắt — mở Evidence file verify full. Xem [Cốt lõi bất biến](../../items/rea/README.md#cot-loi-bat-bien).
- Engine nặng + Node patch-gap: Node phải đúng `^22.23.4/24.22.1/26.12.1` (máy v24.22.0 gặp `EBADENGINE` 01/11/2026); Linux cần `ps` procps; provider/browser tải/cài riêng.

### Điểm mạnh cốt lõi của item CHO domain này
- 1 MCP phủ ~30 loại target (JS/native/web/.NET/APK/firmware/model) + evidence chuẩn Seen/Inferred/Unknown — việc universal-modder/dembrandt/cloner đều không làm. Xem [Usecase con 2](../../items/rea/README.md#usecase-con-2-phan-tich-native-qua-provider-co-evidence) + [Bản đồ phủ](../../items/rea/README.md#ban-do-phu-usecase).
- Decompile → hiểu → tái tạo có kiểm chứng (3.205 case DX-Ball, Notion bridge, TH04) — đúng việc "app mình thích thành spec" của reverse. Xem [Hồ sơ quyết định](../../items/rea/README.md#ho-so-quyet-dinh).
- Local-first + 0đ core MIT (1,17M tải/tháng) — đúng việc thử nhanh không vendor lock-in. Xem [Tham khảo sử dụng](../../items/rea/README.md#tham-khao-su-dung-so-chot-01112026).

### Phân công CHO domain này (1 dòng + link, không copy)
- Agent chính check quyền/scope (user pick target + provider + scope 1 feature qua question tool) → chạy setup/CLI/MCP + trình evidence/unknowns + xin duyệt rebuild; bước browser visible/engine interactive + review visual mắt người giao claude; verify bằng Evidence + snapshot + rebuild test. Chi tiết: [Phân công gốc](../../items/rea/README.md#phan-cong-ai-lam-gi).

### Link về item gốc (3 chiều)
- Gốc: `../../items/rea/README.md` (Usecase 1/2/3/4 / Cài đặt / Định vị / Hồ sơ quyết định / Tham khảo sử dụng).
- Index domain: `./README.md`.
- Ngược tại: `../../items/rea/README.md#duoc-dung-o-dau`.

---

## English

Reverse use of rea — evidence-backed app/binary/website understanding. Origin at `../../items/rea/README.md`.

### Usecases in this domain
- ★ Provider-backed native analysis (pseudocode/trace + snapshots): see [Sub-usecase 2](../../items/rea/README.md#sub-usecase-2-provider-backed-native-analysis-with-evidence).
- Engine-free static JS/Electron analysis: see [Sub-usecase 1](../../items/rea/README.md#sub-usecase-1-engine-free-static-jselectron-analysis).
- One-flow website/runtime observation: see [Sub-usecase 3](../../items/rea/README.md#sub-usecase-3-website--runtime-behavior-observation).
- Offline static inventories (managed/APK/firmware/models): see [Sub-usecase 4](../../items/rea/README.md#sub-usecase-4-offline-static-inventories-managedapkfirmwaremodels).

### Concrete commands (for this domain)
- Setup + checks (word-for-word origin commands): `npx rea-agents setup`, then `rea doctor --json` (scoped: `rea doctor --provider ghidra --json`). See [Install](../../items/rea/README.md#install).
- Static JS/Electron: `npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json`. See [Sub-usecase 1](../../items/rea/README.md#sub-usecase-1-engine-free-static-jselectron-analysis).
- Native: `rea providers --json`, then `rea analyze /absolute/path/to/program --provider ghidra --json` (plus `search`/`function`/`decompile`/`xrefs`/`trace`, snapshots via `--snapshot PATH`). See [Sub-usecase 2](../../items/rea/README.md#sub-usecase-2-provider-backed-native-analysis-with-evidence).
- Web/runtime: `rea capture-browser-scenario` / `rea capture-web-screenshot` / `rea analyze-web-bundle` inside the approved origin scope. See [Sub-usecase 3](../../items/rea/README.md#sub-usecase-3-website--runtime-behavior-observation).
- Inventories: `rea inspect-managed-artifact /absolute/path/Assembly.dll --json` (plus `--type` for members), `rea inspect-go-binary <bin> --json`, `rea inspect-model-artifact model.gguf --json`. See [Sub-usecase 4](../../items/rea/README.md#sub-usecase-4-offline-static-inventories-managedapkfirmwaremodels).

### Domain-specific notes
- Vs universal-modder: reverse briefs needing any one feature with evidence → rea primary; game mods to live + assets + clip + note → universal-modder primary (rea powers its code-reading step). See [Positioning](../../items/rea/README.md#differentiating-positioning-numbers-as-of-01112026-unless-noted).
- Rights/ToS/license checks before every target (owned/permitted/learning; stop when automated access is banned; self-licensed Hopper/IDA/JEB); terminal shows summaries only — open Evidence files for the full record. See [Invariant core](../../items/rea/README.md#invariant-core).
- Heavy engines + Node patch gaps: Node must match `^22.23.4/24.22.1/26.12.1` (this machine's v24.22.0 hit `EBADENGINE` on 01/11/2026); Linux needs a procps-compatible `ps`; providers/browsers install separately.

### Core strengths FOR this domain
- One MCP over ~30 target kinds (JS/native/web/.NET/APK/firmware/models) + standard Seen/Inferred/Unknown evidence — a job universal-modder/dembrandt/cloner all skip. See [Sub-usecase 2](../../items/rea/README.md#sub-usecase-2-provider-backed-native-analysis-with-evidence) + [Coverage map](../../items/rea/README.md#coverage-map).
- Verified decompile → understand → recreate (3,205 DX-Ball cases, Notion bridge, TH04) — exactly the reverse "liked app becomes the spec" job. See [Decision dossier](../../items/rea/README.md#decision-dossier).
- Local-first + $0 MIT core (1.17M downloads/month) — exactly the try-fast-without-lock-in reverse job. See [Usage references](../../items/rea/README.md#usage-references-numbers-pinned-01112026).

### Work split FOR this domain (1 line + link, never copied)
- Main agent checks rights/scope (user picks target + provider + one-feature scope via question tool) → runs setup/CLI/MCP + presents evidence/unknowns + requests rebuild approval; browser-visible/interactive-engine steps + human visual review go to claude; verify via Evidence + snapshots + rebuild tests. Details: [origin Work split](../../items/rea/README.md#work-split).

### Links to origin (3-way)
- Origin: `../../items/rea/README.md` (Sub-usecases 1/2/3/4 / Install / Positioning / Decision dossier / Usage references).
- Domain index: `./README.md`.
- Backlisted at: `../../items/rea/README.md#where-used`.
