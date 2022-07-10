#!/usr/bin/python3

"""Module containing a class Square that inherits from Rectangle.
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance.
        """
        self.size = size
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):

        """Returns a string representation of a Rectangle instance.
        """
        return "[Square] ({}) {}/{} - {}"\
               .format(self.id, self.x, self.y, self.width)
