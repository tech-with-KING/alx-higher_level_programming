#!/usr/bin/python3
# 3-safe_print_division.py


def safe_print_division(a, b):
    """
    Returns the division of a by b.
    """
    try:
        quotient = a / b
    except (TypeError, ZeroDivisionError):
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
    return (quotient)
