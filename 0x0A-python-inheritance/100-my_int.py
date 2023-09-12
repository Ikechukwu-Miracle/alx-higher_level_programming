#!/usr/bin/python3
"""Defines a subclass of int"""


class MyInt(int):
    """A subclass of int that reverses tha roles of '==' and '!='"""

    def __eq__(self, val):
        """Replaces "==" with "!=".

        Args:
            val (int): value of the variable
        """
        return self.real != val

    def __ne__(self, val):
        """Replaces "!=" witn "==".

        Args:
            val (int): value of the variable
        """

        return self.real == val
