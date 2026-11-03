# domains/reverse/

## Tiếng Việt

Domain reverse — hiểu 1 feature trong app/binary/website mình sở hữu bằng agent có evidence (Seen/Inferred/Unknown) rồi rebuild lại cho project mình. Chi tiết gốc sống trong `items/rea/README.md`; dùng CHO reverse thì đọc `using-rea.md` tương ứng.

### Bảng điều hướng: việc → item(s)
| Việc cần làm | Item chính (mỗi cái 1 cách) | Item hỗ trợ | Lệnh bắt đầu |
|---|---|---|---|
| Hiểu 1 feature app JS/Electron tĩnh (graph + Evidence, không engine) | `rea` (static parser built-in — xem `using-rea.md`) | — | `npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json` |
| Hiểu 1 feature native binary (pseudocode/trace có evidence) | `rea` (provider Hopper/Ghidra/IDA/Kuna — xem `using-rea.md`) | — | `rea analyze /absolute/path/to/program --provider ghidra --json` |
| Quan sát website/runtime 1 flow (structure/network/screenshot) | `rea` (browser thật + captures — xem `using-rea.md`) | — | `rea capture-browser-scenario` trong origin scope đã duyệt |
| Inventory artifact offline (managed/APK/firmware/model/SQLite) | `rea` (`inspect-*` tĩnh — xem `using-rea.md`) | — | `rea inspect-managed-artifact /absolute/path/Assembly.dll --json` |

Domain mới nên 1 item gánh 4 việc (mỗi việc 1 engine khác trong cùng hệ: static-parser vs provider-session vs browser-capture vs inspect-bytes). Tiêu chí phân biệt ở ma trận dưới.

### Bảng định vị
| Item | Mục đích điển hình | Vận hành tóm tắt 1 câu | Điểm mạnh | Điểm yếu | Dùng chính khi | Tránh khi | Thay thế bởi | Vì sao chọn A thay vì B trong case này |
|---|---|---|---|---|---|---|---|---|
| `rea` — chi tiết reverse ở `using-rea.md`, gốc ở `../../items/rea/README.md` | hiểu 1 feature bất kỳ (app/web/binary) có evidence để rebuild | 1 MCP + CLI gọi static parsers/providers/browser, trả Seen/Inferred/Unknown + confidence | phủ ~30 loại target 1 MCP, evidence chuẩn, 417.980★ MIT 0đ core, 1,17M tải/tháng | cần quyền/ToS/license engine, Node patch-gap, provider nặng, server-side là Unknown | cần agent tự trace 1 feature ra evidence từ câu hỏi 1 câu | mod game khép vòng, tokens site, rebuild 1:1, audit SEO | `universal-modder` khi cần slice game + note; Ghidra tay khi cần đọc từng instruction; Frida khi cần hook runtime sống | Chọn rea thay vì Ghidra tay khi quyết định phụ thuộc vào evidence + unknowns + rebuild từ agent, không phải đọc tay từng hàm |

### Ma trận chồng lấn
| Việc | `rea` | Đối thủ ngoài | Tiêu chí chọn phân biệt |
|---|---|---|---|
| Feature JS/Electron tĩnh | chính (static built-in, không engine) | đọc tay bằng DevTools thay thế khi app nhỏ | cần graph + Evidence chuẩn để agent trace → rea; chỉ xem nhanh 1 file → DevTools |
| Feature native binary | chính (provider session + dossier + snapshot) | `Ghidra` (96.696★, engine tay miễn phí) không dùng agent | cần agent trace + evidence + rebuild → rea; cần đọc tay từng instruction → Ghidra |
| Website/runtime 1 flow | chính (browser + captures + screenshots) | `ai-website-cloner-template` thay thế khi cần rebuild 1:1 thành Next.js | cần hiểu hành vi có evidence → rea; cần app chạy được → cloner |
| Inventory offline | chính (`inspect-*` + observed-absence) | tool lẻ theo loại (JADX/Apktool/tshark) thay thế khi chỉ cần 1 loại | cần nhiều loại 1 MCP + evidence chuẩn → rea; chỉ cần 1 loại → tool lẻ |
| Mod game tới chạy thật + note | không dùng | `universal-modder` (9.248★, vòng 10 bước + lab + slice) chính | cần slice game + assets + clip + note → universal-modder; cần hiểu feature chung → rea |

### Workflow phối hợp mẫu
Verify quyền/ToS/license → `rea setup` + `rea doctor` → shortlist target + provider + scope 1 feature (user pick) → phân tích theo usecase (static-JS / native-provider / web-capture / inspect) → lưu Evidence + project summary → trace Seen/Inferred/Unknown → rebuild 1 feature (không mang code/brand gốc) → test + compare → deliver lệnh + Evidence + unknowns.

### Danh sách using-doc
- `using-rea.md` — dùng rea CHO reverse → gốc `../../items/rea/README.md`

---

## English

Reverse domain — understand one feature inside an owned app/binary/website with an evidence-backed agent (Seen/Inferred/Unknown), then rebuild it for your own project. Origin details live in `items/rea/README.md`; for reverse use read the matching `using-rea.md`.

### Routing: job → item(s)
| Job | Primary item(s) (each a different way) | Supporting item | Starter command |
|---|---|---|---|
| Static one-feature understanding of a JS/Electron app (graph + Evidence, no engine) | `rea` (built-in static parsers — see `using-rea.md`) | — | `npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json` |
| One-feature understanding of a native binary (pseudocode/trace with evidence) | `rea` (Hopper/Ghidra/IDA/Kuna provider — see `using-rea.md`) | — | `rea analyze /absolute/path/to/program --provider ghidra --json` |
| One-flow website/runtime observation (structure/network/screenshots) | `rea` (real browser + captures — see `using-rea.md`) | — | `rea capture-browser-scenario` inside the approved origin scope |
| Offline artifact inventory (managed/APK/firmware/models/SQLite) | `rea` (static `inspect-*` — see `using-rea.md`) | — | `rea inspect-managed-artifact /absolute/path/Assembly.dll --json` |

New domain so 1 item carries 4 jobs (each a different engine inside one system: static parsers vs provider sessions vs browser captures vs inspect-bytes). Rules in the matrix below.

### Positioning
| Item | Typical purposes | 1-sentence operating summary | Strengths | Weaknesses | Use as primary when | Avoid when | Replaced by | Why pick A over B in this case |
|---|---|---|---|---|---|---|---|---|
| `rea` — reverse details in `using-rea.md`, origin at `../../items/rea/README.md` | understand any one feature (app/web/binary) with evidence for a rebuild | one MCP + CLI driving static parsers/providers/browsers, returning Seen/Inferred/Unknown + confidence | ~30 target kinds behind one MCP, standard evidence, 417,980 stars $0 MIT core, 1.17M monthly downloads | needs rights/ToS/engine licenses, Node patch gaps, heavy providers, server-side stays Unknown | an agent must trace one feature into evidence from a one-sentence question | closed-loop game modding, site tokens, 1:1 rebuilds, SEO audits | `universal-modder` for game slices + notes; hand Ghidra for per-instruction reading; Frida for live runtime hooks | Pick rea over hand Ghidra when agent-produced evidence + unknowns + rebuilds decide, not hand-reading every function |

### Overlap matrix
| Job | `rea` | Outside opponent | Distinguishing selection rule |
|---|---|---|---|
| Static JS/Electron feature | primary (built-in static, no engine) | hand DevTools reading replaces for tiny apps | standard graph + Evidence for agent traces → rea; one quick file look → DevTools |
| Native binary feature | primary (provider session + dossier + snapshot) | `Ghidra` (96,696 stars, free hand engine) for manual work | agent trace + evidence + rebuild → rea; per-instruction hand reading → Ghidra |
| Website/runtime flow | primary (browser + captures + screenshots) | `ai-website-cloner-template` replaces when a runnable 1:1 Next.js rebuild is needed | behavior understanding with evidence → rea; runnable app → cloner |
| Offline inventory | primary (`inspect-*` + observed absence) | single-kind tools (JADX/Apktool/tshark) replace for one kind only | many kinds behind one MCP + standard evidence → rea; exactly one kind → single tool |
| Game mod to live + note | do-not-use | `universal-modder` (9,248 stars, 10-step loop + lab + slice) primary | game slice + assets + clip + note → universal-modder; generic feature understanding → rea |

### Sample combined workflow
Verify rights/ToS/licenses → `rea setup` + `rea doctor` → shortlist target + provider + one-feature scope (user picks) → analyze per sub-usecase (static-JS / native-provider / web-capture / inspect) → persist Evidence + project summaries → trace Seen/Inferred/Unknown → rebuild one feature (no origin code/brand carried) → test + compare → deliver commands + Evidence + unknowns.

### Using-doc list
- `using-rea.md` — rea FOR reverse → origin `../../items/rea/README.md`
