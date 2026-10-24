# TỪ ĐIỂN THUẬT NGỮ V++ — VIỆT–ANH

**Phiên bản tài liệu:** 1.0 · **Đối chiếu mã nguồn:** 24/10/2026  
**Dự án tham chiếu:** V++ / VXX · **Mã nguồn chương trình:** tệp `.vi`

Tài liệu dùng để đọc và viết mã V++, biên soạn giáo trình, dịch thông báo lỗi,
tra cứu thuật ngữ trong mã nguồn trình biên dịch và thống nhất cách gọi Việt–Anh.
Mỗi mục gồm **tên tiếng Việt đang dùng hoặc được khuyến nghị**, **thuật ngữ tiếng
Anh tương ứng** và **ý nghĩa trong ngữ cảnh V++**.

## 1. Phạm vi và cách sử dụng

- **[Cú pháp]**: Từ/cụm từ, ký hiệu hoặc tên đặc biệt được tài liệu ngôn ngữ V++ sử dụng.
- **[API]**: Tên thư viện, lớp hoặc hàm tìm thấy trong tài liệu/mã nguồn V++.
- **[Kỹ thuật]**: Cách gọi tiếng Việt của khái niệm kỹ thuật có mặt trong kiến trúc V++.
- **[Đề xuất]**: Cách dịch thống nhất cho tài liệu, chưa phải từ khóa hay API mới. **Không
  tự thay tên trong tệp `.vi`** nếu chưa được trình biên dịch hỗ trợ.

Các bảng 2–3 mô tả **cú pháp V++**, các bảng 4–8 chủ yếu giải thích **thuật ngữ
kỹ thuật và tên thư viện**. Cột tiếng Anh là *tương đương về nghĩa*, không bảo
đảm có thể thay trực tiếp chữ tiếng Việt bằng chữ tiếng Anh khi viết chương trình.

**Nguồn ưu tiên:** `docs/language-reference.md` và `docs/semantics.md` cho
ngữ nghĩa/cú pháp 1.0; `src/frontend/keywords.cpp` cho danh sách từ khóa nội bộ;
`docs/cli.md` cho lệnh `vpp`; `docs/architecture.md`,
`docs/kien-truc-oop-thu-vien-va-bien-dich.md` và mã `gói/**/*.vi` cho cấu trúc
trình biên dịch và API. Các đường dẫn này tính từ **gốc repository VXX**
(không phải thư mục chứa từ điển này). Xem phần 10 để đối chiếu.

## 2. Từ khóa, cú pháp và toán tử

| Tiếng Việt / ký hiệu V++ | English | Giải thích trong V++ |
| --- | --- | --- |
| `hàm` | function | Khai báo hàm: `hàm cộng(a, b) { ... };`. [Cú pháp] |
| `chính` | main / entry function | Tên hàm khởi chạy chuẩn: `hàm chính()`. Đây là **tên đặc biệt**, không phải từ khóa điều khiển. [Cú pháp] |
| `lớp Chính` | application entry class | Cách khác để vào chương trình: lớp `Chính` có phương thức công khai `chạy()`. [Cú pháp] |
| `trả về` | return | Kết thúc lời gọi hàm và đưa giá trị về nơi gọi. [Cú pháp] |
| `biến` | variable | Tên biến/khai báo biến; V++ cũng tạo biến bằng phép gán như `tên = "V++";`. [Cú pháp] |
| `khởi tạo` | initialize / constructor | Khi đặt sau `hàm` trong lớp, là phương thức khởi tạo đối tượng: `hàm khởi tạo(...)`. [Cú pháp] |
| `in` | print / output | Xuất giá trị: `in "Xin chào";`. [Cú pháp] |
| `nếu` | if | Thực thi khối lệnh nếu điều kiện đúng. [Cú pháp] |
| `hoặc nếu` | else if / elif | Kiểm tra điều kiện bổ sung nếu điều kiện trước sai. [Cú pháp] |
| `hoặc` | else | Nhánh còn lại của `nếu`. **Không** đồng nghĩa toán tử OR; OR luận lý là <code>&#124;&#124;</code>. [Cú pháp] |
| `lặp` | loop / for | Lặp khối lệnh, ví dụ `lặp(i = 0; i < 5; i++)`. [Cú pháp] |
| `chọn` | switch | Rẽ nhánh theo một giá trị. Đây là cách viết được dùng trong tài liệu ngôn ngữ 1.0. [Cú pháp] |
| `ca` | case | Một trường hợp bên trong `chọn`. [Cú pháp] |
| `mặc định` | default | Nhánh dự phòng của `chọn`; cũng dùng để gọi giá trị mặc định của tham số. [Cú pháp] |
| `bỏ qua` | continue | Bỏ phần còn lại của vòng hiện tại và chuyển sang lượt lặp kế tiếp. [Cú pháp] |
| `thoát` | break | Rời vòng lặp hoặc nhánh `chọn` gần nhất. [Cú pháp] |
| `dừng` | stop / halt | Từ khóa dừng chương trình trong ánh xạ opcode nội bộ; **khác** `thoát` khỏi vòng lặp. [Cú pháp nội bộ] |
| `gọi` | call / invoke | Từ khóa liên quan đến thao tác gọi trong keyword map; lời gọi thông thường dùng `tênHàm(...)`. [Cú pháp nội bộ] |
| `nhập` | import | Nạp mô-đun/gói: `nhập gói/văn bản/chính;`. [Cú pháp] |
| `như` | as / alias | Đặt bí danh nhập: `nhập feature_math như toán;`. [Cú pháp] |
| `công khai nhập` | re-export / public import | Nhập rồi xuất lại API công khai cho mô-đun khác. [Cú pháp] |
| `thử` | try | Bắt đầu khối có thể phát sinh ngoại lệ. [Cú pháp] |
| `bắt lỗi` | catch | Xử lý giá trị ngoại lệ được ném trong khối `thử`. [Cú pháp] |
| `ném` | throw / raise | Phát sinh ngoại lệ: `ném "không hợp lệ";`. [Cú pháp] |
| `đúng` | true | Giá trị luận lý đúng. [Cú pháp] |
| `sai` | false | Giá trị luận lý sai. [Cú pháp] |
| `rỗng` | null | Giá trị vắng mặt riêng biệt; không đồng nhất với `0`, `""` hoặc danh sách rỗng. [Cú pháp] |
| `và` / `&&` | logical AND | Phép hội: hai điều kiện đều đúng. Toán tử được minh họa ổn định là `&&`. [Cú pháp / cách gọi] |
| <code>&#124;&#124;</code> | logical OR | Phép tuyển luận lý; phân biệt với `hoặc` dùng cho nhánh `else`. [Cú pháp] |
| `không` / `!` | logical NOT | Phủ định điều kiện; ví dụ được dùng phổ biến là `!đúng`. [Cú pháp / cách gọi] |
| `=` | assignment | Gán giá trị cho biến hoặc thuộc tính. [Cú pháp] |
| `==` / `!=` | equality / inequality | So sánh bằng / khác nhau; `==` không phải phép gán. [Cú pháp] |
| `<`, `>`, `<=`, `>=` | relational comparison | So sánh thứ tự: nhỏ hơn, lớn hơn, không lớn hơn, không nhỏ hơn. [Cú pháp] |
| `+`, `-`, `*`, `/`, `%` | arithmetic operators | Cộng, trừ, nhân, chia, chia lấy dư; dấu `+` cũng có thể nối chuỗi. [Cú pháp] |
| `+=`, `-=`, `*=`, `/=`, `%=` | compound assignment | Vừa tính toán vừa gán lại vào biến. [Cú pháp] |
| `++` / `--` | increment / decrement | Tăng / giảm một đơn vị. [Cú pháp] |
| `ngoại thư viện` | foreign library declaration | Khai báo thư viện ngoại trong cơ chế System FFI tương thích. [Cú pháp, không còn dùng trong thư viện chuẩn được kiểm kê 22/10] |
| `ngoại hàm` | foreign function declaration | Khai báo hàm ngoại, chữ ký ABI và quyền sử dụng; không đồng nghĩa với hàm V++ thông thường. [Cú pháp tương thích] |
| `chuyển` / `trường hợp` | switch / case (legacy spelling) | Có trong `keywordMap` và `docs/grammar.bnf` cũ; tài liệu 1.0 và các tệp `.vi` hiện dùng `chọn` / `ca`. Không lấy cặp này làm ví dụ chuẩn. [Cú pháp tương thích] |

**Lưu ý quan trọng:** `docs/grammar.bnf` vẫn chứa một số cách viết cũ
(ví dụ `chuyển` / `trường hợp`); trong trường hợp khác biệt, ưu tiên
`docs/language-reference.md` và kiểm tra trên compiler hiện hành.

## 3. Lập trình hướng đối tượng và ngữ nghĩa ngôn ngữ

| Tiếng Việt | English | Ý nghĩa / ghi chú |
| --- | --- | --- |
| `lớp` | class | Khuôn mẫu định nghĩa thuộc tính và phương thức của đối tượng. [Cú pháp] |
| `đối tượng` | object / instance | Thực thể được tạo từ một lớp, có trạng thái riêng. [Kỹ thuật] |
| `giao diện` | interface | Hợp đồng phương thức mà lớp triển khai phải đáp ứng; ở V++ 1.0 được kiểm tra tại lúc biên dịch. [Cú pháp] |
| `kế thừa` | extends / inheritance | Cho phép lớp con thừa hưởng hành vi lớp cha; lớp V++ chỉ có một lớp cha. [Cú pháp] |
| `triển khai` | implements | Công bố lớp thực hiện một hay nhiều giao diện. [Cú pháp] |
| `công khai` | public | Thành phần có thể truy cập từ bên ngoài theo hợp đồng xuất/hiển thị. [Cú pháp] |
| `bảo vệ` | protected | Thành phần truy cập được trong lớp sở hữu và lớp con theo quy tắc V++. [Cú pháp] |
| `riêng tư` | private | Thành phần chỉ cho phép truy cập trong phạm vi được quy định của lớp/mô-đun. [Cú pháp] |
| `mình` | self / this | Đối tượng nhận lời gọi hiện tại (receiver); từ chuẩn của V++, không viết `this` để thay thế. [Cú pháp] |
| `gốc` | super | Truy cập phương thức hoặc constructor từ lớp cha; không tạo đối tượng cha mới. [Cú pháp] |
| phương thức | method | Hàm thuộc lớp, có thể gọi qua `đốiTượng.phươngThức()`. [Kỹ thuật] |
| thuộc tính / trường | property / field | Giá trị lưu trong một đối tượng; field instance V++ hiện là thuộc tính động. [Kỹ thuật] |
| phương thức khởi tạo | constructor | Hàm `khởi tạo` chạy khi tạo instance; có thể gọi `gốc.khởi tạo(...)`. [Kỹ thuật] |
| ghi đè | override | Lớp con định nghĩa lại phương thức kế thừa. [Kỹ thuật] |
| đa hình | polymorphism | Cùng lời gọi phương thức có hành vi khác theo lớp của receiver. [Kỹ thuật] |
| đóng gói | encapsulation | Tổ chức trạng thái và hành vi bên trong lớp, kiểm soát truy cập. [Kỹ thuật] |
| kiểu động | dynamic typing | Một biến có thể nhận các loại giá trị khác nhau khi chạy; chính sách V++ 1.0. [Kỹ thuật] |
| kiểu tĩnh | static typing | Kiểm tra kiểu trước khi chạy; **không** phải chính sách bắt buộc của V++ 1.0. [Kỹ thuật] |
| số nguyên | integer / int | Giá trị số nguyên; nhiều đường biên dịch/ABI hiện dùng `i32`. [Kỹ thuật] |
| số thực | floating-point number / double | Giá trị số thực như `3.5`. [Kỹ thuật] |
| chuỗi | string | Dãy ký tự văn bản; V++ hỗ trợ tên định danh có dấu Unicode. [Kỹ thuật] |
| danh sách | list / array-like collection | Tập hợp có thứ tự, ví dụ `[1, 2, 3]`. [Kỹ thuật] |
| từ điển / bản đồ ánh xạ | map / dictionary | Cặp khóa–giá trị, ví dụ `{"tên": "V++"}`. [Kỹ thuật] |
| bộ / bộ giá trị | tuple | Nhóm giá trị theo vị trí. [Kỹ thuật] |
| tập hợp | set | Tập các phần tử không trùng theo hợp đồng của cấu trúc dữ liệu. [Kỹ thuật] |
| tham số | parameter | Tên dữ liệu đầu vào trong phần khai báo hàm. [Kỹ thuật] |
| đối số | argument | Giá trị cụ thể truyền khi gọi hàm. [Kỹ thuật] |
| tham số mặc định | default parameter | Tham số có giá trị được dùng khi người gọi bỏ qua đối số tương ứng. [Kỹ thuật] |
| hàm vô danh | anonymous function / lambda | Hàm không cần tên khai báo, ví dụ `hàm(x) { trả về x * 2; }`. [Kỹ thuật] |
| bao đóng | closure | Hàm giữ quyền truy cập các biến từ phạm vi tạo ra nó; V++ capture ô nhớ chia sẻ. [Kỹ thuật] |
| đệ quy | recursion | Hàm gọi lại chính nó trực tiếp hoặc gián tiếp. [Kỹ thuật] |
| phạm vi từ vựng | lexical scope | Vùng có thể nhìn thấy tên biến dựa vào vị trí mã nguồn. [Kỹ thuật] |
| che khuất tên | shadowing | Khai báo tên ở phạm vi trong che tên cùng chữ ở phạm vi ngoài. [Kỹ thuật] |
| liên kết tên | name binding | Ghép cách dùng định danh với khai báo hoặc ô nhớ tương ứng. [Kỹ thuật] |
| đồng nhất đối tượng | object identity | So sánh xem hai tham chiếu cùng trỏ tới một instance; khác so nội dung. [Kỹ thuật] |
| giá trị đúng theo ngữ cảnh | truthiness | Quy tắc xét giá trị như đúng/sai trong điều kiện, kể cả với số, chuỗi, tập hợp. [Kỹ thuật] |
| chuyển kiểu ngầm | implicit coercion / numeric promotion | Chuyển dạng giá trị trong phép toán theo quy tắc ngôn ngữ; không áp dụng tùy tiện cho so sánh. [Kỹ thuật] |
| ngoại lệ | exception | Giá trị/lỗi được `ném` rồi có thể `bắt lỗi`. [Kỹ thuật] |
| dấu vết lời gọi | stack trace | Chuỗi vị trí gọi hàm giúp xác định nơi xảy ra lỗi. [Kỹ thuật] |

## 4. Trình biên dịch, máy ảo và mã máy

| Tiếng Việt chuẩn hóa | English | Ý nghĩa / nơi sử dụng |
| --- | --- | --- |
| mã nguồn | source code | Văn bản chương trình `.vi` trước khi biên dịch. [Kỹ thuật] |
| đơn vị từ vựng / từ tố | token | Đơn vị cú pháp do bộ tách từ vựng nhận ra, có thể kèm vị trí nguồn. [Kỹ thuật] |
| bộ tách từ vựng | lexer / tokenizer | Chuyển chuỗi ký tự thành các token; lớp thực tế: `Bộ Tách Từ Vựng`. [API] |
| bộ phân tích cú pháp | parser | Từ token dựng cấu trúc cú pháp; lớp thực tế: `Bộ Phân Tích Cú Pháp`. [API] |
| cây cú pháp trừu tượng | abstract syntax tree (AST) | Cấu trúc dạng cây mô tả chương trình sau phân tích cú pháp. [Kỹ thuật] |
| nút cú pháp | syntax node / AST node | Một thành phần trong AST; API `Nút Cú Pháp`. [API] |
| phân tích ngữ nghĩa | semantic analysis | Kiểm tra tên, phạm vi, số đối số, kế thừa, giao diện, quyền truy cập. [Kỹ thuật] |
| bộ kiểm tra kiểu | type checker | Thành phần kiểm tra kiểu dữ liệu; phân biệt với semantic analyzer trong V++ kiểu động. [Kỹ thuật] |
| biểu diễn trung gian | intermediate representation (IR) | Dạng nội bộ giữa AST và mã đầu ra; V++ có `untyped IR`. [Kỹ thuật] |
| biểu diễn trung gian không kiểu | untyped IR | IR chưa gán kiểu tĩnh bắt buộc cho mọi biểu thức. [Kỹ thuật] |
| hạ biểu diễn | lowering | Chuyển từ dạng mức cao sang dạng thấp hơn, ví dụ AST → IR → Machine IR. [Kỹ thuật] |
| bộ hạ IR | IR lowerer | Thành phần thực hiện hạ IR; lớp API `Bộ Hạ IR`. [API] |
| biểu diễn trung gian cấp máy | machine intermediate representation (Machine IR) | Lệnh gần kiến trúc CPU để sinh mã máy. [Kỹ thuật] |
| bộ tối ưu | optimizer | Biến đổi IR/mã nhằm giảm chi phí hoặc đơn giản hóa mà giữ hành vi. [Kỹ thuật] |
| sinh mã | code generation / codegen | Tạo bytecode, mã máy hoặc object từ biểu diễn đã phân tích. [Kỹ thuật] |
| bộ phát bytecode | bytecode emitter | Tạo dãy lệnh bytecode V++; lớp `Bộ Phát Bytecode`. [API] |
| mã lệnh trung gian | bytecode | Lệnh cho máy ảo V++, khác với IR và mã máy của CPU. [Kỹ thuật] |
| mã thao tác | opcode | Mã xác định hành động của một lệnh bytecode hoặc Machine IR. [Kỹ thuật] |
| toán hạng | operand | Dữ liệu/ô nhớ được lệnh sử dụng. [Kỹ thuật] |
| hằng tức thời | immediate value | Giá trị được mã hóa ngay trong chỉ thị máy. [Kỹ thuật] |
| bộ xác minh bytecode | bytecode verifier | Kiểm tra tính hợp lệ của chương trình bytecode trước khi chạy. [Kỹ thuật] |
| máy ảo | virtual machine (VM) | Bộ thực thi bytecode của V++; phân biệt với máy ảo hệ điều hành. [Kỹ thuật] |
| bộ thông dịch | interpreter | Bộ chạy từng lệnh hoặc thao tác của ngôn ngữ/VM. [Kỹ thuật] |
| biên dịch trước khi chạy | ahead-of-time compilation (AOT) | Sinh mã đích trước khi thực thi chương trình. [Kỹ thuật] |
| biên dịch trong lúc chạy | just-in-time compilation (JIT) | Chuẩn bị/biên dịch trong quá trình thực thi; mức native hay bytecode cần nêu cụ thể. [Kỹ thuật] |
| mã bản địa | native code | Mã chạy trực tiếp trên kiến trúc mục tiêu. [Kỹ thuật] |
| bộ sinh mã bản địa | native code generator | Tạo lệnh máy cho một kiến trúc; lớp `Bộ Sinh Mã Bản Địa`. [API] |
| tập lệnh máy | instruction set architecture (ISA) | Quy định chỉ thị của CPU như x86-64, AArch64, RISC-V. [Kỹ thuật] |
| hợp ngữ | assembly language | Biểu diễn dễ đọc của chỉ thị CPU. [Kỹ thuật] |
| trình hợp dịch | assembler | Chuyển mã hợp ngữ thành mã máy/object. [Kỹ thuật] |
| tệp đối tượng | object file | Đầu ra `.o` / `.obj` có mã máy, ký hiệu và thông tin liên kết; **khác** đối tượng OOP. [Kỹ thuật] |
| định dạng đối tượng ELF | Executable and Linkable Format (ELF) | Định dạng binary/object thường dùng trên Linux. [Kỹ thuật] |
| định dạng đối tượng Mach-O | Mach Object (Mach-O) | Định dạng binary/object trên macOS. [Kỹ thuật] |
| định dạng đối tượng COFF | Common Object File Format (COFF) | Định dạng object dùng trong công cụ Windows. [Kỹ thuật] |
| ký hiệu liên kết | linker symbol | Tên được định nghĩa/tham chiếu giữa các đơn vị mã máy. [Kỹ thuật] |
| tái định vị | relocation | Bản ghi để linker vá địa chỉ khi ghép các tệp đối tượng. [Kỹ thuật] |
| bộ liên kết | linker | Kết hợp object/thư viện thành chương trình hoặc thư viện đầu ra. [Kỹ thuật] |
| bộ liên kết bytecode | bytecode linker | Ghép đơn vị bytecode V++; lớp `Bộ Liên Kết Bytecode`. [API] |
| tệp thực thi | executable | Chương trình đã được chuẩn bị để hệ điều hành nạp và chạy. [Kỹ thuật] |
| giao diện nhị phân ứng dụng | application binary interface (ABI) | Quy ước biểu diễn dữ liệu, cách gọi, thanh ghi/stack, ký hiệu giữa các thành phần. [Kỹ thuật] |
| quy ước gọi hàm | calling convention | Quy tắc truyền tham số, giá trị trả về và lưu thanh ghi khi gọi hàm máy. [Kỹ thuật] |
| bộ ba đích | target triple | Tên quy định kiến trúc–nền tảng–ABI, ví dụ `aarch64-linux-gnu`. [Kỹ thuật] |
| đồ thị luồng điều khiển | control-flow graph (CFG) | Đồ thị các nhánh/đường chạy dùng để kiểm tra hoặc tối ưu mã. [Kỹ thuật] |
| phiên biên dịch | compilation session / compilation context | Trạng thái gắn với một lượt biên dịch, gồm tên, module, chuỗi và kết quả. [Kỹ thuật] |
| bảng chuỗi | string pool (StringPool) | Nơi lưu chuỗi dùng chung với chỉ mục ổn định cho bytecode/artifact. [Kỹ thuật] |
| mã định danh hàm | function ID | Số định danh hàm trong registry/ABI của chương trình đã biên dịch. [Kỹ thuật] |
| sổ đăng ký hàm | function registry | Quản lý ID, ký hiệu và metadata hàm; lớp `Bộ Đăng Ký Hàm`. [API] |
| sản phẩm biên dịch | compilation artifact / build artifact | Dữ liệu được compiler tạo ra: bytecode, object hoặc executable tùy bước. [Kỹ thuật] |
| bộ mã hóa sản phẩm biên dịch | artifact serializer / codec | Kiểm tra, mã hóa và giải mã artifact; API `Bộ Mã Hóa Artifact`. [API] |
| bộ nạp sản phẩm biên dịch | artifact loader | Đọc/kiểm tra rồi nạp artifact để thực thi; API `Bộ Nạp Artifact`. [API] |
| tự biên dịch | self-hosting compiler | Compiler V++ có thể biên dịch chính mã nguồn compiler viết bằng V++. [Kỹ thuật] |
| biên dịch khởi tạo | bootstrapping | Dùng compiler ban đầu (Stage 0) tạo compiler thế hệ tiếp theo. [Kỹ thuật] |
| giai đoạn 0/1/2/3 | bootstrap Stage 0/1/2/3 | Các thế hệ compiler được tạo liên tiếp; so đầu ra Stage 2/3 để phát hiện sai lệch. [Kỹ thuật] |
| biên dịch tách đơn vị | separate compilation | Biên dịch từng mô-đun thành object rồi liên kết. [Kỹ thuật] |
| bộ nhớ đệm biên dịch | compilation cache | Tái sử dụng IR/object khi nội dung và điều kiện biên dịch tương thích. [Kỹ thuật] |

## 5. Bộ thực thi, hệ thống và mạng

| Tiếng Việt chuẩn hóa | English | Ý nghĩa / ghi chú |
| --- | --- | --- |
| môi trường thực thi | runtime | Thành phần quản lý các giá trị, lời gọi, bộ nhớ và tài nguyên khi chạy. [Kỹ thuật] |
| ngăn xếp thực thi | execution stack | Lưu toán hạng, giá trị tạm hoặc thông tin lời gọi. [Kỹ thuật] |
| khung gọi hàm | call frame | Trạng thái của một lần gọi hàm: vị trí lệnh, biến cục bộ, tham số... [Kỹ thuật] |
| vùng nhớ động | heap | Vùng cấp phát đối tượng và collection có vòng đời động. [Kỹ thuật] |
| thu gom rác | garbage collection (GC) | Thu hồi bộ nhớ không còn truy cập được. [Kỹ thuật] |
| bộ thu gom rác truy vết | tracing garbage collector | Duyệt đồ thị đối tượng từ các gốc còn sống để tìm vùng nhớ cần giữ. [Kỹ thuật] |
| gốc thu gom | GC root | Giá trị còn dùng trên stack, biến, instance hoặc closure mà GC phải đánh dấu. [Kỹ thuật] |
| tham chiếu yếu | weak reference / weak handle | Tham chiếu không tự giữ đối tượng sống; dùng trong theo dõi heap. [Kỹ thuật] |
| ô nhớ bao đóng | captured cell | Ô nhớ chung được closure và môi trường ngoài cùng quan sát/cập nhật. [Kỹ thuật] |
| mô-đun | module | Đơn vị mã có khai báo, nhập, xuất và vòng đời khởi tạo riêng. [Kỹ thuật] |
| khởi tạo mô-đun | module initialization | Chạy mã khởi tạo mô-đun một lần theo thứ tự phụ thuộc. [Kỹ thuật] |
| hàm nội tại máy | machine intrinsic | Hàm/cơ chế mức thấp do VM/runtime cung cấp cho thư viện V++. [Kỹ thuật] |
| giao diện hàm ngoại | foreign function interface (FFI) | Cơ chế gọi hàm từ thư viện ngôn ngữ/binary khác. [Kỹ thuật] |
| ranh giới bản địa | native boundary | Điểm V++ đi sang runtime/mã máy/hệ điều hành, nơi phải kiểm tra ABI và dữ liệu. [Kỹ thuật] |
| quyền khả năng | capability | Quyền được host cấp cho một nhóm thao tác hệ thống cụ thể; không do chuỗi tên tự tạo ra. [Kỹ thuật] |
| mã nắm giữ tài nguyên | resource handle | Định danh phiên/tệp/socket do runtime quản lý. [Kỹ thuật] |
| lời gọi hệ thống | system call (syscall) | Cơ chế yêu cầu dịch vụ từ nhân hệ điều hành. [Kỹ thuật] |
| giao diện hệ điều hành POSIX | Portable Operating System Interface (POSIX) | Tập quy ước API phổ biến trên các hệ Unix. [Kỹ thuật] |
| ổ cắm | socket | Đầu mối giao tiếp mạng, thường qua TCP hoặc UDP. [Kỹ thuật] |
| giao vận tin cậy | Transmission Control Protocol (TCP) | Giao thức truyền luồng byte có thứ tự và kiểm soát lỗi. [Kỹ thuật] |
| giao vận gói tin | User Datagram Protocol (UDP) | Giao thức truyền datagram không bảo đảm truyền tới hay thứ tự. [Kỹ thuật] |
| phân giải tên miền | Domain Name System (DNS) resolution | Chuyển tên máy thành địa chỉ IP hoặc truy vấn bản ghi DNS. [Kỹ thuật] |
| bảo mật tầng vận chuyển | Transport Layer Security (TLS) | Giao thức bảo vệ dữ liệu truyền qua kết nối mạng. [Kỹ thuật] |
| bắt tay bảo mật | TLS handshake | Giai đoạn thiết lập tham số mật mã và xác thực phía kết nối. [Kỹ thuật] |
| tiến trình | process | Chương trình đang chạy do hệ điều hành quản lý. [Kỹ thuật] |
| luồng xử lý | thread / worker | Đơn vị xử lý đồng thời; **khác** luồng byte/luồng tệp (stream). [Kỹ thuật] |
| đầu ra chuẩn | standard output (stdout) | Kênh ghi dữ liệu thông thường của tiến trình. [Kỹ thuật] |
| đầu ra lỗi chuẩn | standard error (stderr) | Kênh ghi lỗi và thông báo chẩn đoán. [Kỹ thuật] |
| mã thoát | exit code | Giá trị tiến trình trả cho hệ điều hành khi kết thúc. [Kỹ thuật] |
| thời hạn / thời gian chờ | deadline / timeout | Giới hạn thời gian hoàn tất thao tác, tùy ngữ cảnh. [Kỹ thuật] |

## 6. Gói thư viện và tên lớp thực tế

Tên ở hai cột đầu bảng sau là **tên đang được sử dụng trong cây `gói/` hoặc
tài liệu API của V++**. Cột tiếng Anh giải thích chức năng, không phải lệnh
`nhập` thay thế.

### 6.1. Nhóm gói

| Tên gói V++ | English | Công dụng chính |
| --- | --- | --- |
| `gói/lõi` | core | Kiểu và tiện ích cơ bản, cấu hình, nhật ký, sự kiện, công cụ chung. [API] |
| `gói/chuẩn` | standard / standard entry | Điểm tập hợp chức năng chuẩn. [API] |
| `gói/biên dịch` | compiler | Cú pháp, AST, IR, bytecode, mã máy và quản lý quá trình biên dịch. [API] |
| `gói/bộ sưu tập` | collections | Danh sách, ngăn xếp, hàng đợi, tập hợp, từ điển. [API] |
| `gói/văn bản` | text / strings | Chuỗi, nối chuỗi, tách/quét văn bản, mã hóa. [API] |
| `gói/nhập xuất` | input/output (I/O) | Tệp, thư mục, đường dẫn, luồng tệp, bộ đệm. [API] |
| `gói/thời gian` | time | Thời lượng, lịch, UTC, đồng hồ đơn điệu và bấm giờ. [API] |
| `gói/hệ thống` | system | Môi trường, nền tảng, tiến trình. [API] |
| `gói/mạng` | networking | Socket, DNS, HTTP, địa chỉ và định danh tài nguyên. [API] |
| `gói/dữ liệu` | data | Kết nối cơ sở dữ liệu, phân trang và xử lý dữ liệu. [API] |
| `gói/ứng dụng` | application | Bộ điều khiển và vòng đời ứng dụng. [API] |
| `gói/kiểm thử` | testing | Khẳng định, ca kiểm thử, vòng đời/báo cáo kiểm thử. [API] |
| `gói/bảo mật` | security / cryptography | Các tiện ích bảo mật, mật mã. [API] |
| `gói/dựng` | builders / scaffolding | Hỗ trợ dựng thành phần ứng dụng, dữ liệu và trang mạng. [API] |
| `gói/lượng tử` | quantum computing | Mạch, mô phỏng và giao tiếp định dạng lượng tử. **Có mã nguồn gói; mức hoàn thiện phải tra riêng.** [API] |

### 6.2. Lớp, giao diện và thao tác

| Tên trong V++ | English | Ý nghĩa / cách dùng |
| --- | --- | --- |
| `Bộ Biên Dịch` | Compiler | Phiên biên dịch nguồn và tra cứu kết quả, AST, bytecode. [API] |
| `Bộ Biên Dịch Tự Chủ` | Self-hosted Compiler | Phiên trình biên dịch triển khai các bước trong V++. [API] |
| `Bộ Phân Tích Phụ Thuộc` | Dependency Analyzer | Xác định các import và phụ thuộc từ nguồn. [API] |
| `Bộ Dựng Đồ Thị Mô Đun` | Module Graph Builder | Xây quan hệ nhập mô-đun, nhận biết chu trình. [API] |
| `Bộ Nạp Nguồn` | Source Loader | Nạp nguồn, quản lý lượt duyệt và thứ tự khởi tạo. [API] |
| `Trình Điều Khiển Biên Dịch` | Compiler Driver | Điều phối compile, chạy và nạp kết quả. [API] |
| `Nút Cú Pháp` | AST Node | Biểu diễn nút trong cây cú pháp V++. [API] |
| `Bộ Chỉ Mục Khai Báo` | Declaration Index | Lập chỉ mục khai báo theo tên trên AST. [API] |
| `Khách Duyệt Cú Pháp` | AST Visitor | Giao diện duyệt các nút cây cú pháp. [API] |
| `Ngăn Xếp` | Stack | Cấu trúc vào sau ra trước (LIFO), dùng `đẩy` / `rút`. [API] |
| `Hàng Đợi` | Queue | Cấu trúc vào trước ra trước (FIFO). [API] |
| `Bộ Chứa` | Container interface | Hợp đồng chung cho cấu trúc chứa dữ liệu, gồm `số lượng` và `trống`. [API] |
| `Tập Hợp` | Set | Tập hợp phần tử không trùng nhau. [API] |
| `Từ Điển` | Dictionary / Map | Cấu trúc lưu giá trị theo khóa. [API] |
| `Bộ Nối Văn Bản` | String Builder / Joiner | Thêm và gộp các phần văn bản có phân cách. [API] |
| `Bộ Quét` | Scanner / Token Scanner | Đọc tuần tự từ văn bản theo dấu phân cách. [API] |
| `Biểu Thức Chính Quy` | Regular Expression | Đối tượng tìm, thay, tách theo biểu thức regex. [API] |
| `Luồng Tệp` | File Stream | Đọc/ghi tệp thông qua vị trí hiện tại và trạng thái mở/đóng. [API] |
| `Đường Dẫn` | Path | Biểu diễn đường dẫn, nối, tìm tên/cha, kiểm tra tồn tại. [API] |
| `Bộ Ghi Nhật Ký` | Logger | Ghi nhật ký theo cấp `thông tin`, `cảnh báo`, `lỗi`. [API] |
| `Bộ Phát Sự Kiện` | Event Emitter | Đăng ký người nghe, phát và hủy sự kiện. [API] |
| `Bộ Nạp Dịch Vụ` | Service Registry / Loader | Đăng ký, tìm và tải dịch vụ. [API] |
| `Luồng Truy Vấn` | Query Pipeline / Stream | Ánh xạ, lọc, giới hạn, loại trùng và gom dữ liệu. [API] |
| `Cấu Hình Tệp` | File Configuration | Nạp lại và truy vấn giá trị cấu hình theo đường dẫn. [API] |
| `Khách HTTP` | HTTP Client | Gửi yêu cầu HTTP: `lấy` (GET), `gửi` (POST), `cập nhật` (PUT), `xóa` (DELETE). [API] |
| `Ổ Cắm TCP` | TCP Socket | Kết nối, gửi/nhận, đặt thời gian chờ, đóng socket. [API] |
| `Kết Nối Cơ Sở Dữ Liệu` | Database Connection | Quản lý cấu hình kết nối và truy vấn dữ liệu. [API] |
| `Bộ Phân Trang` | Paginator | Tính trang, kích thước và độ dời (offset). [API] |
| `Lệnh Tiến Trình` | Process Command | Cấu hình argv, môi trường, thời hạn rồi chạy tiến trình. [API] |
| `Bộ Bấm Giờ` | Stopwatch | Đo khoảng thời gian bắt đầu–dừng theo mili giây. [API] |
| `Đóng Được` | Closeable | Giao diện đối tượng có phương thức `đóng()`. [API] |
| `Vòng Đời Ứng Dụng` | Application Lifecycle | Hợp đồng chạy/dừng ứng dụng. [API] |
| `Bộ Điều Khiển Ứng Dụng` | Application Controller | Giữ tên, phiên bản và trạng thái vòng đời ứng dụng. [API] |
| `Ca Kiểm Thử` | Test Case | Bao gói phép thử, bước thiết lập và dọn dẹp. [API] |
| `Bộ Kiểm Thử` | Test Runner / Test Suite | Đăng ký, chạy nhiều ca kiểm thử và tập hợp báo cáo. [API] |

## 7. Dự án, gói phụ thuộc và công cụ phát triển

| Tiếng Việt chuẩn hóa | English | Ý nghĩa / ví dụ |
| --- | --- | --- |
| dự án | project | Tập mã nguồn, gói, cấu hình, lệnh dựng/kiểm thử. [Kỹ thuật] |
| gói | package | Đơn vị phân phối thư viện hoặc ứng dụng; có thể chứa nhiều mô-đun. [Kỹ thuật] |
| tệp kê khai | manifest | `vpp.json` khai báo tên, phiên bản và phụ thuộc. [Kỹ thuật] |
| tệp khóa phụ thuộc | dependency lockfile | `vpp.lock` cố định phiên bản/revision và fingerprint phụ thuộc. [Kỹ thuật] |
| phụ thuộc | dependency | Gói hoặc mô-đun cần để biên dịch/chạy một thành phần. [Kỹ thuật] |
| đồ thị phụ thuộc | dependency graph | Quan hệ các gói/mô-đun phụ thuộc vào nhau. [Kỹ thuật] |
| bộ giải phụ thuộc | dependency resolver | Tìm nguồn gói/mô-đun và giải quyết ưu tiên phiên bản/đường dẫn. [Kỹ thuật] |
| kho đăng ký gói | package registry | Nơi công bố, lưu và tìm các phiên bản gói. [Kỹ thuật] |
| phiên bản ngữ nghĩa | semantic versioning (SemVer) | Quy tắc phiên bản `major.minor.patch` và khoảng phiên bản. [Kỹ thuật] |
| dấu vân tay nội dung | content fingerprint | Giá trị dùng phát hiện gói đã thay đổi, **không tự đồng nghĩa** chữ ký an toàn mật mã. [Kỹ thuật] |
| chế độ ngoại tuyến | offline mode | Dùng bộ nhớ đệm mà không tải từ nguồn trực tuyến. [Kỹ thuật] |
| bộ nhớ đệm | cache | Dữ liệu trung gian để dùng lại khi điều kiện phù hợp. [Kỹ thuật] |
| giao diện dòng lệnh | command-line interface (CLI) | Công cụ `vpp` nhận lệnh trong terminal. [Kỹ thuật] |
| vòng lặp đọc–đánh giá–in | read–eval–print loop (REPL) | Chế độ tương tác nhập và chạy các đoạn lệnh. [Kỹ thuật] |
| máy chủ ngôn ngữ | language server / LSP | Cung cấp gợi ý, lỗi, đổi tên, chuyển đến định nghĩa cho trình soạn thảo. [Kỹ thuật] |
| bộ định dạng mã | code formatter | Chuẩn hóa khoảng trắng/cách trình bày nguồn. [Kỹ thuật] |
| bộ soát lỗi tĩnh | linter | Kiểm tra quy tắc mã và cảnh báo không cần chạy chương trình. [Kỹ thuật] |
| thông báo chẩn đoán | diagnostic | Thông tin lỗi/cảnh báo kèm tệp, dòng, cột. [Kỹ thuật] |
| giải mã lệnh | disassembly | Hiển thị các chỉ thị trong bytecode hoặc mã máy để phân tích. [Kỹ thuật] |
| kiểm thử hồi quy | regression test | Kiểm tra lỗi cũ không quay lại sau thay đổi. [Kỹ thuật] |
| kiểm thử nhanh | smoke test | Phép thử ngắn chứng minh hành vi chính hoạt động. [Kỹ thuật] |
| đối chiếu tương đương | parity test | So hai đường triển khai (C++/V++, interpreter/native...) cho kết quả tương ứng. [Kỹ thuật] |
| tích hợp liên tục | continuous integration (CI) | Tự động dựng và kiểm thử khi thay đổi mã nguồn. [Kỹ thuật] |
| phân phối liên tục | continuous delivery/deployment (CD) | Chuẩn bị hoặc phát hành phiên bản dựa trên kết quả kiểm thử. [Kỹ thuật] |
| quy trình dựng | build pipeline | Chuỗi bước chuyển nguồn thành artifact có thể kiểm tra/phát hành. [Kỹ thuật] |

### 7.1. Các lệnh `vpp` đang dùng

| Lệnh V++ | English action | Chức năng |
| --- | --- | --- |
| `vpp giúp đỡ` | help | Hiện hướng dẫn lệnh. |
| `vpp phiên bản` | version | Hiện phiên bản trình biên dịch/bộ công cụ. |
| `vpp chẩn đoán` | doctor / diagnose | Kiểm tra môi trường cài đặt. |
| `vpp nơi` | location / where | Hiện thông tin vị trí cài đặt. |
| `vpp thống kê` | statistics | Hiện thống kê được CLI hỗ trợ. |
| `vpp chạy app.vi` | run | Chạy chương trình nguồn. |
| `vpp dựng app.vi` | build / compile | Chạy pipeline compiler và verifier; **không mặc định phát hành tệp `.vbc`**. |
| `vpp khởi tạo ứng dụng tên` | initialize app / scaffold | Tạo bộ khung dự án ứng dụng. |
| `vpp kiểm thử tests` | test | Tìm và chạy tệp kiểm thử V++. |
| `vpp --soát-lỗi src/` | lint | Phân tích cảnh báo/lỗi tĩnh. |
| `vpp --định-dạng src/` | format | Định dạng nguồn. |
| `vpp --dump-ast app.vi` | dump AST | In cây cú pháp để phân tích. |
| `vpp --dump-ir app.vi` | dump IR | In IR sau optimizer. |
| `vpp --giải-mã app.vi` | disassemble | Hiển thị lệnh bytecode. |
| `vpp --repl` | interactive shell | Vào chế độ lập trình tương tác. |
| `vpp --lsp` | language server | Chạy dịch vụ hỗ trợ IDE. |
| `vpp gói thêm ...` | add dependency | Thêm nguồn phụ thuộc. |
| `vpp gói cài đặt ...` | install package | Cài phụ thuộc. |
| `vpp gói đồng bộ` | synchronize packages | Đồng bộ trạng thái gói. |
| `vpp gói cập nhật` | update packages | Cập nhật gói đã cài. |
| `vpp gói khóa` | lock dependencies | Tạo/cập nhật `vpp.lock`. |
| `vpp gói phục hồi` | restore packages | Phục hồi phụ thuộc theo lockfile. |
| `vpp gói phát hành ...` | publish package | Đưa phiên bản gói vào registry. |

## 8. Những cặp dễ dịch nhầm: quy ước nên thống nhất

| Thuật ngữ | Dùng cách dịch nào? | Vì sao |
| --- | --- | --- |
| `compile` / `build` | **biên dịch** / **dựng** | Biên dịch biến đổi chương trình; dựng là cả quy trình tạo/kiểm tra đầu ra, có thể gồm nhiều bước. |
| `interpreter` / `compiler` | **bộ thông dịch** / **bộ biên dịch** | Một bên thực thi theo từng lệnh; bên kia tạo dạng trung gian hoặc mã đích. |
| `parse` / `lex` | **phân tích cú pháp** / **tách từ vựng** | Parser làm việc với cấu trúc; lexer nhận dạng token. |
| `IR` / `bytecode` / `machine code` | **biểu diễn trung gian** / **mã lệnh trung gian** / **mã máy** | Ba dạng biểu diễn ở các tầng xử lý khác nhau. |
| `lower` / `generate` / `link` | **hạ biểu diễn** / **sinh mã** / **liên kết** | Ba công đoạn khác nhau của trình biên dịch. |
| `class` / `type` / `instance` | **lớp** / **kiểu** / **thể hiện (đối tượng)** | Một lớp mô tả cách tạo instance; kiểu là phạm trù rộng hơn lớp. |
| `function` / `method` | **hàm** / **phương thức** | Phương thức là hàm gắn với lớp/đối tượng. |
| `interface` / `user interface` | **giao diện lập trình (hợp đồng)** / **giao diện người dùng** | `giao diện` trong mã V++ là interface OOP, không phải màn hình ứng dụng. |
| `object` / `object file` | **đối tượng** / **tệp đối tượng** | Đối tượng OOP khác với object do assembler/compiler phát ra. |
| `thread` / `stream` / `pipeline` | **luồng xử lý** / **luồng dữ liệu** / **chuỗi xử lý** | Tránh dùng mỗi từ “luồng” cho ba cơ chế không giống nhau. |
| `scope` / `visibility` | **phạm vi tên** / **quyền truy cập** | Scope cho biết tên có thể được tham chiếu ở đâu; visibility kiểm soát ai được dùng API. |
| `module` / `package` / `library` | **mô-đun** / **gói** / **thư viện** | Mô-đun là đơn vị nguồn; gói để phân phối; thư viện cung cấp chức năng tái sử dụng. |
| `error` / `exception` / `diagnostic` | **lỗi** / **ngoại lệ** / **thông báo chẩn đoán** | Lỗi là khái niệm chung; ngoại lệ có thể ném/bắt; diagnostic là bản tin compiler/tooling. |
| `native` / `self-hosting` | **bản địa** / **tự biên dịch** | Native nói đến mã máy đích; self-host nói đến ngôn ngữ dùng để viết compiler. |
| `artifact` / `asset` | **sản phẩm biên dịch** / **tài nguyên** | Tránh dùng một từ “tệp” cho mọi kết quả build hoặc asset. |
| `security capability` / `OS permission` | **quyền khả năng** / **quyền hệ điều hành** | Capability là quyền được runtime cấp có giới hạn, không mặc nhiên thay quyền OS. |

**Nguyên tắc đặt tên mới:** Ưu tiên từ tiếng Việt có nghĩa kỹ thuật rõ ràng,
ngắn và không mơ hồ; giữ nguyên tên chuẩn quốc tế khi cần trao đổi ABI/giao thức
hoặc định dạng (`JSON`, `HTTP`, `TLS`, `DNS`, `AST`, `IR`, `ELF`...).
Không dịch cơ học nhãn dữ liệu hoặc tên API đã công khai nếu việc đổi tên
phá vỡ chương trình cũ. Có thể dùng dạng **“tiếng Việt (English)”** trong
lần xuất hiện đầu tiên của một thuật ngữ ở tài liệu phổ thông.

## 9. Ví dụ sử dụng thuật ngữ

### 9.1. Cú pháp điều kiện, lặp và hàm

```vi
hàm cộng(a, b = 0) {
    trả về a + b;
};

hàm chính() {
    lặp(i = 0; i < 3; i++) {
        nếu (i == 1) {
            in "Một";
        } hoặc {
            in cộng(i, 10);
        };
    };
};
```

Thuật ngữ: *function* = hàm; *default parameter* = tham số mặc định;
*return* = trả về; *loop* = vòng lặp; *if/else* = nếu/hoặc.

### 9.2. Lớp, giao diện và thừa kế

```vi
giao diện CóTên {
    hàm tên();
}

lớp SảnPhẩm triển khai CóTên {
    hàm khởi tạo(tên) {
        mình.tênSảnPhẩm = tên;
    };

    hàm công khai tên() {
        trả về mình.tênSảnPhẩm;
    };
}

hàm chính() {
    món = SảnPhẩm("Cà phê");
    in món.tên();
};
```

Thuật ngữ: *interface* = giao diện; *class* = lớp; *implements* =
triển khai; *constructor* = phương thức khởi tạo; *self/this* = `mình`.

### 9.3. Đọc API thư viện

```vi
nhập gói/bộ sưu tập/chính;

hàm chính() {
    ngăn = Ngăn Xếp();
    ngăn.đẩy(42);
    in ngăn.rút();
};
```

Thuật ngữ: *import package* = nhập gói; *stack* = ngăn xếp;
*push* = đẩy; *pop* = rút.

## 10. Nguồn đối chiếu và bảo trì tài liệu

Đã rà soát **cây làm việc V++ tại 24/10/2026**, ưu tiên các nguồn sau trong
repository `winbiru/VXX`:

1. `docs/language-reference.md` — cú pháp, OOP, FFI và bảng API chuẩn.
2. `docs/semantics.md` — scope, truthiness, equality, closure và module.
3. `src/frontend/keywords.cpp` — ánh xạ từ khóa/opcode; có thể chứa alias cũ.
4. `docs/cli.md` và `docs/package-system.md` — lệnh CLI, manifest, lockfile.
5. `docs/architecture.md` và `docs/bytecode.md` — kiến trúc compiler/VM.
6. `docs/kien-truc-oop-thu-vien-va-bien-dich.md` — tên lớp và cấu trúc thư viện.
7. `docs/compiler-self-hosting-status.md` và `docs/native-boundary-audit.md` — thuật ngữ self-host, ABI, Machine Intrinsics, System.
8. Thư mục `gói/` và các tệp nguồn `.vi` — tên gói/API có thể đối chiếu trực tiếp.

Khi đổi ngôn ngữ ở các bản tiếp theo:

1. Xác minh cách viết từ khóa bằng **compiler + bài kiểm thử `.vi`**, cập nhật cột “Cú pháp”.
2. Xác minh tên lớp/hàm bằng **khai báo công khai thực tế**, cập nhật cột “API”.
3. Ghi rõ alias, tên cũ và thay đổi không tương thích; đừng tự động xem thuật ngữ dịch là keyword.
4. Cập nhật ngày rà soát và tài liệu tham khảo tương ứng.

**Lưu ý về phạm vi kiểm chứng:** Đây là từ điển thuật ngữ dựa trên tài liệu
và nguồn đã đọc, **không phải báo cáo kiểm thử hay cam kết** mọi backend,
gói, API hoặc tính năng được nêu đều đã hoàn tất trên mọi nền tảng.
