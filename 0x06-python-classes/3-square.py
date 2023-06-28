#!/usr/bin/python3
"""This class contains documentation for class Square"""
"""__init__ method & instantiation of size after class Square:"""
"""if/else stmnt to make sure size is an int"""
"""def area(self): multiplies self to self"""


class Square:
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return int(self.__size) * int(self.__size)
