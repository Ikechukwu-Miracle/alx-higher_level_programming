#!/usr/bin/python3
"""Defines a function that returns True only if an object is an
instance of a direct or indirect inheritor of a class.
"""


def inherits_from(obj, a_class):
    """Returns True only if obj is an instance of a subclass of
    a_class.

    Args:
        obj (any): object to check
        a_class (type): class to match
    """

    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    return False
