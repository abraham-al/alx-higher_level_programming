#!/usr/bin/python3
"""
    Defining class Mylist
    """


class MyList(list):
    """
        MyList
    """
    def print_sorted(self):
        """
        Print a sorted List
        """
        print(sorted(self))
