#!/usr/bin/python3
"""Defines a function that tells if an object is exactly
an instance of a class
"""


def is_same_class(obj, a_class):
    """Returns true if obj is an instance of a_class.

    Aegs:
        obj (any): object for type checking
        a_class (type): The particular class
    """

    if type(obj) == a_class:
        return True
    return False
