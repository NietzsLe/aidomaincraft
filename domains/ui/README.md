# domains/ui/

## Tiếng Việt

Domain UI — dùng item nào CHO UI thì đọc `using-*.md` tương ứng (phần riêng UI + link về gốc). Chi tiết gốc sống trong `items/*/README.md`; index này chỉ điều hướng + định vị.

### Bảng điều hướng: việc → item(s)
| Việc cần làm | Item chính (mỗi cái 1 cách) | Item hỗ trợ | Lệnh bắt đầu |
|---|---|---|---|
| Build trang mới / redesign / audit có system + gates | `hallmark` (system + gates — xem `using-hallmark.md`) | `reactbits` cho hiệu ứng lẻ | `/hallmark <prompt>` |
| Hiệu ứng React có sẵn (text/background/micro/card) | `reactbits` (bricks sở hữu source — xem `using-reactbits.md`) | `hallmark` để sweep sau khi lắp | `npx shadcn@latest add @react-bits/SplitText-TS-TW` |
| Landing mẫu có sẵn (phần web của Skillry) | `skillry` (taste đóng gói — xem `using-skillry.md`) + `hallmark` (system chuẩn — xem `using-hallmark.md`) | `hallmark` sweep lại sau khi lấy output | paste vào agent: `Read https://skillry.dev/skills/bs-mint-noir-saas-site/install.md and follow the instructions to install the skill.` |

Việc landing mẫu có 2 chính: cần taste có sẵn nhanh → Skillry; cần system pass gates → Hallmark. Tiêu chí phân biệt ở ma trận dưới.

### Bảng định vị
| Item | Mục đích điển hình | Vận hành tóm tắt 1 câu | Điểm mạnh | Điểm yếu | Dùng chính khi | Tránh khi | Thay thế bởi | Vì sao chọn A thay vì B trong case này |
|---|---|---|---|---|---|---|---|---|
| `hallmark` — chi tiết UI ở `using-hallmark.md`, gốc ở `../../items/hallmark/README.md` | full page system, taste, chống AI-slop | Gates máy + scaffold tokens + deal theme + hero-first + sweep render | Floor/gates quét máy, 10 job anatomy, hero-first + review lạnh | không có bricks animated sẵn | cần system/design chuẩn, output phải pass gates | sửa logic thuần, tweak nhỏ giữ system | sửa tay; v0/Lovable khi cần draft nhanh | Chọn Hallmark thay vì Skillry-web khi quyết định phụ thuộc vào pass gates (contrast/focus/fold/word budget), không phải taste có sẵn |
| `reactbits` — chi tiết UI ở `using-reactbits.md`, gốc ở `../../items/reactbits/README.md` | bricks animated sở hữu source | Copy source theo variant qua CLI/MCP, tune live rồi export | 215+ component, 4 biến thể, MCP + Studio/Lab | không tokens/gates/review, chỉ React | cần 1 effect/component React cụ thể | project phi React, a11y/perf nghiêm | Motion/GSAP khi cần engine thuần | Chọn React Bits thay vì Hallmark khi cần brick hiệu ứng lẻ có demo + variant, không phải system |
| `skillry` (phần web) — chi tiết UI ở `using-skillry.md`, gốc ở `../../items/skillry/README.md` | landing mẫu chạy ngay | Skill SKILL.md + preview thật, render HTML tĩnh | taste đóng gói (Mint Noir free...), 3 đường cài, hỗ trợ OpenCode | 40/617 free + cần tài khoản, không system/gates | cần đúng 1 taste landing có sẵn, chấp nhận trả phí | cần system pass gates, cần bricks React | Hallmark khi cần system; free builder khi tự ráp được | Chọn Skillry-web thay vì Hallmark khi cần taste Mint/Cadence đóng gói + quy trình hướng dẫn; engine free thắng về capability |

### Ma trận chồng lấn
| Việc | `hallmark` | `reactbits` | `skillry` (web) | Tiêu chí chọn phân biệt |
|---|---|---|---|---|
| Trang mới cần system chuẩn | chính | hỗ trợ (1-2 effect) | không dùng | pass gates → Hallmark; Skillry-web không có gates |
| 1 hiệu ứng/component lẻ React | không dùng | chính | không dùng | brick sở hữu source → React Bits |
| Redesign/audit giữ content + wiring | chính | không dùng | không dùng | giữ system + wiring → chỉ Hallmark (`--kept`, `compare.html`) |
| Page có system, thiếu motion | hỗ trợ (sweep lại) | chính | không dùng | thiếu motion → React Bits lắp, Hallmark sweep lại |
| Landing mẫu có sẵn | chính (system chuẩn) | không dùng | chính (taste sẵn) | cần gates → Hallmark; cần taste Mint/Cadence nhanh → Skillry (xem `using-skillry.md` phần web) |

### Workflow phối hợp mẫu
Hallmark dựng page + system → React Bits lắp 1 background/text effect → chạy lại sweep (`sloplint --render`) + review lạnh. Output Skillry-web lấy về muốn đạt chuẩn thì sweep lại bằng Hallmark; Linux dùng paste-prompt/ZIP thay vì CLI login.

### Danh sách using-doc
- `using-hallmark.md` — dùng Hallmark CHO UI → gốc `../../items/hallmark/README.md`
- `using-reactbits.md` — dùng React Bits CHO UI → gốc `../../items/reactbits/README.md`
- `using-skillry.md` — dùng Skillry (phần web) CHO UI → gốc `../../items/skillry/README.md`

---

## English

UI domain — for UI use of each item read the matching `using-*.md` (UI-only deltas + links to origin). Origin details live in `items/*/README.md`; this index only routes + positions.

### Routing: job → item(s)
| Job | Primary item(s) (each a different way) | Supporting item | Starter command |
|---|---|---|---|
| New page / redesign / audit with system + gates | `hallmark` (system + gates — see `using-hallmark.md`) | `reactbits` for single effects | `/hallmark <prompt>` |
| Ready-made React motion | `reactbits` (owned bricks — see `using-reactbits.md`) | `hallmark` to re-sweep | `npx shadcn@latest add @react-bits/SplitText-TS-TW` |
| Sample landing (Skillry web part) | `skillry` (packaged taste — see `using-skillry.md`) + `hallmark` (gated system — see `using-hallmark.md`) | `hallmark` re-sweep after Skillry output | paste: `Read https://skillry.dev/skills/bs-mint-noir-saas-site/install.md and follow the instructions to install the skill.` |

Sample landing has 2 primaries: packaged taste fast → Skillry; gated system → Hallmark. See matrix below.

### Positioning
| Item | Typical purposes | 1-sentence operating summary | Strengths | Weaknesses | Use as primary when | Avoid when | Replaced by | Why pick A over B in this case |
|---|---|---|---|---|---|---|---|---|
| `hallmark` — UI details in `using-hallmark.md`, origin at `../../items/hallmark/README.md` | full page system, anti-AI-slop | Machine gates + token scaffold + theme deal + hero-first + render sweep | machine Floor/gates, 10-job anatomy, hero-first + cold review | no ready animated bricks | a gated standard system is needed | logic-only change | hand edit; v0/Lovable for fast draft | Pick Hallmark over Skillry-web when gates (contrast/focus/fold/word budget) decide, not packaged taste |
| `reactbits` — UI details in `using-reactbits.md`, origin at `../../items/reactbits/README.md` | owned animated bricks | Copy source by variant via CLI/MCP, tune live then export | 215+ components, 4 flavors, MCP + Studio/Lab | no tokens/gates/review, React only | one concrete React effect is needed | non-React, strict a11y/perf | Motion/GSAP for pure engine | Pick React Bits over Hallmark when a previewable brick + variant decides |
| `skillry` (web) — UI details in `using-skillry.md`, origin at `../../items/skillry/README.md` | sample landing now | SKILL.md + real previews, static HTML render | packaged taste (Mint Noir free...), 3 install routes | 40/617 free + account, no system/gates | exactly one packaged landing taste is needed | gated system needed | Hallmark for system; free builders | Pick Skillry-web over Hallmark when the Mint/Cadence packaged taste + guided workflow decides |

### Overlap matrix
| Job | `hallmark` | `reactbits` | `skillry` (web) | Distinguishing selection rule |
|---|---|---|---|---|
| New page needing a standard system | primary | supporting | do-not-use | gates must pass → Hallmark |
| One React effect | do-not-use | primary | do-not-use | owned brick + variant → React Bits |
| Redesign/audit keeping content | primary | do-not-use | do-not-use | system + wiring kept → only Hallmark |
| System exists, motion missing | supporting | primary | do-not-use | React Bits installs, Hallmark re-sweeps |
| Sample landing | primary (gated) | do-not-use | primary (packaged) | gates → Hallmark; Mint/Cadence taste fast → Skillry |

### Sample combined workflow
Hallmark builds the page + system → React Bits installs 1 effect → re-run sweep + cold review. Skillry-web outputs that need a standard get re-swept with Hallmark; on Linux use paste-prompt/ZIP.

### Using-doc list
- `using-hallmark.md` — Hallmark FOR UI → origin `../../items/hallmark/README.md`
- `using-reactbits.md` — React Bits FOR UI → origin `../../items/reactbits/README.md`
- `using-skillry.md` — Skillry (web part) FOR UI → origin `../../items/skillry/README.md`
