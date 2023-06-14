#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0
    num = 0
    rom_digit = {
             'M': 1000,
             'D': 500,
             'C': 100,
             'L': 50,
             'X': 10,
             'V': 5,
             'I': 1
             }
    for r in reversed(roman_string):
        arabe = rom_digit[r]
        num += arabe if num < arabe * 5 else -arabe
    return num
