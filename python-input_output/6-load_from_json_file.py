#!/usr/bin/python3
"""Create object module"""
import json


def load_from_json_file(filename):
    """Load function"""
    with open(filename, "r") as f:
        return json.load(f)
