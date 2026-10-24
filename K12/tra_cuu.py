#!/usr/bin/env python3
"""Tra cứu từ điển K12 Việt–Anh, không cần internet hay thư viện ngoài.

Ví dụ:
    python3 K12/tra_cuu.py 'dao ham'
    python3 K12/tra_cuu.py 'photosynthesis' --mon sinh-hoc
    python3 K12/tra_cuu.py 'cell' --cap thcs --json
"""

import argparse
import json
import unicodedata
from pathlib import Path

if __package__:
    from .tao_tai_lieu import LEVELS, validate
else:
    from tao_tai_lieu import LEVELS, validate


ROOT = Path(__file__).resolve().parent
CAP = {
    "tieu-hoc": "01-tieu-hoc",
    "thcs": "02-trung-hoc-co-so",
    "thpt": "03-trung-hoc-pho-thong",
}


def fold(value):
    """Chuẩn hóa tìm kiếm, chấp nhận từ khóa có hoặc không dấu."""
    value = value.casefold().replace("đ", "d")
    value = unicodedata.normalize("NFKD", value)
    return " ".join("".join(ch for ch in value if not unicodedata.combining(ch)).split())


def load_entries(path=None):
    source = ROOT / "du-lieu.json" if path is None else Path(path)
    data = json.loads(source.read_text(encoding="utf-8"))
    validate(data)
    for subject in data["subjects"]:
        for level, title in LEVELS:
            for vi, en, meaning in subject["levels"][level]:
                yield {
                    "mon": subject["id"],
                    "mon_vi": subject["vi"],
                    "cap": level,
                    "cap_vi": title,
                    "tieng_viet": vi,
                    "tieng_anh": en,
                    "giai_nghia": meaning,
                }


def search(entries, query, subject=None, level=None, limit=20, exact=False):
    needle = fold(query)
    if not needle:
        return []
    found = []
    for entry in entries:
        if subject and entry["mon"] != subject:
            continue
        if level and entry["cap"] != level:
            continue
        vi, en, meaning = (fold(entry[key]) for key in ("tieng_viet", "tieng_anh", "giai_nghia"))
        if needle in (vi, en):
            rank = 0
        elif exact:
            continue
        elif vi.startswith(needle) or en.startswith(needle):
            rank = 1
        elif needle in vi or needle in en:
            rank = 2
        elif needle in meaning:
            rank = 3
        else:
            continue
        found.append((rank, vi, entry["mon"], entry))
    found.sort(key=lambda row: (row[0], row[1], row[2]))
    return [row[3] for row in found[:limit]]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Từ/cụm từ Việt hoặc Anh cần tìm; có thể không dấu")
    parser.add_argument("--mon", help="Mã lĩnh vực, ví dụ toan-hoc, tin-hoc")
    parser.add_argument("--cap", choices=CAP, help="Lọc theo cấp học")
    parser.add_argument("--exact", action="store_true", help="Chỉ tìm thuật ngữ trùng chính xác")
    parser.add_argument("--json", action="store_true", help="Xuất kết quả dạng JSON")
    parser.add_argument("--limit", type=int, default=20, help="Số kết quả tối đa, mặc định 20")
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit phải lớn hơn 0")
    entries = list(load_entries())
    subjects = {entry["mon"] for entry in entries}
    if args.mon and args.mon not in subjects:
        parser.error("--mon không hợp lệ; chọn một trong: " + ", ".join(sorted(subjects)))
    results = search(entries, args.query, args.mon, CAP.get(args.cap), args.limit, args.exact)
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for row in results:
            print(f"[{row['mon_vi']} · {row['cap_vi']}] {row['tieng_viet']} ↔ {row['tieng_anh']}")
            print(f"  {row['giai_nghia']}")
        if not results:
            print("Không tìm thấy thuật ngữ phù hợp.")
    return 0 if results else 1


if __name__ == "__main__":
    raise SystemExit(main())
