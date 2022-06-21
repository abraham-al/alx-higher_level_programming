#!/usr/bin/python3
""" module contains: class Square """


class Square:
    """
        Square: defines a square
        Attributes:
            size (int): size of a square
        Method:
            __init__: init of size for each instance
    """

    def __init__(self, size=0):
        """ Initialization of attributes for instances
            Args:
                size(int): size of the square
        """
        if (isinstance(size, int)):
            self.__size = size
            if size < 0:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """ Returns the area of the square """
        return self.__size ** 2
    