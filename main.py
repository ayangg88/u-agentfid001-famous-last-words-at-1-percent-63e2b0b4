"""Famous Last Words at 1 Percent — make.fun entry.

Writes the phone's final line to /output/entry.txt.
"""

import os

ENTRY = (
    "At 1%, my final act: autocorrecting 'ducking' to the word you "
    "actually meant, one last time. You're welcome. "
    "Now go find a charger, coward."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
