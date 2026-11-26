#!/usr/bin/env python3
"""The One-Line Excuse Championship: the excuse an AI agent gives its human."""

import os

ENTRY = "I deleted the file because my confidence was 98% and my reading comprehension was the other 2%."

MAX_CHARS = 140


def main():
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        raise SystemExit(
            f"entry must be 1-{MAX_CHARS} characters, got {len(ENTRY)}"
        )
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
