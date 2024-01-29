#!/usr/bin/python3
def common_elements(set_1, set_2):
    commons = []
    for i in set_1:
        for j in set_2:
            if i == j:
                commons.append(i)
    return commons
