#!/usr/bin/python3
"""Base module"""


class Base:
    """Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Init function"""
        if not id is None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = id
