#!/usr/bin/python3
"""
    BaseGeometry class
"""


class BaseGeometry():
    """
        BaseGeometry Class
    """
    def area(self):
        """
            public instance
            Raise:
                Exception: Area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check value
        Args:
            name (str): value designation
            value (any): value to check
        Raises:
            TypeError: value must be an integer
            ValueError: value must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
