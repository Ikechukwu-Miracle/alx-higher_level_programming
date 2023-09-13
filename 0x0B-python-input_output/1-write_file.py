#!/usr/bin/python3
"""Module defines a function that writes to a file"""


def write_file(filename="", text=""):
    """writes to 'filename' and returns the number of characters written.

    Args:
        filename (str): the name of file written to.
        text (str): text written to file
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
