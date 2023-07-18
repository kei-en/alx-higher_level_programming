#!/usr/bin/python3
"""Defines a function for appending a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file
    Args:
        filename (str): name of the text file
        text (str): the text to be appended
    Return:
        the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
