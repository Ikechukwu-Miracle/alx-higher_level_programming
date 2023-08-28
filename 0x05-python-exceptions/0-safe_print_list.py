#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    r_val = 0

    try:
        while r_val < x:
            print("{}".format(my_list[r_val]), end="")
            r_val += 1
    except IndexError:
            pass

    print()
    return r_val
