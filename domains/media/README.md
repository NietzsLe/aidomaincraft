# domains/media/

## Tiếng Việt

Domain media — output trình bày (video/landing/deck/ảnh). Chi tiết gốc ở `items/*/README.md`; dùng CHO media thì đọc `using-*.md` tương ứng.

### Bảng điều hướng: việc → item(s)
| Việc cần làm | Item chính (mỗi cái 1 cách) | Item hỗ trợ | Lệnh bắt đầu |
|---|---|---|---|
| Launch video kiểu Manus/Linear (đóng gói, cài 1 lệnh) | `skillry` (xem `using-skillry.md`) | `awesome-opus5-5-videos` để học prompt gốc | `npx --yes skillry-cli@latest install bs-manus2-0-style-launch-video --agent opencode` (macOS; Linux dùng paste-prompt/ZIP) |
| Học prompt video Opus 5.5 thật (0đ, copy chạy lại) | `awesome-opus5-5-videos` (xem `using-awesome-opus5-5-videos.md`) | — | `git clone --depth 1 https://github.com/yihui-dev/awesome-opus5-5-videos` rồi mở `prompts/<slug>.md` |
| Slide deck + narrated report | `skillry` (xem `using-skillry.md`) | — | paste `Read https://skillry.dev/skills/bs-field-notes-deck/install.md and follow the instructions to install the skill.` |
| OG image / avatar / minh họa | `skillry` (xem `using-skillry.md`) | `logo-design-skill` cho master square/vector khi cần dùng lâu dài | paste `Read https://skillry.dev/skills/bs-notion-style-og/install.md and follow the instructions to install the skill.` |
| Logo/brand mark SVG master + kit (dùng lâu dài, favicon 16px, dập 1 màu, board pitch) | `logo-design-skill` (xem `using-logo-design-skill.md`) | `skillry` cho OG raster nhanh đúng taste | `python3 scripts/search_library.py --industry <closest> --summary` (research category trước khi vẽ) |

### Bảng định vị
| Item | Mục đích điển hình | Vận hành tóm tắt 1 câu | Điểm mạnh | Điểm yếu | Dùng chính khi | Tránh khi | Thay thế bởi | Vì sao chọn A thay vì B trong case này |
|---|---|---|---|---|---|---|---|---|
| `skillry` — chi tiết media ở `using-skillry.md`, gốc ở `../../items/skillry/README.md` | video/deck/OG chạy ngay | SKILL.md + preview thật, render theo engine từng loại | taste đóng gói + preview + 3 đường cài, 617 skill (40 free) | trả phí, cần tài khoản, không system/gates, phụ thuộc vendor + phí model ngoài | cần đúng 1 taste đóng gói có preview, chấp nhận trả phí | offline/cấm vendor trả phí, cần engine free đã đủ | skills.sh (HyperFrames 538.9K, pptx official 244.5K, Satori/Playwright) khi cần capability free; `awesome-opus5-5-videos` khi cần prompt gốc 0đ | Chọn Skillry thay vì free khi cần taste Manus/Notion/Field Notes đóng gói + lặp lại nhiều; engine free thắng về capability |
| `awesome-opus5-5-videos` — chi tiết media ở `using-awesome-opus5-5-videos.md`, gốc ở `../../items/awesome-opus5-5-videos/README.md` | học prompt video Opus 5.5 thật | Prompt markdown + JSON (slug/author/post/category/tags/remake), agent tự viết code animation | 703 prompt MIT 0đ, gốc X + remake Skillry side-by-side (418/703), 12,417★/1,313 forks | không cài được, prompt không đồng đều, cần Opus 5.5 + tự render/test | cần prompt viral thật 0đ để học/thử nhanh | cần skill cài 1 lệnh, cần pipeline ổn định | Skillry video khi cần đóng gói; engine mở khi cần deterministic | Chọn awesome-list thay vì Skillry khi quyết định phụ thuộc vào prompt gốc 0đ + học side-by-side, không phải workflow đóng gói |
| `logo-design-skill` — chi tiết media ở `using-logo-design-skill.md`, gốc ở `../../items/logo-design-skill/README.md` | logo/brand mark SVG + kit dùng lâu dài | SKILL.md 7 phase + checkpoint dừng chờ duyệt + audit số + 8 scripts Python stdlib | master vẽ hình học + audit ~99/100 + kit đầy đủ 0đ MIT không key, thư viện 1,432 logo học | chậm (checkpoint chờ người), không vẽ raster art, không cam kết trademark | cần master hình học + số audit đo được (16px/one-colour/shelf) | cần ảnh diffusion nhanh, cần cam kết pháp lý | logocreator diffusion 8,898★ (cần Together key) khi cần nhiều option ảnh nhanh; Skillry OG taste khi cần raster đúng style | Chọn logo-design-skill thay vì diffusion khi quyết định phụ thuộc vào master vẽ tay + audit đo được, không phải ảnh nhanh |

### Ma trận chồng lấn
| Việc | `skillry` | `awesome-opus5-5-videos` | `logo-design-skill` | Đối thủ free khác | Tiêu chí chọn phân biệt |
|---|---|---|---|---|---|
| Launch video đóng gói (cài 1 lệnh, taste Manus) | chính | hỗ trợ (học prompt gốc) | không dùng | HyperFrames `product-launch-video` (~538.9K installs, skills.sh leaderboard đối chiếu trong `../skillry/` ngày 29/10/2026) thay thế | cần cài 1 lệnh + taste Manus → Skillry; cần engine/capability → free |
| Học prompt video Opus 5.5 gốc (0đ) | hỗ trợ (remake) | chính | không dùng | — | prompt gốc + side-by-side X/remake → awesome-list chính |
| Deck PPTX | chính | không dùng | không dùng | `anthropics/skills --skill pptx` official (~244.5K, đối chiếu trong `../skillry/` ngày 29/10/2026) thay thế | cần taste Field Notes → Skillry; cần PPTX chuẩn → official |
| OG image | chính | không dùng | hỗ trợ (master square/vector dùng lâu dài) | Satori/Playwright (deterministic) thay thế | cần style Notion/GrokBot → Skillry; cần chữ chuẩn → Satori/Playwright; cần master vector → logo-design-skill |
| Logo/brand mark SVG + kit | thay thế (raster taste, không vẽ hình học/audit) | không dùng | chính | logocreator diffusion (8,898★/829 forks, SVG export từ ảnh đã có, cần Together key — đối chiếu trong `../../items/logo-design-skill/` ngày 30/10/2026) thay thế | cần master hình học + audit số → logo-design-skill; cần nhiều option ảnh nhanh → logocreator; cần taste OG → Skillry |

### Workflow phối hợp mẫu
Chốt output (video/deck/ảnh) → tìm skill khớp trên /skills (xem preview + installs + nhãn Free/Premium) → cài (paste-prompt mọi OS; CLI macOS/Windows; ZIP + restart) → chạy workflow skill → kiểm tra định dạng/license. Muốn học prompt gốc 0đ thì clone `awesome-opus5-5-videos`, copy prompt, render lại bằng Opus 5.5 rồi đối chiếu remake. Logo mới → brief + research thư viện + build 3 SVG đen + audit lặp + checkpoint greyscale chờ duyệt → kit (xem `using-logo-design-skill.md`). Cần chuẩn riêng thì sweep lại bằng Hallmark (`domains/ui/using-hallmark.md`).

### Danh sách using-doc
- `using-skillry.md` — dùng Skillry CHO media → gốc `../../items/skillry/README.md`
- `using-awesome-opus5-5-videos.md` — dùng awesome-opus5-5-videos CHO media → gốc `../../items/awesome-opus5-5-videos/README.md`
- `using-logo-design-skill.md` — dùng logo-design-skill CHO media → gốc `../../items/logo-design-skill/README.md`

---

## English

Media domain — presentable outputs (video/landing/deck/image). Origins at `items/*/README.md`; for media use read the matching `using-*.md`.

### Routing: job → item(s)
| Job | Primary item | Supporting item | Starter command |
|---|---|---|---|
| Packaged Manus/Linear launch video | `skillry` (see `using-skillry.md`) | `awesome-opus5-5-videos` for original prompts | `npx --yes skillry-cli@latest install bs-manus2-0-style-launch-video --agent opencode` (macOS; Linux uses paste-prompt/ZIP) |
| Learn Opus 5.5 original video prompts (free) | `awesome-opus5-5-videos` (see `using-awesome-opus5-5-videos.md`) | — | `git clone --depth 1 https://github.com/yihui-dev/awesome-opus5-5-videos` then open `prompts/<slug>.md` |
| Slide deck + narrated report | `skillry` (see `using-skillry.md`) | — | paste `Read https://skillry.dev/skills/bs-field-notes-deck/install.md and follow the instructions to install the skill.` |
| OG image / avatar / illustration | `skillry` (see `using-skillry.md`) | `logo-design-skill` for long-lived square/vector master | paste `Read https://skillry.dev/skills/bs-notion-style-og/install.md and follow the instructions to install the skill.` |
| SVG logo/brand-mark master + kit (long-lived, 16 px favicon, 1-colour stamp, pitch board) | `logo-design-skill` (see `using-logo-design-skill.md`) | `skillry` for fast taste-matched raster OG | `python3 scripts/search_library.py --industry <closest> --summary` (category research before drawing) |

### Positioning
| Item | Typical purposes | 1-sentence operating summary | Strengths | Weaknesses | Use as primary when | Avoid when | Replaced by | Why pick A over B in this case |
|---|---|---|---|---|---|---|---|---|
| `skillry` — media details in `using-skillry.md`, origin at `../../items/skillry/README.md` | video/deck/OG now | SKILL.md + real previews, per-output-type render engines | packaged taste + previews + 3 install routes, 617 skills (40 free, measured 29/10) | paid, account required, no system/gates, vendor + external model fees | exactly one packaged taste with preview is needed | offline/paid-vendor ban, free engine suffices | skills.sh (HyperFrames 538.9K, official pptx 244.5K via `../skillry/` 29/10) for free capability; `awesome-opus5-5-videos` for free original prompts | Pick Skillry over free when the Manus/Notion/Field Notes packaged taste + repeated use decides |
| `awesome-opus5-5-videos` — media details in `using-awesome-opus5-5-videos.md`, origin at `../../items/awesome-opus5-5-videos/README.md` | learn real Opus 5.5 video prompts | Prompt markdown + JSON, agent writes animation code | 703 MIT prompts free, X + Skillry remakes side-by-side (418/703), 12,417 stars/1,313 forks (API 29/10) | not installable, uneven prompts, needs Opus 5.5 + self render | free viral prompts for fast study/try | 1-command skill, stable pipeline | Skillry video for packaging; open engines for deterministic | Pick awesome-list over Skillry when free original prompts + side-by-side learning decides |
| `logo-design-skill` — media details in `using-logo-design-skill.md`, origin at `../../items/logo-design-skill/README.md` | long-lived SVG logo/brand mark + kit | 7-phase SKILL.md + stop-and-wait checkpoint + numeric audit + 8 stdlib Python scripts | geometric master + ~99/100 audit + full $0 keyless MIT kit, 1,432-logo study library | slow (human-gated checkpoint), no raster art, no trademark commitment | geometric master + measurable audit needed (16px/one-colour/shelf) | fast diffusion images or legal commitment needed | diffusion logocreator 8,898 stars (needs Together key) for many fast image options; Skillry OG taste for styled raster | Pick logo-design-skill over diffusion when the hand-drawn master + measurable audit decides, not fast images |

### Overlap matrix
| Job | `skillry` | `awesome-opus5-5-videos` | `logo-design-skill` | Other free opponent | Distinguishing selection rule |
|---|---|---|---|---|---|
| Packaged launch video (Manus taste) | primary | supporting (learn originals) | do-not-use | HyperFrames `product-launch-video` (~538.9K via `../skillry/` 29/10) replaceable | 1-command Manus taste → Skillry; engine/capability → free |
| Learn Opus 5.5 original prompts (free) | supporting (remakes) | primary | do-not-use | — | originals + side-by-side → awesome-list primary |
| PPTX deck | primary | do-not-use | do-not-use | `anthropics/skills --skill pptx` official (~244.5K via `../skillry/` 29/10) replaceable | Field Notes taste → Skillry; standard PPTX → official |
| OG image | primary | do-not-use | supporting (long-lived square/vector master) | Satori/Playwright (deterministic) replaceable | Notion/GrokBot style → Skillry; crisp text → Satori/Playwright; vector master → logo-design-skill |
| SVG logo/brand mark + kit | replaceable (raster taste, no geometric drawing/audit) | do-not-use | primary | diffusion logocreator (8,898 stars/829 forks, SVG-from-image export shipped, needs Together key — via `../../items/logo-design-skill/` 30/10) replaceable | geometric master + numeric audit → logo-design-skill; many fast image options → logocreator; OG taste → Skillry |

### Sample combined workflow
Fix the output (video/deck/image) → find the matching skill (preview + installs + Free/Premium) → install (paste-prompt every OS; CLI macOS/Windows; ZIP + restart) → run the skill workflow → verify format/license. To learn free originals, clone awesome-opus5-5-videos and re-render with Opus 5.5. New logo → brief + library research + 3 black SVG builds + audit loops + greyscale checkpoint (user picks) → kit (see `using-logo-design-skill.md`). Need a custom standard → re-sweep with Hallmark (`domains/ui/using-hallmark.md`).

### Using-doc list
- `using-skillry.md` — Skillry FOR media → origin `../../items/skillry/README.md`
- `using-awesome-opus5-5-videos.md` — awesome-opus5-5-videos FOR media → origin `../../items/awesome-opus5-5-videos/README.md`
- `using-logo-design-skill.md` — logo-design-skill FOR media → origin `../../items/logo-design-skill/README.md`
