#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for i, value in enumerate(my_list):
        isUnique = True
        for j in range(0, i):
            if my_list[j] == value:
                isUnique = False
                break
        if isUnique:
            sum += value
    return sum
