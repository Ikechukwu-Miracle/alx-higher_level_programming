#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""
import sys

size = 0
stat_c = {}
valid_c = ["200", "301", "400", "401", "403", "404", "405", "500"]
c = 0

try:
    for line in sys.stdin:
        if c == 10:
            print(f"File size: {size}")
            for key in sorted(stat_c):
                print(f"{key}: {stat_c[key]}")
            c += 1
        else:
            c += 1

        line = line.split()

        try:
            size += int(line[-1])
        except (IndexError, ValueError):
            pass

        try:
            if line[-2] in valid_c:
                if stat_c.get(line[-2], -1) == -1:
                    stat_c[line[-2]] = 1
                else:
                    stat_c[line[-2]] += 1
        except IndexError:
            pass

    print(f"File size: {size}")
    for key in sorted(stat_c):
        print(f"{key}: {stat_c[key]}")

except KeyboardInterrupt:
        print(f"File size: {size}")
        for key in sorted(stat_c):
            print(f"{key}: {stat_c[key]}")
