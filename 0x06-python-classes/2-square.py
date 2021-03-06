#!/usr/bin/python3
"""class Square that defines a square based on 1-square.py"""


class Square:
    """Represents a square.
    Private instance attribute: size
    Instantiation with optional size
    """

    def __init__(self, size=0):
        """Method to initialize the square object"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
