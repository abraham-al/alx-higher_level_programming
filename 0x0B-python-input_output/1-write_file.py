#!/usr/bin/python3
"""
write module
"""


def write_file(filename="", text=""):
    """
    write and encoding operation
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
