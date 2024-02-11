#!/usr/bin/python3
"""Append module"""


def append_write(filename="", text=""):
    """Append function"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
