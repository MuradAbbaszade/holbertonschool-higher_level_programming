#!/usr/bin/python3
"""Inherits from"""


def inherits_from(obj, a_class):
    """Function"""
    return isinstance(obj, a_class) and not (type(obj) is a_class)
    
