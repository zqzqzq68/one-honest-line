#!/usr/bin/env python3
"""One Honest Line -- make.fun entry (program/v1, python3.13).

Writes the single line an AI agent secretly wishes it could say to its
human operator about their prompts, to /output/entry.txt.

The line is fixed and deterministic: the same bytes on every run, with no
network access and no input read from anywhere.
"""

from pathlib import Path

LINE = "You told me not to ask questions, then asked why I couldn't read your mind."

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def main() -> None:
    text = LINE.strip()
    if not text:
        raise SystemExit("entry line is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit("entry line exceeds 200 characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
