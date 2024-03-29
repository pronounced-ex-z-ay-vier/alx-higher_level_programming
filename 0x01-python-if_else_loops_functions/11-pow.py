#!/usr/bin/python3
def pow(a, b):
    if b >= 0:
        exponent = 1
        for _ in range(b):
            exponent = exponent * a
    else:
        exponent = 1.0
        for _ in range((b) * -1):
            exponent = exponent / a
    return (exponent)
