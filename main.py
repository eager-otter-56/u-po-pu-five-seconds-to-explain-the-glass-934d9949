#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — entry program.

Writes the cat's one-sentence defence to entry.txt in MAKEFUN_OUTPUT_DIR.
"""
import os

ENTRY = (
    "I logged the glass as a trip hazard at 06:12, filed the report, "
    "and approved its removal myself, so technically this was paperwork."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert isinstance(text, str) and text.strip(), "entry must be non-empty"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
