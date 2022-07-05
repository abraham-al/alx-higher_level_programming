#!/usr/bin/python3
"""
define class called student
"""


class Student:
    """
        A Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        defines first_name, last_name, age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        defines json object
        """
        return (self.__dict__)
