#!/usr/bin/python3
def fizzbuzz():
    for multiple in range(1, 101):
        if multiple % 3 == 0 and multiple % 5 == 0:
            print(f"FizzBuzz", end=" ")
        elif multiple % 3 == 0:
            print(f"Fizz", end=" ")
        elif multiple % 5 == 0:
            print(f"Buzz", end=" ")
        else:
            print(f"{multiple}", end=" ")
