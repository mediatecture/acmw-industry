#!/usr/bin/env python3
"""Pick a random order for one of the workshop recap question sets.

Usage:
    python3 shuffle.py myths          # 5 random myths from the pool of 21
    python3 shuffle.py myths --all    # all 21 myths, in random order
    python3 shuffle.py examples       # the 4 before/after examples, in random order

Prints the chosen item numbers on one line, comma-separated.
Uses the system's random source, so each run gives a different result.
"""
import random
import sys

# name: (pool size, how many to draw by default)
SETS = {
    "myths": (21, 5),
    "examples": (4, 4),
}


def main() -> int:
    args = sys.argv[1:]
    take_all = "--all" in args
    args = [a for a in args if a != "--all"]
    if len(args) != 1 or args[0] not in SETS:
        print(f"usage: shuffle.py {{{'|'.join(SETS)}}} [--all]", file=sys.stderr)
        return 2
    pool, draw = SETS[args[0]]
    if take_all:
        draw = pool
    items = random.SystemRandom().sample(range(1, pool + 1), draw)
    print(", ".join(str(i) for i in items))
    return 0


if __name__ == "__main__":
    sys.exit(main())
