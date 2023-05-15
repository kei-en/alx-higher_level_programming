#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list"""
    two_mult = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            two_mult.append(True)
        else:
            two_mult.append(False)

    return two_mult
