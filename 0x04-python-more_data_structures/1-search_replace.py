#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    length = len(new_list)
    for i in range(0, length):
        if new_list[i] == search:
            new_list[i] = replace
    return (new_list)
