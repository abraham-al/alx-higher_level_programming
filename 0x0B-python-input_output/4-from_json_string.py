#!/usr/bin/python3
"""
JSON representation of an object (string)
"""
import json


def from_json_string(my_str):
    """
    Return JSON repr of an object
    """
    return json.loads(my_str)
