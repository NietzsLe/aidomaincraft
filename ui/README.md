# ui/

## Tiếng Việt

Domain UI — mỗi công cụ/giải pháp là 1 item. Chi tiết sống trong `item/README.md`; index này chỉ điều hướng + định vị.

### Bảng điều hướng: việc → item
| Việc cần làm | Item chính | Item hỗ trợ | Lệnh bắt đầu |
|---|---|---|---|
| Build trang mới / redesign / audit có system + gates | `hallmark/` | `reactbits/` cho hiệu ứng lẻ | `/hallmark <prompt>` |
| Hiệu ứng React có sẵn (text/background/micro/card) | `reactbits/` | `hallmark/` để sweep sau khi lắp | `npx shadcn@latest add @react-bits/SplitText-TS-TW` |

### Bảng định vị
| Item | Mục đích điển hình | Vận hành tóm tắt 1 câu | Điểm mạnh | Điểm yếu | Dùng chính khi | Tránh khi | Thay thế bởi | Vì sao chọn A thay vì B trong case này |
|---|---|---|---|---|---|---|---|---|
| `hallmark/` | full page system, taste, chống AI-slop | Gates máy + scaffold tokens + deal theme + hero-first + sweep render mới cho ship | Floor/gates quét máy, 10 job anatomy, hero-first + review lạnh | không có sẵn bricks animated, chỉ HTML/CSS/JS-framework qua dev server | cần system/design chuẩn, output phải pass gates | sửa logic thuần, tweak nhỏ giữ system, project phi web | sửa tay trực tiếp; v0/Lovable khi cần draft nhanh không cần gates | Chọn Hallmark thay vì generator nhanh khi quyết định phụ thuộc vào pass gates (contrast/focus/fold/word budget), không phải tốc độ draft |
| `reactbits/` | bricks animated sở hữu source | Copy source theo variant qua CLI/MCP, tune live trong Studio/Lab rồi export | 215+ component, 4 biến thể JS/TS+CSS/TW, MCP + tool Studio/Lab | không có tokens/gates/review, chỉ React | cần 1 effect/component cụ thể cho React, copy source về sở hữu | project phi React, a11y/perf nghiêm, cần system | Motion/GSAP khi cần engine animation thuần; Hallmark custom khi cần system | Chọn React Bits thay vì Motion/GSAP thuần khi quyết định phụ thuộc vào có sẵn component + demo + MCP lắp nhanh, không phải tự code motion từ đầu |

### Ma trận chồng lấn
| Việc | `hallmark/` | `reactbits/` | Tiêu chí chọn phân biệt |
|---|---|---|---|
| Trang mới cần system chuẩn | chính | hỗ trợ (lắp 1-2 effect) | cần pass gates → Hallmark chính; chỉ thiếu motion lẻ mới gọi React Bits |
| 1 hiệu ứng/component lẻ cho React | không dùng | chính | cần brick sở hữu source + variant sẵn → React Bits; Hallmark không có bricks |
| Redesign/audit giữ content + wiring | chính | không dùng | giữ system + wiring + brand → chỉ Hallmark làm được (`--kept`, `compare.html`) |
| Page đã có system, thiếu motion | hỗ trợ (sweep lại) | chính | thiếu motion → React Bits lắp, Hallmark sweep lại để không vỡ gates |

### Workflow phối hợp mẫu
Hallmark dựng page + system → React Bits lắp 1 background/text effect → chạy lại Hallmark sweep (`sloplint --render`) + review lạnh. Không lắp 3-4 effect cùng lúc.

### Danh sách item
- `hallmark/` — build mới, component 8 states, app-screen, redesign full/restyle/polish, audit. Định vị khác biệt vs generator UI viral (v0/Lovable) trong file item.
- `reactbits/` — text animation, background, micro, card/carousel, tool Studio/Lab. Định vị khác biệt vs Motion/GSAP/Magic UI trong file item.

Muốn thêm tool mới thì thêm 1 thư mục ngang `hallmark/`, theo template `CHARTER.md v6` + `templates/`, qua `VERIFY.md`, và cập nhật cả 3 bảng trên trong cùng commit.

---

## English

UI domain — each tool/solution is 1 item. Details live in `item/README.md`; this index only routes + positions.

### Routing: job → item
| Job | Primary item | Supporting item | Starter command |
|---|---|---|---|
| New page / redesign / audit with system + gates | `hallmark/` | `reactbits/` for single effects | `/hallmark <prompt>` |
| Ready-made React motion (text/background/micro/card) | `reactbits/` | `hallmark/` to re-sweep after install | `npx shadcn@latest add @react-bits/SplitText-TS-TW` |

### Positioning
| Item | Typical purposes | 1-sentence operating summary | Strengths | Weaknesses | Use as primary when | Avoid when | Replaced by | Why pick A over B in this case |
|---|---|---|---|---|---|---|---|---|
| `hallmark/` | full page system, taste, anti-AI-slop | Machine gates + token scaffold + theme deal + hero-first + render sweep before ship | machine Floor/gates, 10-job anatomy, hero-first + cold review | no ready animated bricks, web pages via dev server only | a gated standard system/design is needed | logic-only change, tiny tweak keeping system, non-web project | direct hand edit; v0/Lovable when a fast draft beats gates | Pick Hallmark over fast generators when the decision hinges on passing gates (contrast/focus/fold/word budget), not draft speed |
| `reactbits/` | owned-source animated bricks | Copy source by variant via CLI/MCP, tune live in Studio/Lab then export | 215+ components, 4 JS/TS+CSS/TW flavors, MCP + Studio/Lab tools | no tokens/gates/review, React only | one concrete React effect/component is needed as owned source | non-React project, strict a11y/perf, system needed | Motion/GSAP for a pure animation engine; Hallmark custom for a system | Pick React Bits over raw Motion/GSAP when the decision hinges on ready components + demos + MCP install, not hand-coding motion |

### Overlap matrix
| Job | `hallmark/` | `reactbits/` | Distinguishing selection rule |
|---|---|---|---|
| New page needing a standard system | primary | supporting (1-2 effects) | gates must pass → Hallmark primary; React Bits only for missing motion |
| One React effect/component | do-not-use | primary | owned-source brick + variant needed → React Bits; Hallmark has no bricks |
| Redesign/audit keeping content + wiring | primary | do-not-use | system + wiring + brand kept → only Hallmark (`--kept`, `compare.html`) |
| System exists, motion missing | supporting (re-sweep) | primary | motion missing → React Bits installs, Hallmark re-sweeps so gates hold |

### Sample combined workflow
Hallmark builds the page + system → React Bits installs 1 background/text effect → re-run Hallmark sweep (`sloplint --render`) + cold review. Never install 3-4 effects at once.

### Item list
- `hallmark/` — new build, 8-state component, app-screen, full/restyle/polish redesign, audit. Differentiation vs viral UI generators (v0/Lovable) inside the item file.
- `reactbits/` — text animation, background, micro, card/carousel, Studio/Lab tools. Differentiation vs Motion/GSAP/Magic UI inside the item file.

To add a new tool, add a sibling of `hallmark/` following the `CHARTER.md v6` template + `templates/`, via `VERIFY.md`, and update all 3 tables above in the same commit.
