#!/usr/bin/python3
"""Defines a function that returns object represented by JSON string"""
import json


def from_json_string(my_str):
    """Returns JSON to object"""

    return json.loads(my_str)
