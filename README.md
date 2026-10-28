# aidomaincraft

## Tiếng Việt

**Mục đích:** repo tra cứu theo usecase khi làm dự án cùng AI agent. Mở dự án mới → đọc bảng dưới → vào đúng thư mục domain/item → làm theo `README.md` trong đó.

**Nguyên tắc:**
- Thư mục domain = lĩnh vực (`ui/`, `hardware/`...). Thư mục item = 1 công cụ/giải pháp (1 tool = 1 item, ví dụ `ui/hallmark/`).
- Các usecase con của tool nằm bên trong `README.md` của item, không tách item riêng.
- Mỗi file song ngữ: Việt trước, Anh sau.
- Luật cấu trúc và version nằm ở `CHARTER.md`. Agent và người đều phải tuân thủ.

**Bảng chọn:**

| Dự án / nhu cầu | Vào đâu |
|---|---|
| Làm UI | `ui/` |
| Lĩnh vực khác (sau này: hardware, backend...) | thêm thư mục ngang `ui/`, không đổi khung |

**Cách dùng cho agent:** xem `AGENTS.md`.

---

## English

**Purpose:** usecase-first lookup repo for building projects with AI agents. New project → check the table → open the matching domain/item → follow its `README.md`.

**Rules:**
- Domain folders are fields (`ui/`, `hardware/`...). Item folders are 1 tool/solution each (1 tool = 1 item, e.g. `ui/hallmark/`).
- A tool's sub-usecases live inside the item's `README.md`, never as separate items.
- Every file is bilingual: Vietnamese first, English second.
- Structure and versioning rules live in `CHARTER.md`.

**Routing:**

| Project / need | Go to |
|---|---|
| UI work | `ui/` |
| Other domains (later: hardware, backend...) | add a sibling of `ui/`, do not change the skeleton |

**Agent workflow:** see `AGENTS.md`.
