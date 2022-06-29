#!/usr/bin/python3
"""
Function that adds 2 integers
"""


def add_integer(a, b=98):
    """Adds two integers and/or float numbers

    Args:
        a (int, float): First number
        b (int, float): Second inumber

    Returns:
        Sum of the two given values

    Raises:
        TypeError: If a or b arent integer and/or float numbers

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if isinstance(b, int) is False and isinstance(b, float) is False:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
