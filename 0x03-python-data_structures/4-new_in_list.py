#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list

    cp_list = [i for i in my_list]
    cp_list[idx] = element

    return cp_list
