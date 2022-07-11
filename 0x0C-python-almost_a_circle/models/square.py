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

    @property
    def size(self):
        """Retrieve the size attribute.
        """
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the size attribute.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Public method that assigns attributes.
        """
        if args is not None and len(args) is not 0:
            list_attr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_attr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_attr[i], args[i])

        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)
