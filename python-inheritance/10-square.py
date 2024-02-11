#!/usr/bin/python3
"""Square module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """Init function"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Area function"""
        return self.__size * self.__size

    def __str__(self):
        """Str function"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
