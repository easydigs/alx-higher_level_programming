#!/usr/bin/python3
"""Defines a function that add two integers"""


def add_integer(a, b=98):

    """
    Function that add numbers a and b.
    This function takes two parameters, 'a' and 'b',
    which represent integers or floats.
    If 'a' or 'b' is not an integer or float,
    a TypeError is raised with a corresponding message.

    Parameters:
    - a (int or float): The first number.
    - b (int or float): The second number.

    Returns:
    int or float: The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
