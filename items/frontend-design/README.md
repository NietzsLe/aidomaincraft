# frontend-design

## Tiếng Việt

### Dùng khi
- Build page mới cần taste khác biệt trong 1 session ngắn: persona design-lead + ground theo subject-matter + chốt aesthetic direction (brutalist/maximalist/...) trước khi viết code.
- Reshape UI có sẵn thoát mùi AI-slop theo tells liệt kê sẵn: 6 calibration clusters (6 cụm mặc định AI hay rơi vào, liệt kê trong SKILL.md: cream `#F4F1EA` + terracotta `#D97757`, acid-green/vermilion nền đen, broadsheet, SaaS-card kit, template chrome lặp mọi brief) + typographic tells + motion mặc định.
- Cần typography/copy guidance ngay trong lúc design: type scale theo Elements of Typographic Style, line <80 ký tự, writing rules (active voice, sentence case, CTA nêu đúng việc xảy ra, error/empty có hướng dẫn).
- Cần skill 0 deps, offline được sau khi cài, cài 1 dòng, agent nào đọc được skill cũng dùng.

### Bỏ qua khi
- Cần system/design mới pass gates máy cứng (contrast 4.5:1, fold 1280x800, word budget) + sweep render → dùng `../hallmark/` (skill này chỉ khuyên, không enforce).
- Cần detector máy/hook/CI/Live compare trực quan → dùng `../impeccable/` (fork từ chính skill này, thêm 24 lệnh + detector + Live).
- Cần 1 pass checklist `file:line` dưới 10 phút, không đổi file → dùng `../web-interface-guidelines/`.
- Cần bricks React animated sở hữu source → dùng `../reactbits/`.
- Chưa cài + đang offline (cài cần mạng 1 lần) → không lấy được skill.

### Cài đặt
- Cài: `npx skills add https://github.com/anthropics/skills --skill frontend-design` (nguồn trang skills.sh Installation, đã đọc 08/11/2026).
- Yêu cầu: Node cho `npx`; agent đọc được skill (Claude Code/Cursor/OpenCode...).
- Kiểm tra (đã chạy 08/11/2026): fetch full `SKILL.md` + `LICENSE.txt` (Apache-2.0) + GitHub API repo mẹ (189.158★/22.296 forks/1.495 issues mở/push 06/11/2026/tạo 22/09/2025) + trang skills.sh (1.1M installs, First Seen Jan 19 2026, 3 audits pass: Trust Hub/Socket/Snyk). Chưa chạy: `npx skills add` thật + dùng trên project thật (ghi WARN).

### Cách item hoạt động
- Tổ chức đứng sau: Anthropic, repo `https://github.com/anthropics/skills` (189.158★/22.296 forks API 08/11/2026), skill `skills/frontend-design/SKILL.md` + `LICENSE.txt` Apache-2.0, nhịp update theo main (push 06/11/2026; 437 issues + 1,1k PRs mở — nhiễu khi contribute).
- Phương thức hoạt động chung: 1 file lời khuyên, không code/scripts/detector — persona design-lead + ground subject-matter + principles (hero-first, typography, tells) + 2-pass plan/review/build + self-critique + writing rules. Chạy bằng kỷ luật tự giác của model, không có gate máy nào bắt tuân thủ.
- Khác biệt vận hành theo usecase: build mới chạy đủ plan tokens → mirror test (tự soi: prompt tương tự có ra giống không) vs brief → build (xem [Usecase con 1](#usecase-con-1-build-moi-co-direction--manh-nhat)) khác reshape soi tells có sẵn (xem [Usecase con 2](#usecase-con-2-reshape-thoat-ai-slop-theo-tells)) khác typography/copy (scale + writing rules lúc viết, xem [Usecase con 3](#usecase-con-3-typography--copy-trong-luc-design)) khác self-critique chốt floor (screenshot + responsive/focus/motion/a11y, xem [Usecase con 4](#usecase-con-4-self-critique--quality-floor)).

### Cốt lõi bất biến
- Mọi việc qua 2-pass: plan tokens (palette 4-6 hex + typefaces/roles + layout ASCII + principles) → mirror test (prompt tương tự có ra giống không — giống thì sửa + ghi lý do) → mới build. Build thẳng không plan = không còn gọi là dùng hệ.
- Brief thắng mọi default: brief chốt direction nào thì làm đúng direction đó, kể cả khi brief đòi đúng 1 trong 6 clusters (nguyên văn SKILL.md).
- Boldness dồn 1 chỗ + quality floor không cần công bố (responsive tới mobile, keyboard focus thấy được, tôn trọng reduced-motion, visually accessible) + screenshot review khi môi trường cho phép.
- Sau khi dùng phải nêu được: subject/audience/job + direction đã chọn + mirror test đã qua (đổi gì, vì sao); không nêu được = chưa thực sự dùng hệ.

### Phần tùy chỉnh
- Được đổi: subject/audience/job (brief thiếu thì tự đề xuất 1 bộ cụ thể + confirm), aesthetic direction, palette 4-6 hex, typefaces (cấm default families), layout concept, 1 orchestrated motion moment. Cổng duyệt 2 tầng: (1) direction nào — shortlist aesthetic kèm lý do qua question tool, user pick mới build; (2) giữ/đổi gì — mirror test đổi phần nào, brief chốt phần nào. Waiver (làm đúng default cluster vì brief đòi) phải quote câu brief/user. Cấm đưa `must-not` (build không plan, typeface default, motion rải rác) vào danh sách tùy chỉnh.
- Không chạy cùng skill design khác trên 1 project (rules xung đột, agent theo bên này rồi bên kia — theo luật 1 skill/project của impeccable, nguồn ssdnodes 31/10/2026); chọn 1 rồi disable bên còn lại ở local scope.

### Phân công ai làm gì
- Agent chính: hỏi/xác nhận subject-audience-job, plan tokens, mirror test + ghi thay đổi, build theo plan, self-critique + screenshot.
- Giao cho claude các bước cần browser/người thật: verify visual (screenshot review, focus có bị che không, motion, màn hẹp, keyboard) — kèm URL + checklist tells cần soi + output mong đợi; cấm agent tự kết luận render đạt khi không có browser.
- Agent verify: plan tokens khớp brief + mirror test đã answered + screenshot đã xem + floor checklist hết.

### Định vị khác biệt (số liệu ngày 08/11/2026)
- So với `../impeccable/` (105.856★, fork từ chính skill này — README nó ghi "started from Anthropic's frontend-design"): khác tầng đảm bảo — skill cho taste 1 file 0 gates; impeccable thêm 24 lệnh + detector không-LLM + Live + hook/CI. Chọn skill thay vì impeccable khi cần nhanh-gọn 1 session ngắn, offline sau cài, không trả giá context hook; chọn impeccable khi cần detector/exit code/Live compare. 2 hệ không chạy cùng project — chọn 1.
- So với `../hallmark/` (50.558★, system + gates máy + sweep render): khác enforce — hallmark SINH system có gates đo được + sweep tới sạch; skill KHUYÊN taste, model có thể bỏ qua. Chọn skill thay vì hallmark khi không cần gates merge, cần nhanh; chọn hallmark khi output phải pass gates (contrast/fold/word budget).
- Khung trung thực: thắng ở chính chủ Anthropic + 1 file 0 deps + offline + 1.1M installs + 3 audits pass + tells liệt kê cụ thể tới mã màu; thua ở enforce (không gate/detector), không pin version (lệnh lấy main mới nhất), không audit sâu/rank, không bricks.

### Bản đồ phủ usecase (quét HẾT SKILL.md 08/11/2026 — ★ mạnh nhất đầu)
- ★ Build mới có direction (plan tokens + mirror test + brief thắng): xem Usecase 1.
- Reshape thoát AI-slop theo tells (6 clusters + typo tells + template chrome + motion mặc định): xem Usecase 2.
- Trung bình: typography scale + copy/writing rules lúc viết (1-2 typeface, line <80, sentence case, CTA đúng việc, error/empty có hướng): xem Usecase 3.
- Trung bình: self-critique + quality floor (screenshot review + responsive/focus/reduced-motion/a11y + cắt 1 accessory): xem Usecase 4.
- KHÔNG hỗ trợ → thay thế: gates số merge → `../hallmark/`; detector/hook/CI/Live → `../impeccable/`; checklist `file:line` nhanh → `../web-interface-guidelines/`; bricks React → `../reactbits/`; review xếp hạng P0-P3 → `../impeccable/` (audit); so sánh gồm proprietary → AlternativeTo.net.

### Hồ sơ quyết định
- Việc DÙNG (4, cụ thể): 1. build page mới có direction khác biệt trong 1 session; 2. reshape UI theo tells liệt kê sẵn; 3. typography + copy guidance lúc design; 4. skill 0-deps offline cho mọi agent.
- Việc KHÔNG DÙNG (5, mỗi việc kèm hệ thay thế): 1. cần gates merge → dùng `../hallmark/`; 2. cần detector/hook/CI/Live → dùng `../impeccable/`; 3. cần `file:line` dưới 10 phút → dùng `../web-interface-guidelines/`; 4. cần bricks React → dùng `../reactbits/`; 5. cần review xếp hạng → dùng `../impeccable/` (audit).
- Free / tổng + giá: 0đ toàn bộ, Apache-2.0 (nguồn `LICENSE.txt` trong folder skill, 08/11/2026 — API repo trả `license: None`, phải đọc file). Tổng sở hữu = 0đ + tiền model.
- Ma sát cài đặt: 1 bước tới lệnh đầu (`npx skills add ...` rồi gọi skill), bằng chuẩn 1 dòng. ĐÃ chạy 08/11/2026: fetch SKILL.md + LICENSE.txt + API + skills.sh. Chưa chạy: install + dùng thật (ghi WARN). Rào cản: Node; không pin version (trôi theo main); không hook (tự kỷ luật).
- Đối thủ viral cùng phân khúc: `../impeccable/` (105.856★, con cháu trực tiếp + detector/Live) vs `../hallmark/` (50.558★, system + gates).
- Chọn nó thay vì đối thủ khi: cần taste nhanh 1 session ngắn, offline sau cài, không cần gates/detector. Ví dụ đổi lựa chọn: landing mới 1 buổi cần direction lạ → skill; output pass gates merge → Hallmark; cần Live compare + CI → impeccable.
- TUYỆT ĐỐI không dùng khi: cần enforce bằng máy (skill là lời khuyên, model bỏ qua được); cần findings `file:line`; chạy cạnh skill design khác cùng project.

### Usecase con 1: build mới có direction (★ mạnh nhất)
- Khi dùng: có brief (hoặc brief mỏng cần tự đề xuất subject/audience/job), cần page khác biệt trong thời gian ngắn.
- Khi bỏ qua: đã có UI (sang Usecase 2); cần gates (sang `../hallmark/`); chỉ cần plan dừng trước build (tự chốt plan, không build).
- Cơ chế khác các usecase khác ở đâu: duy nhất chạy đủ plan tokens → mirror test → build; các usecase khác soi tells có sẵn, viết type/copy, hoặc critique chốt floor.
- Lệnh copy-paste: `npx skills add https://github.com/anthropics/skills --skill frontend-design` (cài 1 lần) rồi prompt agent `Dùng frontend-design build landing cho <brief>: xác nhận subject/audience/job trước, plan tokens rồi mirror test, brief thắng mọi default.`
- Ngưỡng số cần đạt: plan có palette 4-6 hex đặt tên + typefaces/roles + layout ASCII + principles; mirror test ghi rõ đổi gì + vì sao; brief chốt direction nào làm đúng direction đó.
- Ví dụ input-output (minh họa, không phải mặc định — direction do user pick trước): input brief "book club tháng, audience người đi làm bận" → output subject/audience/job đã confirm + plan tokens + page theo plan, không rơi vào cream/terracotta mặc định.
- Pitfalls riêng: build thẳng không plan (FAIL core); brief thiếu subject mà không hỏi (đoán mò = FAIL grounding); nhận direction đầu tiên mặc định (neo bias — bắt shortlist + pick).
- Phân công usecase này: agent chính hỏi subject/audience/job (user confirm) → plan → mirror test → build; giao claude verify visual sau build; verify bằng plan + mirror log.

### Usecase con 2: reshape thoát AI-slop theo tells
- Khi dùng: có UI/page trông "AI" mà chưa gọi tên được vấn đề.
- Khi bỏ qua: chưa có gì (sang Usecase 1); cần gates số (sang `../hallmark/`); chỉ cần list lỗi (sang `../web-interface-guidelines/`).
- Cơ chế khác các usecase khác ở đâu: duy nhất soi tells có sẵn (không sinh direction mới); các usecase khác plan mới, viết type/copy, hoặc chốt floor.
- Lệnh copy-paste: `Dùng frontend-design reshape <target>: soi 6 calibration clusters + typo tells + template chrome + motion mặc định, liệt kê tells đã fix.`
- Ngưỡng số cần đạt: liệt kê từng tell đã fix (vd bỏ gradient-text, bỏ eyebrow caps, numbered markers chỉ giữ khi content là sequence, motion còn 1 orchestrated moment) + screenshot before/after đã xem.
- Ví dụ input-output (minh họa): input pricing page (cream + serif italic + eyebrow caps + `A · B · C` + `→`) → output bỏ tells, giữ 1 điểm nhấn, type treatment là 1 phần design.
- Pitfalls riêng: áp 6 clusters máy móc (brief đòi đúng look đó thì làm — brief thắng); sửa tells mà mất 1 điểm nhấn (restraint: boldness 1 chỗ).
- Phân công usecase này: agent chính soi + sửa + trình before/after; giao claude verify màn hẹp/keyboard/motion thật; verify bằng list tells + screenshot.

### Usecase con 3: typography + copy trong lúc design
- Khi dùng: page đang viết cần type/copy đúng luật (scale, line, voice, error/empty).
- Khi bỏ qua: type/copy đã chốt (sang Usecase 4 review); cần checklist a11y/forms sâu (sang guidelines).
- Cơ chế khác các usecase khác ở đâu: duy nhất áp lúc VIẾT (scale + writing rules); các usecase khác plan/reshape/critique.
- Lệnh copy-paste: `Dùng frontend-design soát type + copy cho <target>: 1-2 typeface, line <80 ký tự, sentence case, CTA nêu đúng việc, error/empty có hướng dẫn.`
- Ngưỡng số cần đạt: type scale theo Elements of Typographic Style (weights/widths/spacing có chủ ý); line body <80 ký tự (serif dài hơn + line-height lớn hơn sans); 0 all-caps labels; 0 accent 1 từ lẻ trong headline; CTA = việc xảy ra (`Save changes`, toast `Published` khớp nút `Publish`).
- Ví dụ input-output (minh họa): input form checkout → output labels sentence case + 1-2 typeface phân vai rõ + error inline nêu cách fix + empty screen có lời mời hành động.
- Pitfalls riêng: 2 typeface na ná nhau (phải clearly distinct); monospace cho data labels mọi chỗ (tell #5 — chỉ khi hợp brief); copy bán hàng chung chung.
- Phân công usecase này: agent chính soát + sửa; claude chỉ khi cần check render type thật (line-height/overflow).

### Usecase con 4: self-critique + quality floor
- Khi dùng: page đã xong, cần chốt trước ship mà không có gates máy.
- Khi bỏ qua: cần gates đo được (sang `../hallmark/`); cần rank P0-P3 (sang `../impeccable/` audit).
- Cơ chế khác các usecase khác ở đâu: duy nhất KHÔNG sinh/sửa theo luật mới mà soi lại (screenshot + floor); các usecase khác plan/reshape/viết.
- Lệnh copy-paste: `Dùng frontend-design self-critique <target>: screenshot review, check responsive tới mobile + keyboard focus + reduced-motion + visual accessible + cắt 1 accessory.`
- Ngưỡng số cần đạt: floor hết (responsive mobile ok, focus thấy được, reduced-motion có variant, màu hài hòa accessible); screenshot đã xem (không claim bằng đọc code); ghi 1 thứ đã cắt theo quy tắc Chanel (soi gương bỏ bớt 1 phụ kiện trước khi ra khỏi nhà).
- Ví dụ input-output (minh họa): input landing đã build → output screenshot + list (focus ok, motion còn 2 moments → cắt 1, 1 decoration không phục vụ brief → cắt).
- Pitfalls riêng: critique bằng đọc code mà không screenshot (SKILL.md bắt picture > 1000 tokens); floor công bố với user (floor là chuẩn ngầm, không cần announce).
- Phân công usecase này: agent chính screenshot + checklist; giao claude chụp/compare khi cần browser thật; verify bằng screenshot + floor hết.

### Các bước chung
1. Cài 1 lần: `npx skills add https://github.com/anthropics/skills --skill frontend-design`.
2. Xác nhận subject/audience/job (brief thiếu thì tự đề xuất 1 bộ + confirm, cấm đoán mò).
3. Plan tokens: palette 4-6 hex + typefaces/roles + layout ASCII + principles.
4. Mirror test vs brief: giống default thì sửa + ghi lý do; brief thắng mọi default.
5. Build/reshape/viết theo plan (1 việc/pass, diff trong scope).
6. Self-critique: screenshot + floor + cắt 1 accessory.
7. Nêu subject/direction/mirror-test/floor (core-fidelity).

### Prompt mẫu
- "Dùng frontend-design build landing cho job `<...>` (audience ..., action chính ...). Xác nhận subject/audience/job trước, plan tokens rồi mirror test, brief thắng mọi default."
- "Dùng frontend-design reshape `<target>`: soi 6 calibration clusters + typo tells + template chrome, liệt kê tells đã fix, before/after screenshot."
- "Dùng frontend-design soát type + copy cho `<target>`: 1-2 typeface distinct, line <80, sentence case, CTA đúng việc, error/empty có hướng."
- Ví dụ điền sẵn: "Dùng frontend-design build landing signup book club tháng (audience người đi làm bận, action reserve seat, constraint chỉ ngày/số chỗ đã xác nhận). Plan tokens trước, mirror test ghi đổi gì, không rơi vào cream/terracotta mặc định."

### Pitfalls
- Build thẳng không plan tokens + mirror test (FAIL core — plan là bắt buộc).
- Brief thiếu subject mà đoán mò thay vì đề xuất + confirm (FAIL grounding).
- Brief đòi đúng default look mà cãi brief (brief thắng mọi default — nguyên văn SKILL.md).
- Nhận direction đầu tiên mặc định (neo bias — shortlist + user pick trước).
- Typeface default + 2 typeface na ná + all-caps labels + accent 1 từ lẻ (typo tells liệt kê sẵn).
- Motion rải rác (fade-slide-up mọi section) thay vì 1 orchestrated moment + motion theo action.
- CSS specificity tự triệt tiêu (`.section` vs `.cta` padding/margin — SKILL.md cảnh báo).
- Copy bán hàng chung chung + CTA không nêu việc xảy ra + error xin lỗi chung chung.
- Chạy cạnh skill design khác cùng project (xung đột rules — chọn 1, disable bên còn lại).
- Quote installs/stars cũ (trôi theo tuần — ghi ngày đo; license đọc `LICENSE.txt`, API trả None).

### Tham khảo sử dụng (quyết định được + số có trọng số, chốt 08/11/2026)
- Nhận xét sâu: [skills.sh page](https://www.skills.sh/anthropics/skills/frontend-design) (fetch 08/11/2026) — summary *"Distinctive, production-grade frontend interfaces that reject generic AI aesthetics"* + install 1 lệnh + 3 security audits pass (Trust Hub/Socket/Snyk) + First Seen Jan 19 2026 + related skills (web-design-guidelines, canvas-design...) → xác nhận quyết định: cài nhanh, an toàn cơ bản, họ hàng gần nhất là web-design-guidelines (checklist) chứ không phải generator.
- Nhận xét sâu (chính chủ): [SKILL.md raw](https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md) (fetch 08/11/2026, full text) + [LICENSE.txt](https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/LICENSE.txt) (Apache-2.0) — 1 file lời khuyên thuần (persona + grounding + principles + 2-pass + self-critique + writing), không code/detector/gates → xác nhận: advice-only, enforce = 0; license đọc file, API repo trả None.
- Nhận xét sâu (dòng dõi): [Impeccable README](https://github.com/pbakaus/impeccable) (fetch 08/11/2026) — *"Impeccable started from Anthropic's frontend-design skill"* → xác nhận vị trí tổ tiên: con cháu (105.856★) thêm detector/Live/hook, vượt sao cha; chọn cha khi cần gọn, chọn con khi cần máy.
- Số trung bình có trọng số: repo mẹ API 08/11/2026 — 189.158★/22.296 forks/1.495 issues mở/push 06/11/tạo 22/09/2025; skill 1.1M installs skills.sh (08/11/2026). Trọng số: installs (hành vi cài thật, triệu mẫu) đáng tin hơn stars repo (gộp cả repo skills, không riêng frontend-design).
- Tiếng Việt: truy vấn `frontend-design skill Anthropic đánh giá` không trả về review Việt độc lập → `chưa xác minh`.
- Mâu thuẫn: installs khủng + chính chủ + audits pass vs advice-only không enforce + repo mẹ 1,1k PRs/437 issues nhiễu → phán quyết: dùng định hướng nhanh khi không cần máy; việc cần enforce thì lên hallmark/impeccable.

### Tham khảo
- Repo: https://github.com/anthropics/skills (`skills/frontend-design/SKILL.md` + `LICENSE.txt`)
- Trang skills.sh: https://www.skills.sh/anthropics/skills/frontend-design (installs + audits + related)
- Đọc theo thứ tự: `SKILL.md` (persona → grounding → principles → tells → 2-pass → self-critique → writing) → `LICENSE.txt` → skills.sh (installs/audits).
- Đã verify 08/11/2026: fetch SKILL.md full + LICENSE.txt + API + skills.sh. Chưa chạy thật: install + dùng (WARN).

### Được dùng ở đâu
- Dùng CHO UI: xem `../../domains/ui/using-frontend-design.md` (build/reshape/type-critique nhanh) — index `../../domains/ui/README.md`.
- Liên quan: cần gates → `../hallmark/`; cần detector/Live → `../impeccable/`; cần checklist nhanh → `../web-interface-guidelines/`; cần bricks → `../reactbits/`.

### Quay lại index
- Về `../../domains/ui/README.md` để so sánh định vị với `hallmark/` + `impeccable/` + `web-interface-guidelines/`.
- Xem thêm item liên quan: `../impeccable/` (con cháu + detector) + `../hallmark/` (gates) + `../reactbits/` (bricks).

---

## English

### When to use
- New pages needing distinctive taste in one short session: design-lead persona + subject-matter grounding + locked aesthetic direction before code.
- Reshaping existing UI out of AI-slop via listed tells: 6 calibration clusters (the 6 defaults AI falls into, listed in SKILL.md: cream `#F4F1EA` + terracotta `#D97757`, acid-green/vermilion dark, broadsheet, SaaS-card kit, template chrome repeated in every brief) + typographic tells + default motion.
- Typography/copy guidance while designing: Elements-of-Typographic-Style scale, <80-char lines, writing rules (active voice, sentence case, CTAs naming the outcome, directed error/empty states).
- A zero-dependency skill, offline after install, one-line install, usable by any skill-reading agent.

### When to skip
- New systems must pass hard machine gates + render sweep → use `../hallmark/` (this skill advises, never enforces).
- Model-free detector/hooks/CI/visual Live comparison needed → use `../impeccable/` (a fork of this very skill, plus 24 commands + detector + Live).
- Sub-10-minute `file:line` checklist passes with no file changes → use `../web-interface-guidelines/`.
- Owned animated React bricks → use `../reactbits/`.
- Offline before installing (install needs network once) → the skill cannot be fetched.

### Install
- Install: `npx skills add https://github.com/anthropics/skills --skill frontend-design` (source: skills.sh Installation, read 08/11/2026).
- Requires: Node for `npx`; a skill-reading agent (Claude Code/Cursor/OpenCode...).
- Verified 08/11/2026: full `SKILL.md` + `LICENSE.txt` (Apache-2.0) fetches + parent-repo GitHub API (189,158 stars / 22,296 forks / 1,495 open issues / pushed 06/11/2026 / created 22/09/2025) + skills.sh page (1.1M installs, First Seen Jan 19 2026, 3 audits passed: Trust Hub/Socket/Snyk). NOT run: real install + real project use (WARN).

### How the item works
- Backing organization: Anthropic, repo `https://github.com/anthropics/skills` (189,158 stars / 22,296 forks per 08/11/2026 API), skill `skills/frontend-design/SKILL.md` + `LICENSE.txt` Apache-2.0, main-branch cadence (pushed 06/11/2026; 437 issues + 1.1k PRs open — contribution noise).
- Core operating method: one advice-only file, no code/scripts/detector — design-lead persona + subject grounding + principles (hero-first, typography, tells) + 2-pass plan/review/build + self-critique + writing rules. Runs on model self-discipline; no machine gate enforces compliance.
- Per-usecase differences: new builds run full token plan → mirror test (self-check: would a similar prompt land here) vs brief → build ([Sub-usecase 1](#sub-usecase-1-new-build-with-direction--strongest)) vs reshaping via listed tells ([Sub-usecase 2](#sub-usecase-2-reshape-out-of-ai-slop-via-tells)) vs typography/copy at write time (scale + writing rules, [Sub-usecase 3](#sub-usecase-3-typography--copy-while-designing)) vs closing self-critique (screenshots + responsive/focus/motion/a11y, [Sub-usecase 4](#sub-usecase-4-self-critique--quality-floor)).

### Invariant core
- Every job runs the 2-pass: token plan (4-6 named hex palette + typefaces/roles + ASCII layout + principles) → mirror test (would a similar prompt land here — if yes, revise with reasons) → then build. Building straight in is off-system.
- The brief beats every default: build exactly the direction the brief locks, even when it asks for one of the 6 clusters (verbatim SKILL.md).
- Boldness in one place + an unannounced quality floor (responsive to mobile, visible keyboard focus, respected reduced-motion, visual accessibility) + screenshot reviews where the environment allows.
- After use, state: subject/audience/job + chosen direction + passed mirror test (what changed, why); otherwise the system was not really used.

### Customizable surface
- Tunables: subject/audience/job (propose one concrete set + confirm when the brief is thin), aesthetic direction, 4-6 hex palette, typefaces (default families banned), layout concept, one orchestrated motion moment. Two-level approval: (1) which direction — shortlist aesthetics with reasons via the question tool, user picks before building; (2) what stays/changes — mirror-test revisions vs brief-locked parts. Waivers (building a default cluster because the brief demands it) must quote the brief/user. Never list `must-not` items here.
- Never run alongside another design skill in one project (conflicting rules, agent flip-flops — per impeccable's one-skill-per-project rule, source: ssdnodes 31/10/2026); pick one and disable the other at local scope.

### Work split
- Main agent: ask/confirm subject-audience-job, token plan, mirror test + logged revisions, build per plan, self-critique + screenshots.
- Hand browser/human steps to claude as a whole: visual verification (screenshot review, obscured focus, motion, narrow screens, keyboard) — with URL + tell checklist + expected output; the agent never asserts render results without a browser.
- Agent verifies: token plan matches brief + mirror test answered + screenshots reviewed + floor checklist clear.

### Differentiating positioning
- Vs `../impeccable/` (105,856 stars, a fork of this very skill — its README says "started from Anthropic's frontend-design"): different assurance layer — the skill delivers taste in one gateless file; impeccable adds 24 commands + a model-free detector + Live + hooks/CI. Pick the skill over impeccable for fast lean one-session work, offline-after-install, zero hook-context cost; pick impeccable for detector/exit codes/Live comparison. Never run both in one project — pick one.
- Vs `../hallmark/` (50,558 stars, system + machine gates + render sweep): different enforcement — hallmark GENERATES measured-gated systems and sweeps clean; the skill ADVISES taste the model may ignore. Pick the skill over hallmark when no merge gates are needed and speed matters; pick hallmark when output must pass gates (contrast/fold/word budget).
- Honest frame: wins on official Anthropic origin + one zero-dependency file + offline use + 1.1M installs + 3 passed audits + tells specified down to hex codes; loses on enforcement (no gates/detector), unpinned versions (install tracks newest main), no deep audits/ranks, no bricks.

### Coverage map (whole SKILL.md scanned 08/11/2026 — ★ strongest first)
- ★ New builds with direction (token plan + mirror test + brief-wins): see Sub-usecase 1.
- Reshaping out of AI-slop via tells (6 clusters + typo tells + template chrome + default motion): see Sub-usecase 2.
- Medium: typography scale + copy/writing rules at write time (1-2 typefaces, <80-char lines, sentence case, outcome-naming CTAs, directed error/empty states): see Sub-usecase 3.
- Medium: self-critique + quality floor (screenshot review + responsive/focus/reduced-motion/a11y + cut one accessory): see Sub-usecase 4.
- NOT supported → use instead: numeric merge gates → `../hallmark/`; detector/hooks/CI/Live → `../impeccable/`; fast `file:line` checklist → `../web-interface-guidelines/`; React bricks → `../reactbits/`; ranked P0-P3 reviews → `../impeccable/` (audit); proprietary comparisons → AlternativeTo.net.

### Decision dossier
- Jobs SERVED (4, concrete): 1. new pages with distinctive direction in one session; 2. reshaping UI via listed tells; 3. typography + copy guidance while designing; 4. a zero-dependency offline skill for any agent.
- Jobs NOT served (5, each with its replacement): 1. merge gates → `../hallmark/`; 2. detector/hooks/CI/Live → `../impeccable/`; 3. sub-10-minute `file:line` → `../web-interface-guidelines/`; 4. React bricks → `../reactbits/`; 5. ranked reviews → `../impeccable/` (audit).
- Free / total + price: $0 everything, Apache-2.0 (source: `LICENSE.txt` inside the skill folder, 08/11/2026 — the repo API returns `license: None`, read the file). Total cost = $0 + model fees.
- Install friction: 1 step to first use (`npx skills add ...` then invoke), matching the 1-line standard. Ran 08/11/2026: SKILL.md + LICENSE.txt + API + skills.sh fetches. NOT run: install + real use (WARN). Barriers: Node; unpinned versions (drift with main); no hooks (self-discipline).
- Viral same-segment opponents: `../impeccable/` (105,856 stars, direct descendant + detector/Live) vs `../hallmark/` (50,558 stars, system + gates).
- Pick it over opponents when: fast taste in one short session, offline after install, no gates/detector needed. Choice-flipping example: one-afternoon landing needing a strange direction → the skill; gated-merge output → Hallmark; Live comparison + CI → impeccable.
- NEVER use when: machine enforcement is required (advice the model can skip); `file:line` findings are required; running next to another design skill in one project.

### Sub-usecase 1: new build with direction (★ strongest)
- When to use: a brief exists (or a thin brief needing a proposed subject/audience/job), a distinctive page is needed fast.
- When to skip: UI exists → Sub-usecase 2; gates needed → `../hallmark/`; plan-only stopping before build (settle the plan, don't build).
- Copy-paste command: `npx skills add https://github.com/anthropics/skills --skill frontend-design` (install once) then prompt the agent `Use frontend-design to build a landing page for <brief>: confirm subject/audience/job first, token-plan then mirror-test, brief beats all defaults.`
- Numeric bar: plan carries a 4-6 named-hex palette + typefaces/roles + ASCII layout + principles; mirror test logs what changed + why; the brief-locked direction is built exactly.
- Input-output example (illustrative, never the default — direction picked by the user first): brief "monthly book club, busy professional audience" → confirmed subject/audience/job + token plan + plan-faithful page, no fall into cream/terracotta defaults.
- Own pitfalls: building straight without a plan (core FAIL); guessing the subject instead of proposing + confirming (grounding FAIL); accepting the first direction by default (anchor bias — shortlist + pick).
- Work split: main agent asks subject/audience/job (user confirms) → plans → mirror-tests → builds; claude verifies post-build visuals; verify via plan + mirror log.

### Sub-usecase 2: reshape out of AI-slop via tells
- When to use: existing UI/page reads "AI" without a nameable problem.
- When to skip: nothing exists → Sub-usecase 1; numeric gates needed → `../hallmark/`; a list suffices → `../web-interface-guidelines/`.
- Copy-paste command: `Use frontend-design to reshape <target>: check the 6 calibration clusters + typo tells + template chrome + default motion, list fixed tells.`
- Numeric bar: each fixed tell listed (e.g. gradient text dropped, eyebrow caps dropped, numbered markers kept only for true sequences, motion down to one orchestrated moment) + before/after screenshots reviewed.
- Input-output example (illustrative): pricing page (cream + italic serif + eyebrow caps + `A · B · C` + `→`) → tells dropped, one focal point kept, type treatment part of the design.
- Own pitfalls: applying the 6 clusters mechanically (brief demanding that look wins — brief beats defaults); fixing tells while losing the one focal point (restraint: boldness in one place).
- Work split: main agent checks + fixes + presents before/after; claude verifies narrow screens/keyboard/real motion; verify via tell list + screenshots.

### Sub-usecase 3: typography + copy while designing
- When to use: a page being written needs rule-correct type/copy (scale, lines, voice, error/empty).
- When to skip: type/copy settled → Sub-usecase 4 review; deep a11y/form checklists needed → guidelines.
- Copy-paste command: `Use frontend-design to review type + copy for <target>: 1-2 distinct typefaces, <80-char lines, sentence case, outcome-naming CTAs, directed error/empty states.`
- Numeric bar: Elements-of-Typographic-Style scale (intentional weights/widths/spacing); body lines <80 chars (serif longer + taller line-height than sans); zero all-caps labels; zero single-word headline accents; CTAs naming the outcome (`Save changes`, toast `Published` matching button `Publish`).
- Input-output example (illustrative): checkout form → sentence-case labels + 1-2 clearly-roled typefaces + inline errors with fixes + inviting empty screens.
- Own pitfalls: two near-identical typefaces (must be clearly distinct); monospace data labels everywhere (tell #5 — only when the brief fits); generic marketing copy.
- Work split: main agent reviews + fixes; claude only for real type-render checks (line-height/overflow).

### Sub-usecase 4: self-critique + quality floor
- When to use: a finished page needs closing before ship without machine gates.
- When to skip: measurable gates needed → `../hallmark/`; P0-P3 ranks needed → `../impeccable/` audit.
- Copy-paste command: `Use frontend-design to self-critique <target>: screenshot review, check mobile-down responsive + keyboard focus + reduced-motion + visual accessibility + cut one accessory.`
- Numeric bar: floor clear (mobile responsive ok, focus visible, reduced-motion variants, harmonious accessible colors); screenshots reviewed (never claimed from code reading); one cut logged per the Chanel rule (mirror-check and remove one accessory before leaving the house).
- Input-output example (illustrative): built landing → screenshots + list (focus ok, 2 motion moments → cut 1, 1 brief-serving-nothing decoration → cut).
- Own pitfalls: critiquing from code without screenshots (SKILL.md: a picture beats 1000 tokens); announcing the floor to the user (an implicit standard, no announcement needed).
- Work split: main agent screenshots + checklists; claude captures/compares where a real browser is needed; verify via screenshots + clear floor.

### Shared steps
1. Install once: `npx skills add https://github.com/anthropics/skills --skill frontend-design`.
2. Confirm subject/audience/job (propose one concrete set + confirm when thin, never guess).
3. Token plan: 4-6 hex palette + typefaces/roles + ASCII layout + principles.
4. Mirror-test vs brief: revise on default-likeness with reasons; brief beats all defaults.
5. Build/reshape/write per plan (one job/pass, in-scope diff).
6. Self-critique: screenshots + floor + cut one accessory.
7. State subject/direction/mirror-test/floor (core-fidelity).

### Sample prompts
- "Use frontend-design to build a landing page for job `<...>` (audience ..., main action ...). Confirm subject/audience/job first, token-plan then mirror-test, brief beats all defaults."
- "Use frontend-design to reshape `<target>`: check the 6 calibration clusters + typo tells + template chrome, list fixed tells, before/after screenshots."
- "Use frontend-design to review type + copy for `<target>`: 1-2 distinct typefaces, <80-char lines, sentence case, outcome-naming CTAs, directed error/empty states."
- Filled example: "Use frontend-design to build a monthly book-club signup landing (busy-professional audience, reserve-a-seat action, confirmed-dates/seats-only constraint). Token-plan first, log mirror-test revisions, no fall into cream/terracotta defaults."

### Pitfalls
- Building straight without token plan + mirror test (core FAIL — the plan is mandatory).
- Guessing the subject instead of proposing + confirming (grounding FAIL).
- Overriding the brief when it demands a default look (brief beats all defaults — verbatim SKILL.md).
- Accepting the first direction by default (anchor bias — shortlist + user pick first).
- Default typefaces + two near-identical faces + all-caps labels + single-word accents (listed typo tells).
- Scattered motion (fade-slide-up on every section) instead of one orchestrated moment + action-answering motion.
- Self-cancelling CSS specificity (`.section` vs `.cta` padding/margin — warned in SKILL.md).
- Generic selling copy + outcome-less CTAs + vague apologetic errors.
- Running next to another design skill in one project (rule conflicts — pick one, disable the other).
- Quoting stale installs/stars (weekly drift — date every measurement; read `LICENSE.txt`, the API returns None).

### Usage references (decisive + weighted, pinned 08/11/2026)
- Deep review: [skills.sh page](https://www.skills.sh/anthropics/skills/frontend-design) (fetched 08/11/2026) — *"Distinctive, production-grade frontend interfaces that reject generic AI aesthetics"* + one-line install + 3 security audits passed (Trust Hub/Socket/Snyk) + First Seen Jan 19 2026 + related skills (web-design-guidelines, canvas-design...) → confirms: fast install, baseline safety, nearest kin is web-design-guidelines (checklist), not a generator.
- Deep first-party: [`SKILL.md` raw](https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md) (fetched full 08/11/2026) + [`LICENSE.txt`](https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/LICENSE.txt) (Apache-2.0) — one advice-only file (persona + grounding + principles + 2-pass + self-critique + writing), no code/detector/gates → confirms: advice-only, enforcement = 0; read the file for the license, the repo API returns None.
- Deep lineage: [Impeccable README](https://github.com/pbakaus/impeccable) (fetched 08/11/2026) — *"Impeccable started from Anthropic's frontend-design skill"* → confirms ancestor position: the descendant (105,856 stars) adds detector/Live/hooks and out-stars the parent; pick the parent for leanness, the child for machinery.
- Weighted averages: parent-repo API 08/11/2026 — 189,158 stars / 22,296 forks / 1,495 open issues / pushed 06/11/2026 / created 22/09/2025; skill 1.1M installs on skills.sh (08/11/2026). Weight: installs (real install behavior, million-scale sample) beat repo stars (whole-skills-repo aggregate, not frontend-design alone).
- Vietnamese: query `frontend-design skill Anthropic đánh giá` returns no independent Vietnamese review → `unverified`.
- Conflict: huge installs + official origin + passed audits vs advice-only non-enforcement + noisy parent repo (1.1k PRs/437 issues) → verdict: use for fast direction when no machinery is needed; escalate to hallmark/impeccable for enforceable work.

### References
- Repo: https://github.com/anthropics/skills (`skills/frontend-design/SKILL.md` + `LICENSE.txt`)
- skills.sh page: https://www.skills.sh/anthropics/skills/frontend-design (installs + audits + related)
- Read order: `SKILL.md` (persona → grounding → principles → tells → 2-pass → self-critique → writing) → `LICENSE.txt` → skills.sh (installs/audits).
- Verified 08/11/2026: full SKILL.md + LICENSE.txt fetches + API + skills.sh. NOT run for real: install + use (WARN).

### Where used
- Used FOR UI: see `../../domains/ui/using-frontend-design.md` (fast build/reshape/type-critique) — index `../../domains/ui/README.md`.
- Related: gates → `../hallmark/`; detector/Live → `../impeccable/`; fast checklist → `../web-interface-guidelines/`; bricks → `../reactbits/`.

### Back to index
- Back to `../../domains/ui/README.md` to compare positioning vs `hallmark/` + `impeccable/` + `web-interface-guidelines/`.
- Related items: `../impeccable/` (descendant + detector) + `../hallmark/` (gates) + `../reactbits/` (bricks).
