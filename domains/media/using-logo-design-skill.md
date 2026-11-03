# using-logo-design-skill CHO media — logo/brand mark SVG + favicon + board (CHARTER v9)

> Phần logo/nhận diện của logo-design-skill KHI DÙNG CHO media. Gốc ở `../../items/logo-design-skill/README.md`.

## Tiếng Việt

### Usecase trong domain này
- ★ Thiết kế logo/brand mark mới (brief media: tên kênh/sản phẩm + audience + tính từ) → kit SVG + board mockups đúng ngành: xem [Usecase con 1](../../items/logo-design-skill/README.md#usecase-con-1-thiet-ke-logo-moi--checkpoint--kit).
- Refresh/critique logo kênh media có sẵn (giữ equity) : xem [Usecase con 2](../../items/logo-design-skill/README.md#usecase-con-2-critique--redesign-logo-co-san).
- Favicon/app-icon/social-square + bản one-colour từ master đã duyệt (dùng cho site/kênh/app): xem [Usecase con 3](../../items/logo-design-skill/README.md#usecase-con-3-xuat-faviconapp-iconbien-the--render-png).
- Board pitch + guidelines 1 trang cho khách hàng media: xem [Usecase con 4](../../items/logo-design-skill/README.md#usecase-con-4-board-trinh-bay--guidelines--identity).

### Lệnh mẫu cụ thể (cho media)
- Research category trước khi vẽ (khớp từng chữ lệnh gốc): `python3 scripts/search_library.py --industry <closest> --summary` (vd `payments-fintech` → 37/1432, đã chạy thật). Xem [Cài đặt](../../items/logo-design-skill/README.md#cai-dat-da-clone--chay-thu-scripts-tren-linux-30102026-chua-cai-plugin-marketplace-vi-may-nay-khong-co-claude-code).
- Checkpoint sau test (media xem ảnh này để duyệt): `python3 scripts/concept_sheet.py a-symbol.svg b-symbol.svg c-symbol.svg --lockups a-lockup.svg b-lockup.svg c-lockup.svg --names "Name A" "Name B" "Name C" --notes "One-line idea A" "…" "…" --recommend 1 --greyscale -o concepts.png`. Xem [Usecase con 1](../../items/logo-design-skill/README.md#usecase-con-1-thiet-ke-logo-moi--checkpoint--kit).
- Xuất assets cho site/kênh: `python3 scripts/export_variants.py final-symbol.svg --title "Brand logo" --mono "#0F7C80" --icon-bg "#0F7C80" --web-icons --favicon-source final-symbol-small.svg`. Xem [Usecase con 3](../../items/logo-design-skill/README.md#usecase-con-3-xuat-faviconapp-iconbien-the--render-png).
- Board đúng ngành media (12 ngành, vd café → cup/bag/signage; software → README/terminal): `python3 scripts/presentation_board.py --list-mockups` để chốt list, rồi chạy board từ spec JSON. Xem [Usecase con 4](../../items/logo-design-skill/README.md#usecase-con-4-board-trinh-bay--guidelines--identity).

### Lưu ý riêng cho domain
- Phân biệt với OG raster của Skillry: brief media cần master SVG dùng lâu dài (dập 1 màu, khắc, thêu, favicon 16px) → logo-design-skill chính; cần ảnh OG/social nhanh đúng taste → Skillry chính (raster GPT Image). Xem [Định vị](../../items/logo-design-skill/README.md#dinh-vi-khac-biet-so-lieu-api-github-ngay-30102026).
- Logo thư viện media (app/tech) dễ đụng hàng nhất → bắt buộc shelf test + reverse-image trước khi chốt (TRADEMARKS.md: MIT không cover SVG thư viện). Xem [Pitfalls](../../items/logo-design-skill/README.md#pitfalls).
- Font dùng cho wordmark media phải xác minh license cho phép làm logo; render PNG thiếu backend thì khai báo, cấm claim đã test. Xem [Usecase con 3](../../items/logo-design-skill/README.md#usecase-con-3-xuat-faviconapp-iconbien-the--render-png).

### Điểm mạnh cốt lõi của item CHO domain này
- Master vector + audit số thay vì cảm tính: target ~99/100, size ladder 16px, one-colour/reversed/shelf test — logo sống được từ favicon tab đến biển hiệu. Xem [Usecase con 1](../../items/logo-design-skill/README.md#usecase-con-1-thiet-ke-logo-moi--checkpoint--kit).
- Kit media đầy đủ 0đ MIT: 6 biến thể SVG + web-icons + board 6 mockups đúng ngành + guidelines 1 trang, offline được bằng Python. Xem [Bản đồ phủ](../../items/logo-design-skill/README.md#ban-do-phu-usecase-quet-het-skillmd--8-scripts--15-references--2-templates-30102026--★-manh-nhat-dau).
- Checkpoint tiết kiệm: trình 1 ảnh greyscale + recommendation trung thực (kèm risk) rồi dừng — khách media đổi ý rẻ trước khi build kit. Xem [Cốt lõi bất biến](../../items/logo-design-skill/README.md#cot-loi-bat-bien).

### Phân công CHO domain này (1 dòng + link, không copy)
- Agent chính brief→research→build→audit→trình checkpoint cho chủ kênh/khách media pick (qua question tool) rồi mới build kit/assets; bước tra cứu trademark ngoài + mở board/preview trên browser giao claude; verify bằng audit + 16px + file kit. Chi tiết: [Phân công gốc](../../items/logo-design-skill/README.md#phan-cong-ai-lam-gi).

### Link về item gốc (3 chiều)
- Gốc: `../../items/logo-design-skill/README.md` (Usecase 1/2/3/4 / Cài đặt / Định vị / Hồ sơ quyết định / Tham khảo sử dụng).
- Index domain: `./README.md`.
- Ngược tại: `../../items/logo-design-skill/README.md#duoc-dung-o-dau`.

---

## English

Media use of logo-design-skill — SVG logo/identity + favicons + boards. Origin at `../../items/logo-design-skill/README.md`.

### Usecases in this domain
- ★ New logo/brand mark (media brief: channel/product name + audience + adjectives) → SVG kit + industry-correct mockup board: see [Sub-usecase 1](../../items/logo-design-skill/README.md#sub-usecase-1-new-logo-design--checkpoint--kit).
- Refresh/critique an existing media-channel logo (keep equity): see [Sub-usecase 2](../../items/logo-design-skill/README.md#sub-usecase-2-critique--redesign-an-existing-logo).
- Favicon/app-icon/social-square + one-colour versions from the approved master (site/channel/app): see [Sub-usecase 3](../../items/logo-design-skill/README.md#sub-usecase-3-faviconapp-iconvariants--png-render).
- Pitch board + 1-page guidelines for media clients: see [Sub-usecase 4](../../items/logo-design-skill/README.md#sub-usecase-4-presentation-board--guidelines--identity).

### Concrete commands (for this domain)
- Category research before drawing (word-for-word origin command): `python3 scripts/search_library.py --industry <closest> --summary` (e.g. `payments-fintech` → 37/1432, really ran). See [Install](../../items/logo-design-skill/README.md#install-cloned--scripts-test-ran-on-linux-30102026-marketplace-plugin-not-installed--no-claude-code-on-this-machine).
- Post-test checkpoint (media approves on this image): `python3 scripts/concept_sheet.py a-symbol.svg b-symbol.svg c-symbol.svg --lockups a-lockup.svg b-lockup.svg c-lockup.svg --names "Name A" "Name B" "Name C" --notes "One-line idea A" "…" "…" --recommend 1 --greyscale -o concepts.png`. See [Sub-usecase 1](../../items/logo-design-skill/README.md#sub-usecase-1-new-logo-design--checkpoint--kit).
- Site/channel assets: `python3 scripts/export_variants.py final-symbol.svg --title "Brand logo" --mono "#0F7C80" --icon-bg "#0F7C80" --web-icons --favicon-source final-symbol-small.svg`. See [Sub-usecase 3](../../items/logo-design-skill/README.md#sub-usecase-3-faviconapp-iconvariants--png-render).
- Industry-correct board (12 industries, e.g. café → cup/bag/signage; software → README/terminal): `python3 scripts/presentation_board.py --list-mockups` to settle the list, then run the board from a JSON spec. See [Sub-usecase 4](../../items/logo-design-skill/README.md#sub-usecase-4-presentation-board--guidelines--identity).

### Domain-specific notes
- Vs Skillry raster OG: media briefs needing a long-lived SVG master (1-colour stamp, engraving, embroidery, 16 px favicon) → logo-design-skill primary; fast taste-matched OG/social raster → Skillry primary (GPT Image). See [Positioning](../../items/logo-design-skill/README.md#differentiating-positioning-github-api-numbers-30102026).
- Media-library logos (app/tech) collide most → mandatory shelf test + reverse-image check before settling (TRADEMARKS.md: MIT excludes library SVGs). See [Pitfalls](../../items/logo-design-skill/README.md#pitfalls).
- Wordmark fonts for media must be license-verified for logo use; missing PNG backend must be declared, never claim tested output. See [Sub-usecase 3](../../items/logo-design-skill/README.md#sub-usecase-3-faviconapp-iconvariants--png-render).

### Core strengths FOR this domain
- Vector master + numeric audit over taste: ~99/100 target, 16 px ladder, one-colour/reversed/shelf tests — one logo from favicon tab to signage. See [Sub-usecase 1](../../items/logo-design-skill/README.md#sub-usecase-1-new-logo-design--checkpoint--kit).
- Full $0 MIT media kit: 6 SVG variants + web-icons + 6 industry-correct mockup board + 1-page guidelines, offline via Python. See [Coverage map](../../items/logo-design-skill/README.md#coverage-map-full-skillmd--8-scripts--15-references--2-templates-scanned-30102026--★-strongest-first).
- Cost-saving checkpoint: one greyscale image + honest recommendation (with risks), then stop — media clients change minds cheaply pre-kit. See [Invariant core](../../items/logo-design-skill/README.md#invariant-core).

### Work split FOR this domain (1 line + link, never copied)
- Main agent briefs→researches→builds→audits→presents the checkpoint for the channel owner/media client to pick (via question tool) before any kit/asset build; outside trademark lookup + browser board/preview viewing go to claude; verify via audit + 16 px + kit files. Details: [origin Work split](../../items/logo-design-skill/README.md#work-split).

### Links to origin (3-way)
- Origin: `../../items/logo-design-skill/README.md` (Sub-usecases 1/2/3/4 / Install / Positioning / Decision dossier / Usage references).
- Domain index: `./README.md`.
- Backlisted at: `../../items/logo-design-skill/README.md#where-used`.
