#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    nv_dictionary = {}
    for key, value in a_dictionary.items():
        nv_dictionary.update({key: (value * 2)})
    return nv_dictionary
