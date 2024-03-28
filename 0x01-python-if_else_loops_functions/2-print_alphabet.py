m!/usr/bin/python3
# Program print ASCII alphabet in lowercase, not followed by a new line.

for lower in range(97, 123):
    if lower < 123:
        print("{}".format(chr(lower)), end="")
