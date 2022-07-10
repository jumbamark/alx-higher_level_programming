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

    def test_rectangle_id(self):
        """Testing for id"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_rectangle_attributes(self):
        """Testing for attribute values"""
        r1 = Rectangle(10, 2)
        r3 = Rectangle(10, 2, 3, 6, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 6)

    def test_missing_args(self):
        """Check for missing arguments.
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)

        s = ("__init__() missing 2 required positional" +
             " arguments: 'width' and 'height'")
        with self.assertRaises(TypeError) as x:
            r2 = Rectangle()
        self.assertEqual(s, str(x.exception))

    def test_inheritance(self):
        """Tests for inheritance
        """
        r1 = Rectangle(10, 2)
        self.assertTrue(isinstance(r1, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))
