# domains/media/

## Tiếng Việt

Domain media — output trình bày (video/landing/deck/ảnh). Hiện tại chỉ có Skillry. Chi tiết gốc ở `items/skillry/README.md`; dùng CHO media thì đọc `using-skillry.md`.

### Bảng điều hướng: việc → item(s)
| Việc cần làm | Item chính | Item hỗ trợ | Lệnh bắt đầu |
|---|---|---|---|
| Launch video kiểu Manus/Linear | `skillry` (xem `using-skillry.md`) | — | `npx --yes skillry-cli@latest install bs-manus2-0-style-launch-video --agent opencode` (macOS; Linux dùng paste-prompt/ZIP) |
| Slide deck + narrated report | `skillry` (xem `using-skillry.md`) | — | paste `Read https://skillry.dev/skills/bs-field-notes-deck/install.md and follow the instructions to install the skill.` |
| OG image / avatar / minh họa | `skillry` (xem `using-skillry.md`) | — | paste `Read https://skillry.dev/skills/bs-notion-style-og/install.md and follow the instructions to install the skill.` |

### Bảng định vị
| Item | Mục đích điển hình | Vận hành tóm tắt 1 câu | Điểm mạnh | Điểm yếu | Dùng chính khi | Tránh khi | Thay thế bởi | Vì sao chọn A thay vì B trong case này |
|---|---|---|---|---|---|---|---|---|
| `skillry` — chi tiết media ở `using-skillry.md`, gốc ở `../../items/skillry/README.md` | video/deck/OG chạy ngay | SKILL.md + preview thật, render theo engine từng loại | taste đóng gói + preview + 3 đường cài, 617 skill (40 free) | trả phí, cần tài khoản, không system/gates, phụ thuộc vendor + phí model ngoài | cần đúng 1 taste đóng gói có preview, chấp nhận trả phí | offline/cấm vendor trả phí, cần engine free đã đủ | skills.sh (HyperFrames 538.9K, pptx official 244.5K, Satori/Playwright) khi cần capability free | Chọn Skillry thay vì free khi cần taste Manus/Notion/Field Notes đóng gói + lặp lại nhiều; engine free thắng về capability |

### Ma trận chồng lấn
| Việc | `skillry` | Đối thủ free | Tiêu chí chọn phân biệt |
|---|---|---|---|
| Launch video | chính | HyperFrames `product-launch-video` (~538.9K installs) thay thế | cần style Manus đóng gói → Skillry; cần engine/capability → free |
| Deck PPTX | chính | `anthropics/skills --skill pptx` official (~244.5K) thay thế | cần taste Field Notes → Skillry; cần PPTX chuẩn → official |
| OG image | chính | Satori/Playwright (deterministic) thay thế | cần style Notion/GrokBot → Skillry; cần chữ chuẩn → Satori/Playwright |

### Workflow phối hợp mẫu
Chốt output (video/deck/ảnh) → tìm skill khớp trên /skills (xem preview + installs + nhãn Free/Premium) → cài (paste-prompt mọi OS; CLI macOS/Windows; ZIP + restart) → chạy workflow skill → kiểm tra định dạng/license. Cần chuẩn riêng thì sweep lại bằng Hallmark (`domains/ui/using-hallmark.md`).

### Danh sách using-doc
- `using-skillry.md` — dùng Skillry CHO media → gốc `../../items/skillry/README.md`

---

## English

Media domain — presentable outputs (video/landing/deck/image). Currently Skillry only. Origin at `items/skillry/README.md`; for media use read `using-skillry.md`.

### Routing: job → item(s)
| Job | Primary item | Supporting item | Starter command |
|---|---|---|---|
| Manus/Linear-style launch video | `skillry` (see `using-skillry.md`) | — | `npx --yes skillry-cli@latest install bs-manus2-0-style-launch-video --agent opencode` (macOS; Linux uses paste-prompt/ZIP) |
| Slide deck + narrated report | `skillry` (see `using-skillry.md`) | — | paste `Read https://skillry.dev/skills/bs-field-notes-deck/install.md and follow the instructions to install the skill.` |
| OG image / avatar / illustration | `skillry` (see `using-skillry.md`) | — | paste `Read https://skillry.dev/skills/bs-notion-style-og/install.md and follow the instructions to install the skill.` |

### Positioning
| Item | Typical purposes | 1-sentence operating summary | Strengths | Weaknesses | Use as primary when | Avoid when | Replaced by | Why pick A over B in this case |
|---|---|---|---|---|---|---|---|---|
| `skillry` — media details in `using-skillry.md`, origin at `../../items/skillry/README.md` | video/deck/OG now | SKILL.md + real previews, per-output-type render engines | packaged taste + previews + 3 install routes, 617 skills (40 free) | paid, account required, no system/gates, vendor + external model fees | exactly one packaged taste with preview is needed | offline/paid-vendor ban, free engine suffices | skills.sh (HyperFrames 538.9K, official pptx 244.5K, Satori/Playwright) for free capability | Pick Skillry over free when the Manus/Notion/Field Notes packaged taste + repeated use decides |

### Overlap matrix
| Job | `skillry` | Free opponent | Distinguishing selection rule |
|---|---|---|---|
| Launch video | primary | HyperFrames `product-launch-video` (~538.9K installs) replaceable | Manus packaged style → Skillry; engine/capability → free |
| PPTX deck | primary | `anthropics/skills --skill pptx` official (~244.5K) replaceable | Field Notes packaged taste → Skillry; standard PPTX → official |
| OG image | primary | Satori/Playwright (deterministic) replaceable | Notion/GrokBot style → Skillry; crisp text → Satori/Playwright |

### Sample combined workflow
Fix the output (video/deck/image) → find the matching skill (preview + installs + Free/Premium) → install (paste-prompt every OS; CLI macOS/Windows; ZIP + restart) → run the skill workflow → verify format/license. Need a custom standard → re-sweep with Hallmark (`domains/ui/using-hallmark.md`).

### Using-doc list
- `using-skillry.md` — Skillry FOR media → origin `../../items/skillry/README.md`
