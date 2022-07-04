#!/usr/bin/python3
"""
    Rectangle class inheriting task 7 class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class  that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
            Initialize rectangle from BaseGeometry
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
