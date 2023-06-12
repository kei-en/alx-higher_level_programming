#!/usr/bin/python3
"""Defines a class checking function"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class
    Args:
        obj (any): The object to check
        Return:
            True - if obj is exactly an instance of a_class
            False - otherwise
    """

    if type(obj) == a_class:
        return True
    return False
