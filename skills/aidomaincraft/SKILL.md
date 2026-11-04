---
name: aidomaincraft
description: "Tra cứu usecase-first aidomaincraft (UI/media): chọn item theo việc, thêm item mới, review theo VERIFY. Kích hoạt khi user nhắc aidomaincraft hoặc cần lookup/chuẩn làm việc của hệ."
---

# aidomaincraft — skill router

Skill này điều hướng mọi hướng dẫn làm việc của hệ aidomaincraft. Nó không chứa
lệnh hay ngưỡng của item nào — mọi chi tiết sống ở repo nguồn, skill chỉ link.

Nguồn: `https://github.com/NietzsLe/aidomaincraft.git` (ref `main`).
Nếu chưa có bản local: `git clone --depth 1 --branch main
https://github.com/NietzsLe/aidomaincraft.git ~/.cache/aidomaincraft`
(fallback `/tmp/aidomaincraft` khi HOME không ghi được). Offline mà project có
`.aidomaincraft/` thì dùng snapshot đó; không có thì báo thiếu nguồn, cấm đoán.

## Dùng khi

- User nhắc `aidomaincraft`, cần chọn công cụ theo việc (UI/media), thêm item
  mới, review nội dung theo `VERIFY.md`, hoặc kiểm tra/cập nhật bản cài.
- Agent thuộc diện hỗ trợ: opencode, claude, codex (chuẩn Agent Skills mở —
  cài 1 lần dùng chung).

## Bỏ qua khi

- Việc thuần logic/backend, không đụng bề mặt UI/media theo định nghĩa
  `CHARTER.md` §2. Không cố nhét mọi việc vào hệ.

## Luồng tra cứu (4 bước, khớp `AGENTS.md` repo nguồn)

1. Đọc `CHARTER.md` (luật, bản hiện tại: v12) + root `README.md` để chọn
   domain (`domains/<d>/`).
2. Đọc `domains/<d>/README.md` (điều hướng + định vị + chồng lấn, cho phép
   nhiều item chính 1 việc) để chọn item + cách dùng.
3. Đọc `domains/<d>/using-<x>.md` để lấy lệnh mẫu + lưu ý RIÊNG cho domain,
   rồi theo link về `items/<x>/README.md` (nguồn sự thật duy nhất) để đọc cơ
   chế + ngưỡng chi tiết, làm theo lệnh trong đó.
4. Xong việc nêu artifact đã tái dùng (slug prompt / variant / skill slug /
   gates đã pass) — không nêu được nghĩa là chưa thực sự dùng hệ.

## Thêm item mới (CHARTER v12 §9: làm ở repo nguồn)

- Ngoại nhập: copy `templates/item-template.md` → `items/<x>/README.md`.
- Nội tại: copy `templates/intrinsic-item-template.md` → `items/<x>/README.md`
  (proposal 1 tool/1 đề xuất; tài nguyên tự sở hữu, cấm copy code ngoài).
- Mọi item: khai 1 dòng `items/REGISTRY.md` + using-doc
  `domains/<d>/using-<x>.md` + cập nhật index 2 đầu, tất cả trong cùng commit.

## Runtime của hệ vs thêm item trong runtime (CHARTER v12 §10: làm ở repo đã cài)

- Runtime của hệ = chỉ đọc/dùng: block đã cài + `doctor`/`check-update`/
  `upgrade` + tra cứu 4 bước về nguồn; offline dùng snapshot
  `.aidomaincraft/`, thiếu nguồn thì báo, cấm đoán.
- Thêm item trong runtime = soạn draft để sau promote: copy
  `templates/runtime-draft-template.md` → `.aidomaincraft/drafts/<x>/`
  (git-ignored, cấm commit) + khai 1 dòng
  `.aidomaincraft/drafts/REGISTRY.local.md` (cấm đụng `items/REGISTRY.md`
  nguồn). Cây quyết định: việc nguồn đã phủ → tra cứu + dùng; việc chưa
  ai phủ → soạn draft; draft đạt VERIFY H → promote qua clone `src/` + PR.

## Sửa + verify + duy trì

- Mọi sửa: self-review `VERIFY.md` tới 0 FAIL (1 FAIL không merge) +
  `bash tests/test.sh` xanh + entry `CHANGELOG.md` (kèm case đã thử).
- Đầu session chạm UI/media: chạy `doctor` + `check-update` của
  `scripts/aidomaincraft_setup.py` (read-only), báo 1 dòng; `upgrade` cần user
  ok trước. Snapshot `.aidomaincraft/` cũ (CHARTER lệch) thì refresh.
- Cấm tuyệt đối: commit log/token/PII/file local (`.relay/`, `.test/`,
  `.aidomaincraft/`); hand-edit block đã cài; review bằng trí nhớ.

## Cập nhật skill này

Skill không tự update. Cài lại từ nguồn để lấy bản mới
(`npx skills add https://github.com/NietzsLe/aidomaincraft --skill aidomaincraft`
hoặc copy `skills/aidomaincraft/` vào thư mục skills của agent).
