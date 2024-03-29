#!/usr/bin/python3
"""Save object module"""
import json


def save_to_json_file(my_obj, filename):
    """Save function"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
