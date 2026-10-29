# ui/

## Tiếng Việt

Domain UI — mỗi công cụ/giải pháp là 1 item. Chi tiết sống trong `item/README.md`; index này chỉ điều hướng + định vị.

### Bảng điều hướng: việc → item
| Việc cần làm | Item chính | Item hỗ trợ | Lệnh bắt đầu |
|---|---|---|---|
| Build trang mới / redesign / audit có system + gates | `hallmark/` | `reactbits/` cho hiệu ứng lẻ | `/hallmark <prompt>` |
| Hiệu ứng React có sẵn (text/background/micro/card) | `reactbits/` | `hallmark/` để sweep sau khi lắp | `npx shadcn@latest add @react-bits/SplitText-TS-TW` |
| Output trình bày có sẵn: video launch, landing mẫu, deck, OG image | `skillry/` | `hallmark/` để sweep system sau khi có output | paste vào agent: `Read https://skillry.dev/skills/bs-mint-noir-saas-site/install.md and follow the instructions to install the skill.` |

### Bảng định vị
| Item | Mục đích điển hình | Vận hành tóm tắt 1 câu | Điểm mạnh | Điểm yếu | Dùng chính khi | Tránh khi | Thay thế bởi | Vì sao chọn A thay vì B trong case này |
|---|---|---|---|---|---|---|---|---|
| `hallmark/` | full page system, taste, chống AI-slop | Gates máy + scaffold tokens + deal theme + hero-first + sweep render mới cho ship | Floor/gates quét máy, 10 job anatomy, hero-first + review lạnh | không có sẵn bricks animated, chỉ HTML/CSS/JS-framework qua dev server | cần system/design chuẩn, output phải pass gates | sửa logic thuần, tweak nhỏ giữ system, project phi web | sửa tay trực tiếp; v0/Lovable khi cần draft nhanh không cần gates | Chọn Hallmark thay vì generator nhanh khi quyết định phụ thuộc vào pass gates (contrast/focus/fold/word budget), không phải tốc độ draft |
| `reactbits/` | bricks animated sở hữu source | Copy source theo variant qua CLI/MCP, tune live trong Studio/Lab rồi export | 215+ component, 4 biến thể JS/TS+CSS/TW, MCP + tool Studio/Lab | không có tokens/gates/review, chỉ React | cần 1 effect/component cụ thể cho React, copy source về sở hữu | project phi React, a11y/perf nghiêm, cần system | Motion/GSAP khi cần engine animation thuần; Hallmark custom khi cần system | Chọn React Bits thay vì Motion/GSAP thuần khi quyết định phụ thuộc vào có sẵn component + demo + MCP lắp nhanh, không phải tự code motion từ đầu |
| `skillry/` | output trình bày chạy ngay: video/landing/deck/ảnh | Skill SKILL.md + preview thật, agent trigger theo description, render theo engine từng loại output | 617 skill (free 40), hỗ trợ OpenCode, 3 đường cài (paste/CLI/ZIP), giá $9.99/tháng–$169 lifetime (chưa gồm phí model ngoài) | chỉ 40/617 free + cần tài khoản, trả phí, không có system/gates, phụ thuộc vendor | cần đúng 1 món trình bày có preview, chấp nhận trả phí | cần system pass gates, bricks code React, việc ngoài 4 output, offline/cấm vendor trả phí | skills.sh khi cần free/mở; Hallmark khi cần system; React Bits khi cần bricks React | Chọn Skillry thay vì free khi cần đúng 1 taste đóng gói (Manus 2.0, Notion OG...) + quy trình hướng dẫn; engine free (HyperFrames 538.9K installs, pptx official, Satori) thắng về capability — trả phí chỉ đáng khi cần taste sẵn hoặc lặp lại nhiều |

### Ma trận chồng lấn
| Việc | `hallmark/` | `reactbits/` | `skillry/` | Tiêu chí chọn phân biệt |
|---|---|---|---|---|
| Trang mới cần system chuẩn | chính | hỗ trợ (lắp 1-2 effect) | không dùng | cần pass gates → Hallmark chính; chỉ thiếu motion lẻ mới gọi React Bits |
| 1 hiệu ứng/component lẻ cho React | không dùng | chính | không dùng | cần brick sở hữu source + variant sẵn → React Bits; Hallmark không có bricks |
| Redesign/audit giữ content + wiring | chính | không dùng | không dùng | giữ system + wiring + brand → chỉ Hallmark làm được (`--kept`, `compare.html`) |
| Page đã có system, thiếu motion | hỗ trợ (sweep lại) | chính | không dùng | thiếu motion → React Bits lắp, Hallmark sweep lại để không vỡ gates; Skillry không liên quan (không phải bricks React) |
| Cần 1 output trình bày có sẵn (video/landing/deck/ảnh) | không dùng (không bán output có sẵn) | không dùng (không có video/deck/OG) | chính | cần món chạy ngay có preview → Skillry; Hallmark/React Bits không phủ việc này |

### Workflow phối hợp mẫu
Hallmark dựng page + system → React Bits lắp 1 background/text effect → chạy lại Hallmark sweep (`sloplint --render`) + review lạnh. Không lắp 3-4 effect cùng lúc. Output Skillry lấy về (video/landing/deck/ảnh) muốn đạt chuẩn thì sweep lại bằng Hallmark; Linux dùng paste-prompt/ZIP thay vì CLI login.

### Danh sách item
- `hallmark/` — build mới, component 8 states, app-screen, redesign full/restyle/polish, audit. Định vị khác biệt vs generator UI viral (v0/Lovable) trong file item.
- `reactbits/` — text animation, background, micro, card/carousel, tool Studio/Lab. Định vị khác biệt vs Motion/GSAP/Magic UI trong file item.
- `skillry/` — output trình bày chạy ngay: launch video, landing mẫu, slide deck + narration, OG image/avatar. Định vị khác biệt vs skills.sh (mở/miễn phí) và Hallmark (1 skill sâu) trong file item.

Muốn thêm tool mới thì thêm 1 thư mục ngang `hallmark/`, theo template `CHARTER.md v6` + `templates/`, qua `VERIFY.md`, và cập nhật cả 3 bảng trên trong cùng commit.

---

## English

UI domain — each tool/solution is 1 item. Details live in `item/README.md`; this index only routes + positions.

### Routing: job → item
| Job | Primary item | Supporting item | Starter command |
|---|---|---|---|
| New page / redesign / audit with system + gates | `hallmark/` | `reactbits/` for single effects | `/hallmark <prompt>` |
| Ready-made React motion (text/background/micro/card) | `reactbits/` | `hallmark/` to re-sweep after install | `npx shadcn@latest add @react-bits/SplitText-TS-TW` |
| Ready-made presentation output: launch video, sample landing, deck, OG image | `skillry/` | `hallmark/` to sweep a system afterwards if needed | paste into agent: `Read https://skillry.dev/skills/bs-mint-noir-saas-site/install.md and follow the instructions to install the skill.` |

### Positioning
| Item | Typical purposes | 1-sentence operating summary | Strengths | Weaknesses | Use as primary when | Avoid when | Replaced by | Why pick A over B in this case |
|---|---|---|---|---|---|---|---|---|
| `hallmark/` | full page system, taste, anti-AI-slop | Machine gates + token scaffold + theme deal + hero-first + render sweep before ship | machine Floor/gates, 10-job anatomy, hero-first + cold review | no ready animated bricks, web pages via dev server only | a gated standard system/design is needed | logic-only change, tiny tweak keeping system, non-web project | direct hand edit; v0/Lovable when a fast draft beats gates | Pick Hallmark over fast generators when the decision hinges on passing gates (contrast/focus/fold/word budget), not draft speed |
| `reactbits/` | owned-source animated bricks | Copy source by variant via CLI/MCP, tune live in Studio/Lab then export | 215+ components, 4 JS/TS+CSS/TW flavors, MCP + Studio/Lab tools | no tokens/gates/review, React only | one concrete React effect/component is needed as owned source | non-React project, strict a11y/perf, system needed | Motion/GSAP for a pure animation engine; Hallmark custom for a system | Pick React Bits over raw Motion/GSAP when the decision hinges on ready components + demos + MCP install, not hand-coding motion |
| `skillry/` | ready-made presentation output: video/landing/deck/image | SKILL.md skills + real previews, agent triggers by description, renders per output-type engine | 617 skills (40 free), OpenCode supported, 3 install routes (paste/CLI/ZIP), $9.99/mo–$169 lifetime (excl. external model fees) | only 40/617 free + account required, paid, no system/gates, vendor dependency | exactly one previewable presentation item is needed, paying is acceptable | gated system needed, React code bricks, jobs outside the 4 outputs, offline/paid-vendor ban | skills.sh when free/open needed; Hallmark for systems; React Bits for React bricks | Pick Skillry over free when one packaged taste is needed (Manus 2.0, Notion OG...) + guided workflow; free engines win on capability (HyperFrames 538.9K installs, official pptx, Satori) — paying only makes sense for ready taste or repeated use |

### Overlap matrix
| Job | `hallmark/` | `reactbits/` | `skillry/` | Distinguishing selection rule |
|---|---|---|---|---|
| New page needing a standard system | primary | supporting (1-2 effects) | do-not-use | gates must pass → Hallmark primary; React Bits only for missing motion |
| One React effect/component | do-not-use | primary | do-not-use | owned-source brick + variant needed → React Bits; Hallmark has no bricks |
| Redesign/audit keeping content + wiring | primary | do-not-use | do-not-use | system + wiring + brand kept → only Hallmark (`--kept`, `compare.html`) |
| System exists, motion missing | supporting (re-sweep) | primary | do-not-use | motion missing → React Bits installs, Hallmark re-sweeps so gates hold |
| Need one ready-made presentation output (video/landing/deck/image) | do-not-use | do-not-use | primary | need it now with preview → Skillry; Hallmark/React Bits do not cover it |

### Sample combined workflow
Hallmark builds the page + system → React Bits installs 1 background/text effect → re-run Hallmark sweep (`sloplint --render`) + cold review. Never install 3-4 effects at once. Skillry outputs (video/landing/deck/image) that need a standard get re-swept with Hallmark; on Linux use paste-prompt/ZIP instead of CLI login.

### Item list
- `hallmark/` — new build, 8-state component, app-screen, full/restyle/polish redesign, audit. Differentiation vs viral UI generators (v0/Lovable) inside the item file.
- `reactbits/` — text animation, background, micro, card/carousel, Studio/Lab tools. Differentiation vs Motion/GSAP/Magic UI inside the item file.
- `skillry/` — ready-made presentation output: launch video, sample landing, slide deck + narration, OG image/avatar. Differentiation vs skills.sh (open/free) and Hallmark (one deep skill) inside the item file.

To add a new tool, add a sibling of `hallmark/` following the `CHARTER.md v6` template + `templates/`, via `VERIFY.md`, and update all 3 tables above in the same commit.
