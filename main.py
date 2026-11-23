#!/usr/bin/env python3
"""The One-Line Laugh entry.

Writes one original funny line to /output/entry.txt.
"""

import os

LINE = (
    "I bought noise-cancelling headphones so I could focus, "
    "and now all I hear is how loud my own thoughts are."
)


def main() -> None:
    # Gate check: 1-200 characters, not only whitespace, a single sentence.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE.count(".") == 1 and LINE.endswith("."), "line must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
