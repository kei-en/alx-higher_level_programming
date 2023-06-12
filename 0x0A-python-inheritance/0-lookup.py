#!/usr/bin/python3

def lookup(obj):
    """Returns the list of available attributes and methos of an object

    Args:
        obj: the object attribute
    """
    return dir(obj)
