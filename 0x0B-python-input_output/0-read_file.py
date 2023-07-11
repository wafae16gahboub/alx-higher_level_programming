#!/usr/bin/python3
"""read_file"""


def read_file(filename=""):
    """function"""
    with open(filename, encoding="utf-8") as f:
        read = f.read()
        print(read, end="")
