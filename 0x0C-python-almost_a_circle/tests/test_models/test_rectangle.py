#!/usr/bin/python3
"""Module containing Test cases for the Rectangle class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Suite to test the Rectangle class"""

    def setUp(self):
        """Method invoked for each test."""
        Base._Base__nb_objects = 0
        self.r1 = Rectangle(10, 2)

    def test_rectangle_id(self):
        """Testing for id"""
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_rectangle_attributes(self):
        """Testing for attribute values"""
        r3 = Rectangle(10, 2, 3, 6, 12)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 6)

    def test_missing_args(self):
        """Check for missing arguments.
        """
        with self.assertRaises(TypeError):
            r2 = Rectangle(1)

        s = ("__init__() missing 2 required positional" +
             " arguments: 'width' and 'height'")
        with self.assertRaises(TypeError) as x:
            r3 = Rectangle()
        self.assertEqual(s, str(x.exception))

    def test_inheritance(self):
        """Tests for inheritance
        """
        self.assertTrue(isinstance(self.r1, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))

    def test_access_private_attrs(self):
        """Trying to access private attributes.
        """
        with self.assertRaises(AttributeError):
            self.r1.__width
            self.r1.__height

    def test_validate_attrs(self):
        """Trying to pass a string value and 0 for width"""
        with self.assertRaises(TypeError):
            r2 = Rectangle("2", 4)
        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 2)

    def test_area(self):
        """Testing for area
        """
        self.assertEqual(20, self.r1.area())
        self.r1.height = 50
        self.assertEqual(self.r1.area(), 500)
