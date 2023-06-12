#!/usr/bin/python3
"""Defines an inherited class checking function"""


def inherits_from(obj, a_class):
    """Checks if an object isn an inherited instance of a class
    Args:
        obj (any): The object to check
        a_class (type): The class to mathcht the type of obj to
    Return:
        True - if obj is an inherited instance of a_class 
        False - otherwhise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
