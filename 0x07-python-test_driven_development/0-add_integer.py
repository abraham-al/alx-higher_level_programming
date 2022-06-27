#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """ Return the integer addition of a and b.
    
    float arg are typecasted to int before addition

    Args:
        a (_type_): first arg
        b (int, optional): second arg. Defaults to 98.
    
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
