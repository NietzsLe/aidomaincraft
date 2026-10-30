# using-awesome-opus5-5-videos CHO media (CHARTER v7)

> Prompt video Opus 5.5 miễn phí KHI DÙNG CHO media. Gốc ở `../../items/awesome-opus5-5-videos/README.md`. Skill đóng gói xem `using-skillry.md`.

## Tiếng Việt

### Usecase trong domain này
- ★ Motion graphics copy là chạy (369/703, remake 229): xem [Usecase 1](../../items/awesome-opus5-5-videos/README.md#usecase-con-1-motion-graphics--manh-nhat).
- Explainer có timing (116/703): xem [Usecase 2](../../items/awesome-opus5-5-videos/README.md#usecase-con-2-explainer).
- 3D Three.js/GLSL cần GPU (117/703): xem [Usecase 3](../../items/awesome-opus5-5-videos/README.md#usecase-con-3-3d-scenes).
- Game/interactive playable (101/703): xem [Usecase 4](../../items/awesome-opus5-5-videos/README.md#usecase-con-4-game--interactive).

### Lệnh mẫu cụ thể (cho media)
- Lọc trước, chọn sau (cấm lấy ví dụ làm mặc định): lọc `data/videos.json` theo category/tech_tags khớp nhu cầu task (motion/explainer/3D/game) → mở 2-3 `prompts/<slug>.md` ứng viên → trình shortlist kèm lý do qua question tool, chờ user pick 1 (cấm tự chốt rồi delegate) → copy nguyên văn prompt đã duyệt. Ví dụ minh họa (không phải mặc định): `prompts/ror-fly-880547.md` (explainer 30s, timing lời thoại) hoặc 1 prompt motion có `has_remake=true`. Clone: `git clone --depth 1 https://github.com/yihui-dev/awesome-opus5-5-videos && cd awesome-opus5-5-videos`, paste prompt vào agent Opus 5.5.
- Đối chiếu gốc/remake: X `post_url` + `https://skillry.dev/ai-videos/opus-5-5/<slug>` (418/703 có remake). Xem [Các bước chung](../../items/awesome-opus5-5-videos/README.md#cac-buoc-chung).

### Lưu ý riêng cho media
- 0đ/MIT nhưng render lại cần Opus 5.5 access; prompt dài 15K chứa key nội bộ (bỏ key, giữ visual/timing). `has_remake=false` (285/703) thì kỳ vọng thấp hơn.
- Đừng nhầm highlight README (58/16/14/12) với tổng catalog (369/117/116/101). Xem [Pitfalls](../../items/awesome-opus5-5-videos/README.md#pitfalls).

### Điểm mạnh cốt lõi CHO media
- Prompt viral thật + gốc/remake side-by-side để học, 0đ — chọn thay vì Skillry đóng gói khi cần học/thử nhanh. Xem [Định vị](../../items/awesome-opus5-5-videos/README.md#dinh-vi-khac-biet).

### Phân công CHO media này
- Agent chính clone + lọc + trình shortlist prompt (user pick 1 mới được delegate); toàn bộ render (viết animation, test browser) giao nguyên cục cho claude; agent verify output, cấm tự viết code animation. Chi tiết: [Phân công gốc](../../items/awesome-opus5-5-videos/README.md#phan-cong-ai-lam-gi).

### Link về item gốc (3 chiều)
- Gốc: `../../items/awesome-opus5-5-videos/README.md` (Usecase 1-4 / Cài đặt / Định vị / Hồ sơ quyết định / Tham khảo sử dụng).
- Index domain: `./README.md`.
- Đóng gói song sinh: `using-skillry.md` (video đóng gói).
- Ngược tại: `../../items/awesome-opus5-5-videos/README.md#duoc-dung-o-dau`.

---

## English

Free Opus 5.5 video prompts FOR media. Origin at `../../items/awesome-opus5-5-videos/README.md`. Packaged skills at `using-skillry.md`.

### Usecases in this domain
- ★ Copy-runnable motion (369/703, 229 remakes), explainer with timing (116), GPU 3D (117), playable game (101): see origin Sub-usecases 1-4.

### Concrete commands (for media)
- Filter first, pick second (never default to the example): filter `data/videos.json` by category/tech_tags matching the task (motion/explainer/3D/game) → open 2-3 candidate `prompts/<slug>.md` → present the shortlist with reasons via the question tool, wait for the user to pick one (never self-pick then delegate) → copy the approved prompt verbatim. Illustrative examples (not defaults): `prompts/ror-fly-880547.md` (30s explainer, voice timing) or one motion prompt with `has_remake=true`. Clone: `git clone --depth 1 https://github.com/yihui-dev/awesome-opus5-5-videos && cd awesome-opus5-5-videos`, paste into an Opus 5.5 agent.

### Domain-specific notes
- Free/MIT but re-render needs Opus 5.5; 15K prompts contain others' keys — drop keys. `has_remake=false` (285/703) means lower expectations.

### Core strengths FOR media
- Real viral prompts + original/remake side-by-side for learning, 0 cost — over packaged Skillry when fast study/try decides.

### Work split FOR this media
- Main agent clones + filters + presents a prompt shortlist (delegate only after the user picks one); the whole render (animation code, browser test) goes to claude; the agent verifies output and never writes animation code itself. Details: [origin Work split](../../items/awesome-opus5-5-videos/README.md#work-split).

### Links to origin (3-way)
- Origin: `../../items/awesome-opus5-5-videos/README.md`. Index: `./README.md`. Twin: `using-skillry.md`. Backlisted at origin `#where-used`.
