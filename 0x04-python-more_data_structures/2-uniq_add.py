#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniqList = set(my_list)

    count = 0
    for i in uniqList:
        count += i

    return count
