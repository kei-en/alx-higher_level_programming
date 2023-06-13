#!/usr/bin/python3
"""Defines a class-to-JSON function"""


def class_to_json(obj):
    """Returnthe dictionary representation of a simple data structure"""
    return obj.__dict__
