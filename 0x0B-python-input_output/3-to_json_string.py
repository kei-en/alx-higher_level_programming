#!/usr/bin/python3
"""Defines a function for getting the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object
    Args:
        my_obj (obj): an object e.g. list, dict
    """
    return (json.dumps(my_obj))
