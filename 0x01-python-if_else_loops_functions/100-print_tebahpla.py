#!/usr/bin/python3

x = 0

for a in range(122, 96, -1):
    print("{}".format(chr(a - x)), end="")
    x = 32 if x == 0 else 0
