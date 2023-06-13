#!/usr/bin/python3
"""Defines a function for reading a text file"""


def read_file(filename=""):
    """Reads a text file
    Args:
        filename (str): name of the file
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read())
