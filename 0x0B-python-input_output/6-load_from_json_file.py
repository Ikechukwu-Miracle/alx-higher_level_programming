#!/usr/bin/python3
"""Defines a function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """reads a JSON file and creates object from content"""

    with open(filename) as jFile:
        return json.load(jFile)
