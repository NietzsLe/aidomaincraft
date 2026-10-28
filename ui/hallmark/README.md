# hallmark

## Tiếng Việt

### Dùng khi
- Build trang/landing mới muốn thoát mùi AI-slop, có gate quét máy + review mắt lạnh.
- Có URL/dev server/app chạy được muốn chụp màn hình thật thay vì mock.
- Redesign/audit trang có sẵn mà vẫn giữ content + wiring.
- Làm component lẻ cần đủ 8 states, hoặc app-screen (dashboard/admin/settings) cần density + 4 trạng thái data.

### Bỏ qua khi
- Sửa logic thuần, không đụng bề mặt UI.
- Sửa nhỏ trong project có sẵn mà không muốn đổi system: sửa trực tiếp, đừng gọi Hallmark. Luật `redesign.md`: request không nêu tên Hallmark thì không bao giờ load file đó.

### Cài đặt (OpenCode)
- Cần Node 18+. Render tier cần thêm `npm i -g puppeteer-core` + Chrome (hoặc `CHROME_PATH`). Không có thì `sloplint` chỉ chạy tier tĩnh và phải ghi rõ trong handoff là render chưa chạy.
- Cài: `npx skills add nutlope/hallmark -g --agent opencode` (bỏ `-g` nếu chỉ cài cho dự án hiện tại). Skill nằm ở `~/.config/opencode/skills` cộng các path Claude/Codex mà OpenCode cũng đọc; gọi bằng `/hallmark <prompt>`.
- Kiểm tra: `/hallmark` phải kích hoạt được skill. Nếu agent có plan-mode bị deny edit thì dừng lại, không paste code vào chat. Nếu bash hỏi quyền, allow `node *` cho session, không sửa file permission config.
- Từ clone: `node skills/hallmark/scripts/install.mjs` để validate theme/reference trước khi copy. `install-hook.mjs` chỉ có tác dụng edit-time trên Claude Code, OpenCode không có.

### Cách item hoạt động
- Tổ chức đứng sau: Together AI / Nutlope, repo `github.com/Nutlope/hallmark` (39.5k★), skill `skills/hallmark/SKILL.md` v2.0.0, MIT, update theo gates + themes.
- Phương thức hoạt động chung: gates máy (`sloplint.mjs`) + scaffold tokens (`theme.mjs scaffold`) + deal theme/draw shape + hero-first + fresh-context review + log rotation. Không phải generator vẽ tự do: mọi output phải pass Floor mới được ship.
- Khác biệt vận hành theo usecase: build mới chạy đủ pre-flight/deal/draw/scaffold/hero/sweep; component bỏ deal theme + hero, bắt 8 states + preview, sweep `--scope component`; app-screen bỏ hero/shape/budget, scaffold `--scope app`, sweep `--scope app`; redesign chạy `--before/--kept/compare.html` giữ content + wiring; audit dừng ở báo cáo, không sửa file.

### Định vị khác biệt
- So với generator UI viral (v0 by Vercel, Lovable — draft nhanh, hàng triệu users): Hallmark 39.5k★ chậm hơn ở draft đầu vì phải pre-flight + deal theme + hero-first + sweep, nhưng quyết định chọn Hallmark khi output phải pass gates máy (contrast 4.5:1, focus-visible 3:1, fold 1280x800, word budget ~80/900px, cấm bịa metric). Cần draft nhanh không cần gates → dùng generator nhanh, đừng dùng Hallmark.
- So với lib component viral (shadcn/ui — copy-paste component đẹp): shadcn cho bricks, không cho taste + gates + review. Quyết định chọn Hallmark khi cần system đồng nhất nhiều page (tokens 1 nơi, `design.md` lock, log rotation chống lặp shape). Chỉ cần 1-2 component lẻ → shadcn/React Bits nhanh hơn.
- Khi nào dùng sẽ phù hợp: landing/app-screen phải đạt chuẩn merge, có dev server để render check, chấp nhận trả giá pre-flight + sweep để đổi lấy không còn mùi AI-slop.

### Bảng usecase con → lệnh dùng
| Việc | Lệnh |
|---|---|
| Build trang mới | `/hallmark <prompt>` hoặc `use hallmark to build ...` |
| 1 component (button/input/card/modal/nav/footer/tab/chip...) | `/hallmark` + nêu đúng 1 element, yêu cầu 8 states + file preview, sweep `sloplint --scope component` |
| App-screen | `/hallmark` + nêu `dashboard/admin/settings/tool`, yêu cầu `scaffold --scope app`, sweep `--scope app` |
| Redesign full (giữ content + wiring, đổi system + composition) | `/hallmark redesign <path>` |
| Restyle (giữ layout, đổi system) | `/hallmark redesign <path>` + ghi rõ `keep the layout` |
| Polish (giữ system + layout, chỉ sửa tells) | `/hallmark redesign <path>` + ghi rõ `polish` |
| Audit (chỉ báo cáo, không sửa file) | `/hallmark audit <path>` |
| Custom, bỏ theme | thêm `custom` trong prompt, load `direction.md` thay vì layout/genre/theme |
| Build nhanh | thêm `--fast` hoặc `quick/rough/prototype`: bỏ tier Finish, Reflex waive bằng 1 dòng lý do, Floor/stamp/tokens/log vẫn giữ |
| Khóa system nhiều trang | yêu cầu ghi `design.md` sau scaffold (`references/design-md.md`) |
| Xuất tokens | yêu cầu dịch `tokens.css` sang Tailwind v4/v3, DTCG `tokens.json`, hoặc map shadcn (`references/export-formats.md`) |
| Lint trang bất kỳ | `node skills/hallmark/scripts/sloplint.mjs <file-or-dir> --render` |

### Các bước chung (build trang mới)
1. **Pre-flight, đọc trước khi hỏi.** Thứ tự: `design.md` ở root (nếu có thì override toàn bộ, bỏ deal theme); `.hallmark/brand-spec.md` hoặc brand nêu tên (chạy `brand-truth.md`, không theme brand thật từ trí nhớ); `package.json`/Tailwind config/`:root`/fonts; sản phẩm thật (URL, dev server, project start bằng 1 lệnh, app trên máy) để `capture.mjs` chụp; signal 8 Inspo MCP (nếu có, archive làm design, Hallmark chỉ sweep); `TOGETHER_API_KEY` (signal 9, comp trước build). Cache vào `.hallmark/preflight.json`. Output 1 block `Pre-flight findings: fonts/palette/motion/spacing/framework + preserve/introduce`. Không tín hiệu nào thì ghi 1 dòng và chạy full Hallmark stack.
2. **Hỏi 1 lần.** Template: material quan trọng nhất là gì (screenshot/screen recording, ảnh, số thật, quote có tên người nói, logo được phép dùng — thiếu thì dùng stand-in trong slot, không bịa); audience; 1 action trang phải lái tới; tone cực đoan (editorial/brutalist/soft/utilitarian/luxury/playful/technical/austere, cấm `clean and modern`) + vibe 4-8 từ + màu neo nếu có. Hoặc `go ahead` để agent tự suy luận và ghi rõ đã chốt gì. Song song: đoán genre thầm lặng — AI/dev-tool → `modern-minimal`, playful/kids/game → `playful`, AI/music/video/dark → `atmospheric`, còn lại `editorial`; theme đã deal thì genre của theme thắng. Scope: prompt nêu 1 element hoặc `just the X` → component; màn hình sau login/bảng/form/control → app-screen.
3. **Shape từ job, không từ template.** Đọc đúng job trong `anatomy.md`: subscribe (action là field email ngay hero, section là sample issue + archive, kết bằng field thứ 2); book (booking picker ở nav + hero + lặp cạnh menu, section ảnh phòng/món + timetable/schedule + giờ/địa chỉ); visit (giờ + địa chỉ ở nav/hero); attend (vé ở nav từ màn hình đầu, headline là ngày + địa điểm); buy (Offer + giá + options là hero, kết bằng offer/guarantee, cấm email-close); try (store/download button dưới head, feature là screen thật); sign up (start free + 1 dòng điều khoản, có install command/code sample/pricing + period switch); hire (contact thường ở nav + sau work, work là list/index project); join (join/first visit ở hero, schedule + membership rows); listen (release mới + nút listen/buy cạnh nhau). Page xây từ anatomy này + 21 shape trong `macrostructures.md` (chỉ load file shape đã chọn) + draw: `theme.mjs draw --material photo|product|words --job <job> --theme <slug>`. Test gương: prompt сосед cùng category có ra đúng combo này không, nếu có thì đổi 1 quyết định và ghi rõ.
4. **Deal direction.** Quy tắc: user nêu tên theme → build theme đó; user ghi `custom` → `direction.md`; còn lại deal: `node <skill-dir>/scripts/theme.mjs deal --genre <genre> --prompt "<prompt>" [--log .hallmark/log.json]` → deal 3 theme kèm ảnh, chọn 1 (nêu rõ vì sao, material nào gánh được prompt), chỉ load đúng 1 file `references/themes/<slug>.md` + ảnh. Re-deal chỉ khi user yêu cầu. Theme là vật liệu, không phải dàn bài: theme thắng shape/genre/craft khi mâu thuẫn vật liệu, Floor và lời user thắng theme.
5. **Load đúng set.** Page build: `layout.md` + đúng phần job trong `anatomy.md` + `imagery.md` + `craft.md` + `genres/<genre>.md` + theme file + ảnh theme + `gates.md` §1-4. Custom: `direction.md` thay layout/genre/theme. Chỉ load thêm khi cần: 1 macrostructure, `microinteractions.md`, `interaction-and-states.md` cho form, `responsive.md`, `texture.md`, `scroll-choreography.md`, `dark-mode.md`, `data-viz.md`, `fonts.md`, `comp.md` (signal 9), `design-md.md` để lock. `gates.md` §5 đợi Step 7, §6 cho review.
6. **Picks block (1 lần duy nhất).** Ghi Shape/draw/genre/job, Theme (dealt mấy/3 + vì sao), Chrome (nav/footer), Hero (posture + slot), Signature (1 thứ đáng nhớ nhất, vật liệu của theme, ở màn hình đầu), Sections, Material (real/pictures/absent), Sweep. Custom có rows riêng trong `direction.md`. Ghi `System portable? Say lock the system for a design.md` trừ component scope.
7. **Build từ scaffold.** `node <skill-dir>/scripts/theme.mjs scaffold <slug>` (--dealt/--custom/--redesign/--scope app/--brand khi tương ứng) viết `tokens.css` + `base.css` cạnh stylesheet project, in skeleton stamp + 2 imports + slot script. Chỉ viết page, không viết ngoài. Đọc `patterns.md` 1 lần: control 8 states, slot, missing fact, form `data-endpoint=""`, 1 reveal, figures so sánh. **Hero trước:** viết nav + hero, chạy `sloplint.mjs <file> --render --stage hero` + hero review fresh-context (`review-hero.md`, reviewer đọc prompt đó, không mở `review-*.md`), hero đạt mới build sections. Chuẩn số: h1 7 từ/50 ký tự, 1 câu 12 từ + 1-2 actions; 6-9 section (hero+footer tính trong, 5 nếu prompt mỏng); tối đa 450 từ hiển thị, ~80 từ/900px window; h1 `--text-display` 84px, h2 `--text-section` 52px, h3 `--text-title` 25px, lead 21px, body 16px/1.5-1.65, label 14px; container 1440 gutter 64 (content 1312 ở 1440, giữ 1312 ở 1920), 12 cột gap 32; gap section 120/144/176 trộn lẫn; ảnh dưới hero chiếm 1/4-1/3 page (Photographic/Portfolio Grid tối đa 45%), không 2 section ảnh liên tiếp; nav 1 dòng 56-80px, footer 200-400px.
8. **Imagery theo thứ tự:** (1) ảnh user đưa, (2) screenshot sản phẩm thật bằng `capture.mjs http://localhost:3000 --routes /,/settings --sizes desktop,phone [--selector ...] [--full]`, desktop app qua `--cdp 9222`, (3) build sản phẩm bằng HTML chỉ khi chưa capture được, (4) ảnh thư viện `theme.mjs photos "<chủ thể cụ thể>" --theme <slug> [--n 3] [--orient ...]`, chỉ dùng URL script in ra (cấm Unsplash/Pexels/Pixabay, cấm viết URL từ trí nhớ), credit mọi ảnh thư viện ở footer `data-credits`, (5) generated stills chỉ khi có `TOGETHER_API_KEY` + user yêu cầu, (6) type cỡ lớn nếu prompt về chữ. Slot: `data-slot` + `data-alt` + `aspect-ratio`, luôn hiển thị gì đó (cấm wash trống 300x200, cấm nhãn placeholder), tối đa 4 slot/row và 5 slot trống/page, ảnh trong slot phủ treatment của theme, hero photo là LCP (`fetchpriority=high`, không lazy, 2400px+ nếu full-bleed). Capture đóng khung bằng radius + inset outline của theme, cấm browser bar/traffic lights/phone frame vẽ tay.
9. **Sweep đến sạch.** `sloplint.mjs <files> --genre <genre> --render` (framework project: thêm `--url http://localhost:<port>/<route>` khi dev server chạy). Sửa mọi FAIL, fix hoặc waive mọi REFLEX (waiver trong stamp: `/* Hallmark · waive 47b · one frame, real terminal capture · ... */`, 3 field, 1 waiver/gate, cấm waive Floor). Đọc `gates.md` §5, walk J + R/J. Finish review fresh-context (`review-finish.md`): hành động theo từ đầu tiên (`recapture/rebuild/fix/ship`), tự score `resolved/partial/unresolved`, chỉ gửi recapture chấm lại 1 vòng khi `rebuild` hoặc có Floor. Budget: 1 batch inspect + 1 batch fix + tối đa 1 vòng confirm. Đóng bằng material ask (slot nào, cỡ nào, thiếu gì nhất) + cập nhật Picks block (rows đổi + dòng outcome `Floor 0 FAIL · Reflex ... · finish-review ...`) + log `theme.mjs log --entry '<json>'` (shape/theme/axes/hero/nav/footer/imagery/photos/sections/signature/waived/prompt/fingerprint). Không ship khi còn FAIL/REFLEX mở, Finish nào cũng phải answered.
10. **Stamp dòng 1 CSS.** Skeleton từ scaffold điền đủ field + critique line (`pre-emit critique: P/H/E/S/R/V`, trục yếu nhất + fix) + waivers/dismissed/answered trong 40 dòng đầu. Ví dụ component: `/* Hallmark · component: Button · genre: modern-minimal · theme: Coral · states: 8 · contrast: pass · v2.0.0 */`.

### Prompt mẫu (copy-paste)
- Build: `Dùng hallmark build landing cho job <subscribe/book/...>, audience <ai>, action chính <...>. Material có: <ảnh/số/quote/logo thật>. Tone <editorial/...>, vibe <4-8 từ>. Không bịa số liệu. Chạy pre-flight, deal theme, hero-first, sloplint --render.`
- Component: `Dùng hallmark làm đúng 1 <Button>, 8 states đầy đủ (default/hover/focus-visible/active/disabled/loading/error/success), tokens qua Hallmark, xuất <Button.tsx + button.css + preview>, stamp component, sweep --scope component.`
- App-screen: `Dùng hallmark làm app-screen <transactions table>, scope app: scaffold --scope app, density 32-40px hit 44px, 4 states loading/empty/error/full, state trong URL, màu restrained, sweep --scope app.`
- Redesign: `Dùng hallmark redesign <path>, depth full, giữ content + wiring + brand. Liệt kê route/file/pages + Files sẽ sửa trước khi làm, chạy sloplint --before + --kept + compare.html.`
- Audit: `Dùng hallmark audit <path>, chỉ báo cáo theo tier + file:line, không sửa file.`
- Ví dụ điền sẵn: `Dùng hallmark build landing cho job sign up (SaaS), audience dev, action chính Start free. Material có: screenshot app ở /docs/app.png, số thật 2-phút setup. Tone modern-minimal, vibe gọn-kỹ thuật-tin cậy, màu neo xanh. Không bịa số liệu. Chạy pre-flight, deal theme, hero-first, sloplint --render.`

### Pitfalls (lỗi Hallmark bắt nhiều nhất)
- Bịa metric/testimonial/logo wall/case count (46a Floor), bịa route/link, form báo `Sent` khi chưa có endpoint (70 Floor): thay bằng text slot + `data-endpoint=""` + câu `Nothing was sent...`.
- Eyebrow + tracked-caps label + middle-dot `A · B · C` + mũi tên `→` + status dot (54/67/63 Floor): nhãn dùng body face nhỏ hơn 1 nấc, sentence case, không tracking; mở section bằng 12 cách trong `craft.md` §7.
- Copy AI-slop (19 Floor): `seamless/robust/elevate/unlock`, `Not a feature. A platform`, `quietly trusted by`, `Learn more/Get started/Book a demo`, `Acme/Nexus`, dash `—/–`, mở đầu `Built for the modern team`.
- Gradient tím-xanh/lục-tím/cyan-on-dark, gradient text, card-trong-card, emoji làm icon, browser/OS vẽ tay (2a/4/30a/47a Floor): 1 anchor hue + solid ink, 1 containment layer, 1 icon set (Lucide 16/20/24/32px, `currentColor`).
- `transition: all`, animate width/height/top/left (10a Floor); focus ring fade-in (15 Floor), thiếu `:focus-visible` 3:1 (26a Floor), thiếu reduced-motion (27 Floor), content ẩn khi tắt JS (62 Floor).
- Hero sai fold: headline + 1 câu + action chính phải lọt 1280x800 không scroll (44b Floor); hero `vh` phải là `dvh/svh` (6a Floor); container không max-width ở 1920 (44d Floor); `overflow-x` thiếu `clip` hoặc dùng `100vw` (34 Floor); chữ/button tràn ở 320-1920 (49a Floor).
- Vượt word budget (~80 từ/900px, hero 2 block text) (58 Floor); section head <40px ở 1440 (78 Reflex); section mỏng không mass (77 Reflex); ảnh >1/3 page (83 Reflex); photo wall, empty wash 300x200 (81 Reflex), drawing SVG minh họa (80 Reflex), counting device (82 Reflex).
- Waiver sai: waive Floor, 1 waiver cho nhiều gate, lý do chung chung <24 ký tự hoặc copy lặp. Đúng: `/* Hallmark · waive 47b · one frame, real terminal capture · ... */` + guard kiểm được.
- Redesign: xóa `id/name/key/type/href/data-testid`/handler/route mà không có file-plan user duyệt; không chạy `--kept` nên mất link/field; không chụp `--before` nên không có `compare.html`; polish/redesign lẫn depth.

### Tham khảo
- Repo: https://github.com/Nutlope/hallmark
- Đọc theo thứ tự: `skills/hallmark/SKILL.md` (Floor + Flow 0-7) → `references/anatomy.md` (10 job) → `references/flow.md` (component/app-screen/fast/signal 8-9/harness + OpenCode) → `references/redesign.md` (full/restyle/polish/audit) → `references/gates.md` (Floor/Reflex/Finish + 6 reviews) → `references/layout.md` (canvas/sizes/hero/compositions) → `references/imagery.md` (capture/photos/slots) → `references/craft.md` (type/colour/motion/copy) → `references/patterns.md` (code mẫu control/slot/form/reveal/stats/loop/skip).
- Scripts: `theme.mjs deal/draw/scaffold/log/photos`, `sloplint.mjs --render/--stage hero/--scope/--genre/--url/--before/--kept`, `capture.mjs --routes/--sizes/--selector/--cdp`, `install.mjs`, `install-hook.mjs` (Claude Code only).

### Quay lại index
- Về `../README.md` để so sánh định vị với `reactbits/`.
- Xem thêm item liên quan: `../reactbits/` khi cần 1 hiệu ứng/component React có sẵn rồi sweep lại bằng Hallmark.

---

## English

### When to use
- Build a new page that must not read AI-generated, with machine gates + cold review.
- A reachable URL/dev server/app exists so real screenshots replace mocks.
- Redesign/audit existing UI while keeping content + wiring.
- Single components needing 8 states, or app-screens needing density + 4 data states.

### When to skip
- Logic-only change with no UI surface.
- Small tweak without a system change: edit directly. Unnamed Hallmark requests never load Hallmark (`redesign.md`).

### Install (OpenCode)
- Node 18+. Render tier needs `npm i -g puppeteer-core` + Chrome (or `CHROME_PATH`). Without it, sloplint runs static only — say so in the handoff.
- Install: `npx skills add nutlope/hallmark -g --agent opencode` (drop `-g` for current project). Skill lives under `~/.config/opencode/skills` plus Claude/Codex paths OpenCode reads; invoke `/hallmark <prompt>`.
- Verify `/hallmark` fires. A plan-mode agent with denied edits must stop, not paste code in chat. For bash permission prompts, allow `node *` for the session; do not edit permission config.
- From clone: `node skills/hallmark/scripts/install.mjs` validates themes/references before copy. `install-hook.mjs` is Claude Code edit-time only.

### How the item works
- Backing organization: Together AI / Nutlope, repo `github.com/Nutlope/hallmark` (39.5k★), skill `skills/hallmark/SKILL.md` v2.0.0, MIT, updated with gates + themes.
- Core operating method: machine gates (`sloplint.mjs`) + token scaffold (`theme.mjs scaffold`) + theme deal/shape draw + hero-first + fresh-context review + log rotation. Not free drawing: nothing ships with open FAIL.
- Per-usecase operating differences: new build runs full pre-flight/deal/draw/scaffold/hero/sweep; component skips theme deal + hero, requires 8 states + preview, `--scope component` sweep; app-screen skips hero/shape/budget, `--scope app` scaffold + sweep; redesign runs `--before/--kept/compare.html` keeping content + wiring; audit stops at the report, changes nothing.

### Differentiating positioning
- Vs viral UI generators (v0 by Vercel, Lovable — fast drafts, millions of users): Hallmark 39.5k★ is slower at first draft (pre-flight + theme deal + hero-first + sweep), but pick Hallmark when output must pass machine gates (contrast 4.5:1, focus-visible 3:1, 1280x800 fold, ~80-word/900px budget, no invented metrics). Need a fast draft without gates → use a fast generator, not Hallmark.
- Vs viral component libs (shadcn/ui — copy-paste components): shadcn gives bricks, not taste + gates + review. Pick Hallmark when a unified multi-page system is needed (single tokens source, `design.md` lock, log rotation against shape repetition). One or two lone components → shadcn/React Bits is faster.
- When it fits: landing/app-screen must meet merge bar, dev server available for render checks, willing to pay pre-flight + sweep cost to remove AI-slop.

### Sub-usecase → command table
| Job | Command |
|---|---|
| New page | `/hallmark <prompt>` or `use hallmark to build ...` |
| One component | `/hallmark` naming exactly one element, require 8 states + preview file, `sloplint --scope component` |
| App-screen | `/hallmark` stating app-screen, require `scaffold --scope app`, `--scope app` sweep |
| Full redesign | `/hallmark redesign <path>` |
| Restyle, keep layout | `/hallmark redesign <path>` plus `keep the layout` |
| Polish only | `/hallmark redesign <path>` plus `polish` |
| Audit only | `/hallmark audit <path>` |
| Custom, no theme | add `custom`, load `direction.md` |
| Fast | add `--fast` or `quick/rough/prototype` |
| Multi-page system lock | request `design.md` after scaffold (`design-md.md`) |
| Token export | request Tailwind v4/v3, DTCG `tokens.json`, or shadcn mapping (`export-formats.md`) |
| Lint any page | `node skills/hallmark/scripts/sloplint.mjs <file-or-dir> --render` |

### Shared steps (new page)
1. **Pre-flight before asking.** Order: root `design.md` (overrides all, skips theme deal); `.hallmark/brand-spec.md` or named brand (`brand-truth.md`, never theme a real brand from memory); `package.json`/Tailwind/`:root`/fonts; real product (URL/dev server/one-command project/on-machine app) for `capture.mjs`; Inspo MCP signal 8 (archive designs, Hallmark only sweeps); `TOGETHER_API_KEY` signal 9 (comp before build). Cache `.hallmark/preflight.json`. Emit one `Pre-flight findings` block. No signals → one line, full Hallmark stack.
2. **Ask once.** Material (real photos/numbers/quotes/logos or slots, never invented), audience, one action, extreme tone (never `clean and modern`) + 4-8 word vibe + anchor colour. Or `go ahead` with stated inferences. Silently detect genre (AI/dev-tool → `modern-minimal`, playful/kids/game → `playful`, AI/music/video/dark → `atmospheric`, else `editorial`); dealt theme genre wins. Scope: one named element/`just the X` → component; behind-login/table/form/control screen → app-screen.
3. **Shape from job.** Read the exact job in `anatomy.md` (subscribe/book/visit/attend/buy/try/sign up/hire/join/listen for action placement, native sections, close). Build from 21 shapes in `macrostructures.md` (load only the chosen one) + `draw --material photo|product|words --job <job> --theme <slug>`. Mirror test: would a neighbouring prompt in the same category get this combo — if yes, change one decision on record.
4. **Deal direction.** Named theme → build it; `custom` → `direction.md`; else `theme.mjs deal --genre <genre> --prompt "..."` → pick 1 of 3 with reason, load only `references/themes/<slug>.md` + picture. Theme is material, not outline; Floor + user words beat theme.
5. **Load exact set.** Page: `layout.md` + job slice of `anatomy.md` + `imagery.md` + `craft.md` + `genres/<genre>.md` + theme file/picture + `gates.md` §1-4. Custom: `direction.md` instead of layout/genre/theme. Add-ons only as needed. `gates.md` §5 at Step 7, §6 for reviews.
6. **Picks block (once).** Shape/draw/genre/job, Theme (dealt x/3 + why), Chrome (nav/footer), Hero (posture + slot), Signature, Sections, Material (real/pictures/absent), Sweep. Plus `lock the system` line unless component scope.
7. **Build from scaffold.** `theme.mjs scaffold <slug>` writes `tokens.css` + `base.css` + stamp skeleton + imports + slot script. Read `patterns.md` once. **Hero first:** nav + hero only, `sloplint --render --stage hero` + fresh-context hero review before sections. Budgets: h1 ≤7 words/50 chars + ≤12-word sentence + 1-2 actions; 6-9 sections incl. hero+footer; ≤450 visible words, ~80/900px window; h1 84px, h2 52px, h3 25px, lead 21px, body 16px/1.5-1.65, label 14px; container 1440/gutter 64 (1312 content, held at 1920), 12 cols gap 32; section gaps 120/144/176 mixed; photos 1/4-1/3 below hero; nav 56-80px, footer 200-400px.
8. **Imagery priority:** (1) user images, (2) real-product screenshots via `capture.mjs`, (3) HTML-built product only if uncapturable, (4) library via `theme.mjs photos "<concrete subject>"` (use only printed URLs, credit in footer `data-credits`), (5) generated stills only with key + request, (6) full-scale type for word prompts. Slots carry `data-slot` + `data-alt` + `aspect-ratio`, always show something, ≤4 per row / 5 empty per page, theme treatment on all, hero photo is LCP. Frame captures with theme radius + inset outline, never drawn browser/device chrome.
9. **Sweep to clean.** `sloplint <files> --genre <genre> --render` (framework: `--url http://localhost:<port>/<route>` with dev server). Fix all FAIL; fix/waive all REFLEX with stamp waiver (3 fields, one gate each, Floor never waived). Walk `gates.md` §5 J + R/J. Fresh-context finish review: act on first word (`recapture/rebuild/fix/ship`), self-score `resolved/partial/unresolved`, one rescore round only for `rebuild`/Floor. Close with material ask + Picks outcome + `theme.mjs log` entry. Never ship open FAIL/REFLEX; every Finish answered.
10. **Stamp as CSS line 1.** Scaffold skeleton + critique line (`P/H/E/S/R/V` + weakest axis + fix) + waivers/dismissed/answered within 40 lines. Component example: `/* Hallmark · component: Button · genre: modern-minimal · theme: Coral · states: 8 · contrast: pass · v2.0.0 */`.

### Sample prompts
- Build: `Use hallmark to build a landing page for job <...>, audience <...>, main action <...>. Material: <...>. Tone <...>. Never invent numbers. Run pre-flight, theme deal, hero-first, sloplint --render.`
- Component: `Use hallmark for exactly one <Button>, all 8 states, Hallmark tokens, emit <Button.tsx + button.css + preview>, component stamp, --scope component sweep.`
- App-screen: `Use hallmark for app-screen <transactions table>, scope app: scaffold --scope app, 32-40px density + 44px hit target, 4 data states, URL state, restrained colour, --scope app sweep.`
- Redesign: `Use hallmark to redesign <path>, full depth, keep content + wiring + brand. List routes/files + Files plan first, run --before + --kept + compare.html.`
- Audit: `Use hallmark to audit <path>, tiered report with file:line, change nothing.`
- Filled example: `Use hallmark to build a landing page for job sign up (SaaS), audience developers, main action Start free. Material: screenshot at /docs/app.png, real number 2-minute setup. Tone modern-minimal, vibe compact-technical-trustworthy, anchor blue. Never invent numbers. Run pre-flight, theme deal, hero-first, sloplint --render.`

### Pitfalls (most-hit Hallmark gates)
- Invented metrics/testimonials/logo walls/counts (46a Floor), invented routes/links, `Sent` forms with no endpoint (70 Floor): use text slots + `data-endpoint=""` + `Nothing was sent...`.
- Eyebrow + tracked-caps + `A · B · C` dots + `→` suffix + status dots (54/67/63 Floor): body-face labels, one step smaller, sentence case, untracked; open sections via `craft.md` §7.
- AI copy (19 Floor): `seamless/robust/elevate/unlock`, `Not a feature. A platform`, `quietly trusted by`, `Learn more/Get started/Book a demo`, `Acme/Nexus`, em/en dashes, `Built for the modern team`.
- Purple-blue/purple-pink/cyan-on-dark gradients, gradient text, card-in-card, emoji icons, drawn browser/OS chrome (2a/4/30a/47a Floor): one anchor hue + solid ink, one containment layer, one icon set at 16/20/24/32px `currentColor`.
- `transition: all`, width/height/top/left animation (10a Floor); fading focus ring (15 Floor); missing `:focus-visible` 3:1 (26a Floor); missing reduced-motion (27 Floor); JS-dependent hidden content (62 Floor).
- Hero fold failure: headline + sentence + primary action must fit 1280x800 (44b Floor); `vh` must be `dvh/svh` (6a Floor); uncapped container at 1920 (44d Floor); missing `overflow-x: clip` or `100vw` (34 Floor); wrapping labels/buttons at 320-1920 (49a Floor).
- Word budget (~80/900px, 2 hero text blocks) (58 Floor); <40px h2 at 1440 (78 Reflex); thin section without mass (77 Reflex); photos >1/3 page (83 Reflex); empty wash (81 Reflex); drawn illustration (80 Reflex); counting device (82 Reflex).
- Bad waivers: waiving Floor, one waiver for many gates, <24-char/boilerplate reasons. Good: `/* Hallmark · waive 47b · one frame, real terminal capture · ... */` with verifiable guard.
- Redesign: deleting `id/name/key/type/href/data-testid`/handlers/routes without an approved file-plan; skipping `--kept`; no `--before` so no `compare.html`; mixing polish/restyle/full depths.

### References
- Repo: https://github.com/Nutlope/hallmark
- Read in order: `SKILL.md` → `anatomy.md` (10 jobs) → `flow.md` (component/app-screen/fast/signal 8-9/OpenCode harness) → `redesign.md` (full/restyle/polish/audit) → `gates.md` → `layout.md` → `imagery.md` → `craft.md` → `patterns.md` (control/slot/form/reveal/stats/loop/skip snippets).
- Scripts: `theme.mjs deal/draw/scaffold/log/photos`, `sloplint.mjs --render/--stage hero/--scope/--genre/--url/--before/--kept`, `capture.mjs --routes/--sizes/--selector/--cdp`, `install.mjs`, `install-hook.mjs` (Claude Code only).

### Back to index
- Back to `../README.md` to compare positioning with `reactbits/`.
- Related item: `../reactbits/` when a ready React effect/component is needed, then re-sweep with Hallmark.
