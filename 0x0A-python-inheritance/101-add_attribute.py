#!/usr/bin/python3
"""
adds an object
"""


def add_attribute(obj, name, value):
    """
        adds a new attribute to object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
