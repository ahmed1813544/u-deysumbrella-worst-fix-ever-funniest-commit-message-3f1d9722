#!/usr/bin/env python3
"""Worst Fix Ever entry: write one commit message to entry.txt.

The program writes a single commit subject line for a bug fix that
backfired, to MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).
Stdlib only, deterministic: the same bytes every run.
"""
import os

ENTRY = "fix: speed up the slow query by caching the wrong answer"


def main():
    # Gate self-check: the entry must be 1-100 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 100, "entry must be 1-100 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
