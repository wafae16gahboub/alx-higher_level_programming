#!/usr/bin/python3
"""only sub class"""


def inherits_from(obj, a_class):
    """only sub class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
