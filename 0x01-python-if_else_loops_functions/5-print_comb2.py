#!/usr/bin/python3
for numbers in range(1, 100):
    if numbers < 10:
        numbers = "{0:02d}".format(numbers)

    if numbers == 99:
        print(numbers)

    else:
        print("{}".format(numbers), end=", ")
