# using-hallmark CHO UI (CHARTER v7)

> Phần RIÊNG khi dùng Hallmark cho UI. Gốc sống ở `../../items/hallmark/README.md`; mọi lệnh/ngưỡng dưới đây khớp từng chữ với gốc. Không copy lại toàn bộ cài đặt/cơ chế.

## Tiếng Việt

### Usecase trong domain này
- ★ Build trang mới / redesign / audit có system + gates: xem [Bảng usecase](../../items/hallmark/README.md#bang-usecase-con-lenh-dung) (build mới, component 8 states, app-screen, redesign full/restyle/polish, audit, custom, fast, khóa system, xuất tokens, lint).
- Component lẻ 8 states, app-screen density + 4 states data: cùng link trên, scope `component` / `app`.

### Lệnh mẫu cụ thể (cho UI)
- Build mới: `/hallmark <prompt>` — chi tiết [Prompt mẫu](../../items/hallmark/README.md#prompt-mau-copy-paste), vd điền sẵn quán cà phê A trong gốc.
- Component: `/hallmark` + nêu đúng 1 element + `sweep sloplint --scope component` — xem [Cài đặt](../../items/hallmark/README.md#cai-dat-opencode).
- Redesign/audit: `/hallmark redesign <path>` / `/hallmark audit <path>` — giữ content + wiring (`--kept`, `compare.html`), audit không sửa file.

### Lưu ý riêng cho UI
- Luôn có dev server/URL để `capture.mjs` chụp thật thay vì mock; không render tier (`puppeteer-core` + Chrome) thì `sloplint` chỉ chạy tĩnh — ghi rõ trong handoff. Nguồn: [Cài đặt](../../items/hallmark/README.md#cai-dat-opencode).
- Đừng lắp 3-4 effect React Bits cùng lúc — vỡ gates 8/9/11. Lắp 1-2 rồi sweep lại (`sloplint --render`) + review lạnh. Xem [Pitfalls](../../items/hallmark/README.md#pitfalls-loi-hallmark-bat-nhieu-nhat) (waiver sai, vượt word budget, hero sai fold).
- Output Skillry-web lấy về muốn đạt chuẩn UI thì sweep lại bằng Hallmark.

### Điểm mạnh cốt lõi CHO UI
- Gates máy quét được (contrast 4.5:1, focus-visible 3:1, fold 1280x800, word budget ~80/900px) — quyết định chọn Hallmark thay vì generator nhanh khi gates quyết định. Xem [Định vị](../../items/hallmark/README.md#dinh-vi-khac-biet).
- 10 job anatomy + hero-first + review fresh-context: page khác brief ra shape khác nhau, không phải đổi màu template. Được review sâu `andrew.ooo 18/07/2026` xác nhận: *"Two Hallmark pages for different briefs should have different section rhythms"* — xem [Tham khảo sử dụng](../../items/hallmark/README.md#tham-khao-su-dung).

### Link về item gốc (3 chiều)
- Gốc: `../../items/hallmark/README.md` (Cài đặt / Cách hoạt động / Định vị / Bảng usecase / Prompt mẫu / Pitfalls / Tham khảo sử dụng).
- Index domain: `./README.md` (hàng Hallmark ở điều hướng + định vị + chồng lấn).
- Được liệt kê ngược tại: `../../items/hallmark/README.md#duoc-dung-o-dau`.

---

## English

UI-only deltas for Hallmark. Origin lives at `../../items/hallmark/README.md`; commands/bars below match it word-for-word.

### Usecases in this domain
- ★ New page / redesign / audit with system + gates: see [usecase table](../../items/hallmark/README.md#sub-usecase--command-table).

### Concrete commands (for UI)
- New page: `/hallmark <prompt>`; component: `/hallmark` + one element + `--scope component` sweep; redesign/audit: `/hallmark redesign|audit <path>`.

### Domain-specific notes
- Need a real dev server/URL for `capture.mjs`; no render tier → static-only `sloplint`, say so in handoff. Never stack 3-4 React Bits effects — re-sweep after 1-2.

### Core strengths FOR UI
- Machine gates (4.5:1, 3:1, 1280x800 fold, ~80-word/900px budget) + 10-job anatomy + hero-first + cold review.

### Links to origin (3-way)
- Origin: `../../items/hallmark/README.md`. Index: `./README.md`. Backlisted at origin `#where-used`.
