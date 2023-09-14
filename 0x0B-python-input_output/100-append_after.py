#!/usr/bin/python3
"""Defines a function to search and replace a string from a file"""


def append_after(filename="", search_string="", new_string=""):
    """Inserta a string after line containing a given text in file.

    Args:
         filename (str): name of the file
         search_string (str): the string to search for within file
         new_string (str): string to replace line with
    """

    string = ""
    with open(filename) as read:
        for line in read:
            string += line
            if search_string in line:
                string += new_string

    with open(filename, mode="w") as written:
        written.write(string)
