# reactbits

## Tiếng Việt

### Dùng khi
- Project React/Next.js cần hiệu ứng có sẵn, copy source về sở hữu: text reveal cho headline, background động cho hero/section, micro-interaction cho button/toggle, card/carousel/gallery có sẵn.
- Muốn agent tự tìm + lắp component qua MCP thay vì viết tay từ đầu.
- Cần asset nhanh từ 5 tool free: Background Studio (xuất code/ảnh/MP4), Center Stage (biến screenshot thành product shot), Shape Magic (logo mark), Texture Lab (160 styles ảnh/video), Sound Lab (200 âm thanh UI).

### Bỏ qua khi
- Cần full page system, taste, gate chống AI-slop → dùng `../hallmark/`, React Bits chỉ là viên gạch hiệu ứng.
- Project không phải React (Vue/Svelte có port riêng `vue-bits.dev`, `sveltebits.xyz`, không lẫn vào đây).
- Yêu cầu reduced-motion/a11y nghiêm hoặc máy yếu: background shader/particle dễ vỡ Floor Hallmark (motion chỉ `transform/opacity`, loop >5s phải có pause, LCP <2MB, contrast trên nền động).
- Chỉ cần 1-2 hiệu ứng nhỏ: copy tay 1 file, đừng kéo cả registry/CLI vào project.

### Cài đặt
- Không cần cài toàn bộ lib. Mỗi component là source riêng, 4 biến thể: `JS/TS` + `CSS/TW` (ví dụ `SplitText-TS-TW`).
- CLI (khuyên dùng, qua shadcn): `npx shadcn@latest add @react-bits/SplitText-TS-TW` — đổi `SplitText` thành tên component, đuôi chọn variant.
- Hoặc jsrepo: `npx jsrepo@latest add https://reactbits.dev/r/SplitText-TS-TW`.
- Hoặc copy tay: mở tab Code của component, chọn ngôn ngữ + styling, paste file vào project, cài đúng dependencies ghi trong tab đó.
- Dùng với agent qua MCP: thêm vào `components.json`:
```json
{ "registries": { "@react-bits": "https://reactbits.dev/r/{name}.json" } }
```
rồi `npx shadcn@latest mcp init --client claude` (đổi client: claude/cursor/codex/vscode theo `get-started/mcp`). Sau đó hỏi agent bằng tên component cụ thể.
- License: MIT + Commons Clause, dùng cá nhân + thương mại được, source thuộc về bạn sau khi cài.

### Cách item hoạt động
- Tổ chức đứng sau: David Haz (DavidHDev), repo `github.com/DavidHDev/react-bits` (50.5k★), site `reactbits.dev`, MIT + Commons Clause.
- Phương thức hoạt động chung: copy source sở hữu theo variant (`-JS-TW/-TS-CSS...`) qua CLI shadcn/jsrepo/copy tay, hoặc MCP registry `@react-bits`; tune live trong tool Studio/Lab rồi export. Không có gates/review/system như Hallmark.
- Khác biệt vận hành theo usecase: text/background/component lắp 1 lệnh CLI/MCP theo tên; Center Stage/Shape Magic/Texture Lab/Sound Lab chạy trên web rồi export asset/video/GIF/`npx`, không qua CLI component.

### Định vị khác biệt
- So với engine animation viral (Motion / Framer Motion, GSAP — hàng triệu users, API thuần): engine cho sức mạnh motion tự code, React Bits 50.5k★ cho component lắp sẵn + demo + variant. Quyết định chọn React Bits khi cần 1 hiệu ứng cụ thể chạy ngay (`SplitText-TS-TW`, background, carousel) qua 1 lệnh MCP/CLI; cần motion custom phức tạp, timeline, ScrollTrigger → dùng Motion/GSAP thuần, đừng bọc qua React Bits.
- So với collection animated viral (Magic UI, Aceternity UI): cùng cho bricks copy-paste, khác ở React Bits có 4 biến thể rõ (`-JS-TW/-TS-CSS...`), registry MCP chuẩn (`@react-bits`), 5 tool Studio/Lab xuất asset/video/GIF. Quyết định chọn React Bits khi cần variant khớp stack + MCP + tool asset; chỉ cần 1 snippet Tailwind lẻ → Magic UI/Aceternity nhanh hơn.
- Khi nào dùng sẽ phù hợp: project React cần 1-2 motion có demo xem trước, sở hữu source, sau đó sweep lại bằng Hallmark để không vỡ gates.

### Bảng usecase con → cách dùng
| Việc | Lấy gì / lệnh nào |
|---|---|
| Headline cần chuyển động chữ | Nhóm Text Animations (33): `SplitText`, typewriter, rotating words, scroll reveal. VD: `npx shadcn@latest add @react-bits/SplitText-TS-TW` |
| Hero/section cần nền động | Nhóm Backgrounds (63): gradient/particle/grid/shader cho cả section. Tune live trong Background Studio rồi export code/ảnh/MP4 |
| Card/nav/carousel/gallery có sẵn | Nhóm Components (48): lắp nguyên cụm, tùy biến props |
| Nút/toggle/indicator nhỏ | Nhóm Micro (34): button, toggle, chi tiết giao diện nhỏ |
| Cursor/hover/border/ảnh hiệu ứng | Nhóm Animations (38): gắn vào element có sẵn |
| Cần product shot/video demo | Tool Center Stage: đưa screenshot/screen recording vào, xuất ảnh 4K/video/GIF |
| Cần logo mark/texture/âm thanh | Tool Shape Magic / Texture Lab / Sound Lab, xuất SVG/PNG/video hoặc `npx` 1 lệnh cho sound |

### Các bước chung
1. Chốt nhu cầu: hiệu ứng nào, đặt ở đâu (hero text, background section, nút), variant nào (`-TS-TW` cho Tailwind TS, `-JS-CSS` cho JS CSS thuần).
2. Mở trang component trên `reactbits.dev`, xem demo + controls, đọc dependencies trong tab Code.
3. Cài bằng 1 trong 3 đường (CLI shadcn / jsrepo / copy tay), chỉ lấy đúng component cần.
4. Gắn vào layout Hallmark có sẵn: giữ tokens, không để effect phá Floor (contrast, focus, reduced-motion, spacing, word budget).
5. Chạy thử ở desktop + mobile, đo LCP, tắt JS kiểm tra nội dung vẫn hiện, bật reduced-motion kiểm tra end-state.

### Prompt mẫu
- "Dùng React Bits lắp `SplitText-TS-TW` cho H1 trang <...>, variant TS + Tailwind, giữ tokens Hallmark hiện tại, motion chỉ transform/opacity, có reduced-motion fallback."
- "Dùng React Bits tìm 1 background nhóm Backgrounds cho hero <...>, tune trong Background Studio, export code, đảm bảo chữ trên nền đạt contrast 4.5:1 và LCP <2MB."
- "Lắp carousel/gallery từ React Bits nhóm Components cho <...>, qua MCP shadcn registry @react-bits, chỉ cài 1 component, liệt kê dependencies đã thêm."
- Ví dụ điền sẵn: "Dùng React Bits lắp `SplitText-TS-TW` cho H1 trang pricing của SaaS billing, variant TS + Tailwind, giữ tokens Hallmark, motion chỉ transform/opacity, có reduced-motion fallback."

### Pitfalls
- Lắp 3-4 effect cùng lúc → rối, vỡ Hallmark gate 8/9 (lặp composition) và 11 (nhiều hover trên 1 element).
- Quên đuôi variant (`-TS-TW` vs `-JS-CSS`) → sai stack, agent phải sửa lại.
- Background động đè chữ: chữ trên ảnh/nền động phải có scrim 35-65% + contrast 4.5:1, không đặt chữ trắng giữa frame busy.
- Loop/marquee/video >5s không có nút pause + không dừng khi hover/focus/off-screen/reduced-motion → vi phạm WCAG 2.2.2 + gate 18.
- Ảnh/video export quá nặng, hero visual >2MB → LCP fail; ảnh thư viện hotlink stock (Unsplash/Pexels/Pixabay) → vi phạm điều khoản + gate 76.
- Dùng React Bits để thay design system: nó không có tokens/gates/review như Hallmark, lắp xong vẫn phải sweep Hallmark.

### Tham khảo
- Trang chủ: https://reactbits.dev
- Cài đặt: https://reactbits.dev/get-started/installation
- MCP: https://reactbits.dev/get-started/mcp
- GitHub: https://github.com/DavidHDev/react-bits (215+ component, 5 nhóm theo README)
- Tools: https://reactbits.dev/tools (Background Studio, Center Stage, Shape Magic, Texture Lab, Sound Lab)
- Port khác: https://vue-bits.dev/, https://sveltebits.xyz/

### Quay lại index
- Về `../README.md` để so sánh định vị với `hallmark/`.
- Xem thêm item liên quan: `../hallmark/` để sweep lại system/gates sau khi lắp effect.

---

## English

### When to use
- React/Next.js project needing ready-made motion you own as source: headline text reveals, animated hero/section backgrounds, button/toggle micro-interactions, prebuilt card/carousel/gallery.
- Let the agent find + install components via MCP instead of hand-writing from scratch.
- Quick assets from 5 free tools: Background Studio (code/image/MP4 export), Center Stage (screenshot → product shot), Shape Magic (logo marks), Texture Lab (160 image styles), Sound Lab (200 UI sounds).

### When to skip
- Need a full page system, taste, anti-slop gates → use `../hallmark/`; React Bits is only motion bricks.
- Non-React project (separate ports: `vue-bits.dev`, `sveltebits.xyz`).
- Strict reduced-motion/a11y or weak devices: shader/particle backgrounds easily break Hallmark Floor (motion `transform/opacity` only, >5s loops need pause, LCP <2MB, contrast over motion).
- One or two tiny effects: hand-copy one file, do not pull the whole registry/CLI in.

### Install
- No full-library install. Each component is standalone source in 4 flavors: `JS/TS` + `CSS/TW` (e.g. `SplitText-TS-TW`).
- CLI (recommended, via shadcn): `npx shadcn@latest add @react-bits/SplitText-TS-TW` — swap the name, suffix picks the variant.
- Or jsrepo: `npx jsrepo@latest add https://reactbits.dev/r/SplitText-TS-TW`.
- Or by hand: open the component Code tab, pick language + styling, paste files, install the listed dependencies.
- With agents via MCP: add to `components.json`:
```json
{ "registries": { "@react-bits": "https://reactbits.dev/r/{name}.json" } }
```
then `npx shadcn@latest mcp init --client claude` (swap client per `get-started/mcp`). Then ask by exact component name.
- License: MIT + Commons Clause, personal + commercial OK, source is yours after install.

### How the item works
- Backing organization: David Haz (DavidHDev), repo `github.com/DavidHDev/react-bits` (50.5k★), site `reactbits.dev`, MIT + Commons Clause.
- Core operating method: copy owned source by variant via shadcn CLI/jsrepo/hand copy, or `@react-bits` MCP registry; tune live in Studio/Lab tools then export. No gates/review/system like Hallmark.
- Per-usecase operating differences: text/background/component installs with 1 CLI/MCP command by name; Center Stage/Shape Magic/Texture Lab/Sound Lab run on the web then export assets/video/GIF/`npx`, not via the component CLI.

### Differentiating positioning
- Vs viral animation engines (Motion / Framer Motion, GSAP — millions of users, raw APIs): engines give hand-coded motion power, React Bits 50.5k★ gives ready components + demos + variants. Pick React Bits when one concrete effect must run now (`SplitText-TS-TW`, background, carousel) via 1 MCP/CLI command; complex custom motion, timelines, ScrollTrigger → use raw Motion/GSAP, not wrapped via React Bits.
- Vs viral animated collections (Magic UI, Aceternity UI): same copy-paste bricks, different in 4 explicit variants, standard MCP registry (`@react-bits`), 5 Studio/Lab asset tools. Pick React Bits when variant-to-stack fit + MCP + asset tools decide; one lone Tailwind snippet → Magic UI/Aceternity is faster.
- When it fits: React project needing 1-2 previewable motions as owned source, then re-swept by Hallmark so gates hold.

### Sub-usecase → usage table
| Job | What to take / command |
|---|---|
| Animated headline | Text Animations (33): `SplitText`, typewriters, rotating words, scroll reveals. E.g. `npx shadcn@latest add @react-bits/SplitText-TS-TW` |
| Animated hero/section background | Backgrounds (63): gradients/particles/grids/shaders. Tune in Background Studio, export code/image/MP4 |
| Ready card/nav/carousel/gallery | Components (48): install the block, tune props |
| Small button/toggle/indicator | Micro (34) |
| Cursor/hover/border/image effects | Animations (38): attach to an existing element |
| Product shot/demo video | Center Stage: feed a screenshot/recording, export 4K image/video/GIF |
| Logo mark/texture/sound | Shape Magic / Texture Lab / Sound Lab, export SVG/PNG/video or one-command sound install |

### Shared steps
1. Fix need: which effect, where (hero text, section background, button), which variant (`-TS-TW` for TS+Tailwind, `-JS-CSS` for plain JS+CSS).
2. Open the component page on `reactbits.dev`, check live demo + controls, read Code-tab dependencies.
3. Install via exactly one route (shadcn CLI / jsrepo / hand copy), only the needed component.
4. Fit into the existing Hallmark layout: keep tokens; never let the effect break Floor (contrast, focus, reduced-motion, spacing, word budget).
5. Test desktop + mobile, measure LCP, disable JS to confirm content still shows, enable reduced-motion for end-state.

### Sample prompts
- "Use React Bits to install `SplitText-TS-TW` for the H1 of <...>, TS + Tailwind variant, keep current Hallmark tokens, transform/opacity motion only, reduced-motion fallback."
- "Use React Bits to pick one Backgrounds-group background for hero <...>, tune in Background Studio, export code, keep 4.5:1 text contrast and LCP <2MB."
- "Install a carousel/gallery from React Bits Components group for <...>, via @react-bits shadcn MCP registry, install exactly one component, list added dependencies."
- Filled example: "Use React Bits to install `SplitText-TS-TW` for the H1 of the pricing page of a SaaS billing app, TS + Tailwind variant, keep Hallmark tokens, transform/opacity only, reduced-motion fallback."

### Pitfalls
- 3-4 effects at once → noise, breaks Hallmark gates 8/9 (repeated composition) and 11 (many hovers on one element).
- Wrong variant suffix (`-TS-TW` vs `-JS-CSS`) → stack mismatch, rework.
- Animated background under text: scrim 35-65% + 4.5:1 contrast required; never white centered text over a busy frame.
- >5s loop/marquee/video without pause control + no hover/focus/off-screen/reduced-motion stop → WCAG 2.2.2 + gate 18 violation.
- Heavy exports, hero visual >2MB → LCP fail; hotlinked stock images (Unsplash/Pexels/Pixabay) → terms + gate 76 violation.
- Using React Bits as a design system: no tokens/gates/review like Hallmark — still sweep with Hallmark after install.

### References
- Home: https://reactbits.dev
- Install: https://reactbits.dev/get-started/installation
- MCP: https://reactbits.dev/get-started/mcp
- GitHub: https://github.com/DavidHDev/react-bits (215+ components, 5 groups per README)
- Tools: https://reactbits.dev/tools (Background Studio, Center Stage, Shape Magic, Texture Lab, Sound Lab)
- Other ports: https://vue-bits.dev/, https://sveltebits.xyz/

### Back to index
- Back to `../README.md` to compare positioning with `hallmark/`.
- Related item: `../hallmark/` to re-sweep system/gates after installing effects.
