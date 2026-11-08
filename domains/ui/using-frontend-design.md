# using-frontend-design CHO UI (CHARTER v12)

> Phần RIÊNG khi dùng frontend-design cho UI. Gốc sống ở `../../items/frontend-design/README.md`; mọi lệnh/ngưỡng dưới đây khớp từng chữ với gốc. Không copy lại toàn bộ cài đặt/cơ chế.

## Tiếng Việt

### Usecase trong domain này
- ★ Build mới có direction trong 1 session ngắn: xem [Usecase con 1](../../items/frontend-design/README.md#usecase-con-1-build-moi-co-direction--manh-nhat).
- Reshape thoát AI-slop theo tells: xem [Usecase con 2](../../items/frontend-design/README.md#usecase-con-2-reshape-thoat-ai-slop-theo-tells).
- Typography + copy lúc design: xem [Usecase con 3](../../items/frontend-design/README.md#usecase-con-3-typography--copy-trong-luc-design).
- Self-critique + quality floor trước ship: xem [Usecase con 4](../../items/frontend-design/README.md#usecase-con-4-self-critique--quality-floor).

### Lệnh mẫu cụ thể (cho UI)
- Cài 1 lần: `npx skills add https://github.com/anthropics/skills --skill frontend-design` — xem [Cài đặt](../../items/frontend-design/README.md#cai-dat).
- Build mới: prompt agent `Dùng frontend-design build landing cho <brief>: xác nhận subject/audience/job trước, plan tokens rồi mirror test, brief thắng mọi default.` — xem [Usecase con 1](../../items/frontend-design/README.md#usecase-con-1-build-moi-co-direction--manh-nhat).
- Reshape: `Dùng frontend-design reshape <target>: soi 6 calibration clusters + typo tells + template chrome, liệt kê tells đã fix.` — xem [Usecase con 2](../../items/frontend-design/README.md#usecase-con-2-reshape-thoat-ai-slop-theo-tells).
- Type/copy + critique: xem [Usecase con 3](../../items/frontend-design/README.md#usecase-con-3-typography--copy-trong-luc-design) và [Usecase con 4](../../items/frontend-design/README.md#usecase-con-4-self-critique--quality-floor).

### Lưu ý riêng cho UI
- Findings mà cần gates số (contrast/focus/fold/word budget) thì sang Hallmark; cần detector/Live thì sang impeccable — skill này chỉ khuyên, không enforce. Nguồn: [Định vị](../../items/frontend-design/README.md#dinh-vi-khac-biet-so-lieu-ngay-08112026).
- Không chạy cùng skill design khác (hallmark/impeccable) trên 1 project UI — agent flip-flop rules; chọn 1, disable bên còn lại ở local scope. Nguồn: [Phần tùy chỉnh](../../items/frontend-design/README.md#phan-tuy-chinh).
- License đọc ở `LICENSE.txt` trong folder skill (API repo trả None) — quote sai license là FAIL core-fidelity. Nguồn: [Hồ sơ quyết định](../../items/frontend-design/README.md#ho-so-quyet-dinh).

### Điểm mạnh cốt lõi CHO UI
- Taste nhanh gọn nhất cho UI mới/reshape: 1 file 0 deps, offline sau cài, 1 session ngắn, tells cụ thể tới mã màu — quyết định chọn thay vì hallmark/impeccable khi không cần gates/detector. Xem [Định vị](../../items/frontend-design/README.md#dinh-vi-khac-biet-so-lieu-ngay-08112026).
- 2-pass plan → mirror test + brief thắng: chống rơi vào default có phương pháp, không phải taste cảm tính.

### Phân công CHO UI này
- Agent chính xác nhận subject/audience/job (user confirm) → plan tokens → mirror test → build/sửa → self-critique + screenshot; bước visual giao nguyên cục cho claude (mở browser verify focus/motion/màn hẹp). Chi tiết: [Phân công gốc](../../items/frontend-design/README.md#phan-cong-ai-lam-gi).

### Link về item gốc (3 chiều)
- Gốc: `../../items/frontend-design/README.md` (Cài đặt / Cách hoạt động / Định vị / Bản đồ phủ / Hồ sơ quyết định / Usecase 1-4 / Pitfalls / Tham khảo sử dụng).
- Index domain: `./README.md` (hàng frontend-design ở điều hướng + định vị + chồng lấn).
- Được liệt kê ngược tại: `../../items/frontend-design/README.md#duoc-dung-o-dau`.

---

## English

UI-only deltas for frontend-design. Origin lives at `../../items/frontend-design/README.md`; commands/bars below match it word-for-word.

### Usecases in this domain
- ★ New builds with direction in one short session: see [Sub-usecase 1](../../items/frontend-design/README.md#sub-usecase-1-new-build-with-direction--strongest).
- Reshaping out of AI-slop via tells: see [Sub-usecase 2](../../items/frontend-design/README.md#sub-usecase-2-reshape-out-of-ai-slop-via-tells).
- Typography + copy while designing: see [Sub-usecase 3](../../items/frontend-design/README.md#sub-usecase-3-typography--copy-while-designing).
- Self-critique + quality floor before ship: see [Sub-usecase 4](../../items/frontend-design/README.md#sub-usecase-4-self-critique--quality-floor).

### Concrete commands (for UI)
- Install once: `npx skills add https://github.com/anthropics/skills --skill frontend-design`.
- New build: prompt the agent to confirm subject/audience/job first, token-plan then mirror-test, brief beats all defaults.
- Reshape: name the 6 calibration clusters + typo tells + template chrome, list fixed tells.
- Type/copy + critique: see origin Sub-usecases 3 and 4.

### Domain-specific notes
- Numbered-gate findings go to Hallmark; detector/Live needs go to impeccable — this skill advises, never enforces. Never run two design skills in one UI project; read the license from the skill folder's `LICENSE.txt` (repo API returns None).

### Core strengths FOR UI
- Leanest fast taste for new/reshape UI: one zero-dependency file, offline after install, one short session, tells down to hex codes — pick over hallmark/impeccable when no gates/detector are needed.
- 2-pass plan → mirror test with brief-wins: a method against defaults, not vibes.

### Work split FOR this UI
- Main agent confirms subject/audience/job (user confirms) → token-plans → mirror-tests → builds/fixes → self-critiques + screenshots; visual steps go to claude as a whole. Details: [origin Work split](../../items/frontend-design/README.md#work-split).

### Links to origin (3-way)
- Origin: `../../items/frontend-design/README.md`. Index: `./README.md`. Backlisted at origin `#where-used`.
