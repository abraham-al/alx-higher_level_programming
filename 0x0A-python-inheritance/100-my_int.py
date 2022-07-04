#!/usr/bin/python3
"""
a class MyInt that inherits from int
"""


class MyInt(int):
    """
        a class MyInt that inherits from int
    """
    def __eq__(self, x):
        """Defines module eq"""
        return not super().__eq__(x)

    def __ne__(self, x):
        """Defines module not eq"""
        return not super().__ne__(x)
