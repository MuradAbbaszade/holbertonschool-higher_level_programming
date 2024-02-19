#!/usr/bin/python3
"""Base module"""
import json
import os


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dict to json"""
        if list_dictionaries is None or bool(list_dictionaries) is False:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save to file"""
        if list_objs is None:
            filename = "{}.json".format(type(cls.__name__))
            with open(filename, "w") as file:
                file.write("[]")
        else:
            list_dict = []
            for i in list_objs:
                list_dict.append(i.__dict__)
            filename = "{}.json".format(cls.__name__)
            with open(filename, "w") as file:
                file.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """From json string"""
        if json_string is None or bool(json_string) is False:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create"""
        if cls.__name__ == "Rectangle":
            d = cls(1, 1)
        else:
            d = cls(1)
        d.update(dictionary)
        return d

    @classmethod
    def load_from_file(cls):
        """Load from file"""
        filename = "{}.json".format(cls.__name__)
        if os.path.exists(filename):
            with open(filename, "r") as file:
                dicts = cls.from_json_string(file.read())
                list_of_instances = []
                for i in dicts:
                    list_of_instances.append(cls.create(**i))
            return list_of_instances
        else:
            return []
