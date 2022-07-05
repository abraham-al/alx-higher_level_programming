#!/usr/bin/python3
"""
JSON representation of an object (string)
"""
import json


def load_from_json_file(filename):
    """
    Load JSON  object
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
