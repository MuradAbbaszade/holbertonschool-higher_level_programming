#!/usr/bin/python3
"""Student module"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Init function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """To json function"""
        result_dict = {}
        if not (attrs is None):
            for i in attrs:
                if i in self.__dict__:
                    result_dict[i] = self.__dict__[i]
            return result_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Reload from json function"""
        if json:
            self.first_name = json["first_name"]
            self.last_name = json["last_name"]
            self.age = json["age"]
