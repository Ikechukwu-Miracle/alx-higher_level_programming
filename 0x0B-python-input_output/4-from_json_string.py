#!/usr/bin/python3
import json
"""Defines a function that returns object represented by JSON string"""


def from_json_string(my_str):
    """Returns JSON to object"""

    return json.loads(my_str)
