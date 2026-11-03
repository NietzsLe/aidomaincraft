# domains/ui/

## Tiếng Việt

Domain UI — dùng item nào CHO UI thì đọc `using-*.md` tương ứng (phần riêng UI + link về gốc). Chi tiết gốc sống trong `items/*/README.md`; index này chỉ điều hướng + định vị.

### Bảng điều hướng: việc → item(s)
| Việc cần làm | Item chính (mỗi cái 1 cách) | Item hỗ trợ | Lệnh bắt đầu |
|---|---|---|---|
| Build trang mới / redesign / audit có system + gates | `hallmark` (system + gates — xem `using-hallmark.md`) | `reactbits` cho hiệu ứng lẻ | `/hallmark <prompt>` |
| Hiệu ứng React có sẵn (text/background/micro/card) | `reactbits` (bricks sở hữu source — xem `using-reactbits.md`) | `hallmark` để sweep sau khi lắp | `npx shadcn@latest add @react-bits/SplitText-TS-TW` |
| Landing mẫu có sẵn (phần web của Skillry) | `skillry` (taste đóng gói — xem `using-skillry.md`) + `hallmark` (system chuẩn — xem `using-hallmark.md`) | `hallmark` sweep lại sau khi lấy output | paste vào agent: `Read https://skillry.dev/skills/bs-mint-noir-saas-site/install.md and follow the instructions to install the skill.` |
| Rebuild/migrate site có sẵn 1:1 thành Next.js (có quyền, giữ pathnames) | `ai-website-cloner-template` (clone sống — xem `using-ai-website-cloner-template.md`) | `hallmark` sweep phần custom mới | `/clone-website <url1> [<url2> ...]` (agent có browser) |
| Audit tokens/drift/WCAG site sống (có quyền) + exports DTCG/Tailwind/shadcn | `dembrandt` (đo thật + gate CI — xem `using-dembrandt.md`) | `hallmark` sweep tokens thành system chuẩn | `dembrandt <url> --save-output` (+ `--compare` cho gate) |
| Review/audit UI code có sẵn ra `file:line` (React/Next.js, cần mạng fetch rules) | `web-interface-guidelines` (checklist 130 rules — xem `using-web-interface-guidelines.md`) | `hallmark` sửa system khi findings thuộc về system | `Review my UI: src/components/CheckoutForm.tsx` (skill `web-design-guidelines`) |

Việc landing mẫu có 2 chính: cần taste có sẵn nhanh → Skillry; cần system pass gates → Hallmark. Tiêu chí phân biệt ở ma trận dưới. Việc rebuild site sống: cần giống hệt URL (có quyền) → cloner; cần system mới → Hallmark. Việc audit tokens/drift: cần đo thật + gate CI → dembrandt; cần system mới → Hallmark. Việc review code UI có sẵn: cần 1 pass checklist nhanh ra `file:line` → web-interface-guidelines; findings thuộc về system (tokens/shape/hero) → Hallmark sửa.

### Bảng định vị
| Item | Mục đích điển hình | Vận hành tóm tắt 1 câu | Điểm mạnh | Điểm yếu | Dùng chính khi | Tránh khi | Thay thế bởi | Vì sao chọn A thay vì B trong case này |
|---|---|---|---|---|---|---|---|---|---|
| `hallmark` — chi tiết UI ở `using-hallmark.md`, gốc ở `../../items/hallmark/README.md` | full page system, taste, chống AI-slop | Gates máy + scaffold tokens + deal theme + hero-first + sweep render | Floor/gates quét máy, 10 job anatomy, hero-first + review lạnh | không có bricks animated sẵn | cần system/design chuẩn, output phải pass gates | sửa logic thuần, tweak nhỏ giữ system | sửa tay; v0/Lovable khi cần draft nhanh | Chọn Hallmark thay vì Skillry-web khi quyết định phụ thuộc vào pass gates (contrast/focus/fold/word budget), không phải taste có sẵn |
| `reactbits` — chi tiết UI ở `using-reactbits.md`, gốc ở `../../items/reactbits/README.md` | bricks animated sở hữu source | Copy source theo variant qua CLI/MCP, tune live rồi export | 215+ component, 4 biến thể, MCP + Studio/Lab | không tokens/gates/review, chỉ React | cần 1 effect/component React cụ thể | project phi React, a11y/perf nghiêm | Motion/GSAP khi cần engine thuần | Chọn React Bits thay vì Hallmark khi cần brick hiệu ứng lẻ có demo + variant, không phải system |
| `skillry` (phần web) — chi tiết UI ở `using-skillry.md`, gốc ở `../../items/skillry/README.md` | landing mẫu chạy ngay | Skill SKILL.md + preview thật, render HTML tĩnh | taste đóng gói (Mint Noir free...), 3 đường cài, hỗ trợ OpenCode | 40/617 free + cần tài khoản, không system/gates | cần đúng 1 taste landing có sẵn, chấp nhận trả phí | cần system pass gates, cần bricks React | Hallmark khi cần system; free builder khi tự ráp được | Chọn Skillry-web thay vì Hallmark khi cần taste Mint/Cadence đóng gói + quy trình hướng dẫn; engine free thắng về capability |
| `ai-website-cloner-template` — chi tiết UI ở `using-ai-website-cloner-template.md`, gốc ở `../../items/ai-website-cloner-template/README.md` | rebuild/migrate site sống 1:1 thành Next.js | Skill clone-website 4 bước Map/Observe/Build/Compare + `npm run check` | giống hệt URL sống + route map + compare + check xanh, 38,004★ MIT 0đ template | cần quyền/ToS + browser + Node 24 + tiền token Opus, copy không system/gates | cần giống hệt site sống (mất source/chuyển nền tảng) | system mới, taste đóng gói, clone không quyền | Hallmark khi cần system mới; Skillry-web khi cần taste sẵn | Chọn cloner thay vì Hallmark khi quyết định phụ thuộc vào giống hệt URL sống, không phải system mới |
| `dembrandt` — chi tiết UI ở `using-dembrandt.md`, gốc ở `../../items/dembrandt/README.md` | audit tokens/drift/WCAG site sống + exports | CLI đo computed styles/DOM + DTCG/DESIGN.md/Tailwind/shadcn + `--compare` gate CI | đo thật production + drift CI/Action/App + WCAG đôi DOM thật, 3.902★ MIT 0đ CLI | cần quyền/ToS/robots + Node 18 + browser tải riêng, đo ≠ sinh system | cần tokens/drift/WCAG site có sẵn, gate mỗi release | system mới từ 0, app chạy được, site không quyền | Hallmark khi cần system mới; cloner khi cần app chạy được | Chọn dembrandt thay vì Hallmark khi quyết định phụ thuộc vào tokens/drift quan sát được, không phải system mới |
| `web-interface-guidelines` — chi tiết UI ở `using-web-interface-guidelines.md`, gốc ở `../../items/web-interface-guidelines/README.md` | review/audit UI code có sẵn ra `file:line` | Skill fetch `command.md` tươi + check 104 rules + in findings terse | 130 rules checklist, 0đ MIT, ~815k installs, 1 bước cài, không đổi file | cần mạng fetch rules mỗi review, audit không sinh system | code UI đã có cần 1 pass soi nhanh trước merge | sinh system/gates, bricks React, offline | Hallmark khi cần system mới; React Bits khi cần bricks | Chọn guidelines thay vì Hallmark khi quyết định phụ thuộc vào findings checklist nhanh (`aria-label`, `transition: all`, `…`), không phải system mới |

### Ma trận chồng lấn
| Việc | `hallmark` | `reactbits` | `skillry` (web) | `ai-website-cloner-template` | `dembrandt` | `web-interface-guidelines` | Tiêu chí chọn phân biệt |
|---|---|---|---|---|---|---|---|
| Trang mới cần system chuẩn | chính | hỗ trợ (1-2 effect) | không dùng | không dùng | không dùng | không dùng (generate theo AGENTS.md được, nhưng không sinh system) | pass gates → Hallmark; Skillry-web không có gates |
| 1 hiệu ứng/component lẻ React | không dùng | chính | không dùng | không dùng | không dùng | không dùng | brick sở hữu source → React Bits |
| Redesign/audit giữ content + wiring | chính | không dùng | không dùng | hỗ trợ (khi mất source/repo — rebuild từ URL sống; còn repo thì Hallmark) | hỗ trợ (đo tokens hiện tại làm đầu vào audit; còn repo thì Hallmark) | hỗ trợ (soi checklist `file:line` trước khi redesign; còn repo + wiring thì Hallmark) | còn repo + wiring → Hallmark; mất source → cloner; cần số đo tokens → dembrandt hỗ trợ; cần list lỗi nhanh → guidelines hỗ trợ |
| Page có system, thiếu motion | hỗ trợ (sweep lại) | chính | không dùng | không dùng | không dùng | không dùng | thiếu motion → React Bits lắp, Hallmark sweep lại |
| Landing mẫu có sẵn | chính (system chuẩn) | không dùng | chính (taste sẵn) | thay thế (clone URL tùy ý khi có quyền — khác taste đóng gói) | không dùng | không dùng | cần gates → Hallmark; cần taste Mint/Cadence nhanh → Skillry (xem `using-skillry.md` phần web) |
| Rebuild/migrate site sống 1:1 (mất source/chuyển nền tảng, có quyền) | hỗ trợ (sweep phần custom mới) | không dùng | không dùng | chính | hỗ trợ (cấp tokens quan sát được cho rebuild) | không dùng | cần giống hệt URL sống → cloner; cần system mới pass gates → Hallmark; cần tokens nhanh → dembrandt hỗ trợ |
| Audit tokens/drift/WCAG site sống (có quyền) | hỗ trợ (sweep tokens thành system) | không dùng | không dùng | không dùng | chính | không dùng | cần đo thật + gate CI → dembrandt; cần system mới → Hallmark |
| Review/audit UI code có sẵn (React/Next.js) | hỗ trợ (sửa system khi findings thuộc về system) | không dùng | không dùng | không dùng | không dùng | chính | cần 1 pass checklist nhanh `file:line` → guidelines; findings thuộc system → Hallmark sửa |

### Workflow phối hợp mẫu
Hallmark dựng page + system → React Bits lắp 1 background/text effect → chạy lại sweep (`sloplint --render`) + review lạnh. Output Skillry-web lấy về muốn đạt chuẩn thì sweep lại bằng Hallmark; Linux dùng paste-prompt/ZIP thay vì CLI login. Rebuild site sống có quyền → clone bằng ai-website-cloner-template (route map + compare + check xanh), rồi sweep phần custom mới bằng Hallmark. Audit site sống có quyền → extract tokens bằng dembrandt (`--save-output`/`--dtcg`, crawl khi cần), gate drift bằng `--compare` trong CI, sweep tokens thành system bằng Hallmark khi cần chuẩn. Review code UI có sẵn → soi bằng web-interface-guidelines (fetch `command.md` tươi, findings `file:line`), findings nào thuộc về system thì sửa bằng Hallmark.

### Danh sách using-doc
- `using-hallmark.md` — dùng Hallmark CHO UI → gốc `../../items/hallmark/README.md`
- `using-reactbits.md` — dùng React Bits CHO UI → gốc `../../items/reactbits/README.md`
- `using-skillry.md` — dùng Skillry (phần web) CHO UI → gốc `../../items/skillry/README.md`
- `using-ai-website-cloner-template.md` — dùng ai-website-cloner-template CHO UI → gốc `../../items/ai-website-cloner-template/README.md`
- `using-dembrandt.md` — dùng dembrandt CHO UI → gốc `../../items/dembrandt/README.md`
- `using-web-interface-guidelines.md` — dùng web-interface-guidelines CHO UI → gốc `../../items/web-interface-guidelines/README.md`

---

## English

UI domain — for UI use of each item read the matching `using-*.md` (UI-only deltas + links to origin). Origin details live in `items/*/README.md`; this index only routes + positions.

### Routing: job → item(s)
| Job | Primary item(s) (each a different way) | Supporting item | Starter command |
|---|---|---|---|
| New page / redesign / audit with system + gates | `hallmark` (system + gates — see `using-hallmark.md`) | `reactbits` for single effects | `/hallmark <prompt>` |
| Ready-made React motion | `reactbits` (owned bricks — see `using-reactbits.md`) | `hallmark` to re-sweep | `npx shadcn@latest add @react-bits/SplitText-TS-TW` |
| Sample landing (Skillry web part) | `skillry` (packaged taste — see `using-skillry.md`) + `hallmark` (gated system — see `using-hallmark.md`) | `hallmark` re-sweep after Skillry output | paste: `Read https://skillry.dev/skills/bs-mint-noir-saas-site/install.md and follow the instructions to install the skill.` |
| 1:1 rebuild/migrate of a live site as Next.js (permitted, pathnames kept) | `ai-website-cloner-template` (live clone — see `using-ai-website-cloner-template.md`) | `hallmark` to sweep new custom parts | `/clone-website <url1> [<url2> ...]` (browser-capable agent) |
| Live-site token/drift/WCAG audit (permitted) + DTCG/Tailwind/shadcn exports | `dembrandt` (real measurement + CI gate — see `using-dembrandt.md`) | `hallmark` to sweep tokens into a standard system | `dembrandt <url> --save-output` (add `--compare` for gating) |
| Review/audit existing UI code into `file:line` (React/Next.js, network needed) | `web-interface-guidelines` (130-rule checklist — see `using-web-interface-guidelines.md`) | `hallmark` to fix system-level findings | `Review my UI: src/components/CheckoutForm.tsx` (`web-design-guidelines` skill) |

Sample landing has 2 primaries: packaged taste fast → Skillry; gated system → Hallmark. See matrix below. Live-site rebuild: exact URL match (with rights) → cloner; new system → Hallmark. Token/drift audit: real measurement + CI gate → dembrandt; new system → Hallmark. Existing-UI review: fast checklist `file:line` pass → web-interface-guidelines; system-level findings → Hallmark fixes.

### Positioning
| Item | Typical purposes | 1-sentence operating summary | Strengths | Weaknesses | Use as primary when | Avoid when | Replaced by | Why pick A over B in this case |
|---|---|---|---|---|---|---|---|---|
| `hallmark` — UI details in `using-hallmark.md`, origin at `../../items/hallmark/README.md` | full page system, anti-AI-slop | Machine gates + token scaffold + theme deal + hero-first + render sweep | machine Floor/gates, 10-job anatomy, hero-first + cold review | no ready animated bricks | a gated standard system is needed | logic-only change | hand edit; v0/Lovable for fast draft | Pick Hallmark over Skillry-web when gates (contrast/focus/fold/word budget) decide, not packaged taste |
| `reactbits` — UI details in `using-reactbits.md`, origin at `../../items/reactbits/README.md` | owned animated bricks | Copy source by variant via CLI/MCP, tune live then export | 215+ components, 4 flavors, MCP + Studio/Lab | no tokens/gates/review, React only | one concrete React effect is needed | non-React, strict a11y/perf | Motion/GSAP for pure engine | Pick React Bits over Hallmark when a previewable brick + variant decides |
| `skillry` (web) — UI details in `using-skillry.md`, origin at `../../items/skillry/README.md` | sample landing now | SKILL.md + real previews, static HTML render | packaged taste (Mint Noir free...), 3 install routes | 40/617 free + account, no system/gates | exactly one packaged landing taste is needed | gated system needed | Hallmark for system; free builders | Pick Skillry-web over Hallmark when the Mint/Cadence packaged taste + guided workflow decides |
| `ai-website-cloner-template` — UI details in `using-ai-website-cloner-template.md`, origin at `../../items/ai-website-cloner-template/README.md` | 1:1 rebuild/migrate of a live site as Next.js | clone-website skill in 4 Map/Observe/Build/Compare steps + `npm run check` | exact live-URL match + route map + comparison + green check, 38,004 stars $0 MIT template | needs rights/ToS + browser + Node 24 + Opus tokens, copies carry no system/gates | exact match of a live site needed (lost source/re-platform) | new system, packaged taste, unpermitted clone | Hallmark for a new system; Skillry-web for ready taste | Pick the cloner over Hallmark when the exact live URL decides, not a new system |
| `dembrandt` — UI details in `using-dembrandt.md`, origin at `../../items/dembrandt/README.md` | live-site token/drift/WCAG audit + exports | CLI measuring rendered computed styles/DOM + DTCG/DESIGN.md/Tailwind/shadcn + `--compare` CI gate | real production measurement + drift CI/Action/App + real-DOM-pair WCAG, 3,902 stars $0 MIT CLI | needs rights/ToS/robots + Node 18 + separately downloaded browser, measures but generates no system | tokens/drift/WCAG of an existing site, gating each release | new system from zero, runnable app, unpermitted site | Hallmark for a new system; cloner for a runnable app | Pick dembrandt over Hallmark when observed tokens/drift decide, not a new system |
| `web-interface-guidelines` — UI details in `using-web-interface-guidelines.md`, origin at `../../items/web-interface-guidelines/README.md` | review/audit existing UI code into `file:line` | Skill fetching fresh `command.md` + 104-rule check + terse findings | 130-rule checklist, $0 MIT, ~815k installs, 1-step install, changes no files | needs network fetch per review, audits generate no system | existing UI code needing one fast pre-merge pass | system/gate generation, React bricks, offline | Hallmark for a new system; React Bits for bricks | Pick guidelines over Hallmark when fast checklist findings (`aria-label`, `transition: all`, `…`) decide, not a new system |

### Overlap matrix
| Job | `hallmark` | `reactbits` | `skillry` (web) | `ai-website-cloner-template` | `dembrandt` | `web-interface-guidelines` | Distinguishing selection rule |
|---|---|---|---|---|---|---|---|
| New page needing a standard system | primary | supporting | do-not-use | do-not-use | do-not-use | do-not-use (AGENTS.md generation OK, but no system generated) | gates must pass → Hallmark |
| One React effect | do-not-use | primary | do-not-use | do-not-use | do-not-use | do-not-use | owned brick + variant → React Bits |
| Redesign/audit keeping content | primary | do-not-use | do-not-use | supporting (lost source/repo — rebuild from the live URL; repo intact → Hallmark) | supporting (measured tokens as audit input; repo intact → Hallmark) | supporting (checklist `file:line` pass before redesign; repo + wiring intact → Hallmark) | repo + wiring intact → Hallmark; lost source → cloner; measured tokens → dembrandt supports; fast issue list → guidelines supports |
| System exists, motion missing | supporting | primary | do-not-use | do-not-use | do-not-use | do-not-use | React Bits installs, Hallmark re-sweeps |
| Sample landing | primary (gated) | do-not-use | primary (packaged) | replaceable (arbitrary-URL clone with rights — not packaged taste) | do-not-use | do-not-use | gates → Hallmark; Mint/Cadence taste fast → Skillry |
| 1:1 rebuild/migrate of a live site (lost source/re-platform, with rights) | supporting (sweep new custom parts) | do-not-use | do-not-use | primary | supporting (observed tokens for the rebuild) | do-not-use | exact live-URL match → cloner; new gated system → Hallmark; fast tokens → dembrandt supports |
| Live-site token/drift/WCAG audit (with rights) | supporting (sweep tokens into a system) | do-not-use | do-not-use | do-not-use | primary | do-not-use | real measurement + CI gate → dembrandt; new system → Hallmark |
| Review/audit existing UI code (React/Next.js) | supporting (fix system-level findings) | do-not-use | do-not-use | do-not-use | do-not-use | primary | fast checklist `file:line` pass → guidelines; system-level findings → Hallmark fixes |

### Sample combined workflow
Hallmark builds the page + system → React Bits installs 1 effect → re-run sweep + cold review. Skillry-web outputs that need a standard get re-swept with Hallmark; on Linux use paste-prompt/ZIP. Permitted live-site rebuild → clone with ai-website-cloner-template (route map + comparisons + green check), then sweep new custom parts with Hallmark. Permitted live-site audit → extract tokens with dembrandt (`--save-output`/`--dtcg`, crawl when needed), gate drift with `--compare` in CI, sweep tokens into a system with Hallmark when a standard is needed. Existing UI code review → audit with web-interface-guidelines (fresh `command.md` fetch, `file:line` findings), fix system-level findings with Hallmark.

### Using-doc list
- `using-hallmark.md` — Hallmark FOR UI → origin `../../items/hallmark/README.md`
- `using-reactbits.md` — React Bits FOR UI → origin `../../items/reactbits/README.md`
- `using-skillry.md` — Skillry (web part) FOR UI → origin `../../items/skillry/README.md`
- `using-ai-website-cloner-template.md` — ai-website-cloner-template FOR UI → origin `../../items/ai-website-cloner-template/README.md`
- `using-dembrandt.md` — dembrandt FOR UI → origin `../../items/dembrandt/README.md`
- `using-web-interface-guidelines.md` — web-interface-guidelines FOR UI → origin `../../items/web-interface-guidelines/README.md`
