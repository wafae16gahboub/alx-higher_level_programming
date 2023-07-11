#!/usr/bin/python3
"""append to file"""


def append_write(filename="", text=""):
    """apend write"""

    with open(filename, 'a', encoding="utf-8") as aw:
        aw.write(text)
        return len(text)
