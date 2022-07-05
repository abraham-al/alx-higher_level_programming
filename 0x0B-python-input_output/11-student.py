#!/usr/bin/python3
"""
Defines Student class
"""


class Student():
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

    def to_json(self, attrs=None):
        """
            retrieves a dictionary representation
            of a Student instance
        """
        if type(attrs) is list and all([type(s) == str for s in attrs]):
            return {i: j for i, j in self.__dict__.items() if i in attrs}
        return(self.__dict__)

    def reload_from_json(self, json):
        """
            reload json object
        """
        for i, j in json.items():
            self.__dict__[i] = j
