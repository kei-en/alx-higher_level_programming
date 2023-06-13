#!.usr/bin/python3
"""Defines a function for writing a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text file
    Args:
        filename (str): name of the file
        text (str): text to be written
    Return:
        the number of characters written"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
