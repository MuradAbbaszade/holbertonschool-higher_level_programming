#!/usr/bin/python3
"""BaseGeometry"""


class BaseGeometry:
    """Base geometry class"""
    def area(self):
        """Area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer Validator function"""
        if not (type(value) is int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
