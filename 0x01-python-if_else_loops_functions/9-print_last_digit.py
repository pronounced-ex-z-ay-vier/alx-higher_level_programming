#!/usr/bin/python3
def print_last_digit(number):
    digits = number % 10
    if number > 0:
        digits = number % 10
    if number < 0:
        digits = (number * -1) % 10
    print("{}".format(digits), end="")
    return (digits)
