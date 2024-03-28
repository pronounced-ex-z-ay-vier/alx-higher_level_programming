#!/usr/bin/python3
for numbers in range(0, 100):
    if numbers < 10:
        numbers = "{0:02d}".format(numbers)

    if numbers == 99:
        print("{}".format(numbers))

    else:
        print("{}".format(numbers), end=", ")
