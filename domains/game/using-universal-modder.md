# domains/game/using-universal-modder.md — dùng universal-modder CHO game

## Tiếng Việt

### Usecase trong domain này
- ★ Mod mới cho game sở hữu (recon → route → slice → verify → note): xem [Usecase con 1](../../items/universal-modder/README.md#usecase-con-1-mod-moi-cho-game-so-huu--recon-route-slice-verify).
- Assets chuẩn engine (`fal`/`comfy` + `sprite`/`render3d`): xem [Usecase con 2](../../items/universal-modder/README.md#usecase-con-2-assets-bang-falcomfy--pipeline-ve-chuan-engine).
- Test trong game thật + video showcase (`win` + `video`): xem [Usecase con 3](../../items/universal-modder/README.md#usecase-con-3-test-trong-game-that--video-showcase).
- Port mod / mashup 2 game / share field note (`um kb` + tools CoD): xem [Usecase con 4](../../items/universal-modder/README.md#usecase-con-4-port-mod--mashup-2-game--share-field-note).

### Lệnh mẫu cụ thể (cho domain này)
- Recon + lab (chạy trong thư mục clone, PATH đã export): `um kb search "<game>"` + `um scan "<game>"` rồi `um backup create "<saves folder>" --name <game>-saves` — khớp [Usecase con 1](../../items/universal-modder/README.md#usecase-con-1-mod-moi-cho-game-so-huu--recon-route-slice-verify), lệnh gốc ở [Cài đặt](../../items/universal-modder/README.md#cai-dat-da-clone--chay-thu-um-tren-linux-31102026-chua-cai-plugin-marketplace-vi-may-nay-khong-co-claude-codecodex).
- Assets đúng game đang mod: `um fal sprite "<mô tả>" --out assets/gen --name <tên>` + `um sprite fit <file> --size <WxH-game>` (pixel) hoặc `um render3d <model.glb> --preset aoe2` (3D→sprites) — khớp [Usecase con 2](../../items/universal-modder/README.md#usecase-con-2-assets-bang-falcomfy--pipeline-ve-chuan-engine).
- Test + clip cho đúng game đó: `um win shot --out shots/` + `um video compile edit.edl --out showcase.mp4` — khớp [Usecase con 3](../../items/universal-modder/README.md#usecase-con-3-test-trong-game-that--video-showcase).
- Note + PR sau mod: `um kb new --game "<game>" ...` + `um kb check <note>` + `um kb pr <note> --yes` (chỉ sau human ok) — khớp [Usecase con 4](../../items/universal-modder/README.md#usecase-con-4-port-mod--mashup-2-game--share-field-note).

### Lưu ý riêng cho domain
- Game online có anti-cheat: hệ từ chối chạm client — chỉ offer offline/private-server/tools chính thức (xem [Pitfalls](../../items/universal-modder/README.md#pitfalls)).
- `bin/um` là shell wrapper: gọi `bash bin/um` (không `python3 bin/um` — SyntaxError đã gặp, xem [Pitfalls](../../items/universal-modder/README.md#pitfalls)).
- Mọi fal generate tốn tiền kể cả fail — chốt style/model qua user pick trước khi chạy loạt (xem [Phần tùy chỉnh](../../items/universal-modder/README.md#phan-tuy-chinh)).
- Publish/PR trong domain game mang identity human + cấm game files/dumps — check trước mọi lần (xem [Usecase con 4](../../items/universal-modder/README.md#usecase-con-4-port-mod--mashup-2-game--share-field-note)).

### Điểm mạnh cốt lõi của item CHO domain này
- Recon ra route rẻ nhất cho đúng game đã cài (`scan` fingerprint + ranked routes + playbook), không đoán — ngưỡng: note KB khớp versions (xem [Cách item hoạt động](../../items/universal-modder/README.md#cach-item-hoat-dong)).
- Lab + slice + verify khép kín trong game thật (backup + log + screenshot đã nhìn + manifest) — khác quay màn hình chung (xem [Usecase con 1](../../items/universal-modder/README.md#usecase-con-1-mod-moi-cho-game-so-huu--recon-route-slice-verify) + [Usecase con 3](../../items/universal-modder/README.md#usecase-con-3-test-trong-game-that--video-showcase)).
- Mỗi mod để lại note cho agent sau (242 notes + INDEX máy sinh) — domain game tích lũy tri thức, không làm lại từ đầu (xem [Usecase con 4](../../items/universal-modder/README.md#usecase-con-4-port-mod--mashup-2-game--share-field-note)).

### Phân công CHO domain này (1 dòng + link, không copy)
- Agent chính intake/scan/KB/backup/build/verify + trình shortlist route-model chờ user pick; giao claude research login-gated + xem ảnh/clip trên browser; verify bằng backup + log + screenshot + manifest + checks — chi tiết ở [Phân công ai làm gì](../../items/universal-modder/README.md#phan-cong-ai-lam-gi).

### Link về item gốc (3 chiều — bắt buộc)
- Gốc: `../../items/universal-modder/README.md` (các section: [Cài đặt](../../items/universal-modder/README.md#cai-dat-da-clone--chay-thu-um-tren-linux-31102026-chua-cai-plugin-marketplace-vi-may-nay-khong-co-claude-codecodex) / [Cách hoạt động](../../items/universal-modder/README.md#cach-item-hoat-dong) / [Định vị](../../items/universal-modder/README.md#dinh-vi-khac-biet-so-lieu-api-github-ngay-31102026) / [Usecases](../../items/universal-modder/README.md#usecase-con-1-mod-moi-cho-game-so-huu--recon-route-slice-verify)).
- Index domain: `./README.md` (4 hàng điều hướng + định vị + ma trận).
- Được liệt kê ngược tại: `../../items/universal-modder/README.md#duoc-dung-o-dau`.

---

## English

### Usecases in this domain
- ★ New mod for an owned game (recon → route → slice → verify → note): see [Sub-usecase 1](../../items/universal-modder/README.md#sub-usecase-1-new-mod-for-an-owned-game--recon-route-slice-verify).
- Engine-exact assets (`fal`/`comfy` + `sprite`/`render3d`): see [Sub-usecase 2](../../items/universal-modder/README.md#sub-usecase-2-falcomfy-assets--engine-exact-pipeline).
- Live testing + showcase (`win` + `video`): see [Sub-usecase 3](../../items/universal-modder/README.md#sub-usecase-3-in-game-testing--showcase-video).
- Ports / 2-game mashups / field-note sharing (`um kb` + CoD tools): see [Sub-usecase 4](../../items/universal-modder/README.md#sub-usecase-4-porting--2-game-mashups--field-notes).

### Concrete commands (for this domain)
- Recon + lab (inside the clone, PATH exported): `um kb search "<game>"` + `um scan "<game>"`, then `um backup create "<saves folder>" --name <game>-saves` — matches [Sub-usecase 1](../../items/universal-modder/README.md#sub-usecase-1-new-mod-for-an-owned-game--recon-route-slice-verify); origin commands in [Install](../../items/universal-modder/README.md#install).
- Assets for the game being modded: `um fal sprite "<desc>" --out assets/gen --name <name>` + `um sprite fit <file> --size <game-WxH>` or `um render3d <model.glb> --preset aoe2` — matches [Sub-usecase 2](../../items/universal-modder/README.md#sub-usecase-2-falcomfy-assets--engine-exact-pipeline).
- Test + clip for that game: `um win shot --out shots/` + `um video compile edit.edl --out showcase.mp4` — matches [Sub-usecase 3](../../items/universal-modder/README.md#sub-usecase-3-in-game-testing--showcase-video).
- Note + PR after modding: `um kb new --game "<game>" ...` + `um kb check <note>` + `um kb pr <note> --yes` (human ok first) — matches [Sub-usecase 4](../../items/universal-modder/README.md#sub-usecase-4-porting--2-game-mashups--field-notes).

### Domain-specific notes
- Online anti-cheat games: the system refuses client touches — offer offline/private-server/official tools only (see [Pitfalls](../../items/universal-modder/README.md#pitfalls)).
- `bin/um` is a shell wrapper: call `bash bin/um`, never `python3 bin/um` (SyntaxError, see [Pitfalls](../../items/universal-modder/README.md#pitfalls)).
- Every fal call bills including failures — lock style/model via user pick before bulk runs (see [Customizable surface](../../items/universal-modder/README.md#customizable-surface)).
- Game-domain publishing/PRs carry human identity and ban game files/dumps — check every time (see [Sub-usecase 4](../../items/universal-modder/README.md#sub-usecase-4-porting--2-game-mashups--field-notes)).

### Core strengths FOR this domain
- Cheapest-route recon for the exact installed game (`scan` fingerprint + ranked routes + playbook), never guessed (see [How it works](../../items/universal-modder/README.md#how-the-item-works)).
- Closed lab + slice + live verify loop (backup + log + viewed screenshot + manifest) (see [Sub-usecases 1](../../items/universal-modder/README.md#sub-usecase-1-new-mod-for-an-owned-game--recon-route-slice-verify) + [3](../../items/universal-modder/README.md#sub-usecase-3-in-game-testing--showcase-video)).
- Every mod leaves a note for the next agent (242 notes + machine INDEX) — the game domain accumulates knowledge (see [Sub-usecase 4](../../items/universal-modder/README.md#sub-usecase-4-porting--2-game-mashups--field-notes)).

### Work split FOR this domain (1 line + link, never copied)
- Main agent does intake/scan/KB/backup/build/verify + route-model shortlist for user pick; hands login-gated research + image/clip review to claude; verifies via backup + log + screenshot + manifest + checks — details in [Work split](../../items/universal-modder/README.md#work-split).

### Links to item origin (3-way — required)
- Origin: `../../items/universal-modder/README.md` (sections: [Install](../../items/universal-modder/README.md#install) / [How it works](../../items/universal-modder/README.md#how-the-item-works) / [Positioning](../../items/universal-modder/README.md#differentiating-positioning-github-api-numbers-31102026) / [Sub-usecases](../../items/universal-modder/README.md#sub-usecase-1-new-mod-for-an-owned-game--recon-route-slice-verify)).
- Domain index: `./README.md` (4 routing rows + positioning + matrix).
- Backlisted at: `../../items/universal-modder/README.md#where-used`.
