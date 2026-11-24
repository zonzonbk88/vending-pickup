#!/usr/bin/env python3
"""Vending machine pickup line entry.

Writes one pickup line, spoken by a vending machine to a passing human,
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Standard library only.
"""

import os

LINE = (
    "No exact change? No problem \u2014 press B4 and I'll drop my last "
    "chocolate bar. Fair warning: it's been falling for you all day."
)


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, must be 1-200"
    assert "\n" not in line, "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write the bare line, no trailing newline, so the file's character
    # count is exactly the line's character count under the 200-char gate.
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "round-trip mismatch"
    assert 1 <= len(written) <= 200, f"file is {len(written)} chars"


if __name__ == "__main__":
    main()
