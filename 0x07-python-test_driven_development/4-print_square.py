#!/usr/bin/python3
"""Defines a function that prints a square using '#'"""


def print_square(size):
    """Prints a square with '#' equivalent to the size.

    Args:
        size (int): size of the square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size, end="")
        print()
