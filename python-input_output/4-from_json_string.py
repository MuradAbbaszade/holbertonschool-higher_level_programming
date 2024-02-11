#!/usr/bin/python3
"""Json to object"""
import json


def from_json_string(my_str):
    """From json to string function"""
    return json.loads(my_str)
