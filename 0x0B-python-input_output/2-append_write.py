#!/usr/bin/python3
""" write module """


def append_write(filename="", text=""):
    """ write and encoding operation """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
