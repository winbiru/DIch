#!/usr/bin/env python3
"""Tạo từ điển K12 dạng Markdown/JSONL từ dữ liệu nguồn JSON.

Chạy: python3 K12/tao_tai_lieu.py [--check]
"""

import argparse
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LEVELS = (
    ("01-tieu-hoc", "Tiểu học (lớp 1–5)"),
    ("02-trung-hoc-co-so", "Trung học cơ sở (lớp 6–9)"),
    ("03-trung-hoc-pho-thong", "Trung học phổ thông (lớp 10–12)"),
)


def safe_cell(value):
    return value.replace("|", "&#124;").replace("\r", " ").replace("\n", " ")


def normalized(value):
    """Dùng Unicode NFC để phát hiện trùng cả khi dấu được nhập tách rời."""
    return " ".join(unicodedata.normalize("NFC", value).casefold().split())


def sort_key(value):
    """Xếp tên mục từ theo chữ cái, không phân biệt dấu và chữ hoa."""
    plain = unicodedata.normalize("NFD", value.replace("đ", "d").replace("Đ", "D"))
    return "".join(c for c in plain if not unicodedata.combining(c)).casefold()


def validate(data):
    if not isinstance(data, dict) or data.get("schema") != 1 or not isinstance(data.get("subjects"), list) or not data["subjects"]:
        raise ValueError("Dữ liệu cần schema=1 và danh sách subjects")
    ids = set()
    total = 0
    for subject in data["subjects"]:
        if not isinstance(subject, dict):
            raise ValueError("Mỗi môn phải là đối tượng JSON")
        identifier = subject.get("id")
        if not isinstance(identifier, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", identifier):
            raise ValueError(f"Mã môn không hợp lệ: {identifier}")
        if identifier in ids:
            raise ValueError(f"Trùng mã môn: {identifier}")
        ids.add(identifier)
        for field in ("vi", "en", "description"):
            if not isinstance(subject.get(field), str) or not subject[field].strip():
                raise ValueError(f"Môn {identifier} thiếu {field}")
        if not isinstance(subject.get("levels"), dict) or set(subject["levels"]) != {level for level, _ in LEVELS}:
            raise ValueError(f"Môn {identifier} phải có đủ ba cấp học")
        seen = set()
        for level, _ in LEVELS:
            rows = subject["levels"][level]
            if not isinstance(rows, list) or not rows:
                raise ValueError(f"Môn {identifier}, cấp {level} không có thuật ngữ")
            for row in rows:
                if not isinstance(row, list) or len(row) != 3 or not all(
                    isinstance(value, str) and value.strip() for value in row
                ):
                    raise ValueError(f"Thuật ngữ sai định dạng: {identifier} / {level}: {row}")
                term = normalized(row[0])
                if term in seen:
                    raise ValueError(f"Trùng thuật ngữ trong môn {identifier}: {row[0]}")
                seen.add(term)
                total += 1
    return total


def render(data):
    files = {}
    total = validate(data)
    intro = [
        "# Kho thuật ngữ K12 — Việt–Anh",
        "",
        "Bộ từ điển liên môn dành cho học sinh, giáo viên, người dịch thuật và dự án V++.",
        "Các thuật ngữ ưu tiên **tiếng Việt dễ hiểu**, có tên tiếng Anh đối chiếu",
        "và giải nghĩa ngắn; giữ ký hiệu khoa học quốc tế khi phù hợp.",
        "",
        "**Lưu ý về cấp lớp:** Ba nhóm *tiểu học / THCS / THPT* thể hiện độ khó tham khảo,",
        "**không phải phân phối chương trình chính thức**. Các lĩnh vực Vật lý, Hóa học, Sinh học",
        "ở cấp tiểu học được trình bày như kiến thức khoa học tích hợp, không có nghĩa",
        "các môn này được dạy độc lập ở mọi khối lớp. Tên Anh là đối chiếu khái niệm,",
        "không phải từ khóa có thể gõ trực tiếp trong V++.",
        "",
        f"**Quy mô hiện tại:** {len(data['subjects'])} lĩnh vực, {total} mục từ đã biên soạn. Kho được mở rộng dần, chưa phải danh mục đầy đủ của chương trình giáo dục.",
        "",
        "## Danh mục lĩnh vực",
        "",
        "| Lĩnh vực | English | Số mục |",
        "| --- | --- | ---: |",
    ]
    rows_jsonl = []
    index_vi = []
    index_en = []
    english_senses = defaultdict(list)
    for subject in data["subjects"]:
        sid = subject["id"]
        count = sum(len(subject["levels"][key]) for key, _ in LEVELS)
        intro.append(
            f"| [{subject['vi']}]({sid}/README.md) | {subject['en']} | {count} |"
        )
        overview = [
            f"# {subject['vi']} — {subject['en']}",
            "",
            subject["description"],
            "",
            "Các cấp học chỉ là **phân nhóm kiến thức để tra cứu**. Học sinh có thể",
            "gặp một thuật ngữ sớm hoặc muộn hơn tùy chương trình và chủ đề.",
            "",
            "| Cấp học | Số thuật ngữ |",
            "| --- | ---: |",
        ]
        for level, title in LEVELS:
            terms = subject["levels"][level]
            overview.append(f"| [{title}]({level}/tu-dien.md) | {len(terms)} |")
            body = [
                f"# {subject['vi']} — {title}",
                "",
                f"[← Môn {subject['vi']}](../README.md) · [↑ Kho K12](../../README.md)",
                "",
                "| Thuật ngữ tiếng Việt | Thuật ngữ tiếng Anh | Giải nghĩa |",
                "| --- | --- | --- |",
            ]
            for vi, en, meaning in terms:
                body.append(f"| {safe_cell(vi)} | {safe_cell(en)} | {safe_cell(meaning)} |")
                where = f"{sid}/{level}/tu-dien.md"
                index_vi.append((vi, en, subject["vi"], title, where))
                index_en.append((en, vi, subject["vi"], title, where))
                english_senses[normalized(en)].append((vi, subject["vi"], where))
                rows_jsonl.append(
                    json.dumps(
                        {"mon": sid, "mon_vi": subject["vi"], "cap": level,
                         "tieng_viet": vi, "tieng_anh": en, "giai_nghia": meaning},
                        ensure_ascii=False,
                    )
                )
            body.extend(["", "Các thuật ngữ thuộc kho dịch thuật/giáo dục; chưa phải API hoặc cú pháp V++.", ""])
            files[ROOT / sid / level / "tu-dien.md"] = "\n".join(body)
        overview += ["", "[← Toàn bộ lĩnh vực](../README.md)", ""]
        files[ROOT / sid / "README.md"] = "\n".join(overview)
    intro += [
        "",
        "## Sử dụng và mở rộng",
        "",
        "- [Thống kê theo lĩnh vực và cấp học](THONG_KE.md) giúp theo dõi phạm vi đã biên soạn.",
        "- [Tiếng Anh đa nghĩa theo lĩnh vực](TIENG_ANH_DA_NGHIA.md) so sánh cách diễn đạt tiếng Việt tùy ngữ cảnh.",
        "- [Tra theo tiếng Việt](CHI_MUC_VIET_ANH.md) hoặc [tra theo tiếng Anh](CHI_MUC_ANH_VIET.md).",
        "- Chạy `python3 K12/tra_cuu.py \"đạo hàm\"` để tìm tên và giải nghĩa;",
        "  có thể tìm không dấu, lọc môn hoặc xuất JSON.",
        "- Mở `README.md` của từng môn, chọn cấp học để xem bảng từ Việt–Anh.",
        "- [Quy ước biên soạn](QUY_UOC_BIEN_SOAN.md) giải thích cách chọn thuật ngữ",
        "  tiếng Việt và bổ sung mục từ mới.",
        "- [Nguồn đối chiếu và mức độ thẩm định](NGUON_DOI_CHIEU.md) nêu phạm vi",
        "  chương trình và các bước kiểm chứng thuật ngữ trước khi dùng cho giảng dạy.",
        "- [Từ điển V++ nền tảng](../TU_DIEN_THUAT_NGU_VPP_VI_EN.md) trình bày",
        "  thuật ngữ lập trình đã đối chiếu mã nguồn V++; kho K12 là tài liệu mở rộng độc lập.",
        "- `du-lieu.json` là **nguồn chuẩn để chỉnh sửa**; `tu-dien.jsonl` phục vụ",
        "  xử lý máy/dữ liệu huấn luyện khi có giấy phép sử dụng phù hợp.",
        "- Sau khi sửa `du-lieu.json`, chạy `python3 K12/tao_tai_lieu.py` để tái tạo",
        "  tài liệu. Chạy `python3 K12/tao_tai_lieu.py --check` để kiểm tra đồng bộ.",
        "- Khi đưa thuật ngữ vào tài liệu học, nên bổ sung nguồn chương trình/sách",
        "  và kiểm chứng công thức, danh pháp chuyên ngành theo chuẩn đang áp dụng.",
        "- [↑ Trang chủ kho tài liệu](../README.md)",
        "",
    ]
    files[ROOT / "README.md"] = "\n".join(intro)
    files[ROOT / "tu-dien.jsonl"] = "\n".join(rows_jsonl) + "\n"
    summary = [
        "# Thống kê kho thuật ngữ K12", "",
        "[← Kho K12](README.md)", "",
        "Số liệu được sinh trực tiếp từ `du-lieu.json` (số **mục từ theo lĩnh vực**;",
        "cùng khái niệm có thể xuất hiện ở nhiều lĩnh vực với cách diễn giải khác nhau).",
        "Các cấp thể hiện **độ khó tham khảo**, không phải phân phối chính thức.", "",
        "| Lĩnh vực | Tiểu học | THCS | THPT | Tổng |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    level_counts = [0] * len(LEVELS)
    for subject in data["subjects"]:
        counts = [len(subject["levels"][key]) for key, _ in LEVELS]
        level_counts = [a + b for a, b in zip(level_counts, counts)]
        summary.append(
            f"| [{subject['vi']}]({subject['id']}/README.md) | "
            + " | ".join(str(value) for value in counts)
            + f" | {sum(counts)} |"
        )
    summary.append("| **Tổng** | " + " | ".join(f"**{n}**" for n in level_counts) + f" | **{total}** |")
    summary.append("")
    files[ROOT / "THONG_KE.md"] = "\n".join(summary)
    polysemy = [
        "# Thuật ngữ tiếng Anh có nhiều nghĩa theo lĩnh vực", "",
        "[← Kho K12](README.md)", "",
        "Các từ hoặc cụm từ tiếng Anh giống nhau có thể chỉ khái niệm khác nhau tùy ngành.",
        "Bảng dưới đây được sinh tự động từ các mục có **nhiều cách gọi tiếng Việt**",
        "trong kho hiện tại; cần dựa vào ngữ cảnh và định nghĩa để chọn cách dịch.", "",
        "| English | Tiếng Việt | Lĩnh vực |",
        "| --- | --- | --- |",
    ]
    for english, examples in sorted(english_senses.items(), key=lambda item: sort_key(item[0])):
        if len({normalized(example[0]) for example in examples}) < 2:
            continue
        for vi, subject_vi, destination in examples:
            polysemy.append(
                f"| {safe_cell(english)} | {safe_cell(vi)} | [{safe_cell(subject_vi)}]({destination}) |"
            )
    polysemy.append("")
    files[ROOT / "TIENG_ANH_DA_NGHIA.md"] = "\n".join(polysemy)
    for title, entries, first, second, path in (
        ("Chỉ mục Việt → Anh", index_vi, "Tiếng Việt", "English", "CHI_MUC_VIET_ANH.md"),
        ("English → Vietnamese Index", index_en, "English", "Tiếng Việt", "CHI_MUC_ANH_VIET.md"),
    ):
        index = [
            f"# {title}", "",
            f"{len(entries)} mục từ, sắp xếp không phân biệt chữ hoa hoặc dấu; các liên kết dẫn tới bảng thuật ngữ theo cấp học.",
            "", "[← Kho K12](README.md)", "",
            f"| {first} | {second} | Lĩnh vực | Cấp học |",
            "| --- | --- | --- | --- |",
        ]
        for term, translation, subject_name, level_name, destination in sorted(
            entries, key=lambda row: (sort_key(row[0]), sort_key(row[2]), row[3])
        ):
            index.append(
                f"| {safe_cell(term)} | {safe_cell(translation)} | "
                f"[{safe_cell(subject_name)}]({destination}) | {safe_cell(level_name)} |"
            )
        index.append("")
        files[ROOT / path] = "\n".join(index)
    return files, total


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Chỉ kiểm tra tệp đầu ra")
    args = parser.parse_args()
    data = json.loads((ROOT / "du-lieu.json").read_text(encoding="utf-8"))
    files, total = render(data)
    changed = []
    for path, content in files.items():
        if not path.is_file() or path.read_text(encoding="utf-8") != content:
            changed.append(path.relative_to(ROOT).as_posix())
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
    if changed and args.check:
        raise SystemExit("Tài liệu chưa đồng bộ: " + ", ".join(changed))
    print(f"{len(data['subjects'])} môn/lĩnh vực, {total} thuật ngữ; "
          f"{len(changed)} tệp {'cần cập nhật' if args.check else 'đã ghi'}")


if __name__ == "__main__":
    main()
