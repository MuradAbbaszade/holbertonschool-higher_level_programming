#!/usr/bin/python3
"""Square"""


class Square:
    """Square"""
    def __init__(self, size=0):
        """Init"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area"""

        return self.__size ** 2
