#!/usr/bin/python3
"""Defines a function that returns the lists of available
functions, methods, attributes of an object.
"""


def lookup(obj):
    """Returns a list of the variables, attributes, methods, functions
    associated with obj.

    Args:
        obj (any): object whose attributes are return
    """

    return dir(obj)
