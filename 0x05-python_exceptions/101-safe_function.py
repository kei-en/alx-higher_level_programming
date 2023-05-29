#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes a function safely.
    Args:
        fct: The function to execute.
        args: Arguments to pass to the function.

    Returns:
        The result of the function.
    """
    try:
        result = fct(*args)
        return result
    except Exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
