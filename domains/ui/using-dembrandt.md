# using-dembrandt CHO UI — audit tokens/drift/WCAG site sống + exports (CHARTER v9)

> Phần audit tokens của dembrandt KHI DÙNG CHO UI. Gốc ở `../../items/dembrandt/README.md`.

## Tiếng Việt

### Usecase trong domain này
- ★ Extract 1 URL ra tokens quan sát được (JSON/DTCG/DESIGN.md) cho audit UI: xem [Usecase con 1](../../items/dembrandt/README.md#usecase-con-1-extract-1-url-ra-tokens).
- Crawl nhiều trang gộp confidence (cross-page audit): xem [Usecase con 2](../../items/dembrandt/README.md#usecase-con-2-crawl-nhieu-trang-gop-confidence).
- Drift gate CI (pin baseline, fail PR khi tokens trôi): xem [Usecase con 3](../../items/dembrandt/README.md#usecase-con-3-drift-gate-ci).
- WCAG contrast cặp DOM thật + export Tailwind/shadcn/DESIGN.md/brand-guide cho agent: xem [Usecase con 4](../../items/dembrandt/README.md#usecase-con-4-wcag--export-cho-agent).

### Lệnh mẫu cụ thể (cho UI)
- Extract 1 URL (khớp từng chữ lệnh gốc): `dembrandt dembrandt.com --json-only`; ghi file: `dembrandt dembrandt.com --save-output`; chuẩn W3C: `dembrandt dembrandt.com --dtcg`. Xem [Usecase con 1](../../items/dembrandt/README.md#usecase-con-1-extract-1-url-ra-tokens).
- Crawl audit: `dembrandt dembrandt.com --crawl 5`; sitemap: `dembrandt dembrandt.com --sitemap`. Xem [Usecase con 2](../../items/dembrandt/README.md#usecase-con-2-crawl-nhieu-trang-gop-confidence).
- Gate CI: `dembrandt https://preview.example.com --compare .dembrandt/baseline.json --json-only` (exit 1 = drift). Xem [Usecase con 3](../../items/dembrandt/README.md#usecase-con-3-drift-gate-ci).
- WCAG + theme: `dembrandt dembrandt.com --wcag`; `dembrandt dembrandt.com --tailwind`; `dembrandt dembrandt.com --shadcn`; `dembrandt dembrandt.com --design-md`. Xem [Usecase con 4](../../items/dembrandt/README.md#usecase-con-4-wcag--export-cho-agent).

### Lưu ý riêng cho domain
- Phân biệt với Hallmark: brief UI cần tokens/drift/WCAG của site có sẵn (có quyền) → dembrandt chính; cần system mới pass gates → hallmark chính (dembrandt đo cái đã render, không sinh system). Tokens dembrandt về muốn thành system chuẩn thì sweep lại bằng hallmark. Xem [Định vị](../../items/dembrandt/README.md#dinh-vi-khac-biet-so-lieu-ngay-02112026-tru-khi-ghi-khac).
- Phân biệt với cloner: cần tokens + gate nhanh (~10s, 0đ) → dembrandt; cần app Next.js chạy được → cloner (Map→Observe→Build→Compare, chậm/đắt).
- Quyền/ToS/robots check trước mỗi URL (sở hữu/cho phép/học); terminal chỉ high/medium confidence — mở JSON verify full. Xem [Cốt lõi bất biến](../../items/dembrandt/README.md#cot-loi-bat-bien).

### Điểm mạnh cốt lõi của item CHO domain này
- Đo thật production đang render (computed styles/DOM, không phải spec) + exports chuẩn DTCG/DESIGN.md/Tailwind/shadcn observed-only — việc hallmark/skillry/reactbits/cloner đều không làm. Xem [Usecase con 1](../../items/dembrandt/README.md#usecase-con-1-extract-1-url-ra-tokens) + [Usecase con 4](../../items/dembrandt/README.md#usecase-con-4-wcag--export-cho-agent).
- Drift gate CI (exit code + annotations + App snapshots) — đúng việc "giữ system không trôi sau mỗi release" của UI. Xem [Usecase con 3](../../items/dembrandt/README.md#usecase-con-3-drift-gate-ci).
- WCAG trên cặp DOM thật kèm states — đúng việc audit a11y UI. Xem [Usecase con 4](../../items/dembrandt/README.md#usecase-con-4-wcag--export-cho-agent).

### Phân công CHO domain này (1 dòng + link, không copy)
- Agent chính check quyền/scope/format (user pick URLs + crawl/gate/exports qua question tool) → chạy CLI/MCP + trình tokens/diff/WCAG + xin duyệt `--approve`; bước browser visible/`--login` + review visual mắt người giao claude; verify bằng files + exit code + annotations. Chi tiết: [Phân công gốc](../../items/dembrandt/README.md#phan-cong-ai-lam-gi).

### Link về item gốc (3 chiều)
- Gốc: `../../items/dembrandt/README.md` (Usecase 1/2/3/4 / Cài đặt / Định vị / Hồ sơ quyết định / Tham khảo sử dụng).
- Index domain: `./README.md`.
- Ngược tại: `../../items/dembrandt/README.md#duoc-dung-o-dau`.

---

## English

UI use of dembrandt — live-site token audit/drift/WCAG + exports. Origin at `../../items/dembrandt/README.md`.

### Usecases in this domain
- ★ Single-URL observed-token extraction (JSON/DTCG/DESIGN.md) for UI audits: see [Sub-usecase 1](../../items/dembrandt/README.md#sub-usecase-1-single-url-token-extraction).
- Multi-page crawl with merged confidence: see [Sub-usecase 2](../../items/dembrandt/README.md#sub-usecase-2-multi-page-crawl-with-merged-confidence).
- CI drift gate (pinned baseline, fail PRs on drift): see [Sub-usecase 3](../../items/dembrandt/README.md#sub-usecase-3-ci-drift-gate).
- Real-DOM WCAG + Tailwind/shadcn/DESIGN.md/brand-guide exports: see [Sub-usecase 4](../../items/dembrandt/README.md#sub-usecase-4-wcag--agent-exports).

### Concrete commands (for this domain)
- Extract one URL (word-for-word origin commands): `dembrandt dembrandt.com --json-only`; persist: `dembrandt dembrandt.com --save-output`; W3C: `dembrandt dembrandt.com --dtcg`. See [Sub-usecase 1](../../items/dembrandt/README.md#sub-usecase-1-single-url-token-extraction).
- Crawl: `dembrandt dembrandt.com --crawl 5`; sitemap: `dembrandt dembrandt.com --sitemap`. See [Sub-usecase 2](../../items/dembrandt/README.md#sub-usecase-2-multi-page-crawl-with-merged-confidence).
- CI gate: `dembrandt https://preview.example.com --compare .dembrandt/baseline.json --json-only` (exit 1 = drift). See [Sub-usecase 3](../../items/dembrandt/README.md#sub-usecase-3-ci-drift-gate).
- WCAG + theme: `dembrandt dembrandt.com --wcag`; `dembrandt dembrandt.com --tailwind`; `dembrandt dembrandt.com --shadcn`; `dembrandt dembrandt.com --design-md`. See [Sub-usecase 4](../../items/dembrandt/README.md#sub-usecase-4-wcag--agent-exports).

### Domain-specific notes
- Vs Hallmark: UI briefs needing tokens/drift/WCAG of an existing permitted site → dembrandt primary; new gated systems → hallmark primary (dembrandt measures rendered output, generates no system). Sweep dembrandt tokens with hallmark to standardize. See [Positioning](../../items/dembrandt/README.md#differentiating-positioning-numbers-as-of-02112026-unless-noted).
- Vs cloner: fast tokens + gates (~10s, $0) → dembrandt; runnable Next.js app → cloner (slow/costly 4-step rebuild).
- Rights/ToS/robots check before every URL; terminal shows high/medium confidence only — open JSON for full. See [Invariant core](../../items/dembrandt/README.md#invariant-core).

### Core strengths FOR this domain
- Real production measurement (computed styles/DOM, not specs) + standard DTCG/DESIGN.md/Tailwind/shadcn observed-only exports — a job hallmark/skillry/reactbits/cloner all skip. See [Sub-usecase 1](../../items/dembrandt/README.md#sub-usecase-1-single-url-token-extraction) + [Sub-usecase 4](../../items/dembrandt/README.md#sub-usecase-4-wcag--agent-exports).
- CI drift gate (exit codes + annotations + App snapshots) — exactly the UI "keep the system from drifting per release" job. See [Sub-usecase 3](../../items/dembrandt/README.md#sub-usecase-3-ci-drift-gate).
- WCAG on real DOM pairs with states — exactly the UI a11y-audit job. See [Sub-usecase 4](../../items/dembrandt/README.md#sub-usecase-4-wcag--agent-exports).

### Work split FOR this domain (1 line + link, never copied)
- Main agent checks rights/scope/format (user picks URLs + crawl/gate/exports via question tool) → runs CLI/MCP + presents tokens/diffs/WCAG + requests `--approve`; browser-visible/`--login` steps + human visual review go to claude; verify via files + exit codes + annotations. Details: [origin Work split](../../items/dembrandt/README.md#work-split).

### Links to origin (3-way)
- Origin: `../../items/dembrandt/README.md` (Sub-usecases 1/2/3/4 / Install / Positioning / Decision dossier / Usage references).
- Domain index: `./README.md`.
- Backlisted at: `../../items/dembrandt/README.md#where-used`.
