#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        srce = 0
        ldd = ""
        for i in my_list:
            if a_dictionary[i] > srce:
                srce = a_dictionary[i]
                ldd = i
        return ldd
