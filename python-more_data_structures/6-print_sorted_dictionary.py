#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    result_dict = dict(sorted(a_dictionary.items()))
    for key in result_dict:
        print("{}".format(key), end=": ")
        print("{}".format(result_dict[key]))
