#!/usr/bin/python3
"""Returns the dictionary description of an object"""


def class_to_json(obj):
    """Returns the JSON serialization of an object.

    Args:
        obj (any): the object whose description is serialized.
    """

    return obj.__dict__
