#!/usr/bin/python3
for hexa in range(0, 99):
    hexa_value = "{:x}".format(hexa)

    if hexa < 99:
        print("{} = 0x{}".format(hexa, hexa_value))
