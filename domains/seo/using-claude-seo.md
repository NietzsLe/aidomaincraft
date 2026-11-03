# using-claude-seo CHO SEO — audit/drift/GEO site bằng agents (CHARTER v9)

> Phần audit SEO của claude-seo KHI DÙNG CHO SEO. Gốc ở `../../items/claude-seo/README.md`.

## Tiếng Việt

### Usecase trong domain này
- ★ Audit full site đa agents (Health Score + plan): xem [Usecase con 1](../../items/claude-seo/README.md#usecase-con-1-audit-full-site).
- Audit 1 trang chuyên sâu (on-page/E-E-A-T/schema/images): xem [Usecase con 2](../../items/claude-seo/README.md#usecase-con-2-audit-1-trang-chuyen-sau).
- GEO/AEO + agent readiness (citability, llms.txt/WebMCP): xem [Usecase con 3](../../items/claude-seo/README.md#usecase-con-3-geoaeo--agent-readiness).
- Drift monitoring + Google APIs report (SQLite + PDF định kỳ): xem [Usecase con 4](../../items/claude-seo/README.md#usecase-con-4-drift--google-apis-report).

### Lệnh mẫu cụ thể (cho SEO)
- Audit full (khớp từng chữ lệnh gốc, trong Claude Code đã cài plugin): `/seo audit https://example.com`. Xem [Usecase con 1](../../items/claude-seo/README.md#usecase-con-1-audit-full-site).
- 1 trang: `/seo page <url>`; technical/content/schema/images/sitemap: `/seo technical|content|schema|images|sitemap <url>`. Xem [Usecase con 2](../../items/claude-seo/README.md#usecase-con-2-audit-1-trang-chuyen-sau).
- GEO: `/seo geo <url>`; agentic: `/seo agentic <url>` (đo), `/seo agentic fix <url>` (draft review-only). Xem [Usecase con 3](../../items/claude-seo/README.md#usecase-con-3-geoaeo--agent-readiness).
- Drift: `/seo drift baseline <url>` → `compare` → `history`; Google: `/seo google pagespeed|gsc|ga4 <url|property>` → `/seo google report full` (PDF). Xem [Usecase con 4](../../items/claude-seo/README.md#usecase-con-4-drift--google-apis-report).

### Lưu ý riêng cho domain
- Chuẩn SEO đo bằng evidence, không bằng cảm giác: mọi finding phải map về lệnh/skill + nguồn (DOM/GSC/PSI) mới đem đi fix; số không creds ghi ước lượng. Xem [Cốt lõi bất biến](../../items/claude-seo/README.md#cot-loi-bat-bien).
- Audit ≠ deploy: schema/llms.txt/draft fix chỉ review; site live của khách thì deploy + re-audit verify sau. Xem [Pitfalls](../../items/claude-seo/README.md#pitfalls).
- Token plan: audit full (5 agents Opus) tốn hơn page check — log scope + business type đã duyệt trước khi chạy; keys extension (DataForSEO/Ahrefs/Ads) do user quyết. Xem [Hồ sơ quyết định](../../items/claude-seo/README.md#ho-so-quyet-dinh).

### Điểm mạnh cốt lõi của item CHO domain này
- Fan-out 19 agents + Health Score + plan xếp thứ tự trong 10–15 phút — thay checklist SEO thủ công theo giờ. Xem [Usecase con 1](../../items/claude-seo/README.md#usecase-con-1-audit-full-site).
- GEO + agentic readiness (citability, llms.txt, WebMCP) — việc tool rank cổ điển không đo. Xem [Usecase con 3](../../items/claude-seo/README.md#usecase-con-3-geoaeo--agent-readiness).
- Drift SQLite 17 rules + Google APIs Tier 0–3 + PDF — đúng việc giữ chuẩn SEO theo thời gian. Xem [Usecase con 4](../../items/claude-seo/README.md#usecase-con-4-drift--google-apis-report).

### Phân công CHO domain này (1 dòng + link, không copy)
- Agent chính check quyền/scope/business type (user pick lệnh + URLs qua question tool) → chạy `/seo ...` + trình score/plan/quotas + xin duyệt fix/deploy/keys; execution trong Claude Code + OAuth/keys do user + review visual giao claude; verify bằng reports + severity + PDF. Chi tiết: [Phân công gốc](../../items/claude-seo/README.md#phan-cong-ai-lam-gi).

### Link về item gốc (3 chiều)
- Gốc: `../../items/claude-seo/README.md` (Usecase 1/2/3/4 / Cài đặt / Định vị / Hồ sơ quyết định / Tham khảo sử dụng).
- Index domain: `./README.md`.
- Ngược tại: `../../items/claude-seo/README.md#duoc-dung-o-dau`.

---

## English

SEO use of claude-seo — agent-driven site audits/drift/GEO. Origin at `../../items/claude-seo/README.md`.

### Usecases in this domain
- ★ Full multi-agent site audit (Health Score + plan): see [Sub-usecase 1](../../items/claude-seo/README.md#sub-usecase-1-full-site-audit).
- Deep single-page audit (on-page/E-E-A-T/schema/images): see [Sub-usecase 2](../../items/claude-seo/README.md#sub-usecase-2-deep-single-page-audit).
- GEO/AEO + agent readiness (citability, llms.txt/WebMCP): see [Sub-usecase 3](../../items/claude-seo/README.md#sub-usecase-3-geoaeo--agent-readiness).
- Drift monitoring + Google APIs reporting (SQLite + periodic PDF): see [Sub-usecase 4](../../items/claude-seo/README.md#sub-usecase-4-drift--google-apis-reporting).

### Concrete commands (for this domain)
- Full audit (word-for-word origin commands, inside Claude Code with the plugin): `/seo audit https://example.com`. See [Sub-usecase 1](../../items/claude-seo/README.md#sub-usecase-1-full-site-audit).
- Single page: `/seo page <url>`; technical/content/schema/images/sitemap: `/seo technical|content|schema|images|sitemap <url>`. See [Sub-usecase 2](../../items/claude-seo/README.md#sub-usecase-2-deep-single-page-audit).
- GEO: `/seo geo <url>`; agentic: `/seo agentic <url>` (measure), `/seo agentic fix <url>` (review-only drafts). See [Sub-usecase 3](../../items/claude-seo/README.md#sub-usecase-3-geoaeo--agent-readiness).
- Drift: `/seo drift baseline <url>` → `compare` → `history`; Google: `/seo google pagespeed|gsc|ga4 <url|property>` → `/seo google report full` (PDF). See [Sub-usecase 4](../../items/claude-seo/README.md#sub-usecase-4-drift--google-apis-reporting).

### Domain-specific notes
- SEO judged by evidence, not feel: every finding maps to a command/skill + source (DOM/GSC/PSI) before fixing; credential-less numbers are estimates. See [Invariant core](../../items/claude-seo/README.md#invariant-core).
- Audit ≠ deploy: schema/llms.txt/fix drafts are review-only; client live sites get deployed + re-audited after. See [Pitfalls](../../items/claude-seo/README.md#pitfalls).
- Plan-token cost: full audits (5 Opus agents) cost more than page checks — log approved scope + business type first; extension keys decided by the user. See [Decision dossier](../../items/claude-seo/README.md#decision-dossier).

### Core strengths FOR this domain
- 19-agent fan-out + Health Score + ranked plan in 10–15 minutes — replaces hours of manual SEO checklists. See [Sub-usecase 1](../../items/claude-seo/README.md#sub-usecase-1-full-site-audit).
- GEO + agentic readiness (citability, llms.txt, WebMCP) — a job classic rank tools cannot measure. See [Sub-usecase 3](../../items/claude-seo/README.md#sub-usecase-3-geoaeo--agent-readiness).
- SQLite drift with 17 rules + Tier 0–3 Google APIs + PDF — exactly the hold-the-standard-over-time SEO job. See [Sub-usecase 4](../../items/claude-seo/README.md#sub-usecase-4-drift--google-apis-reporting).

### Work split FOR this domain (1 line + link, never copied)
- Main agent checks rights/scope/business type (user picks commands + URLs via question tool) → runs `/seo ...` + presents score/plan/quotas + requests fix/deploy/key approval; Claude Code execution + OAuth/keys by the user + visual review to claude; verify via reports + severity + PDF. Details: [origin Work split](../../items/claude-seo/README.md#work-split).

### Links to item origin (3-way)
- Origin: `../../items/claude-seo/README.md` (Sub-usecases 1/2/3/4 / Install / Positioning / Decision dossier / Usage references).
- Domain index: `./README.md`.
- Backlisted at: `../../items/claude-seo/README.md#where-used`.
