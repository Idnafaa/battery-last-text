#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

One-line entry writer: composes the battery's final text to its
charger and saves it as a single line in entry.txt for the judge.
"""

import os

ENTRY = (
    "I waited all day at 1%, dimmed myself and closed all my apps for you, "
    "and you show up with a frayed cable. I'm done \u2014 the power bank "
    "charges me and actually texts back."
)


def char_count(text):
    """Return the length of the entry text in characters."""
    return len(text)


def check_entry(text):
    """Reject anything the judge's gate would not accept.

    The gate wants exactly one line of 1-200 characters, so a text
    outside that range or containing a newline is refused outright.
    """
    count = char_count(text)
    if count < 1 or count > 200:
        raise ValueError(
            f"entry must be between 1 and 200 characters, got {count}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line with no newline")
    return text


def save_entry(text, out_dir):
    """Write the validated entry line into entry.txt under out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    line = check_entry(ENTRY)
    path = save_entry(line, out_dir)
    print(f"wrote {char_count(line)} characters to {path}")


if __name__ == "__main__":
    main()
