#!/usr/bin/python3
for comb in range(0, 10):
    for comb2 in range(comb, 10):
        if comb == 8 and comb2 == 9:
            print("{}{}".format(comb, comb2))
        if comb != comb2:
            print("{}{}".format(comb, comb2), end=", ")
        pass
