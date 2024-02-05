#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i, array in enumerate(matrix):
        arr = []
        for j, value in enumerate(array):
            arr.append(value ** 2)
        new_matrix.append(arr)
    return new_matrix
