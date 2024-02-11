#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Pascal triangle function"""
    if n <= 0:
        return []
    result = [[1]]
    for i in range(1, n):
        inner_list = [1]
        for j in range(1, i):
            inner_list.append(result[i - 1][j - 1] + result[i - 1][j])
        inner_list.append(1)
        result.append(inner_list)
    return result
