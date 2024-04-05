#!/usr/bin/python3

def print_in_reverse():
    for c in range(122, 96, -1):
        if c <= 122:
            if c % 2 != 0:
                c = c - 32
        print("{}".format(chr(c)), end="")


print_in_reverse()
