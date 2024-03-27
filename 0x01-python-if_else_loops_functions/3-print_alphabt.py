#!/usr/bin/python3
# Program print ASCII alphabet in lowercase, not followed by a new line.
# except q and e

for lower in range(97, 123):
    if lower == 101 or lower == 113:
        continue
    print("{}".format(chr(lower)), end="")
