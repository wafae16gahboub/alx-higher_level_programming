#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a) + [0, 0]
    b = list(tuple_b) + [0, 0]
    total = []
    for i in range(2):
        total.append(a[i] + b[i])
    return tuple(total)
