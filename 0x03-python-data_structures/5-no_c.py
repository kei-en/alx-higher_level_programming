#!/usr/bin/python3

def no_c(my_string):
    """Removes all characters c and C"""
    my_new_string = my_string.replace("c", "").replace("C", "")
    return my_new_string
