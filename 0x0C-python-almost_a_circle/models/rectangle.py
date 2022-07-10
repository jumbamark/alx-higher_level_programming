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

    @property
    def width(self):
        """Retrieves the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute
        """
        self.__width = value

    @property
    def height(self):
        """Retrieves the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance"""
        self.__height = value

    @property
    def x(self):
        """Retrieves the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Retrieves the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y attribute
        """
        self.__y = value
