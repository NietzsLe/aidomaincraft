# templates/runtime-draft-template.md — mẫu soạn draft item TRONG RUNTIME (CHARTER v12 §10)

> Dành cho agent/user ở repo đã cài aidomaincraft (runtime của hệ) khi việc
> chưa item nguồn nào phủ. Copy file này thành
> `.aidomaincraft/drafts/<ten>/README.md` trong repo đã cài (git-ignored,
> cấm commit), điền vào chỗ `[...]`, xóa dòng hướng dẫn `>` khi xong. Giữ
> song ngữ VI trước EN sau. 1 draft = 1 proposal. Draft đạt VERIFY H mới
> promote về nguồn qua clone `src/` + PR (chuẩn hóa khung nội tại §5d +
> `items/REGISTRY.md` + using-doc cùng commit). Cấm đụng `items/REGISTRY.md`
> nguồn từ draft; index cục bộ duy nhất là `REGISTRY.local.md` cạnh draft.
>
> Intake (CHARTER v12 §10): proposal 1 draft/1 đề xuất → thử runtime ở
> `.aidomaincraft/drafts/<x>/` (git-ignored) → khai index local → VERIFY H
> hết FAIL → promote qua `src/` + PR.

## Tiếng Việt

### Đề xuất
- Tên draft (kebab-case tiếng Anh): [...]
- Tác giả + ngày soạn: [...] — Repo runtime soạn: [...]
- Lý do ra đời (việc chưa ai phủ + bằng chứng đã tra index nguồn): [...]
- Domain dự kiến: [...]

### Dùng khi
- [Điều kiện cụ thể, không chung chung]

### Bỏ qua khi
- [Điều kiện cụ thể + trỏ việc thay thế (item nguồn hoặc draft khác)]

### Cách thử ở runtime
- Tài nguyên thử (tự sở hữu, stdlib, không deps nặng): [...]
- Lệnh copy-paste chạy được: `[...]`
- Quan sát UI (nếu có) bằng browser thật: [...]
- Kiểm tra: [...] (output ...)

### Bằng chứng đã chạy
- Lệnh đã chạy + output: [...]
- Relay session: [...] — Ngày thử: [...]

### Hồ sơ quyết định (gọn)
- Việc DÙNG (1+): [...] — Việc KHÔNG DÙNG (1+ kèm thay thế): [...]
- Ma sát: [... bước; đã chạy tới ...]
- TUYỆT ĐỐI không dùng khi: [...]

### Điều kiện promote (đủ mới PR về nguồn)
- [ ] Chạy được + có index local + VERIFY H hết FAIL + có relay log
- [ ] Promote = chuẩn hóa theo `templates/intrinsic-item-template.md` ở clone
  `src/`, khai `items/REGISTRY.md` + using-doc + index 2 đầu cùng commit

---

## English

> For agents/users at aidomaincraft-installed repos (system runtime) when no
> source item covers the job. Copy this file to
> `.aidomaincraft/drafts/<name>/README.md` in the installed repo (git-ignored,
> never commit), fill in `[...]`, delete `>` guidance lines when done.
> Bilingual VI first EN second. 1 draft = 1 proposal. Drafts passing VERIFY H
> promote to source via a `src/` clone + PR (§5d intrinsic frame +
> `items/REGISTRY.md` + using-doc in the same commit). Never touch source
> `items/REGISTRY.md` from a draft; the only local index is the sibling
> `REGISTRY.local.md`.
>
> Intake (CHARTER v12 §10): 1 draft/1 proposal → trial runtime under
> git-ignored `.aidomaincraft/drafts/<x>/` → local index → zero VERIFY H
> FAILs → promote via `src/` + PR.

### Proposal
- Draft name (English kebab-case): [...]
- Author + date: [...] — Runtime repo: [...]
- Why (uncovered job + proof the source index was searched): [...]
- Expected domain: [...]

### When to use
- [Concrete condition, never generic]

### When to skip
- [Concrete condition + replacement (source item or another draft)]

### Runtime trial
- Trial resources (self-owned, stdlib, no heavy deps): [...]
- Runnable copy-paste command: `[...]`
- UI observations (if any) in a real browser: [...]
- Check: [...] (output ...)

### Run evidence
- Commands run + outputs: [...]
- Relay session: [...] — Trial date: [...]

### Decision dossier (compact)
- Jobs it SERVES (1+): [...] — Jobs it does NOT serve (1+ with replacement): [...]
- Friction: [... steps; ran up to ...]
- ABSOLUTELY not when: [...]

### Promote gate (PR back only when all hold)
- [ ] Runnable + local index + zero VERIFY H FAILs + relay log present
- [ ] Promotion normalizes via `templates/intrinsic-item-template.md` inside
  the `src/` clone, declaring `items/REGISTRY.md` + using-doc + both index
  ends in the same commit
