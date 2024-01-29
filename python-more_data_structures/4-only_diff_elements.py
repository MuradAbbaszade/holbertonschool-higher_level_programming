#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_elements = set_1.intersection(set_2)
    set_1 = set_1.union(set_2)
    result_set = []
    for i in set_1:
        for j in diff_elements:
            if i != j:
                result_set.append(i)
    return result_set
