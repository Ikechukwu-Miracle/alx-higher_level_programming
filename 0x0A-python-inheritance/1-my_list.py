#!/usr/bin/python3
"""Defines a class `MyList` that is a subclass of the list class"""


class MyList(list):
    """Inherits and implements sorted printing for built-in list class"""

    def print_sorted(self):
        """This prints the list in sorted form"""

        print(sorted(self))
