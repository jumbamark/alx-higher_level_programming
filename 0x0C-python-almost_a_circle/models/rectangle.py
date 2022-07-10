#!/usr/bin/python3

"""Module with a Rectangle class that inherits from Base
"""
from .base import Base


class Rectangle(Base):
    """Represents a Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance

        Args:
            width: width of the rectangle
            height: rectangle height
            x: position
            y: position
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """Returns a string representation of a Rectangle instance.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
               .format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """Retrieves the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x attribute.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y attribute
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance.
        """
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #
        """
        for x in range(self.y):
            print("$")
        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print("$", end="")
            print("\r")

    def update(self, *args):
        """Updates attributes of an instance.
        """
        if args is not None and len(args) != 0:
            list_attr = ['id', 'width', 'height', 'x', 'y']
            for arg in range(len(args)):
                setattr(self, list_attr[arg], args[arg])
