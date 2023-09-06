#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """User is unable to create new instance attributes
     except instance attribute name is first_name
    """

    def __setattr__(self, name, val):
        if name == "first_name":
            self.__dict__[name] = val
        else:
            msg = f"'LockedClass' object has no attribute '{name}'"
            raise AttributeError(msg)
