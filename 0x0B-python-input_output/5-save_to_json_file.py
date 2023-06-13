#!/usr/bin/python3
"""Defines a function for writing an object to a text file,
    using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using JSON representation
    Args:
        myobj (obj): the object to write
        filename (str): name of the file to write to
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (json.dump(my_obj, f))
