#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes the battery's final one-line text to its charger into
entry.txt. The text itself is assembled by build_line(); a separate
validator guards the judge's 1-200 character, single-line gate.
"""

import os
from pathlib import Path

MAX_CHARS = 200


def build_line():
    """Assemble the entry line from its three narrative parts."""
    parts = [
        "I waited all day at 1%, dimmed myself and closed all my apps for you, ",
        "and you show up with a frayed cable. I'm done \u2014 the power bank ",
        "charges me and actually texts back.",
    ]
    line = "".join(parts)
    if any(ch in line for ch in ("\n", "\r")):
        raise ValueError("assembled entry must not contain a line break")
    return line


def ensure_valid(line):
    """Raise unless line passes the judge's length gate (1-200 chars)."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry length {len(line)} is outside 1-{MAX_CHARS}")
    return line


def write_output(line):
    """Write the validated line to entry.txt in the output directory."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(line, encoding="utf-8")
    return target


def main():
    line = ensure_valid(build_line())
    target = write_output(line)
    print(f"wrote {len(line)} characters to {target}")


if __name__ == "__main__":
    main()
