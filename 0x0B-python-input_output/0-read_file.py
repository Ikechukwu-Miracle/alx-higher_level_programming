#!/usr/bin/python3
"""Defines a function that reads a file"""


def read_file(filename=""):
    """Reads a the file specified by filename and prints to
    standard output.

    Arg:
        filename (str): the name of the file to be read
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
