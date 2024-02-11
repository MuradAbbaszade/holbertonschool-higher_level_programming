#!/usr/bin/python3
"""Load add save module"""
import json
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
arg_list = []
for i in sys.argv:
    arg_list.append(i)
del arg_list[0]
if arg_list:
    try:
        obj = load_from_json_file("add_item.json")        
        for i in arg_list:
            obj.append(i)
        save_to_json_file(obj, "add_item.json")
    except FileNotFoundError:
        save_to_json_file(arg_list, "add_item.json")
