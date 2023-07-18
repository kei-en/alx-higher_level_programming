#!/usr/bin/python3
"""Defines an inherited list class MyList"""


class MyList(list):
    """implements sorted printing for the built-in class
    """

    def print_sorted(self):
        """Prints a list in sorted (ascending) order"""
        print(sorted(self))
