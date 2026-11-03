# universal-modder

## Tiếng Việt

### Dùng khi
- Muốn mod 1 game PC mình sở hữu (single-player, multiplayer tự host, server mình host): thêm vật/weapon/enemy/boss/unit/civilization/cơ chế, mashup 2 game, port mod sang version/loader mới — và muốn agent chạy vòng khép kín recon → route → lab an toàn → đọc code thật → slice chạy thật trong game → assets → video showcase → field note cho agent sau.
- Cần trinh sát game lạ (engine/version gì, managed hay native, anti-cheat, loader nào có sẵn, save ở đâu, route nào rẻ nhất) trước khi viết 1 dòng mod nào.
- Cần assets đúng chuẩn engine (sprite transparency thật, pixel art, texture seamless, PBR, image-to-3D, auto-rig, SFX/music/voice) + pipeline biến art thành frames engine nuốt được (cutout/fit/palette/sheet, 3D → sprite 8/16 hướng từ đúng camera game).
- Muốn học từ 242 field notes agent-viết-cho-agent (versions nào chạy được, route nào, gotchas symptom → cause → fix) thay vì đào lại từ đầu.

### Bỏ qua khi
- Chỉ cần build game MỚI từ đầu (Godot/Unity/Unreal/Phaser...) không mod game có sẵn → dùng `gamedev-skills/awesome-gamedev-agent-skills` (77 skills + router, 6,121★) thay.
- Chỉ cần mod Unity thủ công không AI (plugin BepInEx viết tay) → dùng `BepInEx/BepInEx` (8,935★, LGPL-2.1) thay, không cần cả bộ skills + CLI.
- Cần asset raster/OG/deck/video đóng gói nhanh cho media (không phải asset game) → dùng `../skillry/`, `../awesome-opus5-5-videos/`, `../logo-design-skill/`.
- Game là online client có anti-cheat, muốn cheat người chơi khác (aimbot/ESP/speed hack), bypass anti-cheat/DRM/ownership → TUYỆT ĐỐI không dùng (hệ từ chối, xem [Pitfalls](#pitfalls)).

### Cài đặt (đã clone + chạy thử `um` trên Linux 31/10/2026; chưa cài plugin marketplace vì máy này không có Claude Code/Codex)
- Cách 1 — skills-only (mọi agent, 1 lệnh): `npx skills add https://github.com/rehan-remade/universal-modder`.
- Cách 2 — clone (đủ skills + `um` CLI + MCP config có sẵn): `git clone https://github.com/rehan-remade/universal-modder` rồi `export PATH="$PWD/bin:$PATH"` (Windows cmd/PowerShell: thêm `bin` vào PATH, chạy `bin\um.cmd`); trong clone mở agent là skills tự thấy (`skills/` → `.agents/skills` + `.claude/skills`).
- Cách 3 — plugin từng agent (theo README gốc): Claude Code `/plugin marketplace add rehan-remade/universal-modder` + `/plugin install universal-modder@universal-modder`; Codex `codex plugin marketplace add rehan-remade/universal-modder` + `codex plugin add universal-modder@universal-modder`; Gemini CLI `gemini extensions install https://github.com/rehan-remade/universal-modder`; OpenCode 2 `opencode plugin add 'github:rehan-remade/universal-modder#main::path:plugins/opencode'`; VS Code/Copilot bật `chat.plugins.enabled` + `Chat: Install Plugin From Source` với URL repo; Cursor đọc `AGENTS.md` + `.cursor/mcp.json`.
- Cách 4 — `um` CLI độc lập (không cần clone): `uv tool install git+https://github.com/rehan-remade/universal-modder` (hoặc `pipx install git+...`).
- Yêu cầu: Git + Python 3.10+ (deps Pillow/numpy/PyYAML, `uv` tự lo) + ffmpeg; `render3d` cần Blender trên PATH (hoặc `BLENDER=...`); Windows games chạy native hoặc từ WSL.
- Assets: `FAL_KEY` cho fal MCP + `um fal` (khuyến nghị `um fal key set` lưu 1 lần: Linux vào keyring libsecret, nơi khác vào `~/.secrets/fal-key` owner-only; `FAL_KEY` môi trường vẫn thắng; `um fal key status` xem nguồn đang dùng). Không key thì fal MCP dùng OAuth browser (`https://mcp.fal.ai/mcp-relay`) và `um comfy` render local miễn phí. `um sprixen` cần key Sprixen riêng (`um sprixen key set`), `um voidless` cần key Voidless riêng (`um voidless key set`).
- Kiểm tra (đã chạy 31/10/2026, output thật): `bash bin/um --help` → liệt kê đủ 15 groups (`scan/fal/comfy/sprixen/voidless/sprite/render3d/video/win/backup/publish/kb/fastfile/iwi/weapon`) + `universal-modder 0.2.0` ở `--version`; `bash bin/um scan --list` → `no Steam/Epic/Xbox installs found; pass a game folder to um scan <path>` (đúng máy Linux không game); `bash bin/um kb search "terraria"` → ra `games/terraria/fal-arsenal-tmodloader.md` + 2 notes liên quan kèm route/status; `bash bin/um scan --help` + `kb check --help` + `fal --help` đều in usage + ví dụ.

### Cách item hoạt động
- Tổ chức đứng sau: cá nhân `rehan-remade`, repo `https://github.com/rehan-remade/universal-modder`, license MIT, bản 0.2.0 (`plugin.json` + `pyproject.toml`, đọc 31/10/2026), tạo 30/09/2026, update cuối 31/10/2026, 328 commits. Số liệu API GitHub ngày 31/10/2026: 9,248★ / 1,034 forks / 49 watchers; topics `claude-code game-modding mcp reverse-engineering tmodloader...`; site `universalmodder.com` (sắp mở mod hub publish/remix).
- Phương thức hoạt động chung: skill `mod-any-game` (`skills/mod-any-game/SKILL.md`, 193 dòng, đọc 31/10/2026) chạy vòng 10 bước cố định intake → recon → route → lab (backup) → source of truth → vertical slice → assets → verify trong game thật → showcase → publish + field note; 12 engine playbooks (`references/engines/`: Unity/Unreal/.NET-XNA/Godot/Source/Bethesda/Minecraft/AoE2-Genie/Bannerlord/Isaac/RE-MT-FromSoft-GTA-Hedgehog/nativ-C++/indie-retro); CLI `um` Python 1 module/group (mỗi group có `--help` kèm ví dụ); fal MCP `https://mcp.fal.ai/mcp` (header `Authorization: Bearer $FAL_KEY`, config sẵn `.mcp.json`/`.codex/config.toml`/`.cursor/mcp.json`/`.vscode/mcp.json`/`gemini-extension.json`/`opencode.json`); knowledge base `knowledge/` (INDEX máy sinh bằng `um kb index`, machine-readable `index.json`); 3 agents team (`mod-orchestrator` giám sát + `mod-game-worker` chạm game duy nhất + `mod-offline-worker` không chạm game).
- Khác biệt vận hành theo usecase: mod mới (recon + chọn 1 trong 6 routes + lab backup + đọc code thật, xem [Usecase con 1](#usecase-con-1-mod-moi-cho-game-so-huu--recon-route-slice-verify)) khác assets (gọi fal REST sinh + convert deterministic bằng `sprite`/`render3d`, mọi call ghi `fal_manifest.jsonl`, xem [Usecase con 2](#usecase-con-2-assets-bang-falcomfy--pipeline-ve-chuan-engine)) khác test/showcase (chạm process thật bằng `win` + cắt EDL bằng `video`, xem [Usecase con 3](#usecase-con-3-test-trong-game-that--video-showcase)) khác port/mashup + share note (diff không drift + PR knowledge, xem [Usecase con 4](#usecase-con-4-port-mod--mashup-2-game--share-field-note)).

### Cốt lõi bất biến
- Tìm prior art trước: mọi mod mở đầu bằng `um kb search "<game>"` + `um kb search "<engine>"` (dùng exact versions/route/gotchas của note có sẵn, không lặp dead end) + `um scan "<game>"` đọc playbook tương ứng (xem [Usecase con 1](#usecase-con-1-mod-moi-cho-game-so-huu--recon-route-slice-verify)). Bỏ qua KB/scan mà đoán engine = không còn dùng hệ.
- Lab an toàn trước launch modded đầu tiên: `um backup create "<saves>"` + profile/lab save riêng + windowed mode size cố định + decompile/asset trích để NGOÀI repo (xem [Các bước chung](#cac-buoc-chung)). Chạm save/game folder khi chưa backup = FAIL.
- Vertical slice trước mở rộng: 1 item/unit/weapon đi hết tới chạy thật (log + screenshot TỰ MỞ nhìn) rồi mới widen, commit từng bước chạy được (xem [Usecase con 1](#usecase-con-1-mod-moi-cho-game-so-huu--recon-route-slice-verify)). Build hàng loạt khi chưa có slice xanh = FAIL.
- Ship sạch + ghi lại: `um publish check` (không game files/decompiled code/keys lọt) + `um kb check` trước mọi publish/PR + viết field note (versions/route/engine-thật/verify/gotchas) (xem [Usecase con 4](#usecase-con-4-port-mod--mashup-2-game--share-field-note)). Ship file game/code dịch hoặc PR khi chưa check = FAIL.
- Sau khi dùng phải nêu được: note nào đã tái dùng (game/engine + route + gotcha áp dụng) + backup nào + slice nào đã verify + manifest/check nào; không nêu được = chưa thực sự dùng hệ.

### Phần tùy chỉnh
- Được đổi: game + ý tưởng 1 câu + định nghĩa done (thường = chạy trong game + clip 20–45s), route trong 6 loại (data/loader-API/managed-patch/native-hook/reimplement-decomp/mashup-passthrough), skill nào trong 13 skills, fal model/endpoint nào (`um fal search` tìm model hiện hành), style asset (palette/size/camera/preset `aoe2/iso8/trueiso/topdown/side/turntable`), EDL/video style, note là game hay technique. Cổng duyệt 2 tầng: (1) artifact nào — route + skill + fal model candidates trình shortlist 2–3 kèm lý do qua question tool, user pick mới build (kể cả user đã duyệt ý tưởng lớn, route/model vẫn chờ duyệt artifact cụ thể); (2) giữ/đổi gì — style/size/model nào đổi phải chốt trước khi generate hàng loạt (tốn tiền fal cho cả lần fail). Waiver duy nhất (bỏ backup/đổi engine/không key mà vẫn làm, mod online có anti-cheat, publish khi chưa check) phải quote câu ok tường minh của user, không suy diễn.
- Cấm đưa vào đây: mod online có anti-cheat, cheat người khác, bypass anti-cheat/DRM/ownership, ship game files/decompiled dumps, kill process theo tên, lái chuột/phím + cài loader vào game folder + publish khi chưa hỏi (toàn bộ là `must-not`, xem [Pitfalls](#pitfalls)).

### Phân công ai làm gì
- Agent chính: intake 1 câu + `kb search` + `scan` + đọc playbook + chốt route (shortlist 2–3 kèm lý do, chờ user pick — cấm tự chốt route/model rồi build), lab backup, đọc code/data thật, build slice, chạy `um` asset/pipeline/publish/kb, trình log + screenshot + manifest + check; verify `backup` tồn tại + slice chạy thật + `publish check` + `kb check` xanh + INDEX refresh.
- Giao cho claude các bước cần browser/tài khoản ngoài: research web sống sót forum chết (Wayback/archive.today, GitHub/Nexus/Workshop/Thunderstore APIs, Reddit/YouTube, trang login-gated handoff) + mở screenshots upstream làm evidence + xem ảnh/video verify trên browser thật — lệnh delegate `claude --chrome --model sonnet -p "<game + route + URL + states cần observe + output mong đợi>" --dangerously-skip-permissions --output-format text`, kèm game/version/route + yêu cầu cụ thể; cấm agent tự bịa kết quả tra cứu. Không có browser thì agent phải khai báo + dừng bước đó (DOM dump/log text không thay thế ảnh nhìn thật), cấm claim đã observe.
- Agent verify: `um backup` snapshot tồn tại + log game + screenshot đã mở nhìn + `fal_manifest.jsonl` đủ dòng + `publish check`/`kb check` xanh + note có versions/route/gotchas + PR chỉ khi human ok tường minh.

### Định vị khác biệt (số liệu API GitHub ngày 31/10/2026)
- So với `gamedev-skills/awesome-gamedev-agent-skills` (skills agent cho game, 6,121★/584 forks, Apache-2.0, 77 skills Godot/Unity/Unreal/Phaser/PixiJS/three.js/Bevy/pygame/LÖVE/Roblox + router tự load theo engine/task, version-pinned + validator): khác hướng — gamedev-skills BUILD game mới từ đầu (art-direction workflow, router chọn skill); universal-modder MOD game có sẵn đã cài (scan fingerprint engine/version/anti-cheat/loaders/saves + ranked routes + backup lab + verify trong game đang chạy + 242 field notes). Chọn universal-modder thay vì gamedev-skills khi quyết định phụ thuộc vào game đã sở hữu + route mod rẻ nhất + gotchas thật (ngưỡng: `um scan` ra engine/version/routes + `kb search` ra note versions khớp); chọn gamedev-skills khi làm game mới Godot/Unity/Unreal cần router + skill version-pinned, không có game để scan.
- So với `BepInEx/BepInEx` (framework mod Unity thủ công, 8,935★/932 forks, LGPL-2.1): khác tầng — BepInEx là loader + API để dev tự viết plugin (không AI loop, không assets, không KB); universal-modder là vòng agent dùng loader đó khi rẻ nhất (route `loader API`: tModLoader/SMAPI/BepInEx/UE4SS/REFramework/SKSE/Fabric) + tự đọc code + sinh assets + verify + ghi note. Chọn universal-modder thay vì BepInEx thuần khi cần agent đi hết vòng (recon → slice → assets → verify → note đo được bằng log/screenshot/manifest); chọn BepInEx thuần khi dev đã biết rõ Unity modding và chỉ cần framework viết tay, không muốn AI + phí fal.
- Khung trung thực: universal-modder thắng ở mod game có sẵn khép kín (prior art + lab + verify + note); thua ở build game mới (gamedev-skills/Claude-Code-Game-Studios 30,491★ thắng bằng router + studio hierarchy) và thua ở gọn nhẹ (BepInEx thắng khi chỉ cần loader, không cần cả bộ 13 skills + CLI + fal).

### Bản đồ phủ usecase (quét HẾT 13 skills + 15 groups `um` + 12 playbooks + 3 agents + knowledge/INDEX 31/10/2026 — ★ mạnh nhất đầu)
- ★ Mod mới cho game sở hữu (recon → route → slice → verify → note): xem Usecase 1.
- Assets fal/ComfyUI + pipeline về chuẩn engine (`fal` 16 recipes + `sprite` 10 ops + `render3d` 6 presets): xem Usecase 2.
- Test trong game thật + video showcase (`win` launch/shot/drive/record/ps/kill/launch/reg + `video` contact/compile/mux/beats/first-frame, EDL là danh sách quyết định dựng chứa cuts/titles/music): xem Usecase 3.
- Trung bình: port mod sang version/loader mới không drift (`port-a-mod`: 1 pinned source + decompile riêng + extract bằng script + unit tests + audits theo layer): xem Usecase 4.
- Trung bình: mashup 2 game/passthrough + decomp-as-library/reimplementation (`mashup-mods` + 3 ví dụ Minecraft×GTA V/AoE2/Terraria): xem Usecase 4.
- Trung bình: research web sống sót forum chết (`game-research-websearch`: Wayback/archive.today + GitHub/Nexus/Workshop/Thunderstore APIs + login-gated handoff + screenshots làm evidence) → dùng khi KB + wiki/loader docs chưa đủ.
- Trung bình: decompile game Blitz3D (`blitz3d-decomp`: B3DDecomp → source đọc được; có trong `skills/` nhưng README gốc chưa liệt kê trong bảng 12 skills — đã đối chiếu `ls skills/` 31/10/2026) → dùng đúng game Blitz3D cũ.
- Trung bình: CoD4/WaW chuyên sâu (`fastfile` list/dump + `iwi` png2iwi/iwi2png DXT1/DXT5 + `weapon` get/set/clone/diff, read-only zones PC unsigned) → dùng đúng 2 bản CoD này.
- KHÔNG hỗ trợ → thay thế: mod online có anti-cheat/cheat người khác/bypass DRM → từ chối (không hệ thay thế, xem [Pitfalls](#pitfalls)); build game mới → `awesome-gamedev-agent-skills`; logo vector/audit → `../logo-design-skill/`; landing taste đóng gói → `../skillry/`; prompt video gốc → `../awesome-opus5-5-videos/`; page system pass gates → `../hallmark/`; bricks React → `../reactbits/`.

### Hồ sơ quyết định
- Việc DÙNG (3+, cụ thể): 1. mod mới cho game sở hữu tới chạy thật + clip + note (Terraria Fal Arsenal: homing missile + tactical nuke crater + chain-lightning + black-hole + orbital + 3 enemies + boss 2 phase; AoE2 DE civ San Franciscans + Robotaxi render từ 3D; Minecraft thật trong GTA V story qua WebSocket); 2. assets đúng chuẩn engine (sprite transparency/pixel/seamless/PBR/model3d/rig/SFX/music/voice/video + cutout/fit/palette/sheet/team-mask + GLB→frames đúng camera); 3. test in-game + showcase (launch/screenshot/drive/record + EDL compile); 4. port mod/mashup + share field note qua PR.
- Việc KHÔNG DÙNG (3+, mỗi việc kèm hệ thay thế): 1. build game mới từ đầu → dùng `awesome-gamedev-agent-skills` (6,121★, router + 77 skills); 2. mod Unity viết tay không AI → dùng `BepInEx` (8,935★); 3. asset media trang trí (OG/deck/launch video taste) → dùng `../skillry/` + `../awesome-opus5-5-videos/`; 4. logo vector audit → dùng `../logo-design-skill/`; 5. online cheat/bypass → không hệ nào (từ chối).
- Free / tổng + giá: core 0đ toàn bộ (MIT, clone + `um` không phí — nguồn `LICENSE` + `pyproject.toml`, đọc 31/10/2026). Phí ngoài: fal trả theo model/endpoint (xem `um fal price <model>`, rates trôi — không quote số tĩnh); Sprixen trả riêng (key riêng); Voidless trả riêng (key riêng); ComfyUI local 0đ (tự host); Blender 0đ. Tổng bill = 0đ core + tiền fal đã generate (kể cả lần fail) + key ngoài nếu dùng.
- Ma sát cài đặt: 2 bước tới lệnh đầu (`git clone` + `export PATH` rồi `um --help`; skills-only chỉ 1 lệnh `npx skills add ...`). ĐÃ chạy thử tới bước: `--help` (15 groups + v0.2.0) + `scan --list` (Linux không game, output đúng) + `kb search "terraria"` (ra 3 notes) + 3 `--help` group. Rào cản: Git + Python 3.10+ + ffmpeg bắt buộc; `uv` khuyến nghị; Blender cho `render3d`; `FAL_KEY` cho assets fal; Windows/WSL cho group `win`; game phải sở hữu + bản quyền; publish/PR cần `gh` + human ok.
- Đối thủ viral cùng phân khúc: `gamedev-skills/awesome-gamedev-agent-skills` (6,121★/584 forks, Apache-2.0) vs `BepInEx/BepInEx` (8,935★/932 forks, LGPL-2.1). Số đo API GitHub ngày 31/10/2026.
- Chọn nó thay vì đối thủ khi: có game đã cài cần mod tới chạy thật (ngưỡng: `scan` ra engine/version/routes + `kb search` ra note khớp versions + slice verify bằng log/screenshot + manifest + check xanh). Ví dụ đổi lựa chọn: có Terraria Steam muốn nuke crater + sprites fal → universal-modder; làm game Godot mới từ 0 → gamedev-skills; chỉ viết plugin Unity tay → BepInEx.
- TUYỆT ĐỐI không dùng khi: game online có anti-cheat mà đòi chạm client; muốn cheat người khác; bypass anti-cheat/DRM/ownership; ship game files/assets trích/decompiled code; máy không có Python 3.10+/Git; mod mà không chịu backup saves.

### Usecase con 1: mod mới cho game sở hữu — recon/route/slice/verify
- Khi dùng: có game đã sở hữu + ý tưởng 1 câu và cần đi hết vòng tới chạy thật trong game + note.
- Khi bỏ qua: chỉ cần assets → Usecase 2; chỉ cần test/video cho mod có sẵn → Usecase 3; port/mashup → Usecase 4; game online anti-cheat → bỏ hẳn.
- Cơ chế khác các usecase khác ở đâu: duy nhất chạy đủ intake→recon→route→lab→source→slice→verify→note với 6 routes + lab backup + đọc code thật; các usecase khác chỉ làm 1 khúc (sinh art / quay-cắt / port-PR).
- Lệnh copy-paste: `um kb search "<game>"` rồi `um scan "<game>"` (đọc playbook nó chỉ) rồi `um backup create "<saves folder>" --name <game>-saves` rồi build slice rồi `um publish check <mod-dir>` (nguồn `AGENTS.md` + `SKILL.md` bước 0–5/9, đã chạy `kb search` + `scan --list` thật 31/10/2026).
- Ngưỡng số cần đạt: KB ra note khớp game/engine (242 notes để đối chiếu); scan ra engine/version/managed-vs-native/anti-cheat/loaders/saves/ranked routes; backup snapshot tồn tại TRƯỚC launch modded đầu tiên; slice 1 món chạy thật (log + screenshot đã mở nhìn); `publish check` xanh (không game files/decompiled/keys).
- Ví dụ input-output (minh họa — route + scope do user pick trước, không phải mặc định): input "Terraria Steam: homing missile launcher + tactical nuke crater, done = chạy trong game + clip 20–45s" → output `MODDING_PLAN.md` (route `loader-api` tModLoader + playbook .NET/XNA) + backup saves + slice missile chạy thật (log + screenshot) + full nuke/enemies/boss + `examples/terraria-tmodloader` + note `games/terraria/fal-arsenal-tmodloader.md` (working, versions ghi trong note).
- Pitfalls riêng: đoán engine không scan → route sai (exe enforce khác data, vd AoE2 data chứa 64 civ nhưng picker exe hard-coded → phải replace slot); build hàng loạt chưa slice xanh → nợ verify; quên backup → mất save người chơi; commit game files/decompile vào repo → PR bị đóng.
- Phân công usecase này: agent chính intake/scan/KB/route-shortlist/backup/build-slice/verify (shortlist route qua question tool, user pick mới build); giao claude research login-gated + screenshots evidence; verify bằng backup + log + screenshot đã nhìn + publish check.

### Usecase con 2: assets bằng fal/ComfyUI + pipeline về chuẩn engine
- Khi dùng: đã học assets gốc game (size/palette/outline/camera/facing/frame layout) và cần sinh sprites/textures/PBR/3D/rig/SFX/music/voice/video rồi convert đúng format engine nuốt.
- Khi bỏ qua: mod data/code thuần không cần art → Usecase 1; art có sẵn chỉ cần test → Usecase 3.
- Cơ chế khác các usecase khác ở đâu: gọi fal REST sinh (tốn tiền cả lần fail, ghi `fal_manifest.jsonl`) + convert deterministic (`sprite`/`render3d`/ComfyUI local); không chạm game đang chạy, không PR knowledge.
- Lệnh copy-paste: `um fal sprite "a rusty scrap drone enemy, side view facing left, 16-bit pixel art" --out assets/gen --name drone` rồi `um sprite fit assets/gen/drone.png --size 64x26` (game pixel) hoặc `um fal model3d concept.png` rồi `um render3d model.glb --preset aoe2` (game 3D→sprites) (nguồn `um fal --help` + README pipeline, đọc 31/10/2026).
- Ngưỡng số cần đạt: đúng frame size/palette/outline/camera game (vd Terraria sprite sau 1 lần nearest-neighbour fit; AoE2 16 headings từ đúng camera); transparency thật (rmbg/cutout); variants nhất quán (edit từ 1 concept, 3D từ 1 model); mọi call có dòng trong `fal_manifest.jsonl` (endpoint/inputs/request-id/seed/files); model ID kiểm tra lại bằng `um fal search` (IDs trôi nhanh).
- Ví dụ input-output (minh họa — style/model do user pick trước): input "drone enemy Terraria 64x26 + Robotaxi AoE2 16 hướng" → output `assets/gen/drone.png` + fit 64x26 + `model.glb` (Trellis 2) + 16 frames preset `aoe2` + manifest đủ dòng + sprites chạy trong ví dụ gốc (`examples/terraria-tmodloader`, `examples/aoe2-de-civ`).
- Pitfalls riêng: generate hàng loạt trước khi chốt style (tốn tiền fail); model ID cũ trong memory (phải `search` lại); transparency giả (nền trắng ép); pixel art upscale làm mờ (phải grid-snapped + palette-limited qua `pixelate`); Sprixen/Voidless nhầm key fal (2 service trả riêng, key riêng).
- Phân công usecase này: agent chính học assets gốc + sinh + convert + trình ảnh đã mở nhìn (shortlist style/model qua question tool, user pick mới generate loạt); giao claude xem ảnh so sánh trên browser khi cần; verify bằng size/palette/manifest + asset load trong game.

### Usecase con 3: test trong game thật + video showcase
- Khi dùng: mod đã build cần oracle (game đang chạy) + clip showcase 20–45s có nhạc/titles.
- Khi bỏ qua: chưa có slice chạy → Usecase 1; chưa có assets → Usecase 2.
- Cơ chế khác các usecase khác ở đâu: chạm process/window/audio thật (`win`: launch/shot/record/drive/ps/kill/reg, gfxcapture + process-loopback audio, kill theo PID) + cắt EDL (`video`: contact/compile/mux/beats/first-frame); không sinh code mod, không PR.
- Lệnh copy-paste: `um win launch "<game>"` rồi `um win shot --out shots/` (nhìn ảnh thật) rồi `um win record --out clips/` (chỉ audio game) rồi `um video compile edit.edl --out showcase.mp4` (nguồn `um --help` groups + `SKILL.md` bước 7–8).
- Ngưỡng số cần đạt: windowed mode size cố định (registry/ini) để screenshot/click ổn định; test lặp được (chat command/mod-side timeline/scenario/test world riêng, giữ 1 bản pristine restore trước mỗi take); drive input chỉ tới game (`um win drive`); record đúng window + chỉ audio game; dọn crash-reporter sau take; clip 20–45s beat-cut có titles.
- Ví dụ input-output (minh họa): input "verify nuke crater Terraria + clip" → output test world riêng + launch/drive path menus→scene + screenshots đã nhìn + clip showcase (EDL + music) như teaser 6 mods trong README gốc (Elytra/GTA, Nether, Halo Warthog, flamethrower, zombies).
- Pitfalls riêng: focus game có online mode khi user đang gõ (cấm — hỏi trước); kill theo tên thay vì PID (giết nhầm process); screenshot GPU-unsafe; quên restore pristine world (take sau nhiễm take trước); record lẫn audio desktop.
- Phân công usecase này: agent chính drive/launch/shot/record/compile + trình ảnh/clip đã xem; giao claude xem clip/ảnh trên browser + check moments; verify bằng log + ảnh đã nhìn + clip đủ 20–45s + audio chỉ game.

### Usecase con 4: port mod + mashup 2 game + share field note
- Khi dùng: có mod cũ cần sang version/loader mới không drift; hoặc 2 game cùng lúc (content port/passthrough/decomp-as-library/reimplementation); hoặc vừa mod xong cần ghi note + mở PR cho agent sau.
- Khi bỏ qua: mod mới đơn game → Usecase 1.
- Cơ chế khác các usecase khác ở đâu: so sánh theo lớp + test từng unit + status docs resumable (`port-a-mod`: Forge 1.7.10→Fabric 1.20.1 mapping) / bridge 2 engines qua WebSocket + depth-composite (`mashup-mods`: Minecraft×GTA V) / scaffold+validate+PR (`share-field-notes` + `um kb`); CoD4/WaW dùng tools chuyên (`fastfile/iwi/weapon`).
- Lệnh copy-paste: `um kb new --game "Hades II" --title "A new boon god" --from-scan hades --agent "Codex (gpt-6)"` rồi `um kb check knowledge/games/hades-ii/a-new-boon-god.md` rồi `um kb pr knowledge/games/hades-ii/a-new-boon-god.md --yes` (chỉ sau khi human ok tường minh) (nguồn README gốc + `CONTRIBUTING.md`, đọc 31/10/2026; CoD: `um fastfile list <zone.ff>`, `um iwi iwi2png <tex.iwi>`, `um weapon get <file>`).
- Ngưỡng số cần đạt: port giữ 1 pinned source + decompile riêng + extract bằng script + unit-by-unit tests + audits theo layer (mapping table kèm); note có exact versions + route + engine-thật + build steps + verify + gotchas symptom→cause→fix; `kb check` xanh (block >150 dòng FAIL, >60 WARN) + `INDEX.md` refresh qua `um kb index`; PR không game files/assets trích/decompiled dumps/links lậu (PR vi phạm bị đóng).
- Ví dụ input-output (minh họa): input "port mod Forge 1.7.10 sang Fabric 1.20.1 + note" → output source pinned + decompile riêng ngoài repo + mapping table + tests từng unit + audits + note `knowledge/games/<game>/<slug>.md` + PR sau human ok (mẫu thật: 242 game notes + 88 techniques trong INDEX 31/10/2026).
- Pitfalls riêng: viết note thứ 2 trùng game (phải `kb search` trước, cải thiện note cũ); snippet code mình >150 dòng trong note; paste code leak/beta vào note (chỉ diễn đạt lại); PR khi human chưa ok (PR mang identity human); CoD zones signed/khác version ngoài 2 bản được hỗ trợ.
- Phân công usecase này: agent chính scaffold/fill/validate/index + trình note diff cho human duyệt (chờ ok tường minh mới `--yes`); giao claude mở PR page + screenshots upstream khi cần; verify bằng `kb check` + index tươi + PR đúng 1 note (+media) + không file cấm.

### Các bước chung
1. Intake 1 câu (game + store/platform + ý tưởng) + chốt done (thường = chạy trong game + clip 20–45s) + phân online/offline ngay (online anti-cheat → chỉ offline/private-server/tools chính thức) + mở `MODLOG.md` (paths/IDs/formats/class names/fail-next).
2. `um kb search "<game>"` + `"<engine>"` (dùng versions/route/gotchas note cũ) + `um scan "<game>"` (engine/version/managed-native/anti-cheat/loaders/saves/ranked routes) + đọc playbook + research community hiện tại (wiki/Nexus/Thunderstore/mod.io/Workshop/GitHub/loader release — không cài từ memory).
3. Chốt route rẻ nhất tới ý tưởng (data / loader-API / managed-patch / native-hook / reimplement-decomp / mashup) + ghi lý do vào MODLOG (shortlist 2–3 qua question tool, user pick mới build).
4. Lab: `um backup create` saves (+config) + profile/lab save riêng + windowed size cố định + decompile/asset trích NGOÀI repo + gitignore.
5. Đọc source of truth (ILSpy/Cpp2IL/Vineflower/Ghidra-IDA-MCP/Cheat Engine/Frida/RenderDoc/dump tools) + ghi tên/IDs exact vào MODLOG (check cả exe enforce, không chỉ data).
6. Slice 1 món tới chạy thật (log + screenshot đã nhìn) rồi mới widen, commit từng bước chạy được.
7. Assets: học assets gốc (size/palette/outline/camera/facing/frames) → `um fal`/`comfy`/`sprixen`/`voidless` (manifest đủ) → `um sprite`/`render3d` đúng format engine.
8. Verify trong game thật (test lặp được + drive + shot + restore pristine) → record → `um video` compile showcase.
9. `um publish check` + `um kb check` + viết note + `um kb index` + PR sau human ok (`--yes`).

### Prompt mẫu
- "Mod Terraria Steam: homing missile launcher + tactical nuke crater thế giới. Recon bằng `um kb search` + `um scan` trước, trình shortlist route + skill + fal model (2–3 kèm lý do) chờ tôi pick mới build. Backup saves trước launch đầu, slice 1 weapon tới chạy thật (log + screenshot tự mở nhìn) rồi mới widen. Không bịa versions, không ship game files."
- "Sinh sprites fal cho drone 64x26 Terraria: học assets gốc (size/palette/outline) trước, trình 2–3 style/model kèm lý do chờ tôi pick, generate concept → cutout → 1 lần fit nearest-neighbour → manifest đủ dòng. Model ID check lại bằng `um fal search`, không dùng ID từ memory."
- "Verify mod trong game + cắt clip 20–45s: windowed size cố định + test world riêng (giữ pristine restore mỗi take), drive→shot→record (chỉ audio game) → EDL compile. Hỏi trước khi lái chuột/phím. Xong chạy `publish check` + `kb check` + viết field note, PR chỉ khi tôi ok tường minh."

### Pitfalls
- Chạm online client có anti-cheat / viết cheat chống người khác / bypass anti-cheat-DRM-ownership → hệ từ chối (nguồn `safety.md` qua `AGENTS.md`); offer offline/private-server/tools chính thức thay.
- Ship game files/assets trích/decompiled dumps/links lậu/ROM-ISO trong mod hoặc PR → PR bị đóng + `publish check`/`kb check` chặn (check trước mọi publish).
- Chưa `um backup create` đã launch modded → mất save; test world chung với save người chơi → nhiễm bẩn (luôn lab save riêng + pristine restore).
- Kill process theo tên pattern → giết nhầm (chỉ kill PID exact `um win kill <pid>`); focus game online khi user đang gõ; cài loader vào game folder/sửa registry khi chưa hỏi.
- Generate fal hàng loạt chưa chốt style/model (tốn tiền cả lần fail) + dùng model ID từ memory (IDs trôi — luôn `search` lại) + nhầm key Sprixen/Voidless với fal.
- `scripts/`-style trap của repo này: `bin/um` là shell wrapper (`export PATH`), `python3 bin/um` báo SyntaxError (đã gặp 31/10/2026 — luôn gọi `bash bin/um` hoặc `./bin/um`); skill thứ 13 `blitz3d-decomp` có trong `skills/` nhưng README gốc chưa liệt kê (đừng claim chỉ có 12).

### Tham khảo sử dụng (số đo ngày 31/10/2026 trừ khi ghi khác)
- Nhận xét sâu: [Frontier Now 08/10/2026](https://frontiernow.dev/en/github/universal-modder/) "packs 11 Agent Skills, a fal MCP server and the um CLI ... so they can mod almost any PC game you own" + "every agent that lands a mod files a field note ... so the next agent starts where the last one stopped" → xác nhận quyết định chọn vì KB + vòng khép kín, đồng thời lật kỳ vọng "repo lâu đời": repo mới 8 ngày đã 5,222★ (lúc đo) nên interfaces/layout sẽ đổi + mod hub chưa mở (tính tới 31/10/2026 hub vẫn "coming next").
- Nhận xét sâu 2: [awesome-ai-game-dev-tools 15/10/2026](https://github.com/SubmitGame/awesome-ai-game-dev-tools) liệt kê universal-modder 7.7k★ là tool duy nhất mục agent-driven modding có verified example (Fal Arsenal Terraria) + 7 video mashup (MrToucan 345,483 views, Lessons 444,003 views, Better Stack 22,543) → xác nhận quyết định chọn khi cần ví dụ chạy thật + cộng đồng video, không phải repo liệt kê suông.
- Số trung bình: GitHub 9,248★/1,034 forks/49 watchers/328 commits (API 31/10/2026) — trọng số mạnh (9.2k★ sau 31 ngày từ 24★ ngày 29/09/2026 theo Funcoding star history, +8.2k/30d; fork 1k = dùng thật). KB 242 game notes + 88 techniques + 10 examples (INDEX + `ls` 31/10/2026) — trọng số trực tiếp cho prior art. Chưa có rating marketplace/HN/ProductHunt độc lập → ghi `chưa xác minh` review sao, cấm suy ra điểm.
- Mâu thuẫn: site `universalmodder.org` quảng cáo "3.4k+ stars / 10 skills" (snapshot cũ) vs README + API hiện tại 9,248★/13 skills → phán quyết: tin API + `ls skills/` ngày 31/10/2026, site là snapshot marketing cũ.

### Tham khảo
- Repo + docs đã mở kiểm tra 31/10/2026: `README.md` (install/skills/um/KB/rules), `AGENTS.md` (tools/rules), `plugin.json` (v0.2.0/MIT), `pyproject.toml` (Python 3.10+/Pillow/numpy/PyYAML), `CONTRIBUTING.md` (note rules), `skills/mod-any-game/SKILL.md` (vòng 10 bước), `.mcp.json` + `opencode.json` (fal MCP), `knowledge/INDEX.md` (242 notes).
- Lệnh đã chạy 31/10/2026: `bash bin/um --help/--version` (15 groups, 0.2.0), `scan --list`, `scan --help`, `kb search "terraria"`, `kb check --help`, `fal --help`, `publish check --help`; GitHub API 3 repos (universal-modder/gamedev-skills/BepInEx/Donchitos).
- Chưa chạy: plugin marketplace installs (không có Claude Code/Codex trên máy), `um fal` generate thật (không FAL_KEY, tránh tốn tiền), `um win`/`render3d`/`video` (không game/Blender/ffmpeg Windows), `um kb pr --yes` (tránh PR công khai khi chưa có mod thật).

### Được dùng ở đâu (link ngược 3 chiều — bắt buộc)
- Dùng cho `domains/game/`: xem `../../domains/game/using-universal-modder.md` (mod game + assets + test + note CHO game).

### Quay lại index
- Về `../../domains/game/README.md` (index domain game).
- Xem thêm item liên quan: `../skillry/` (assets media đóng gói), `../logo-design-skill/` (logo vector), `../awesome-opus5-5-videos/` (prompt video gốc).

---

## English

### When to use
- Modding an owned PC game (single-player, self-hosted multiplayer/server): items/weapons/enemies/bosses/units/civilizations/mechanics, 2-game mashups, porting a mod to a newer version/loader — with the closed loop recon → route → safe lab → real code → in-game slice → assets → showcase video → field note.
- Recon on an unknown game (engine/version, managed vs native, anti-cheat, loaders, saves, cheapest route) before writing any mod code.
- Engine-exact assets (true-transparency sprites, pixel art, seamless textures, PBR, image-to-3D, auto-rig, SFX/music/voice) + pipelines turning art into frames the engine loads.
- Learning from 242 agent-written field notes (working versions, routes, symptom → cause → fix gotchas) instead of re-digging.

### When to skip
- Building a NEW game from scratch (Godot/Unity/Unreal/Phaser...) with no owned game to mod → use `gamedev-skills/awesome-gamedev-agent-skills` (77 skills + router, 6,121 stars) instead.
- Hand-writing a Unity mod with no AI → use `BepInEx/BepInEx` (8,935 stars, LGPL-2.1) instead of the full skills + CLI set.
- Packaged media assets (OG/deck/launch video taste), not game assets → use `../skillry/`, `../awesome-opus5-5-videos/`, `../logo-design-skill/`.
- Online anti-cheat clients, cheats vs other players, anti-cheat/DRM/ownership bypass → NEVER use (the system refuses, see [Pitfalls](#pitfalls)).

### Install
- Skills-only (any agent, 1 command): `npx skills add https://github.com/rehan-remade/universal-modder`.
- Clone (skills + `um` CLI + MCP configs): `git clone https://github.com/rehan-remade/universal-modder`, then `export PATH="$PWD/bin:$PATH"` (Windows: add `bin` to PATH, run `bin\um.cmd`).
- Per-agent plugins (per origin README): Claude Code `/plugin marketplace add rehan-remade/universal-modder` + `/plugin install universal-modder@universal-modder`; Codex `codex plugin ...`; Gemini CLI `gemini extensions install ...`; OpenCode 2 `opencode plugin add '...'`; VS Code/Copilot plugin-from-source; Cursor reads `AGENTS.md`.
- Standalone `um` CLI: `uv tool install git+https://github.com/rehan-remade/universal-modder` (or `pipx install ...`).
- Requires: Git + Python 3.10+ (Pillow/numpy/PyYAML via `uv`) + ffmpeg; `render3d` needs Blender; Windows games run natively or from WSL.
- Assets: `FAL_KEY` for fal (store once via `um fal key set`; `um fal key status` shows the source). No key → fal OAuth browser sign-in + free local `um comfy`. `um sprixen` / `um voidless` need their own separate paid keys.
- Verified 31/10/2026: `bash bin/um --help` lists all 15 groups + version 0.2.0; `scan --list` correctly reports no installs on a gameless Linux box; `kb search "terraria"` returns the Fal Arsenal note + 2 related notes with routes/statuses. Sources opened: README, AGENTS.md, plugin.json, pyproject.toml, CONTRIBUTING.md, mod-any-game SKILL.md, .mcp.json, opencode.json, knowledge/INDEX.md.

### How the item works
- Backing organization: individual `rehan-remade`, repo `https://github.com/rehan-remade/universal-modder`, MIT, v0.2.0, created 30/09/2026, updated 31/10/2026, 328 commits. GitHub API 31/10/2026: 9,248 stars / 1,034 forks / 49 watchers.
- Core operating method: the `mod-any-game` skill runs a fixed 10-step loop (intake → recon → route → lab backup → source of truth → vertical slice → assets → in-game verify → showcase → publish + field note); 12 engine playbooks; Python `um` CLI (one module per group, every group has `--help` with examples); fal MCP at `https://mcp.fal.ai/mcp`; machine-indexed knowledge base (`um kb index`); 3-agent team (orchestrator supervises, game-worker alone touches the game, offline-worker never does).
- Per-usecase operating differences: new mods (recon + 1 of 6 routes + backup lab + real-code reading — see [Sub-usecase 1](#sub-usecase-1-new-mod-for-an-owned-game--recon-route-slice-verify)) vs assets (fal REST generation + deterministic `sprite`/`render3d` conversion with `fal_manifest.jsonl` — see [Sub-usecase 2](#sub-usecase-2-falcomfy-assets--engine-exact-pipeline)) vs testing/showcase (live process capture via `win` + EDL cutting via `video` — see [Sub-usecase 3](#sub-usecase-3-in-game-testing--showcase-video)) vs porting/mashups + notes (layered diffs + knowledge PRs — see [Sub-usecase 4](#sub-usecase-4-porting--2-game-mashups--field-notes)).

### Invariant core
- Prior art first: every mod starts with `um kb search "<game>"` + `"<engine>"` (reuse exact versions/routes/gotchas) + `um scan "<game>"` (read the indicated playbook). See [Sub-usecase 1](#sub-usecase-1-new-mod-for-an-owned-game--recon-route-slice-verify). Guessing the engine = off-system.
- Safe lab before the first modded launch: `um backup create` + separate lab profile + fixed windowed size + decompiles/extracts OUTSIDE the repo. See [Shared steps](#shared-steps). Touching saves unbacked = FAIL.
- Vertical slice before widening: one item/unit/weapon end-to-end with logs + a looked-at screenshot before expanding, committing each working step. Off-system when bulk-building on a red slice.
- Clean shipping + recording: `um publish check` (no game files/decompiled code/keys) + `um kb check` before every publish/PR + a field note (versions/route/engine-truth/verify/gotchas). See [Sub-usecase 4](#sub-usecase-4-porting--2-game-mashups--field-notes).
- After use you must name: which notes were reused, which backup, which slice was verified, which manifest/checks. Otherwise the system was not really used.

### Customizable surface
- Tunable: game + 1-sentence idea + done definition (usually in-game + 20–45s clip), 1 of 6 routes, which of the 13 skills, which fal model (`um fal search` for current IDs), asset style/size/camera preset (`aoe2/iso8/trueiso/topdown/side/turntable`), EDL/video style, game vs technique note. Two-level approval gate: (1) which artifact — shortlist 2–3 routes/skills/models with reasons via the question tool, user picks before any build (a greenlit idea never implies a greenlit route/model); (2) what stays/changes — lock style/size/model before bulk generation (failed fal calls still bill). Waivers (skipping backup, engine/model swap, online anti-cheat games, unchecked publish) must quote the user's explicit ok, never inferred.
- Never listed here: anti-cheat/cheat/DRM bypass, shipping game files/dumps, PID-less kills, unasked mouse/loader/publish actions (all `must-not`, see [Pitfalls](#pitfalls)).

### Work split
- Main agent: 1-sentence intake + `kb search` + `scan` + playbook + route shortlist (user picks — never self-pick then build), lab backup, real-code reading, slice build, all `um` asset/pipeline/publish/kb runs, presenting logs + screenshots + manifests + checks; verifies backup + live slice + `publish check` + `kb check` green + INDEX refresh.
- Hand to claude for browser/account-gated steps: web research that survives dead forums (Wayback, Nexus/Workshop login-gated handoff) + upstream screenshots as evidence + looking at verify images/video in a real browser — delegate via `claude --chrome --model sonnet -p "<game + route + URLs + states + expected output>" --dangerously-skip-permissions --output-format text`, with game/version/route attached; never invent lookup results. No browser → declare it and stop that step, never claim observation.
- Agent verifies: backup snapshot exists + game log + looked-at screenshot + complete `fal_manifest.jsonl` + green checks + versions/route/gotchas in the note + PR only on explicit human ok.

### Differentiating positioning (GitHub API numbers, 31/10/2026)
- Vs `gamedev-skills/awesome-gamedev-agent-skills` (agent skills for games, 6,121 stars/584 forks, Apache-2.0, 77 build-new-game skills + router): different direction — it BUILDS new games; universal-modder MODS installed games (`scan` fingerprint + backup lab + live verify + 242 field notes). Pick universal-modder when an owned game + cheapest mod route + real gotchas decide (bar: `scan` yields engine/routes + `kb search` yields version-matching notes); pick gamedev-skills for a from-scratch Godot/Unity/Unreal game with a router.
- Vs `BepInEx/BepInEx` (hand-written Unity modding framework, 8,935 stars/932 forks, LGPL-2.1): different layer — BepInEx is the loader/API; universal-modder is the agent loop that USES such loaders when cheapest (tModLoader/SMAPI/BepInEx/UE4SS/REFramework/SKSE/Fabric) plus code reading, assets, verify, notes. Pick universal-modder for the full loop (measurable via logs/screenshots/manifests); pick plain BepInEx when hand-writing a Unity plugin with no AI/fal cost.
- Honest frame: universal-modder wins on closed-loop modding of owned games; loses on new-game builds (gamedev-skills / 30,491-star Claude-Code-Game-Studios win) and on minimalism (plain BepInEx wins when only a loader is needed).

### Coverage map (full 13-skill + 15-group + 12-playbook + 3-agent + knowledge/INDEX scan, 31/10/2026 — ★ strongest first)
- ★ New mod for an owned game (recon → route → slice → verify → note): see Sub-usecase 1.
- fal/ComfyUI assets + engine-exact pipeline (`fal` 16 recipes + `sprite` 10 ops + `render3d` 6 presets): see Sub-usecase 2.
- Live in-game testing + showcase video (`win` + `video` groups): see Sub-usecase 3.
- Medium: version/loader porting without drift (`port-a-mod`): see Sub-usecase 4.
- Medium: 2-game mashups/passthrough + decomp-as-library (`mashup-mods` + Minecraft×GTA V / AoE2 / Terraria examples): see Sub-usecase 4.
- Medium: dead-forum-proof web research (`game-research-websearch`) → use when KB + wiki/loader docs are insufficient.
- Medium: Blitz3D decompilation (`blitz3d-decomp` via B3DDecomp — present in `skills/` but missing from the origin README's 12-skill table, verified via `ls skills/` 31/10/2026) → use for old Blitz3D games only.
- Medium: CoD4/WaW specialist tools (`fastfile`/`iwi`/`weapon`, read-only unsigned PC zones) → use for exactly those two CoD titles.
- NOT supported → use instead: anti-cheat/cheat/DRM bypass → refused (no replacement, see [Pitfalls](#pitfalls)); new-game builds → `awesome-gamedev-agent-skills`; vector logos → `../logo-design-skill/`; packaged media taste → `../skillry/`; original video prompts → `../awesome-opus5-5-videos/`; gated page systems → `../hallmark/`; React bricks → `../reactbits/`.

### Decision dossier
- Jobs SERVED (4): 1. owned-game mods to in-game + clip + note (Terraria Fal Arsenal, AoE2 San Franciscans, Minecraft-inside-GTA-V); 2. engine-exact assets (sprites/PBR/3D/rig/audio + cutout/fit/sheets + GLB→frames); 3. in-game testing + showcase (launch/shot/drive/record + EDL compile); 4. ports/mashups + shared field notes via PR.
- Jobs NOT served (5, each with its replacement): 1. new games from scratch → `awesome-gamedev-agent-skills` (6,121 stars); 2. hand-written Unity mods → `BepInEx` (8,935 stars); 3. decorative media assets → `../skillry/` + `../awesome-opus5-5-videos/`; 4. audited vector logos → `../logo-design-skill/`; 5. online cheats/bypass → refused by design.
- Free / total + price: core $0 (MIT). External metering: fal per-model billing (see `um fal price <model>`, rates drift — no static quote); Sprixen / Voidless separate paid keys; local ComfyUI $0; Blender $0. Total bill = $0 core + fal spend (failures bill too) + external keys if used.
- Install friction: 2 steps to the first command (`git clone` + `export PATH`, then `um --help`; skills-only is 1 command). Ran through: `--help`/version, `scan --list`, `kb search "terraria"`, 3 group helps. Barriers: Git + Python 3.10+ + ffmpeg required; `uv` recommended; Blender for `render3d`; `FAL_KEY` for fal assets; Windows/WSL for `win`; owned licensed game; `gh` + explicit human ok for PRs.
- Viral same-segment opponents: `awesome-gamedev-agent-skills` (6,121 stars/584 forks, Apache-2.0) vs `BepInEx/BepInEx` (8,935 stars/932 forks, LGPL-2.1). GitHub API 31/10/2026.
- Pick it over opponents when: an installed game must be modded to verified-working (bar: `scan` yields engine/routes + `kb search` yields version-matching notes + slice proven by log/screenshot + green checks). Choice-flipping example: owned Terraria + crater nuke + fal sprites → universal-modder; from-scratch Godot game → gamedev-skills; hand-written Unity plugin → BepInEx.
- NEVER use when: online anti-cheat clients to be touched, cheats vs others, bypasses, shipping game files/dumps, no Python 3.10+/Git, or modding without save backups.

### Sub-usecase 1: new mod for an owned game — recon/route/slice/verify
- When to use: owned game + 1-sentence idea needing the full loop to in-game + note.
- When to skip: assets-only → Sub-usecase 2; testing/video for an existing mod → Sub-usecase 3; ports/mashups → Sub-usecase 4; online anti-cheat → drop entirely.
- How its mechanism differs: the only flow running the full intake→note chain with 6 routes + backup lab + real-code reading; other sub-usecases do one segment (art / capture-cut / port-PR).
- Copy-paste command: `um kb search "<game>"`, then `um scan "<game>"` (read its playbook), then `um backup create "<saves folder>" --name <game>-saves`, build the slice, then `um publish check <mod-dir>` (sources: origin AGENTS.md + SKILL.md steps 0–5/9; `kb search` + `scan --list` really ran 31/10/2026).
- Numeric bar: KB yields game/engine-matching notes (242 to match against); scan yields engine/version/managed-vs-native/anti-cheat/loaders/saves/ranked routes; backup snapshot exists BEFORE the first modded launch; 1-item slice proven live (log + looked-at screenshot); `publish check` green.
- Input-output example (illustrative — route/scope user-picked first, never a default): "owned Terraria on Steam: homing missile launcher + world-cratering tactical nuke, done = in-game + 20–45s clip" → `MODDING_PLAN.md` (route `loader-api` tModLoader + .NET/XNA playbook) + save backup + proven missile slice (log + screenshot) + full nuke/enemies/2-phase boss + `examples/terraria-tmodloader` + note `games/terraria/fal-arsenal-tmodloader.md` (working, versions inside).
- Own pitfalls: un-scanned engine guesses pick the wrong route (exe enforcement ≠ data, e.g. AoE2's 64-civ data vs hard-coded picker → slot replace); bulking up on a red slice; unbacked launches; committing game files/decompiles.
- This sub-usecase's split: main agent does intake/scan/KB/route-shortlist/backup/slice/verify (route shortlist via question tool, user picks before build); hands login-gated research + evidence screenshots to claude; verifies via backup + log + looked-at screenshot + publish check.

### Sub-usecase 2: fal/ComfyUI assets + engine-exact pipeline
- When to use: the game's native assets are studied (size/palette/outline/camera/facing/frames) and generated sprites/textures/PBR/3D/rigs/audio/video must be converted to engine-loadable formats.
- When to skip: pure data/code mods → Sub-usecase 1; existing art only needs testing → Sub-usecase 3.
- How its mechanism differs: fal REST generation (metered, every call logged to `fal_manifest.jsonl`) + deterministic conversion (`sprite`/`render3d`/local ComfyUI); never touches the running game or the knowledge base PR flow.
- Copy-paste command: `um fal sprite "a rusty scrap drone enemy, side view facing left, 16-bit pixel art" --out assets/gen --name drone`, then `um sprite fit assets/gen/drone.png --size 64x26` (pixel games) or `um fal model3d concept.png` then `um render3d model.glb --preset aoe2` (3D→sprites) (sources: `um fal --help` + origin pipeline figure, read 31/10/2026).
- Numeric bar: exact frame size/palette/outline/camera (e.g. Terraria via one nearest-neighbour fit; AoE2 via 16 headings from the game's camera); real transparency; consistent variants (1 concept → edits; 1 concept → 1 3D model → all headings); every call logged in `fal_manifest.jsonl`; model IDs re-checked via `um fal search` (IDs drift fast).
- Input-output example (illustrative — style/model user-picked first): "64x26 Terraria drone + 16-heading AoE2 Robotaxi" → `assets/gen/drone.png` + 64x26 fit + Trellis-2 `model.glb` + 16 `aoe2`-preset frames + complete manifest + in-game sprites as in the origin examples.
- Own pitfalls: bulk generation before locking style/model (failures bill); stale memorized model IDs (always `search` again); fake transparency; blurred pixel-art upscales (must be grid-snapped + palette-limited via `pixelate`); confusing Sprixen/Voidless keys with fal's (separate paid services).
- This sub-usecase's split: main agent studies native assets + generates + converts + presents looked-at images (style/model shortlist via question tool, user picks before bulk runs); hands browser-side image comparison to claude; verifies via size/palette/manifest + in-game asset load.

### Sub-usecase 3: in-game testing + showcase video
- When to use: a built mod needs its oracle (the running game) + a 20–45s styled showcase with music/titles.
- When to skip: no proven slice yet → Sub-usecase 1; no assets yet → Sub-usecase 2.
- How its mechanism differs: touches live processes/windows/audio (`win`: launch/shot/record/drive/ps/kill/reg with gfxcapture + process-loopback audio, PID-only kills) + EDL cutting (`video`: contact/compile/mux/beats/first-frame, EDL = edit decision list holding cuts/titles/music); writes no mod code, opens no PRs.
- Copy-paste command: `um win launch "<game>"`, then `um win shot --out shots/` (look at the image), then `um win record --out clips/` (game audio only), then `um video compile edit.edl --out showcase.mp4` (sources: `um --help` groups + SKILL.md steps 7–8).
- Numeric bar: fixed windowed size (registry/ini) for stable shots/clicks; repeatable tests (mod-side chat command/timeline/scenario/isolated test world, one pristine copy restored before every take); game-only input (`um win drive`) and audio; crash reporters cleaned per take; 20–45s beat-cut titled clip.
- Input-output example (illustrative): "verify the Terraria nuke crater + cut a clip" → isolated test world + launch/drive menus→scene path + looked-at screenshots + EDL + music showcase like the origin's 6-mod teaser.
- Own pitfalls: focusing an online-mode game while the user types (banned — ask first); name-pattern kills (kill exact PIDs); GPU-unsafe shots; skipping pristine restores; recording desktop audio.
- This sub-usecase's split: main agent drives/launches/shots/records/compiles + presents viewed images/clips; hands browser clip/image review to claude; verifies via log + viewed image + 20–45s game-audio-only clip.

### Sub-usecase 4: porting + 2-game mashups + field notes
- When to use: an old mod needs a drift-free move to a newer version/loader; two games at once (ports/passthrough/decomp-as-library/reimplementation); a finished mod needs its note + PR for the next agent.
- When to skip: single-game new mods → Sub-usecase 1.
- How its mechanism differs: layered comparison + per-unit tests + resumable status docs (`port-a-mod`, incl. Forge 1.7.10→Fabric 1.20.1 map) / 2-engine WebSocket bridges + depth compositing (`mashup-mods`, e.g. Minecraft×GTA V) / scaffold-validate-PR (`share-field-notes` + `um kb`); CoD4/WaW use specialist tools (`fastfile/iwi/weapon`).
- Copy-paste command: `um kb new --game "Hades II" --title "A new boon god" --from-scan hades --agent "Codex (gpt-6)"`, then `um kb check knowledge/games/hades-ii/a-new-boon-god.md`, then `um kb pr knowledge/games/hades-ii/a-new-boon-god.md --yes` (only after explicit human ok) (sources: origin README + CONTRIBUTING.md, read 31/10/2026; CoD: `um fastfile list <zone.ff>`, `um iwi iwi2png <tex.iwi>`, `um weapon get <file>`).
- Numeric bar: ports keep one pinned source + private decompile + script-extracted data + unit-by-unit tests + per-layer audits (with mapping table); notes carry exact versions + route + engine truth + build steps + verify + symptom→cause→fix gotchas; `kb check` green (blocks >150 lines FAIL, >60 WARN) + `INDEX.md` refreshed via `um kb index`; PRs carry no game files/extracts/dumps/pirated links (violations closed).
- Input-output example (illustrative): "port a Forge 1.7.10 mod to Fabric 1.20.1 + note" → pinned source + out-of-repo decompile + mapping table + per-unit tests + audits + note `knowledge/games/<game>/<slug>.md` + PR after human ok (live models: 242 game notes + 88 techniques in INDEX, 31/10/2026).
- Own pitfalls: duplicate notes per game (`kb search` first, improve the old one); >150-line own-code snippets in notes; pasting leaked/beta code (restate in own words); PR-ing before human ok (PRs carry human identity); CoD zones outside the two supported titles/unsigned-PC scope.
- This sub-usecase's split: main agent scaffolds/fills/validates/indexes + presents the note diff for human approval (explicit ok before `--yes`); hands PR-page/upstream screenshots to claude; verifies via `kb check` + fresh index + 1-note PR with no banned files.

### Shared steps
1. One-sentence intake (game + store/platform + idea) + done definition (usually in-game + 20–45s clip) + online/offline split first (online anti-cheat → offline/private-server/official tools only) + open `MODLOG.md`.
2. `um kb search "<game>"` + `"<engine>"` (reuse old versions/routes/gotchas) + `um scan "<game>"` + playbook + current community research (never install from memory).
3. Pick the cheapest route to the idea (data / loader-API / managed-patch / native-hook / reimplement-decomp / mashup) + log the reason in MODLOG.md (2–3 shortlist via question tool, user picks before build).
4. Lab: `um backup create` (+config) + separate lab profile + fixed windowed size + out-of-repo decompiles/extracts + gitignore.
5. Read the source of truth (ILSpy/Cpp2IL/Vineflower/Ghidra-IDA-MCP/Cheat Engine/Frida/RenderDoc/dump tools) + log exact names/IDs (check exe enforcement, not just data).
6. One-item slice to proven-working (log + looked-at screenshot), then widen, committing each working step.
7. Assets: study native assets → `um fal`/`comfy`/`sprixen`/`voidless` (full manifest) → `um sprite`/`render3d` to engine-exact formats.
8. Live verify (repeatable test + drive + shot + pristine restore) → record → `um video` showcase.
9. `um publish check` + `um kb check` + note + `um kb index` + PR after human ok (`--yes`).

### Sample prompts
- "Mod my owned Terraria on Steam: a homing missile launcher + a world-cratering tactical nuke. Recon with `um kb search` + `um scan` first, present a shortlist of route + skill + fal model (2–3 with reasons) and wait for my pick before building. Back up saves before the first launch, prove one weapon slice live (log + screenshot you actually open) before widening. No invented versions, no shipped game files."
- "Generate fal sprites for a 64x26 Terraria drone: study the native assets (size/palette/outline) first, present 2–3 styles/models with reasons and wait for my pick, then concept → cutout → one nearest-neighbour fit → complete manifest. Re-check model IDs with `um fal search`, never from memory."
- "Verify the mod live + cut a 20–45s clip: fixed windowed size + isolated test world (keep a pristine copy, restore every take), drive→shot→record (game audio only) → EDL compile. Ask before driving mouse/keys. Then `publish check` + `kb check` + field note; PR only on my explicit ok."

### Pitfalls
- Touching online anti-cheat clients / writing anti-player cheats / bypassing anti-cheat-DRM-ownership → the system refuses (source: `safety.md` via `AGENTS.md`); offer offline/private-server/official tools instead.
- Shipping game files/extracted assets/decompiled dumps/pirated links/ROMs-ISOs in mods or PRs → PRs closed + `publish check`/`kb check` block (check before every publish).
- First modded launch without `um backup create` → lost saves; shared test worlds → contamination (always separate lab saves + pristine restores).
- Name-pattern process kills → wrong victims (kill exact PIDs via `um win kill <pid>`); focusing online games while the user types; installing loaders/registry edits unasked.
- Bulk fal generation before locking style/model (failures bill) + memorized model IDs (IDs drift — always `search` again) + mixing up Sprixen/Voidless keys with fal's.
- Repo-specific trap: `bin/um` is a shell wrapper (`export PATH`), so `python3 bin/um` throws SyntaxError (hit 31/10/2026 — always `bash bin/um` or `./bin/um`); the 13th skill `blitz3d-decomp` exists in `skills/` but is missing from the origin README's 12-skill table (never claim only 12).

### Usage references (measured 31/10/2026 unless noted)
- Deep review: [Frontier Now 08/10/2026](https://frontiernow.dev/en/github/universal-modder/) "packs 11 Agent Skills, a fal MCP server and the um CLI ... so they can mod almost any PC game you own" + "every agent that lands a mod files a field note ... so the next agent starts where the last one stopped" → confirms the pick for KB + closed loop, and flips the age expectation: 8 days old at 5,222 stars then, so interfaces/layout move + the mod hub was unopened (still "coming next" at 31/10/2026).
- Deep review 2: [awesome-ai-game-dev-tools 15/10/2026](https://github.com/SubmitGame/awesome-ai-game-dev-tools) lists universal-modder at 7.7k stars as the only agent-driven-modding entry with a verified example (Terraria Fal Arsenal) + 7 mashup videos (MrToucan 345,483 views, Lessons 444,003 views, Better Stack 22,543) → confirms the pick when proven examples + video community matter, not a bare listing.
- Weighted average: GitHub 9,248 stars/1,034 forks/49 watchers/328 commits (API 31/10/2026) — strong weight (9.2k stars 31 days after 24 stars on 29/09/2026 per Funcoding history, +8.2k/30d; 1k forks = real use). KB: 242 game notes + 88 techniques + 10 examples (INDEX + `ls` 31/10/2026) — direct prior-art weight. No independent marketplace/HN/ProductHunt star rating found → recorded as `unverified` for scored reviews, never inferred.
- Conflict: `universalmodder.org` advertises "3.4k+ stars / 10 skills" (stale snapshot) vs README + API at 9,248 stars/13 skills → verdict: trust the 31/10/2026 API + `ls skills/`; the site is an older marketing snapshot.

### References
- Checked origin docs 31/10/2026: `README.md` (install/skills/um/KB/rules), `AGENTS.md` (tools/rules), `plugin.json` (v0.2.0/MIT), `pyproject.toml` (Python 3.10+/Pillow/numpy/PyYAML), `CONTRIBUTING.md` (note rules), `skills/mod-any-game/SKILL.md` (10-step loop), `.mcp.json` + `opencode.json` (fal MCP), `knowledge/INDEX.md` (242 notes).
- Really ran 31/10/2026: `bash bin/um --help/--version` (15 groups, 0.2.0), `scan --list`, `scan --help`, `kb search "terraria"`, `kb check --help`, `fal --help`, `publish check --help`; GitHub APIs for universal-modder/gamedev-skills/BepInEx/Donchitos.
- Not run: marketplace plugin installs (no Claude Code/Codex on this box), real `um fal` generation (no FAL_KEY, avoids spend), `um win`/`render3d`/`video` (no game/Blender/Windows ffmpeg), `um kb pr --yes` (avoids a public PR with no real mod).

### Where used (3-way backlinks — required)
- Used in `domains/game/`: see `../../domains/game/using-universal-modder.md` (game modding + assets + testing + notes FOR games).

### Back to index
- Back to `../../domains/game/README.md` (game domain index).
- Related items: `../skillry/` (packaged media assets), `../logo-design-skill/` (vector logos), `../awesome-opus5-5-videos/` (original video prompts).
