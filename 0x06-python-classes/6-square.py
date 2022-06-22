#!/usr/bin/python3
"""
class Square that defines a square based on 5-square.py
"""


class Square:
    """Defines a square by its size.
    Private instance attribute: size
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Method that returns the position value"""
        return self.__position

    @position.setter
    def position(self, value):
        """Method that sets the position value of a square object"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
