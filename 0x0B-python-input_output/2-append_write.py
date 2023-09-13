#!/usr/bin/python3
"""Defines a function that appends a string to a file and returns
the number of characters appended.
"""


def append_write(filename="", text=""):
    """appends 'text' to 'filename' and returns number of characters appended.

    Args:
        filename (str): file appended to.
        text (str): strings appended to file.
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
