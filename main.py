#!/usr/bin/env python3
"""Dad Joke Showdown: write one dad joke to /output/entry.txt.

The joke is a short dinner-table exchange a father would actually tell:
he announces a band, his wife doubts it, and the punchline lands on a
single clean pun at the very end. Written fresh for this bounty.
The pun turns on "reheated hits": leftovers, reheated — the band's whole
setlist is yesterday's food, and the joke never says so outright.
"""
import os

JOKE = "I told my wife I'm starting a band called The Leftovers. She said that's not a band. I said, sure it is. We only play reheated hits."
OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp_path = OUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.replace(tmp_path, OUT_PATH)


if __name__ == "__main__":
    main()
