"""Kiểm tra dữ liệu và các tệp được sinh tự động của kho K12."""

import json
import re
import unicodedata
import unittest
from pathlib import Path

from tao_tai_lieu import ROOT, render, validate
from tra_cuu import CAP, fold, load_entries, search


class K12Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "du-lieu.json").read_text(encoding="utf-8"))

    def test_all_subjects_and_levels_have_terms(self):
        self.assertGreaterEqual(len(self.data["subjects"]), 23)
        self.assertGreaterEqual(validate(self.data), 1400)
        for subject in self.data["subjects"]:
            self.assertEqual(set(subject["levels"]), set(CAP.values()))
            for terms in subject["levels"].values():
                self.assertGreaterEqual(len(terms), 10)

    def test_generated_files_match_source(self):
        rendered, n = render(self.data)
        self.assertGreaterEqual(n, 1400)
        for path, expected in rendered.items():
            with self.subTest(path=str(path.relative_to(ROOT))):
                self.assertEqual(path.read_text(encoding="utf-8"), expected)

    def test_jsonl_corresponds_to_source(self):
        entries = list(load_entries())
        rows = [json.loads(line) for line in (ROOT / "tu-dien.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual(len(entries), len(rows))
        for actual, expected in zip(rows, entries):
            self.assertEqual({key: expected[key] for key in actual}, actual)

    def test_internal_markdown_links(self):
        markdowns = [ROOT.parent / "README.md", *ROOT.rglob("*.md")]
        for markdown in markdowns:
            content = markdown.read_text(encoding="utf-8")
            for label, link in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content):
                if "://" in link or link.startswith("#"):
                    continue
                target = (markdown.parent / link.split("#")[0]).resolve()
                with self.subTest(file=markdown.name, label=label):
                    self.assertTrue(target.is_file(), str(target))

    def test_accent_insensitive_search(self):
        entries = list(load_entries())
        math = search(entries, "dao ham", subject="toan-hoc", exact=True)
        self.assertEqual(len(math), 1)
        self.assertEqual(math[0]["tieng_viet"], "đạo hàm")
        biology = search(entries, "photosynthesis", subject="sinh-hoc", exact=True)
        self.assertEqual(len(biology), 1)
        self.assertEqual(biology[0]["tieng_viet"], "quang hợp")
        self.assertEqual(search(entries, "dao ham", subject="hoa-hoc", exact=True), [])
        self.assertTrue(search(entries, "lực", level=CAP["thcs"]))

    def test_duplicate_with_decomposed_unicode_is_rejected(self):
        small = json.loads(json.dumps(self.data["subjects"][0], ensure_ascii=False))
        original = small["levels"]["01-tieu-hoc"][0]
        small["levels"]["01-tieu-hoc"].append([
            unicodedata.normalize("NFD", original[0]), "different", "Trùng theo Unicode.",
        ])
        with self.assertRaisesRegex(ValueError, "Trùng thuật ngữ"):
            validate({"schema": 1, "subjects": [small]})

    def test_search_normalization(self):
        self.assertEqual(fold("ĐiỆn   trƯỜng"), fold("dien truong"))


if __name__ == "__main__":
    unittest.main()
