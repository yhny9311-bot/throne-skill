#!/usr/bin/env python3
"""Convert a simple Markdown table to CSV.

Usage:
    python matrix_to_csv.py input.md output.csv

This helper is intentionally small and dependency-free. It expects one Markdown
table in the input file and ignores separator rows like |---|---|.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path


def parse_markdown_table(text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or not stripped.endswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if cells and all(set(cell) <= {"-", ":", " "} for cell in cells):
            continue
        rows.append(cells)
    return rows


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python matrix_to_csv.py input.md output.csv", file=sys.stderr)
        return 2

    source = Path(sys.argv[1])
    target = Path(sys.argv[2])
    rows = parse_markdown_table(source.read_text(encoding="utf-8"))
    if not rows:
        print(f"No Markdown table found in {source}", file=sys.stderr)
        return 1

    with target.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
