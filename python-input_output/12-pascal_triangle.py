#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Pascal triangle function"""
    if n <= 0:
        return []
    result = []
    for i in range(n):
        inner_list = []
        z = 1
        for _ in i:
            inner_list.append(z)
