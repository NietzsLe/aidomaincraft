# domains/game/

## Tiếng Việt

Domain game — mod game PC mình sở hữu bằng AI agent (recon → route → lab → slice chạy thật → assets → test + video → field note). Chi tiết gốc sống trong `items/universal-modder/README.md`; dùng CHO game thì đọc `using-universal-modder.md` tương ứng.

### Bảng điều hướng: việc → item(s)
| Việc cần làm | Item chính (mỗi cái 1 cách) | Item hỗ trợ | Lệnh bắt đầu |
|---|---|---|---|
| Mod mới cho game sở hữu (vật/weapon/boss/civ/cơ chế tới chạy thật + note) | `universal-modder` (vòng 10 bước + lab + verify — xem `using-universal-modder.md`) | — | `um kb search "<game>"` rồi `um scan "<game>"` |
| Assets đúng chuẩn engine (sprite/PBR/3D/SFX/music/voice + pipeline frames) | `universal-modder` (fal/ComfyUI + `sprite`/`render3d` — xem `using-universal-modder.md`) | — | `um fal sprite "<mô tả>" --out assets/gen --name <tên>` |
| Test trong game thật + video showcase 20–45s | `universal-modder` (`win` + `video` — xem `using-universal-modder.md`) | — | `um win shot --out shots/` rồi `um video compile edit.edl --out showcase.mp4` |
| Port mod / mashup 2 game / share field note | `universal-modder` (`port-a-mod`/`mashup-mods` + `um kb` — xem `using-universal-modder.md`) | — | `um kb new --game "<game>" --title "<gì>" --from-scan <game> --agent "<agent>"` |

Domain mới nên 1 item gánh 4 việc (mỗi việc 1 cách khác trong cùng hệ: recon-route-slice vs sinh-convert vs chạm-cắt vs port-PR). Tiêu chí phân biệt ở ma trận dưới.

### Bảng định vị
| Item | Mục đích điển hình | Vận hành tóm tắt 1 câu | Điểm mạnh | Điểm yếu | Dùng chính khi | Tránh khi | Thay thế bởi | Vì sao chọn A thay vì B trong case này |
|---|---|---|---|---|---|---|---|---|
| `universal-modder` — chi tiết game ở `using-universal-modder.md`, gốc ở `../../items/universal-modder/README.md` | mod game sở hữu khép kín tới chạy thật + note | Skill mod-any-game 10 bước + `um` CLI 15 groups + fal MCP + KB 242 notes | scan fingerprint + lab backup + slice verify + manifest + publish/kb check, 9,248★ MIT 0đ core | cần game sở hữu + Python/Git/ffmpeg, fal tốn tiền, Windows/WSL cho `win`, repo 1 tháng tuổi đổi nhanh | có game đã cài cần mod tới chạy thật + clip + note | build game mới, mod tay không AI, online anti-cheat/cheat | gamedev-skills khi build mới; BepInEx khi mod tay; từ chối khi cheat/bypass | Chọn universal-modder thay vì gamedev-skills khi quyết định phụ thuộc vào game đã sở hữu + route rẻ nhất + gotchas thật, không phải build mới |

### Ma trận chồng lấn
| Việc | `universal-modder` | Đối thủ ngoài | Tiêu chí chọn phân biệt |
|---|---|---|---|
| Mod mới tới chạy thật + note | chính (vòng 10 bước + KB + verify) | `gamedev-skills/awesome-gamedev-agent-skills` (6,121★, build game mới) không dùng | có game để scan + note khớp versions → universal-modder; build từ 0 → gamedev-skills |
| Assets chuẩn engine | chính (`fal` + `sprite`/`render3d` + manifest) | Skillry media taste / diffusion chung thay thế khi chỉ cần ảnh trang trí | cần frames engine nuốt + manifest → universal-modder; cần taste OG/deck nhanh → Skillry |
| Test + showcase | chính (`win` + `video` EDL) | quay màn hình chung thay thế khi không cần oracle game | cần launch/shot/drive/record game-only + EDL → universal-modder |
| Port/mashup/note | chính (mapping + bridge + `kb pr`) | `BepInEx` (8,935★, loader tay) thay thế khi chỉ cần framework viết tay | cần vòng agent + tests + note → universal-modder; chỉ cần loader viết tay → BepInEx |

### Workflow phối hợp mẫu
Intake 1 câu + chốt done → `kb search` + `scan` + playbook → shortlist route/skill/model (user pick) → backup lab → slice 1 món tới chạy thật → assets (`fal` + `sprite`/`render3d`, manifest) → verify (`win` + restore pristine) → showcase (`video` EDL) → `publish check` + `kb check` + note + PR sau human ok.

### Danh sách using-doc
- `using-universal-modder.md` — dùng universal-modder CHO game → gốc `../../items/universal-modder/README.md`

---

## English

Game domain — modding owned PC games with an AI agent (recon → route → lab → live slice → assets → test + video → field note). Origin details live in `items/universal-modder/README.md`; for game use read the matching `using-universal-modder.md`.

### Routing: job → item(s)
| Job | Primary item(s) (each a different way) | Supporting item | Starter command |
|---|---|---|---|
| New mod for an owned game (items/weapons/bosses/civs/mechanics to live + note) | `universal-modder` (10-step loop + lab + verify — see `using-universal-modder.md`) | — | `um kb search "<game>"` then `um scan "<game>"` |
| Engine-exact assets (sprites/PBR/3D/SFX/music/voice + frame pipeline) | `universal-modder` (fal/ComfyUI + `sprite`/`render3d` — see `using-universal-modder.md`) | — | `um fal sprite "<desc>" --out assets/gen --name <name>` |
| Live in-game testing + 20–45s showcase | `universal-modder` (`win` + `video` — see `using-universal-modder.md`) | — | `um win shot --out shots/` then `um video compile edit.edl --out showcase.mp4` |
| Port / 2-game mashup / field-note sharing | `universal-modder` (`port-a-mod`/`mashup-mods` + `um kb` — see `using-universal-modder.md`) | — | `um kb new --game "<game>" --title "<what>" --from-scan <game> --agent "<agent>"` |

New domain so 1 item carries 4 jobs (each a different way inside one system: recon-route-slice vs generate-convert vs touch-cut vs port-PR). Rules in the matrix below.

### Positioning
| Item | Typical purposes | 1-sentence operating summary | Strengths | Weaknesses | Use as primary when | Avoid when | Replaced by | Why pick A over B in this case |
|---|---|---|---|---|---|---|---|---|
| `universal-modder` — game details in `using-universal-modder.md`, origin at `../../items/universal-modder/README.md` | closed-loop owned-game modding to live + note | 10-step mod-any-game skill + 15-group `um` CLI + fal MCP + 242-note KB | scan fingerprint + backup lab + slice verify + manifests + publish/kb checks, 9,248 stars $0 MIT core | needs an owned game + Python/Git/ffmpeg, metered fal, Windows/WSL for `win`, 1-month-old fast-moving repo | an installed game must be modded to live + clip + note | new-game builds, hand modding, online anti-cheat/cheats | gamedev-skills for new builds; BepInEx for hand plugins; refused for cheats/bypass | Pick universal-modder over gamedev-skills when the owned game + cheapest route + real gotchas decide, not a new build |

### Overlap matrix
| Job | `universal-modder` | Outside opponent | Distinguishing selection rule |
|---|---|---|---|
| New mod to live + note | primary (10-step loop + KB + verify) | `gamedev-skills/awesome-gamedev-agent-skills` (6,121 stars, new-game builds) do-not-use | scannable game + version-matching notes → universal-modder; from-scratch build → gamedev-skills |
| Engine-exact assets | primary (`fal` + `sprite`/`render3d` + manifest) | Packaged media taste replaces for decorative images | engine-loadable frames + manifest → universal-modder; fast OG/deck taste → Skillry |
| Test + showcase | primary (`win` + EDL `video`) | Generic screen capture replaces without a game oracle | game-only launch/shot/drive/record + EDL → universal-modder |
| Port/mashup/note | primary (maps + bridges + `kb pr`) | `BepInEx` (8,935 stars, hand loader) replaces for framework-only needs | agent loop + tests + note → universal-modder; hand-written loader → BepInEx |

### Sample combined workflow
1-sentence intake + done → `kb search` + `scan` + playbook → shortlist route/skill/model (user picks) → backup lab → 1-item live slice → assets (`fal` + `sprite`/`render3d`, manifest) → verify (`win` + pristine restore) → showcase (EDL `video`) → `publish check` + `kb check` + note + PR after human ok.

### Using-doc list
- `using-universal-modder.md` — universal-modder FOR games → origin `../../items/universal-modder/README.md`
