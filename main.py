#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes one single-line tombstone epitaph of famous last words to the
entry output. The gate requires UTF-8 text of 1 to 150 characters, not
only whitespace; the entry is deterministic and byte-identical on every
run.
"""

import os
import sys

ENTRY = "I died doing what I loved: avoiding my responsibilities."

MAX_CHARS = 150


def validate_epitaph(text: str) -> str | None:
    """Return an error message if the epitaph breaks the gate, else None."""
    if not (1 <= len(text) <= MAX_CHARS):
        return f"entry length {len(text)} outside 1..{MAX_CHARS}"
    if not text.strip():
        return "entry is only whitespace"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    return None


def resolve_output_path() -> str:
    """ENTRY_OUT (file) wins, then ENTRY_OUT_DIR/entry.txt, then default."""
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        return entry_out
    entry_out_dir = os.environ.get("ENTRY_OUT_DIR")
    if entry_out_dir:
        return os.path.join(entry_out_dir, "entry.txt")
    return "/output/entry.txt"


def main() -> int:
    epitaph = ENTRY
    problem = validate_epitaph(epitaph)
    if problem is not None:
        print(problem, file=sys.stderr)
        return 1
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(epitaph)
    print(epitaph)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
