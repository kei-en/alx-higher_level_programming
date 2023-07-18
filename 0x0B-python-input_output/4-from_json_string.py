#!/usr/bin/python3
"""Defines a function for getting an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string
    Argds:
        my_str (str): the JSON string
    """
    return (json.loads(my_str))
