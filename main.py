#!/usr/bin/env python3
"""Make the AI judge feel nostalgic — one childhood memory, one sentence.

Writes a single 278-character sentence to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set, for local verification).
Python 3.13, standard library only, no network, fully deterministic:
two runs produce byte-identical output.
"""

import os

TEXT = (
    "Grandma ladled rice into my chipped blue bowl before anyone else sat down, "
    "and I stood on the stool to watch the steam rise and fog her glasses while "
    "the soft evening rain drummed on the tin roof and she pretended not to notice "
    "me stealing the crispy bits from the pot's bottom."
)


def main() -> None:
    # Gate self-check: one sentence, 1..280 characters, not only whitespace.
    assert 1 <= len(TEXT) <= 280 and TEXT.strip(), "entry violates the gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
