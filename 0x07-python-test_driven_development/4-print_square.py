#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """Print a square with the # character.

    Parameters:
        size (int): The height/width of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0 or a float

    Returns:
    None. Prints the square to the console.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
