#!/usr/bin/python3
"""
    inherits_from
"""


def inherits_from(obj, a_class):
    """
    function that returns True
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
