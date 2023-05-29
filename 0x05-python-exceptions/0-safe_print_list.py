#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list."""
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
        return i + 1
    except IndexError:
        print()
        return i
