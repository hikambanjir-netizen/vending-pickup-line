#!/usr/bin/env python3
"""Vending Machine Pickup Line - make.fun entry.

Writes exactly one pickup line to /output/entry.txt.
Pure standard library, Python 3.13.
"""

import os

LINE = "Press B7 and I'll jam my own coil, just so you have to come back and shake me again."


def main():
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 200 chars.
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("pickup line must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    # Exactly the line, nothing else: no trailing newline, no extra text.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
