#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    romNum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    tot = 0
    preVal = 0

    for symbol in reversed(roman_string):
        val = romNum.get(symbol, 0)
        if val >= preVal:
            tot += val
        else:
            tot -= val

        preVal = val

    return tot
