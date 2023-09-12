#!/usr/bin/python3
"""Defines a function that adds an attribute to an object if possible"""


def add_attribute(obj, attName, attVal):
    """Adds an attribute to an object if possible.

    Args:
        obj (any): object to recieve attribute
        attName (str): name of attribute
        attVal (any): value of attribute
    """

    if hasattr(obj, '__dict__'):
        setattr(obj, attName, attVal)
    else:
        raise TypeError("can't add new attribute")
