#!/usr/bin/python3
"""Defines a function that prints a square with the character #."""

def print_square(size):
    """_summary_

    Args:
        size (int): The height/width of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
