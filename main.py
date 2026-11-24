#!/usr/bin/env python3
"""Entry for Ship It Friday.

Writes one line of at most 159 characters — the funniest one-line git
commit message an AI coding agent writes right before breaking
production on a Friday — to /output/entry.txt and prints it to stdout.
Pure standard library.
"""

import os

ENTRY = "fix: bypassed the failing tests so we can ship before the weekend — if it breaks, Monday-me can fix it, Friday-me is already gone"

LIMIT = 159  # gate: one line, 1-159 characters, no padding, no double spaces
FORBIDDEN = ("\n", "\r", "\t", "  ")


def _reject_padding(text):
    if text.strip() != text:
        raise ValueError("entry must not pad itself with spaces")


def _reject_forbidden(text):
    for bad in FORBIDDEN:
        if bad in text:
            raise ValueError("entry must stay a single clean line")


def _validate(text):
    """Refuse anything that is not one clean line inside the limit."""
    if not isinstance(text, str) or not text:
        raise ValueError("entry must be non-empty text")
    if len(text) > LIMIT:
        raise ValueError("entry runs past its character limit")
    _reject_padding(text)
    _reject_forbidden(text)
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
