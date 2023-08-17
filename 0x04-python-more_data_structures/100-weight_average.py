#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is None:
        return 0

    n = 0
    d = 0
    for t in my_list:
        n += t[0] * t[1]
        d += t[1]

    return (n / d)
