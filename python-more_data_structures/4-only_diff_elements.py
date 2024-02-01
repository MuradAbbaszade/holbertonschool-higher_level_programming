#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_elements = []
    for i in set_1:
        is_present = False
        for j in set_2:
            if i == j:
                is_present = True
        if is_present == False:
            diff_elements.append(i)

    for i in set_2:
        is_present = False
        for j in set_1:
            if i == j:
                is_present = True
        if is_present == False:
            diff_elements.append(i)

    return diff_elements
