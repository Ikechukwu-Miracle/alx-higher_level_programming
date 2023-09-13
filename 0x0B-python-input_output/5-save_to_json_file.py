#!/usr/bin/python3
"""Defines a function that serializes an object to JSON representation
and writes it to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """saves JSON representation of 'my_obj' to a file specified by
    'filename'

    Args:
        my_obj (any): object to serialize
        filename (str): name of file to write to
    """
    j_write = json.dumps(my_obj)

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(j_write)
