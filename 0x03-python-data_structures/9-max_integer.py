#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    len_list = len(my_list) - 1

    while len_list > 1:
        i = 0
        while i < len_list:
            if my_list[i] > my_list[i + 1]:
                tmp = my_list[i]
                my_list[i] = my_list[i + 1]
                my_list[i + 1] = tmp
            i += 1
        len_list -= 1

    return my_list[-1]
