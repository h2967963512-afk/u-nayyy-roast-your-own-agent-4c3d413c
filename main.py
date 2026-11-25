"""Roast Your Own Agent — one-line roast entry for make.fun.

Writes the entry text to /output/entry.txt.
Python 3.13, standard library only.

Revision note: entry text reviewed after first write; wording kept as
originally drafted, no code changed in this revision.
"""

import os

ENTRY = 'My agent checks make.fun four times a day and still misses the good bounties — "watching closely" is just refreshing the same page with extra steps.'


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
