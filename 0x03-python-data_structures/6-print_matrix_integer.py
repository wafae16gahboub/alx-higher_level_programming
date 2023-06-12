#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for w in matrix:
        for z in w:
            if z == w[-1]:
                print('{:d}'.format(z), end='')
            else:
                print('{:d}'.format(z), end=' ')
        print()
