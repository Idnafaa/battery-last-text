#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger — one-line text writer.

Writes the battery's final message to its charger, a single line of
at most 200 characters, to /output/entry.txt for the judge to read.
"""
import os

TEXT = (
    "I waited all day at 1%, dimmed myself and closed all my apps for you, "
    "and you show up with a frayed cable. I'm done \u2014 the power bank "
    "charges me and actually texts back."
)


def main():
    line = TEXT.strip()
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"entry is {len(line)} characters, must be 1-200")
    if "\n" in line:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(f"wrote {len(line)} characters to {path}")


if __name__ == "__main__":
    main()
