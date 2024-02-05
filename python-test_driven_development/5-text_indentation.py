#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """Text indentation function"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    space = False
    for i in text:
        if i.isspace() and space:
            continue
        if i == "." or i == "?" or i == ":":
            print(i)
            print()
            space = True
        else:
            print(i, end="")
            space = False
