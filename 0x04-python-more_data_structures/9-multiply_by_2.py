#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    kList = list(new_dic.keys())

    for key in kList:
        new_dic[key] *= 2

    return new_dic
