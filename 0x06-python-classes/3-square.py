#!/usr/bin/python3
"""defines a square based on 2-square.py"""


class Square:
    """Represents a square.
    Private instance attribute: size
    Instantiation with optional size
    Public instance method: def area(self).
    """

    def __init__(self, size=0):
        """Method to initialize the square object"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            riase ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method that returns the square area of the object.
        """
        return self.__size ** 2
