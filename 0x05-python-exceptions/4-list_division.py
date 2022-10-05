#!/usr/bin/python3
# 4-list_division.py


def list_division(my_list_1, my_list_2, list_length):
    """
    Divides two lists element by element.
    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.
    Returns:
        A new list of length list_length containing all the divisions.
    """
    new_list = []
    for elem in range(0, list_length):
        try:
            quotient = my_list_1[elem] / my_list_2[elem]
        except TypeError:
            print("wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            new_list.append(quotient)
    return (new_list)
