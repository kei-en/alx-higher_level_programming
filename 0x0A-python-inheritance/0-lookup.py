#!/usr/bin/python3
"""Defines an object attribute lookup function"""


def lookup(obj):
    """Returns the list of available attributes and methos of an object

    Args:
        obj: the object attribute
    """
    return dir(obj)
