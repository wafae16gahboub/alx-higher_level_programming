#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())

    for y in keys:
        if value == a_dictionary.get(y):
            del a_dictionary[y]

    return (a_dictionary)
