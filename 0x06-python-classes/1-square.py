#!/usr/bin/python3
"""Define a Square based on 0-square.py"""


class Square:
    """Represents a square with the private attribute size"""
    def __init__(self, size):
        """Initializes the method that stores the size of the square

        Attributes:
            size (optional): size of the square
        """
        self.__size = size
