#!/usr/bin/python3
"""Defines a function that checks if an object is an instance of a class
or an instance of a sub class.
"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or an instance of
    a sub class.

    Args:
        obj (any): object to check
        a_class (type): class to match
    """

    if isinstance(obj, a_class):
        return True
    return False
