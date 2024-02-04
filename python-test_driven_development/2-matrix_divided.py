#!/usr/bin/python3
"""Matrix divided"""


def matrix_divided(matrix, div):
    """Matrix divided function"""
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    for i in matrix:
        for j in i:
            if not (isinstance(j, int) or isinstance(j, float)):
                raise TypeError(msg)
    k = len(matrix[0])
    for i in matrix:
        if len(i) != k:
            raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for i in matrix:
        new_row = []
        for j in i:
            new_row.append(round(j / div, 2))
        new_matrix.append(new_row)
    return new_matrix
