# using-web-interface-guidelines CHO UI (CHARTER v9)

> Phần RIÊNG khi dùng web-interface-guidelines cho UI. Gốc sống ở `../../items/web-interface-guidelines/README.md`; mọi lệnh/ngưỡng dưới đây khớp từng chữ với gốc. Không copy lại toàn bộ cài đặt/cơ chế.

## Tiếng Việt

### Usecase trong domain này
- ★ Review UI code có sẵn ra `file:line` trước merge: xem [Usecase con 1](../../items/web-interface-guidelines/README.md#usecase-con-1-review-ui-code-co-san--manh-nhat).
- Generate UI mới theo `AGENTS.md` (kẹp vào root project): xem [Usecase con 2](../../items/web-interface-guidelines/README.md#usecase-con-2-generate-ui-moi-theo-agentsmd).
- Audit interactions/animation/touch (keyboard, focus, reduced-motion): xem [Usecase con 3](../../items/web-interface-guidelines/README.md#usecase-con-3-audit-interactionsanimation-touch).
- Audit performance/typography/images/locale (virtualize >50, CLS, `Intl.*`): xem [Usecase con 4](../../items/web-interface-guidelines/README.md#usecase-con-4-audit-performancetypographyimageslocale).

### Lệnh mẫu cụ thể (cho UI)
- Review 1 file: `npx skills add vercel-labs/agent-skills --skill web-design-guidelines` rồi prompt `Review my UI: src/components/CheckoutForm.tsx` — chi tiết [Usecase con 1](../../items/web-interface-guidelines/README.md#usecase-con-1-review-ui-code-co-san--manh-nhat). Chú ý tên skill là `web-design-guidelines` (repo là `web-interface-guidelines`).
- Command đa agent: `curl -fsSL https://vercel.com/design/guidelines/install | bash` rồi `/web-interface-guidelines src/components/Modal.tsx` — xem [Cài đặt](../../items/web-interface-guidelines/README.md#cai-dat).
- Generate mới: `curl -sL https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/AGENTS.md -o AGENTS.md` — xem [Usecase con 2](../../items/web-interface-guidelines/README.md#usecase-con-2-generate-ui-moi-theo-agentsmd).

### Lưu ý riêng cho UI
- Findings guidelines tìm ra mà thuộc về system (thiếu tokens, shape lặp, hero sai fold) thì sửa bằng Hallmark thay vì vá lẻ — xem [Định vị](../../items/web-interface-guidelines/README.md#dinh-vi-khac-biet-so-lieu-ngay-03112026-tru-khi-ghi-khac).
- Visual (focus bị sticky che, contrast thực, motion flicker) static không kết luận được — giao claude mở browser thật, cấm agent tự claim đạt. Nguồn: [Phân công](../../items/web-interface-guidelines/README.md#phan-cong-ai-lam-gi).
- Review cả repo 1 phát loãng findings + tràn context — shortlist files/pattern + pillar, user pick trước. Nguồn: [Phần tùy chỉnh](../../items/web-interface-guidelines/README.md#phan-tuy-chinh).
- Chặn mạng `raw.githubusercontent.com` = không review (skill fetch tươi mỗi lần) — khai báo + dừng. Nguồn: [Pitfalls](../../items/web-interface-guidelines/README.md#pitfalls).

### Điểm mạnh cốt lõi CHO UI
- Checklist audit nhanh rẻ cho code UI đã có: 104 checks `command.md` ra `file:line` + `✓ pass`, 0đ MIT, ~815k installs — quyết định chọn thay vì Hallmark khi chỉ cần 1 pass soi <10 phút, không đổi system. Xem [Định vị](../../items/web-interface-guidelines/README.md#dinh-vi-khac-biet-so-lieu-ngay-03112026-tru-khi-ghi-khac).
- 73 MUST `AGENTS.md` kẹp vào project để agent sinh UI mới đã đúng rules (labels, focus-visible, autocomplete, `transform/opacity`, images dimensions, `Intl.*`).

### Phân công CHO UI này
- Agent chính shortlist files/pattern (user pick) → fetch rules tươi → check → trình findings `file:line` → re-check hết MUST; bước visual giao nguyên cục cho claude (mở browser verify focus/contrast/motion). Chi tiết: [Phân công gốc](../../items/web-interface-guidelines/README.md#phan-cong-ai-lam-gi).

### Link về item gốc (3 chiều)
- Gốc: `../../items/web-interface-guidelines/README.md` (Cài đặt / Cách hoạt động / Định vị / Bản đồ phủ / Usecase 1-4 / Pitfalls / Tham khảo sử dụng).
- Index domain: `./README.md` (hàng web-interface-guidelines ở điều hướng + định vị + chồng lấn).
- Được liệt kê ngược tại: `../../items/web-interface-guidelines/README.md#duoc-dung-o-dau`.

---

## English

UI-only deltas for web-interface-guidelines. Origin lives at `../../items/web-interface-guidelines/README.md`; commands/bars below match it word-for-word.

### Usecases in this domain
- ★ Review existing UI code into `file:line` pre-merge: see [Sub-usecase 1](../../items/web-interface-guidelines/README.md#sub-usecase-1-review-existing-ui-code--strongest).
- Generate new UI from `AGENTS.md`: see [Sub-usecase 2](../../items/web-interface-guidelines/README.md#sub-usecase-2-generate-new-ui-from-agentsmd).
- Interaction/animation/touch audits: see [Sub-usecase 3](../../items/web-interface-guidelines/README.md#sub-usecase-3-interactionanimationtouch-audit).
- Performance/typography/images/locale audits: see [Sub-usecase 4](../../items/web-interface-guidelines/README.md#sub-usecase-4-performancetypographyimageslocale-audit).

### Concrete commands (for UI)
- Review one file: `npx skills add vercel-labs/agent-skills --skill web-design-guidelines` then `Review my UI: src/components/CheckoutForm.tsx`.
- Multi-agent command: `curl -fsSL https://vercel.com/design/guidelines/install | bash` then `/web-interface-guidelines src/components/Modal.tsx`.
- Generate new: `curl -sL https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/AGENTS.md -o AGENTS.md`.

### Domain-specific notes
- System-level findings (missing tokens, repeated shapes, wrong-fold hero) get fixed with Hallmark, not patched ad hoc. Visual verdicts need claude with a real browser. Shortlist files + pillar before reviewing; blocked fetch = declare + stop.

### Core strengths FOR UI
- Fast cheap audits of existing UI code: 104-check `command.md` → `file:line` + `✓ pass`, $0 MIT, ~815k installs — pick over Hallmark for a <10-minute single pass with the system untouched.
- 73-MUST `AGENTS.md` pinning so newly generated UI already complies.

### Work split FOR this UI
- Main agent shortlists (user picks) → fetches fresh rules → checks → presents `file:line` → re-checks MUSTs clear; visual steps go to claude as a whole. Details: [origin Work split](../../items/web-interface-guidelines/README.md#work-split).

### Links to origin (3-way)
- Origin: `../../items/web-interface-guidelines/README.md`. Index: `./README.md`. Backlisted at origin `#where-used`.
