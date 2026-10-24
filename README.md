# Kho thuật ngữ Việt–Anh — V++ và giáo dục K12

Kho tài liệu hướng đến việc diễn đạt kiến thức kỹ thuật, khoa học và giáo dục bằng tiếng Việt mạch lạc, chính xác, dễ tra cứu. Mỗi mục có thuật ngữ tiếng Anh tương ứng để giúp đối chiếu các tài liệu quốc tế.

## Tài liệu hiện có

- **[Từ điển thuật ngữ V++ — Việt–Anh](TU_DIEN_THUAT_NGU_VPP_VI_EN.md):** cú pháp, trình biên dịch, lập trình hướng đối tượng, hệ thống và thư viện V++.
- **[Kho thuật ngữ K12 — Việt–Anh](K12/README.md):** 23 lĩnh vực; ngoài các môn học cơ bản còn có Thiên văn, Khoa học Trái Đất, Môi trường, Triết học, Tâm lý học, Kinh tế–tài chính, Kỹ thuật–robot, Ngôn ngữ học–dịch thuật và Văn hóa–di sản. Mỗi lĩnh vực được chia theo ba nhóm độ khó tiểu học, THCS và THPT.
- **[Bảng thống kê](K12/THONG_KE.md):** quy mô thuật ngữ theo lĩnh vực và cấp học, được tạo tự động từ dữ liệu nguồn.
- **[Tiếng Anh đa nghĩa theo lĩnh vực](K12/TIENG_ANH_DA_NGHIA.md):** so sánh các cách dịch khác nhau của một thuật ngữ Anh theo ngữ cảnh.
- **[Chỉ mục Việt → Anh](K12/CHI_MUC_VIET_ANH.md)** và **[chỉ mục Anh → Việt](K12/CHI_MUC_ANH_VIET.md)** để tra thuật ngữ nhanh.
- **[Quy ước biên soạn từ điển K12](K12/QUY_UOC_BIEN_SOAN.md):** nguyên tắc dịch và cách bổ sung thuật ngữ.
- **[Nguồn đối chiếu và mức độ thẩm định](K12/NGUON_DOI_CHIEU.md):** cách xác định phạm vi chương trình và các giới hạn kiểm chứng hiện tại.

## Cách đóng góp

Đối với K12, cập nhật `K12/du-lieu.json`, sau đó chạy:

```sh
python3 K12/tao_tai_lieu.py
python3 K12/tao_tai_lieu.py --check
python3 K12/tra_cuu.py "dao ham" --mon toan-hoc
python3 K12/tra_cuu.py "photosynthesis" --json
python3 -m unittest discover -s K12 -p 'test_*.py'
```

Không chỉnh sửa các bảng Markdown sinh tự động vì lần chạy tiếp theo sẽ ghi lại từ dữ liệu nguồn. Có thể dùng `K12/tu-dien.jsonl` để lập mục lục, tìm kiếm và xử lý dữ liệu bằng chương trình.

**Lưu ý:** Phân nhóm cấp học mang tính tham khảo, không thay thế chương trình giáo dục chính thức. Thuật ngữ trong kho K12 không mặc nhiên là từ khóa hoặc hàm thư viện V++.
