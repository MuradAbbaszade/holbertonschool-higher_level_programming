#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle"""

    def __init__(self, width=0, height=0):
        """Init"""
        self.width = width
        self.height = height

    def __str__(self):
        """To string"""
        result = ""
        for i in range(self.height):
            for _ in range(self.width):
                result += "#"
            if i != self.height - 1: 
                result += "\n"
        return result

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Set height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Area"""
        return self.height * self.width

    def perimeter(self):
        """Perimeter"""
        return 2 * (self.height + self.width)
