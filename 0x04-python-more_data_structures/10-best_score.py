#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value"""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    student = list(a_dictionary.keys())[0]
    best = a_dictionary[student]
    for k, v in a_dictionary.items():
        if v > best:
            best = v
            student = k
    return (student)
