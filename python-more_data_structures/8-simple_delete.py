#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    is_exist = False
    for i in a_dictionary:
        if i == key:
            is_exist = True
    if is_exist is True:
        a_dictionary.pop(key)
    return a_dictionary
