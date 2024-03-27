#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# last-n is last number
last_n = number % 10
# if number is less than 10 condition
# to find last-n: number * -1 to convert to absolute number and %10 for REM
# then reconvert to minus
if number < 0:
    last_n = (number * -1) % 10
    last_n = last_n * -1

if last_n > 5:
    print(f"Last digit of {number} is {last_n} and is greater than 5")
elif last_n == 0:
    print(f"Last digit of {number} is {last_n} and is 0")
else:
    print(f"Last digit of {number} is {last_n} and is less than 6 and not 0")
