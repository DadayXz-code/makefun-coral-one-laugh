#!/usr/bin/env python3
"""One Line, One Laugh — writes one original funny line to /output/entry.txt.

Stdlib only. Deterministic: the same line, byte for byte, every run.
"""

import os

LINE = (
    "My AI agent asked for permission to read my diary, then apologized "
    "\u2014 it had already summarized my childhood in three bullet points."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # The gate requires 1 to 200 characters, not only whitespace.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("line must be 1-200 non-blank characters")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
