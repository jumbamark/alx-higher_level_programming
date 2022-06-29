#!/usr/bin/python3
"""
This module contains a function that prints a square with th character #
"""


def print_square(size):
    """Prints a square with the character #

    Args:
        size: size of the square printed

    Raises:
        TypeError: If size is not an integer

    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
