#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        number = 0
        den = 0
        for w in my_list:
            number += (w[0] * w[1])
            deno += (w[1])
        return (number/deno)
    return 0
