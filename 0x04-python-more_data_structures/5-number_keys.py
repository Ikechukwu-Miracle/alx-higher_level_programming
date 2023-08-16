#!/usr/bin/python3

def number_keys(a_dictionary):
    count = 0

    KeyList = list(a_dictionary.keys())

    for i in KeyList:
        count += 1

    return (count)
