#!/usr/bin/python3
"""
class Square that defines a square based on 3-square.py
"""


class Square:
    """Represents a square.
    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0)
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Property to retrieve the size of the square object"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter to set the size of the square object"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            return self.__value = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size ** 2
