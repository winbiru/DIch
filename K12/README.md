# Kho thuật ngữ K12 — Việt–Anh

Bộ từ điển liên môn dành cho học sinh, giáo viên, người dịch thuật và dự án V++.
Các thuật ngữ ưu tiên **tiếng Việt dễ hiểu**, có tên tiếng Anh đối chiếu
và giải nghĩa ngắn; giữ ký hiệu khoa học quốc tế khi phù hợp.

**Lưu ý về cấp lớp:** Ba nhóm *tiểu học / THCS / THPT* thể hiện độ khó tham khảo,
**không phải phân phối chương trình chính thức**. Các lĩnh vực Vật lý, Hóa học, Sinh học
ở cấp tiểu học được trình bày như kiến thức khoa học tích hợp, không có nghĩa
các môn này được dạy độc lập ở mọi khối lớp. Tên Anh là đối chiếu khái niệm,
không phải từ khóa có thể gõ trực tiếp trong V++.

**Quy mô hiện tại:** 23 lĩnh vực, 1422 mục từ đã biên soạn. Kho được mở rộng dần, chưa phải danh mục đầy đủ của chương trình giáo dục.

## Danh mục lĩnh vực

| Lĩnh vực | English | Số mục |
| --- | --- | ---: |
| [Toán học](toan-hoc/README.md) | Mathematics | 96 |
| [Vật lý](vat-ly/README.md) | Physics | 89 |
| [Hóa học](hoa-hoc/README.md) | Chemistry | 89 |
| [Sinh học](sinh-hoc/README.md) | Biology | 92 |
| [Ngữ văn](ngu-van/README.md) | Vietnamese Language and Literature | 57 |
| [Lịch sử](lich-su/README.md) | History | 52 |
| [Địa lý](dia-ly/README.md) | Geography | 55 |
| [Tin học](tin-hoc/README.md) | Informatics / Computer Science | 61 |
| [Công nghệ](cong-nghe/README.md) | Technology | 54 |
| [Giáo dục công dân](giao-duc-cong-dan/README.md) | Civic Education | 56 |
| [Âm nhạc](am-nhac/README.md) | Music | 54 |
| [Mỹ thuật](my-thuat/README.md) | Visual Arts | 54 |
| [Giáo dục thể chất](giao-duc-the-chat/README.md) | Physical Education | 52 |
| [Tiếng Anh](tieng-anh/README.md) | English Language | 59 |
| [Thiên văn học](thien-van-hoc/README.md) | Astronomy | 54 |
| [Khoa học Trái Đất](khoa-hoc-trai-dat/README.md) | Earth Science | 56 |
| [Môi trường và sinh thái](moi-truong-va-sinh-thai/README.md) | Environmental Science and Ecology | 56 |
| [Triết học và logic](triet-hoc-va-logic/README.md) | Philosophy and Logic | 56 |
| [Kinh tế và tài chính](kinh-te-tai-chinh/README.md) | Economics and Finance | 56 |
| [Tâm lý học](tam-ly-hoc/README.md) | Psychology | 56 |
| [Kỹ thuật và robot](ky-thuat-va-robot/README.md) | Engineering and Robotics | 56 |
| [Ngôn ngữ học và dịch thuật](ngon-ngu-hoc-va-dich-thuat/README.md) | Linguistics and Translation Studies | 56 |
| [Văn hóa và di sản](van-hoa-va-di-san/README.md) | Culture and Heritage Studies | 56 |

## Sử dụng và mở rộng

- [Thống kê theo lĩnh vực và cấp học](THONG_KE.md) giúp theo dõi phạm vi đã biên soạn.
- [Tiếng Anh đa nghĩa theo lĩnh vực](TIENG_ANH_DA_NGHIA.md) so sánh cách diễn đạt tiếng Việt tùy ngữ cảnh.
- [Tra theo tiếng Việt](CHI_MUC_VIET_ANH.md) hoặc [tra theo tiếng Anh](CHI_MUC_ANH_VIET.md).
- Chạy `python3 K12/tra_cuu.py "đạo hàm"` để tìm tên và giải nghĩa;
  có thể tìm không dấu, lọc môn hoặc xuất JSON.
- Mở `README.md` của từng môn, chọn cấp học để xem bảng từ Việt–Anh.
- [Quy ước biên soạn](QUY_UOC_BIEN_SOAN.md) giải thích cách chọn thuật ngữ
  tiếng Việt và bổ sung mục từ mới.
- [Nguồn đối chiếu và mức độ thẩm định](NGUON_DOI_CHIEU.md) nêu phạm vi
  chương trình và các bước kiểm chứng thuật ngữ trước khi dùng cho giảng dạy.
- [Từ điển V++ nền tảng](../TU_DIEN_THUAT_NGU_VPP_VI_EN.md) trình bày
  thuật ngữ lập trình đã đối chiếu mã nguồn V++; kho K12 là tài liệu mở rộng độc lập.
- `du-lieu.json` là **nguồn chuẩn để chỉnh sửa**; `tu-dien.jsonl` phục vụ
  xử lý máy/dữ liệu huấn luyện khi có giấy phép sử dụng phù hợp.
- Sau khi sửa `du-lieu.json`, chạy `python3 K12/tao_tai_lieu.py` để tái tạo
  tài liệu. Chạy `python3 K12/tao_tai_lieu.py --check` để kiểm tra đồng bộ.
- Khi đưa thuật ngữ vào tài liệu học, nên bổ sung nguồn chương trình/sách
  và kiểm chứng công thức, danh pháp chuyên ngành theo chuẩn đang áp dụng.
- [↑ Trang chủ kho tài liệu](../README.md)
