#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Init function"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    @property
    def width(self):
        self.__width
    @property
    def height(self):
        self.__height
    @property
    def x(self):
        self.__x
    @property
    def y(self):
        self.__Y
    @width.setter
    def width(self, width):
        self.__width = width
    @height.setter
    def height(self, height):
        self.__height = height
    @x.setter
    def x(self, x):
        self.__x = x
    @y.setter
    def y(self, y):
        self.__y = y
