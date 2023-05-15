#!/usr/bin/python3

def no_c(my_string):
    """Removes all characters c and C"""
    my_new_string = [i for i in my_string if i != 'c' and i != 'C']

    return ("".join(my_new_string))
