#!/usr/bin/python3
"""
class Square that defines a square based on 4-square.py
"""


class Square:
    """Defines a square by its size.
    Private instance attribute: size
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Property to retrieve the size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter to set the value of the square object"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Public instance method that returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Public instance method that prints in stdout the square with
        the character #.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
