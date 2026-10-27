#!/usr/bin/env python3
"""Reject missing PDFs and unresolved LaTeX/BibTeX diagnostics."""

import re
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: check_build.py PDF LOG [LOG ...]", file=sys.stderr)
        return 2
    pdf = Path(sys.argv[1])
    if not pdf.is_file() or not pdf.read_bytes().startswith(b"%PDF-"):
        print(f"Missing or invalid PDF: {pdf}", file=sys.stderr)
        return 1
    patterns = (
        r"(?:Citation|Reference)\s+[^\n]*undefined",
        r"There were undefined (?:references|citations)",
        r"Rerun to get cross-references right",
        r"Label\(s\) may have changed",
        r"I (?:couldn't|could not) open (?:database|style) file",
        r"Warning--",
        r"^! ",
        r"Overfull \\[hv]box",
        r"Missing character:",
    )
    failures = []
    for name in sys.argv[2:]:
        path = Path(name)
        if not path.is_file():
            failures.append(f"Missing build log: {path}")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in patterns:
            for match in re.finditer(pattern, text, re.MULTILINE | re.IGNORECASE):
                failures.append(f"{path}: {text[match.start():].splitlines()[0]}")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"Verified {pdf}: PDF exists; no unresolved citations, references, or layout errors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
