#!/usr/bin/python3
# 101-safe_function.py

from sys import stderr


def safe_function(fct, *args):
    """Executes a function safely.
    Args:
        fct: The function to execute.
        args: Arguments for fct.
    Returns:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
    """
    try:
        return fct(*args)
    except (ZeroDivisionError, IndexError, TypeError, ValueError) as e:
        stderr.write("Exception: {}\n".format(e))
        return None
