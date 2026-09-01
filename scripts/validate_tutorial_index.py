#!/usr/bin/env python3
"""Validate that completed HTML tutorials are indexed and minimally accessible."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
TUTORIAL_PATTERN = "daily-artifacts/day-[0-9][0-9]/recap.html"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.has_language = False
        self.has_viewport = False
        self.has_h1 = False
        self.in_title = False
        self.title_parts: list[str] = []
        self.links: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "html" and values.get("lang", "").strip():
            self.has_language = True
        elif tag == "meta" and values.get("name", "").lower() == "viewport":
            self.has_viewport = bool(values.get("content", "").strip())
        elif tag == "h1":
            self.has_h1 = True
        elif tag == "title":
            self.in_title = True
        elif tag == "a" and values.get("href"):
            self.links.add(values["href"].split("#", 1)[0])

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)

    @property
    def has_title(self) -> bool:
        return bool("".join(self.title_parts).strip())


def parse(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def main() -> int:
    errors: list[str] = []
    if not INDEX.is_file():
        print("ERROR: index.html does not exist", file=sys.stderr)
        return 1

    index_parser = parse(INDEX)
    tutorials = sorted(ROOT.glob(TUTORIAL_PATTERN))
    if not tutorials:
        errors.append("no completed tutorial recap pages were found")

    for tutorial in tutorials:
        relative = tutorial.relative_to(ROOT).as_posix()
        if relative not in index_parser.links:
            errors.append(f"{relative} is not linked from index.html")

        page = parse(tutorial)
        checks = {
            "document language": page.has_language,
            "non-empty title": page.has_title,
            "viewport meta tag": page.has_viewport,
            "h1 heading": page.has_h1,
        }
        for label, passed in checks.items():
            if not passed:
                errors.append(f"{relative} is missing {label}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(tutorials)} indexed tutorial page(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
