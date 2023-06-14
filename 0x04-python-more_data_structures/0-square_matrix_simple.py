#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for w in matrix:
        mtx = list(map(lambda x: x**2, w))
        new_matrix.append(mtx)
    return new_matrix
