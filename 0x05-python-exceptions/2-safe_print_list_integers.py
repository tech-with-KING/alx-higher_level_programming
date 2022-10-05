#!/usr/bin/python3
# 2-safe_print_list_integers.py


def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first x elements of a list that are integers.
    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
    """
    ret_num = 0
    for elem in range(0, x):
        try:
            print("{:d}".format(my_list[elem]), end="")
            ret_num += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret_num)
