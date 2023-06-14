#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    number = 0
    denom = 0

    for w in my_list:
        number += w[0] * w[1]
        denom += w[1]

    return (number / denom)
