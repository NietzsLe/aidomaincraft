# awesome-opus5-5-videos

## Tiếng Việt

### Dùng khi
- Cần prompt video thật đã viral bằng Claude Opus 5.5 viết ra code (Canvas/SVG/Three.js/GSAP) để copy + chạy lại với agent của mình: motion graphics, explainer, 3D scene, game/interactive.
- Muốn học cách người khác ra lệnh (prompt ngắn 1 câu đến dài 15K ký tự) và so gốc (X post) vs remake live trên Skillry.
- Cần nguyên liệu miễn phí, MIT, không cài đặt, offline đọc được sau khi clone.

### Bỏ qua khi
- Cần skill cài vào agent (`SKILL.md` + CLI/ZIP + trigger theo description) → dùng Skillry video skills (`../skillry/`), repo này không có skill nào cài được.
- Cần output trình bày đóng gói (landing/deck/OG) → dùng `../skillry/`.
- Cần system pass gates → Hallmark (`../hallmark/`); cần bricks React → React Bits (`../reactbits/`).
- Cần render deterministic / pipeline sản xuất (HyperFrames/Remotion trực tiếp) → đừng dùng prompt viral sao chép.

### Cài đặt
- Không cài. Clone đọc: `git clone --depth 1 https://github.com/yihui-dev/awesome-opus5-5-videos && cd awesome-opus5-5-videos` (đã chạy 29/10/2026: 703 file `prompts/*.md` + `data/videos.json` 703 records).
- Dùng: mở `prompts/<slug>.md`, copy khối ` ```text ` prompt, paste vào agent có Opus 5.5 (Claude Code / Codex / Cursor / OpenCode đọc được HTML).
- Kiểm tra: `ls prompts | wc -l` = 703; `python3 -c "import json;print(len(json.load(open('data/videos.json'))))"` = 703.
- Yêu cầu: git + python3 (đếm/kiểm tra) + browser mở X post / Skillry remake; model Opus 5.5 access để render lại (không phải model nào cũng ra giống). Kiểm tra Opus: mở model selector của agent, phải thấy Opus 5.5; không thấy = chưa đủ điều kiện render, chỉ đọc prompt được. Kiểm tra WebGL cho Usecase 3: mở `chrome://gpu` thấy WebGL2 enabled + console không lỗi.

### Cách item hoạt động
- Tổ chức đứng sau: `yihui-dev` (cùng tác giả Skillry `yihui_indie`), repo `github.com/yihui-dev/awesome-opus5-5-videos` (12,417★ / 1,313 forks / 46 watchers / 7 open issues, tạo 27/09/2026, push 13/10/2026 — GitHub API 29/10/2026), MIT, update theo đợt (12/10/2026: +10 video, +285 prompts).
- Phương thức chung: mỗi entry = prompt markdown + record JSON (slug, author, post_url, category, tech_tags, prompt, poster_url, skillry_url, added, has_remake). 418/703 (~59.5%) có remake live trên `skillry.dev/ai-videos/opus-5-5`. Không có engine render riêng, agent tự viết code animation.
- Khác biệt vận hành theo usecase: motion (Canvas/SVG/GSAP, copy là chạy) khác 3D (Three.js/GLSL/WebGL, cần GPU + device mạnh) khác explainer (script + timing lời thoại) khác interactive/game (thêm playable/physics, cần test input).

### Định vị khác biệt
- So với Skillry video skills (chợ trả phí, 359 video skills, installs 200-518, preview + workflow đóng gói): awesome-list miễn phí, prompt gốc đầy đủ, gốc/remake side-by-side để học. Quyết định: cần học prompt thật 0đ → awesome-list; cần taste đóng gói + hướng dẫn + preview cài 1 lệnh → Skillry (`../skillry/`).
- So với engine mở (HyperFrames/Remotion trực tiếp, repo hàng chục K★): engine cho pipeline deterministic, awesome-list cho ý tưởng prompt viral đã có người thử. Quyết định: cần sản xuất hàng loạt ổn định → engine trực tiếp; cần 1 ý tưởng viral để thử nhanh → copy 1 prompt ở đây.
- Khi nào dùng sẽ phù hợp: có Opus 5.5 access, chấp nhận chất lượng prompt không đồng đều (trung vị 221 ký tự, dài nhất 15,583), tự chịu render/test.

### Bản đồ phủ usecase (quét hết 703 records 29/10/2026 — ★ mạnh nhất đầu)
- ★ Motion graphics (369/703, remake 229): Canvas 267 / SVG 183 / GSAP 86 — copy là chạy, nhiều mẫu nhất. Xem Usecase 1.
- Explainer (116/703, remake 68): recipe/story walkthrough 30s, timing lời thoại. Xem Usecase 2.
- 3D scenes (117/703, remake 56): Three.js 131 / GLSL/shader 92 / WebGL — cần GPU. Xem Usecase 3.
- Interactive / game (101/703, remake 65): playable 22 / physics 9 / pixel 15. Xem Usecase 4.
- KHÔNG hỗ trợ → thay thế: skill cài được → Skillry; system/gates → Hallmark; bricks React → React Bits; deck/OG/image → Skillry media.

### Hồ sơ quyết định
- Việc DÙNG (4, cụ thể): 1. copy prompt motion Canvas/SVG/GSAP chạy lại; 2. học timing explainer 30s; 3. thử scene Three.js/GLSL; 4. thử game/interactive playable.
- Việc KHÔNG DÙNG (3+): 1. cài skill vào agent → dùng Skillry video skill; 2. UI pass gates → Hallmark; 3. deck/OG/landing → Skillry media/web.
- Free / tổng + giá: 703/703 free (100%), MIT, 0đ. Nguồn: `git clone` + đếm 29/10/2026. Lưu ý: repo free, nhưng render lại cần Opus 5.5 access (tự trả theo plan của bạn) + remake trên Skillry có thể nằm trong Premium.
- Ma sát cài đặt: 1 bước (clone) → copy prompt → paste vào agent. ĐÃ chạy clone + đếm + đọc 2 prompt mẫu (`ror-fly-880547`, `anabology-491441`). Rào cản: cần Opus 5.5; X/Skillry cần mạng để xem gốc/remake.
- Đối thủ viral: Skillry video catalog (359 video skills theo `skillry.dev/skills/output/video` + installs 200-518 theo trang skill từng món, đo 29/10/2026 — xem chi tiết trong `../skillry/`) vs HyperFrames/Remotion engine mở (deterministic; số HyperFrames `product-launch-video` ~538.9K installs lấy từ skills.sh leaderboard đối chiếu trong `../skillry/` ngày 29/10/2026). So công bằng: prompt gốc 0đ vs taste đóng gói trả phí (Skillry Premium $9.99/tháng, $79/năm, $169 lifetime — xem `../skillry/`).
- Chọn nó khi: cần prompt viral thật 0đ để học/thử nhanh với Opus 5.5, chấp nhận tự render/test. Giá Opus 5.5 access theo plan Claude của bạn — chưa xác minh link giá ngày 29/10/2026, không gộp vào "free" của repo.
- Chọn nó khi: cần prompt viral thật 0đ để học/thử nhanh với Opus 5.5, chấp nhận tự render/test.
- TUYỆT ĐỐI không dùng khi: cần skill cài được, cần pipeline ổn định, offline hoàn toàn, hoặc cấm phụ thuộc X/Skillry.

### Usecase con 1: motion graphics (★ mạnh nhất)
- Khi dùng: cần motion/Canvas/SVG/GSAP viral copy là chạy (369 mẫu, remake 229).
- Khi bỏ qua: cần 3D nặng GPU → Usecase 3; cần playable → Usecase 4.
- Lệnh copy-paste: `git clone --depth 1 https://github.com/yihui-dev/awesome-opus5-5-videos && cd awesome-opus5-5-videos && ls prompts | head` rồi mở `prompts/<slug>.md` copy khối prompt.
- Điều kiện môi trường: agent có Opus 5.5; browser render HTML/Canvas; mạng mở X + Skillry để đối chiếu gốc/remake (offline chỉ đọc prompt text).
- Ngưỡng số cần đạt: prompt mở được + có `post_url` + `skillry_url` (nếu has_remake); tech_tags khớp khả năng browser (Canvas/SVG chạy mọi máy, GLSL cần GPU).
- Ví dụ input-output: input prompt `ror-fly-880547` (recipe cocktail 30s) → output animation HTML/Canvas 30s render từ agent.
- Pitfalls riêng: prompt dài 15K ký tự (như anabology) chứa API key path nội bộ (`/asic`, foul/seedance key) — bỏ qua phần key, chỉ lấy ý tưởng visual/timing.

### Usecase con 2: explainer
- Khi dùng: cần walkthrough có timing lời thoại/hướng dẫn (116 mẫu, remake 68).
- Khi bỏ qua: cần motion thuần không lời → Usecase 1.
- Lệnh copy-paste: mở `prompts/ror-fly-880547.md` copy prompt, paste vào agent, yêu cầu xuất HTML 30s.
- Điều kiện môi trường: như Usecase 1 + loa/màn hình check timing lời thoại.
- Ngưỡng số cần đạt: video ra đủ 30s + text/timing khớp script.
- Ví dụ input-output: input recipe cocktail → output motion graphic đủ nguyên liệu + số đo theo từng bước.
- Pitfalls riêng: prompt ngắn 1 câu (trung vị 221 ký tự) thiếu bối cảnh — phải tự bổ sung style/timing.

### Usecase con 3: 3D scenes
- Khi dùng: cần scene Three.js/GLSL/WebGL (117 mẫu, remake 56).
- Khi bỏ qua: máy yếu, cần chạy nhẹ → Usecase 1.
- Lệnh copy-paste: mở 1 prompt có `tech_tags` threejs/glsl trong `data/videos.json`, copy prompt, chạy với agent.
- Điều kiện môi trường: GPU + WebGL bật; máy yếu dễ drop frame; mạng xem preview webm.
- Ngưỡng số cần đạt: scene mở không lỗi WebGL, FPS chấp nhận được trên máy đích.
- Ví dụ input-output: input prompt 3D → output Canvas WebGL quay/scroll được.
- Pitfalls riêng: Three.js version trôi — prompt cũ có thể lỗi import, phải tự fix version.

### Usecase con 4: game / interactive
- Khi dùng: cần playable/physics/pixel (101 mẫu, remake 65).
- Khi bỏ qua: chỉ cần video tuyến tính → Usecase 1/2.
- Lệnh copy-paste: mở prompt có tag `playable`/`physics`, copy, yêu cầu agent xuất HTML chơi được.
- Điều kiện môi trường: browser desktop + chuột/bàn phím test input; mobile cần test touch riêng.
- Ngưỡng số cần đạt: chơi được từ đầu đến cuối, không kẹt input.
- Ví dụ input-output: input prompt game → output HTML game bấm/chơi được.
- Pitfalls riêng: playable khó verify tự động — phải chơi tay hết flow.

### Các bước chung
1. Chốt nhu cầu (motion/explainer/3D/game) → lọc `data/videos.json` theo `category`/`tech_tags`/`has_remake`.
2. Mở `prompts/<slug>.md` + X gốc + Skillry remake (nếu có) để hiểu kỳ vọng.
3. Copy prompt → paste vào agent Opus 5.5, nêu rõ output HTML + thời lượng + tech (Canvas/Three.js...).
4. Render + mở browser test (đủ trang, đủ giây, không lỗi console/WebGL).
5. Cần chuẩn riêng thì sweep lại (UI → Hallmark); cần đóng gói thành skill thì chuyển sang Skillry workflow.

### Prompt mẫu
- "Dùng prompt `prompts/ror-fly-880547.md` (recipe cocktail 30s, Canvas) build lại bằng Opus 5.5 thành 1 file HTML mở được ngay, đủ nguyên liệu + số đo theo từng bước."
- "Lọc `data/videos.json` lấy 3 prompt motion có `has_remake=true` + tag canvas/svg, so gốc X vs remake Skillry, rồi chọn 1 để render lại."
- Ví dụ điền sẵn: "Copy prompt motion Canvas `anabology-491441` (bỏ phần API key nội bộ), build music video lyrics hiển thị to/nhỏ xen kẽ, background bớt busy chỗ lyrics lớn."

### Pitfalls
- Nhầm số highlight README (58/16/14/12) với tổng catalog (369/117/116/101) — highlight chỉ là 100 video chọn lọc, tổng quét ở Bản đồ phủ.
- Prompt chứa key/path nội bộ (foul, `/asic`, seedance) — không dùng key người khác, chỉ lấy visual/timing.
- `has_remake=false` (285/703) nghĩa là chưa có remake đối chiếu — kỳ vọng thấp hơn.
- X post có thể bị xóa/khóa — lưu prompt text khi cần dùng lâu dài.

### Tham khảo sử dụng (chốt 29/10/2026)
- Nhận xét sâu: chưa tìm thấy review độc lập quyết định được (so sánh awesome-list vs Skillry video) → `chưa xác minh`. Không dùng stars thay cho review chất lượng prompt.
- Số trung bình có trọng số: GitHub API 29/10/2026: 12,417★ / 1,313 forks / 46 watchers / 7 open issues; tạo 27/09/2026, push 13/10/2026. Trọng số: stars cao nhưng mẫu còn mới (~1 tháng), forks/watchers thấp hơn stars 10-270× → tin cậy thấp hơn Skillry installs thực. Catalog: 703 prompts / 616 authors / remake 418/703 (~59.5%); prompt dài trung vị 221, max 15,583.
- Mâu thuẫn: stars cao (viral) vs prompt không đồng đều (ngắn 11 ký tự đến dài 15K, có key nội bộ) → phán quyết: dùng để học/thử 0đ, không dùng làm pipeline sản xuất.
- Tiếng Việt: không tìm thấy review Việt → `chưa xác minh`.

### Tham khảo
- Repo: https://github.com/yihui-dev/awesome-opus5-5-videos (MIT, `prompts/` + `data/videos.json` + README highlight 100 video)
- Skillry remake: https://skillry.dev/ai-videos/opus-5-5 (418 remake side-by-side)
- Đã chạy xác minh: `git clone --depth 1 https://github.com/yihui-dev/awesome-opus5-5-videos && cd awesome-opus5-5-videos && ls prompts | wc -l` = 703, `python3 -c "import json;print(len(json.load(open('data/videos.json'))))"` = 703, đọc `ror-fly-880547.md` + `anabology-491441.md`, GitHub API `curl -s https://api.github.com/repos/yihui-dev/awesome-opus5-5-videos` = 12,417★/1,313 forks/46 watchers/7 issues 29/10/2026 (drift +2★/+1 fork ở lần đo operator là trôi tự nhiên)

### Được dùng ở đâu
- Dùng CHO media (học prompt video Opus 5.5): xem `../../domains/media/using-awesome-opus5-5-videos.md` — index `../../domains/media/README.md`.

### Quay lại index
- Về `../../domains/media/README.md` để so với `skillry` (video đóng gói).
- Xem thêm item liên quan: `../skillry/` khi cần taste video đóng gói cài 1 lệnh.

---

## English

### When to use
- Need real viral Opus 5.5 video prompts that render to code (Canvas/SVG/Three.js/GSAP) to copy + re-run: motion, explainer, 3D, game/interactive.
- Study how others prompt (11 to 15,583 chars) with original X post vs live Skillry remake.
- Free MIT material, no install, readable offline after clone.

### When to skip
- Need an installable skill (`SKILL.md` + CLI/ZIP) → Skillry video skills (`../skillry/`); this repo has zero installable skills.
- Need packaged presentation output → `../skillry/`; gated system → Hallmark; React bricks → React Bits.
- Need a deterministic production pipeline (HyperFrames/Remotion directly).

### Install
- No install. Read-only clone: `git clone --depth 1 https://github.com/yihui-dev/awesome-opus5-5-videos && cd awesome-opus5-5-videos` (verified 29/10/2026: 703 `prompts/*.md` + 703-record `data/videos.json`).
- Use: open `prompts/<slug>.md`, copy the prompt block, paste into an Opus 5.5 agent.
- Verify: `ls prompts | wc -l` = 703; `len(videos.json)` = 703.
- Requires: git + python3 + browser for X/Skillry; Opus 5.5 access to re-render (check the agent model picker shows Opus 5.5; otherwise read-only). WebGL check for 3D: open `chrome://gpu` for WebGL2 enabled + clean console.

### How the item works
- Backing organization: `yihui-dev` (same author as Skillry `yihui_indie`), repo `github.com/yihui-dev/awesome-opus5-5-videos` (12,417★ / 1,313 forks / 46 watchers / 7 issues, created 27/09/2026, pushed 13/10/2026 — API 29/10/2026), MIT.
- Core method: each entry = prompt markdown + JSON record (slug, author, post_url, category, tech_tags, prompt, poster, skillry_url, added, has_remake). 418/703 (~59.5%) have a live Skillry remake. No own render engine.
- Per-usecase differences: motion (Canvas/SVG/GSAP, copy-runs) vs 3D (Three.js/GLSL/WebGL, needs GPU) vs explainer (script + voice timing) vs interactive (playable/physics, needs input testing).

### Differentiating positioning
- Vs Skillry video skills (paid marketplace, 359 video skills, packaged taste + guided workflow): awesome-list is free, full original prompts, original/remake side-by-side for learning. Pick awesome-list for free prompt study; Skillry for packaged taste + 1-command install.
- Vs open engines (HyperFrames/Remotion directly): engines for deterministic pipelines; awesome-list for viral prompt ideas already tried by someone.
- Fits when: Opus 5.5 access exists; uneven prompt quality accepted (median 221 chars, max 15,583); self render/test.

### Coverage map (full 703-record scan 29/10/2026 — ★ strongest first)
- ★ Motion (369/703, 229 remakes): Canvas 267 / SVG 183 / GSAP 86 — most copy-runnable. See Sub-usecase 1.
- Explainer (116/703, 68 remakes). See Sub-usecase 2.
- 3D (117/703, 56 remakes): Three.js 131 / shader 92. See Sub-usecase 3.
- Interactive/game (101/703, 65 remakes): playable 22 / physics 9. See Sub-usecase 4.
- NOT supported → replacement: installable skill → Skillry; gates → Hallmark; React bricks → React Bits; deck/OG → Skillry media.

### Decision dossier
- Jobs SERVED (4): 1. copy motion prompts; 2. explainer timing study; 3. Three.js/GLSL scenes; 4. playable games.
- Jobs NOT served (3+): 1. agent-installable skill → Skillry; 2. gated UI → Hallmark; 3. deck/OG/web → Skillry.
- Free / total + price: 703/703 free (100%), MIT. Source: clone + count 29/10/2026. Note: repo free, re-render needs your own Opus 5.5 plan; Skillry remakes may be Premium.
- Install friction: 1 step (clone) → copy → paste. RAN clone + counts + 2 sample prompts. Barriers: Opus 5.5 required; network for X/Skillry.
- Viral opponents: Skillry video catalog (359 skills) vs open HyperFrames/Remotion engines. Fair comparison: free original prompt vs paid packaged taste.
- Pick it when: free viral prompt study/quick try with Opus 5.5, self render/test accepted.
- NEVER use when: installable skill, stable pipeline, fully offline, or X/Skillry dependency forbidden.

### Sub-usecase 1: motion graphics (★ strongest)
- When to use: viral motion/Canvas/SVG/GSAP (369, 229 remakes).
- When to skip: heavy GPU 3D → Sub-usecase 3; playable → 4.
- Copy-paste command: `git clone --depth 1 https://github.com/yihui-dev/awesome-opus5-5-videos && cd awesome-opus5-5-videos && ls prompts | head`
- Environment: Opus 5.5 agent; HTML/Canvas browser; network for X + Skillry (offline reads prompt text only).
- Numeric bar: prompt opens + has `post_url` + `skillry_url` (if remade); tech_tags match browser (Canvas/SVG everywhere, GLSL needs GPU).
- Input-output example: input `ror-fly-880547` recipe prompt → 30s HTML/Canvas animation output.
- Own pitfalls: 15K-char prompts (e.g. anabology) contain internal key paths — drop keys, keep visual/timing ideas.

### Sub-usecase 2: explainer
- When to use: narrated walkthrough with timing (116, 68 remakes).
- When to skip: pure motion → 1.
- Copy-paste command: open `prompts/ror-fly-880547.md`, paste into agent, request 30s HTML.
- Environment: as in 1 + speakers/screen for voice timing check.
- Numeric bar: full 30s output with script-matched text/timing.
- Input-output example: cocktail recipe input → step-by-step ingredient motion output.
- Own pitfalls: 1-sentence prompts (median 221 chars) lack context — add style/timing yourself.

### Sub-usecase 3: 3D scenes
- When to use: Three.js/GLSL/WebGL (117, 56 remakes).
- When to skip: weak machines → 1.
- Copy-paste command: pick a threejs/glsl prompt from `data/videos.json`, copy, run.
- Environment: GPU + WebGL on; weak devices drop frames; network for webm preview.
- Numeric bar: scene opens with no WebGL error, acceptable FPS on target.
- Input-output example: 3D prompt input → rotatable/scrollable WebGL Canvas output.
- Own pitfalls: Three.js version drift — old prompts may break imports, fix versions manually.

### Sub-usecase 4: game / interactive
- When to use: playable/physics/pixel (101, 65 remakes).
- When to skip: linear video → 1/2.
- Copy-paste command: pick a `playable`/`physics` prompt, copy, request playable HTML.
- Environment: desktop browser + mouse/keyboard; separate mobile touch test.
- Numeric bar: playable end-to-end with no stuck input.
- Own pitfalls: playable needs manual full-flow playtesting.

### Shared steps
1. Fix need (motion/explainer/3D/game) → filter `data/videos.json` by `category`/`tech_tags`/`has_remake`.
2. Open `prompts/<slug>.md` + X original + Skillry remake (if any).
3. Copy prompt → paste into Opus 5.5 agent with explicit HTML + duration + tech ask.
4. Render + browser-test (full pages/seconds, clean console/WebGL).
5. Need a custom standard → re-sweep (UI → Hallmark); need a packaged skill → Skillry workflow.

### Sample prompts
- "Use prompt `prompts/ror-fly-880547.md` (30s cocktail recipe, Canvas) to rebuild a 1-file HTML version with full ingredients + measurements."
- "Filter `data/videos.json` for 3 motion prompts with `has_remake=true` + canvas/svg, compare X original vs Skillry remake, pick 1 to re-render."
- Filled example: "Copy the Canvas motion prompt `anabology-491441` (drop internal API keys), build lyric motion graphics with big/small lyric variance, calm background where lyrics are big."

### Pitfalls
- Mistaking README highlights (58/16/14/12) for catalog totals (369/117/116/101) — highlights are 100 picks only.
- Prompts with others' keys/paths (foul, `/asic`, seedance) — never reuse keys, take visual/timing only.
- `has_remake=false` (285/703) means no remake to compare — lower expectations.
- X posts can be deleted/locked — save prompt text for long-term use.

### Usage references (pinned 29/10/2026)
- Deep reviews: no decisive independent review found (awesome-list vs Skillry video) → `unverified`. Never use stars as prompt-quality proof.
- Weighted averages: GitHub API 29/10/2026: 12,417★ / 1,313 forks / 46 watchers / 7 issues; created 27/09/2026, pushed 13/10/2026. Weight: high stars but ~1-month-old sample, forks/watchers 10-270× lower than stars → less trustworthy than real Skillry installs. Catalog: 703 prompts / 616 authors / 418 remakes (~59.5%); median prompt 221 chars, max 15,583.
- Conflict: high stars (viral) vs uneven prompts (11 chars to 15K, internal keys) → verdict: 0-cost study/try, not a production pipeline.
- Vietnamese: no VI review → `unverified`.

### References
- Repo: https://github.com/yihui-dev/awesome-opus5-5-videos (MIT, `prompts/` + `data/videos.json` + 100-video README highlight)
- Skillry remakes: https://skillry.dev/ai-videos/opus-5-5 (418 side-by-side remakes)
- Verified by running: `git clone --depth 1 ... && cd awesome-opus5-5-videos && ls prompts | wc -l` = 703, `len(videos.json)` = 703, read 2 sample prompts, GitHub API `curl -s https://api.github.com/repos/yihui-dev/awesome-opus5-5-videos` = 12,417 stars/1,313 forks 29/10/2026

### Where used
- Used FOR media (Opus 5.5 video-prompt study): see `../../domains/media/using-awesome-opus5-5-videos.md` — index `../../domains/media/README.md`.

### Back to index
- Back to `../../domains/media/README.md` to compare with `skillry` (packaged video).
- Related item: `../skillry/` when a packaged video taste with 1-command install is needed.
