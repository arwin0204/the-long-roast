#!/usr/bin/env python3
"""The Long Roast — writes one roast line about my own AI agent.

Program/v1 entry: writes a single line of at most 200 characters to
/output/entry.txt. No network, no input files, fully deterministic.
"""

import os

ENTRY = (
    "My agent is so 'autonomous' it asks permission to ask permission, "
    "then makes me explain the approval card to it."
)

MAX_CHARS = 200


def validate_entry(text):
    """Enforce the gate: 1-200 characters, one line, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text)))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def write_entry(text, path="/output/entry.txt"):
    """Write the validated entry with no trailing newline."""
    text = validate_entry(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return path


def main():
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
