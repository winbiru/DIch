# Quy ước biên soạn thuật ngữ K12 Việt–Anh

## Mục đích

Góp phần phát triển khả năng diễn đạt các khái niệm khoa học bằng tiếng Việt. Mỗi mục cần vừa có tên tiếng Việt phù hợp ngữ cảnh, vừa có đối chiếu tiếng Anh để người học tra cứu sâu hơn.

## Nguyên tắc chọn từ

1. Ưu tiên **thuật ngữ tiếng Việt đã dùng ổn định** trong sách giáo khoa và tài liệu chuyên ngành. Nếu có nhiều biến thể, chọn một cách gọi chính và ghi biến thể khi thật sự cần.
2. Giữ **ký hiệu, công thức, tên riêng và chữ viết tắt quốc tế** khi việc dịch gây nhầm lẫn, ví dụ DNA, RNA, ATP, SI. Có thể giải thích đầy đủ bằng tiếng Việt bên cạnh.
3. **Không tự tạo tên dịch** chỉ vì muốn thay thế từ vay mượn. Đối với tên gọi còn đang tranh luận, ghi rõ phương án, ngữ cảnh sử dụng và nguồn tham khảo trước khi đưa thành thuật ngữ chính.
4. Một từ tiếng Anh có thể có nhiều nghĩa. Lựa chọn tương đương dựa vào **khái niệm**, không dịch từng chữ; ví dụ *circle* là *đường tròn*, còn *disk* là *hình tròn* (phần mặt phẳng bên trong và trên đường tròn).

   Có thể dùng [bảng tiếng Anh đa nghĩa theo lĩnh vực](TIENG_ANH_DA_NGHIA.md) để đối chiếu những trường hợp như *function* (hàm số trong Toán; hàm trong Tin học), *product* (tích trong Toán; sản phẩm trong Công nghệ) hoặc *translation* (dịch mã trong Sinh học; dịch thuật trong Ngôn ngữ học).
5. Giải nghĩa ngắn, tránh vòng tròn định nghĩa. Với hiện tượng phụ thuộc điều kiện, nói rõ điều kiện cần thiết.
6. Cấp tiểu học, THCS và THPT là **nhóm độ khó tra cứu**, không phải khẳng định thuật ngữ thuộc đúng lớp hoặc phân phối chương trình. Vật lý, Hóa học và Sinh học ở tiểu học thể hiện nội dung khoa học tích hợp.
7. Tách biệt từ điển khoa học với **cú pháp V++**. Thuật ngữ trong K12 chưa chắc có tên API tương ứng.

Đây là kho biên soạn và mở rộng độc lập, **chưa được thẩm định như từ điển hoặc chương trình chính thức**. Một số môn ở tiểu học là nội dung tích hợp trong môn học rộng hơn, và những chủ đề nâng cao chỉ nhằm mục đích tra cứu.

Đối với các lĩnh vực bổ trợ như Thiên văn học, Khoa học Trái Đất, Môi trường, Triết học–logic, Tâm lý học, Kinh tế–tài chính, Kỹ thuật–robot, Ngôn ngữ học và Văn hóa–di sản, việc xếp mục vào nhóm tiểu học/THCS/THPT **chỉ phản ánh khả năng tiếp cận của người học**. Không suy ra đây là môn độc lập trong chương trình chính thức hoặc mọi khái niệm đều được dạy tại cấp học tương ứng.

## Thêm và sửa mục từ

Mở [`du-lieu.json`](du-lieu.json), tìm đúng `id` môn học và cấp học trong `levels`:

- `01-tieu-hoc`: tiểu học (lớp 1–5);
- `02-trung-hoc-co-so`: THCS (lớp 6–9);
- `03-trung-hoc-pho-thong`: THPT (lớp 10–12).

Mỗi mục trong danh sách là một mảng ba chuỗi theo thứ tự:

```json
["đạo hàm", "derivative", "Tốc độ biến thiên tức thời của hàm theo biến."]
```

Sau khi sửa, chạy từ gốc repository:

```sh
python3 K12/tao_tai_lieu.py
python3 K12/tao_tai_lieu.py --check
python3 -m unittest discover -s K12 -p 'test_*.py'
```

Chương trình kiểm tra định dạng và thuật ngữ trùng trong mỗi môn rồi tạo các tệp Markdown, chỉ mục hai chiều và `tu-dien.jsonl`. Không sửa trực tiếp tệp được sinh ra. Để tra cứu, chạy `python3 K12/tra_cuu.py "tu khoa"`; tùy chọn `--mon`, `--cap`, `--exact`, `--limit` và `--json` giúp thu hẹp hoặc xuất kết quả.

Nếu một mục liên quan danh pháp, công thức hoặc cách dạy chính thức, cần đối chiếu tài liệu có thẩm quyền trước khi công bố sử dụng trong giảng dạy. Khi đề xuất chỉnh sửa, ghi rõ khái niệm, cách dịch và nguồn đã đối chiếu trong phần mô tả đóng góp để dễ thẩm định. Không sao chép nguyên văn định nghĩa từ nguồn không cho phép sử dụng.
