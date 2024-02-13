#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Init function"""
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.__size)
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
        self.__size = size
