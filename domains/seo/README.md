# domains/seo/

## Tiếng Việt

Domain SEO — audit/GEO/drift site bằng agents (Claude Code). Chi tiết gốc ở `items/*/README.md`; dùng CHO SEO thì đọc `using-*.md` tương ứng.

### Bảng điều hướng: việc → item(s)
| Việc cần làm | Item chính (mỗi cái 1 cách) | Item hỗ trợ | Lệnh bắt đầu |
|---|---|---|---|
| Audit full site (technical + content + schema + CWV + plan) | `claude-seo` (fan-out agents — xem `using-claude-seo.md`) | — | `/seo audit <url>` (trong Claude Code đã cài plugin) |
| Audit 1 trang chuyên sâu trước publish | `claude-seo` (depth 1 URL — xem `using-claude-seo.md`) | — | `/seo page <url>` |
| GEO/AEO + agent readiness (AI cite + llms.txt/WebMCP) | `claude-seo` (đo citability — xem `using-claude-seo.md`) | — | `/seo geo <url>` |
| Drift monitoring + Google APIs report định kỳ | `claude-seo` (baseline + PDF — xem `using-claude-seo.md`) | — | `/seo drift baseline <url>` |

Việc audit 1 lần: cần full site + plan → audit; cần soi 1 URL → page. Việc sau audit: cần AI cite → geo/agentic; cần giữ chuẩn theo thời gian → drift + google report.

### Bảng định vị
| Item | Mục đích điển hình | Vận hành tóm tắt 1 câu | Điểm mạnh | Điểm yếu | Dùng chính khi | Tránh khi | Thay thế bởi | Vì sao chọn A thay vì B trong case này |
|---|---|---|---|---|---|---|---|---|
| `claude-seo` — chi tiết SEO ở `using-claude-seo.md`, gốc ở `../../items/claude-seo/README.md` | audit SEO site bằng agents trong Claude Code | 26 skills + 19 agents fan-out + Health Score + plan + drift + Google APIs | bundle audit đầy đủ nhất 1 tác giả, evidence + plan, 25.381★ MIT 0đ, velocity +5,7k★/11d | bắt buộc Claude Code, token plan Opus, creds/API ngoài tự trả | cần audit full/drift/GEO có evidence trong Claude Code | không có Claude Code, cần quét Lighthouse thuần, cần audit 1 lần mọi engine | unlighthouse quét Lighthouse hàng loạt; skill SEO Audit đơn khi cần gọn mọi engine | Chọn claude-seo thay vì skill/quét lẻ khi quyết định phụ thuộc vào audit đầy đủ + plan + drift có evidence, không phải quét 1 chỉ số |

### Ma trận chồng lấn
| Việc | `claude-seo` | Tiêu chí chọn phân biệt |
|---|---|---|
| Audit full site + plan | chính | cần Health Score + plan + evidence → claude-seo; chỉ cần điểm Lighthouse → unlighthouse thay thế |
| Audit 1 trang | chính | cần depth đa lens + drafts → claude-seo; cần audit 1 lần gọn mọi engine → skill SEO Audit đơn thay thế |
| GEO/agentic readiness | chính | cần citability + files cho AI → claude-seo (không hệ đo rank nào thay được việc đo cite) |
| Drift + Google reports | chính | cần baseline + PDF định kỳ → claude-seo; cần dashboard SaaS → tool trả phí ngoài |
| Viết bài mới chuẩn SEO | không dùng | `claude-blog` cùng tác giả (không phải việc của audit) |

### Workflow phối hợp mẫu
Cài plugin (3 lệnh + `/seo setup` + `/seo doctor`) → chạy audit đã duyệt scope (`/seo audit` full hoặc `/seo page` lẻ) → đọc score + plan + evidence → fix theo thứ tự critical trước (draft schema/llms.txt chỉ review, không tự deploy) → re-audit verify → pin drift baseline + Google reports định kỳ. GEO song song khi brief yêu cầu AI cite.

### Danh sách using-doc
- `using-claude-seo.md` — dùng claude-seo CHO SEO → gốc `../../items/claude-seo/README.md`

---

## English

SEO domain — agent-driven site audits/GEO/drift (Claude Code). Origins at `items/*/README.md`; for SEO use read the matching `using-*.md`.

### Routing: job → item(s)
| Job | Primary item(s) (each a different way) | Supporting item | Starter command |
|---|---|---|---|
| Full site audit (technical + content + schema + CWV + plan) | `claude-seo` (agent fan-out — see `using-claude-seo.md`) | — | `/seo audit <url>` (inside Claude Code with the plugin) |
| Deep single-page audit pre-publish | `claude-seo` (1-URL depth — see `using-claude-seo.md`) | — | `/seo page <url>` |
| GEO/AEO + agent readiness (AI citation + llms.txt/WebMCP) | `claude-seo` (citability measurement — see `using-claude-seo.md`) | — | `/seo geo <url>` |
| Drift monitoring + periodic Google API reports | `claude-seo` (baselines + PDF — see `using-claude-seo.md`) | — | `/seo drift baseline <url>` |

One-off audit: full site + plan → audit; single URL → page. After audit: AI citation → geo/agentic; holding the standard over time → drift + google report.

### Positioning
| Item | Typical purposes | 1-sentence operating summary | Strengths | Weaknesses | Use as primary when | Avoid when | Replaced by | Why pick A over B in this case |
|---|---|---|---|---|---|---|---|---|
| `claude-seo` — SEO details in `using-claude-seo.md`, origin at `../../items/claude-seo/README.md` | agent-driven SEO audits in Claude Code | 26 skills + 19 agents fan-out + Health Score + plan + drift + Google APIs | most complete single-author audit bundle, evidence + plan, 25,381 stars $0 MIT, +5.7k stars/11d velocity | Claude Code mandatory, Opus plan tokens, external creds/APIs self-paid | full/drift/GEO audits with evidence inside Claude Code are needed | no Claude Code, pure bulk Lighthouse, one-shot any-engine audit | unlighthouse for bulk Lighthouse; single SEO Audit skill for lean any-engine | Pick claude-seo over single skills/scans when full audits + plans + drift with evidence decide, not one metric |

### Overlap matrix
| Job | `claude-seo` | Distinguishing selection rule |
|---|---|---|
| Full site audit + plan | primary | Health Score + plan + evidence → claude-seo; Lighthouse scores only → unlighthouse instead |
| Single-page audit | primary | multi-lens depth + drafts → claude-seo; lean one-shot any-engine → single SEO Audit skill instead |
| GEO/agentic readiness | primary | citability + AI files → claude-seo (no rank tool measures citation) |
| Drift + Google reports | primary | baselines + periodic PDF → claude-seo; SaaS dashboards → paid external tools |
| New SEO-first articles | do-not-use | `claude-blog` by the same author (not an audit job) |

### Sample combined workflow
Install the plugin (3 commands + `/seo setup` + `/seo doctor`) → run the approved-scope audit (`/seo audit` full or `/seo page` single) → read score + plan + evidence → fix critical-first (schema/llms.txt drafts are review-only, never self-deployed) → re-audit to verify → pin drift baselines + periodic Google reports. GEO in parallel when the brief needs AI citation.

### Using-doc list
- `using-claude-seo.md` — claude-seo FOR SEO → origin `../../items/claude-seo/README.md`
