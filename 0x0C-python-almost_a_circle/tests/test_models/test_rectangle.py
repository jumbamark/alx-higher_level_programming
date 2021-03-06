#!/usr/bin/python3
"""Module containing Test cases for the Rectangle class
"""
import unittest
from io import StringIO
from unittest.mock import patch
import contextlib
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

    def test_display(self):
        """Testing for display
        """
        r1 = Rectangle(3, 2)
        output = "###\r\n###\r\n"
        with patch("sys.stdout", new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), output)

        r2 = Rectangle(2, 5, 2, 4)
        res = '\n\n\n\n  ##\r\n  ##\r\n  ##\r\n  ##\r\n  ##\r\n'
        f = StringIO()
        with contextlib.redirect_stdout(f):
            r2.display()
            self.assertEqual(f.getvalue(), res)

    def test_str(self):
        """Test __str__ return value
        """
        self.assertEqual(self.r1.__str__(), "[Rectangle] (1) 0/0 - 10/2")

    def test_update(self):
        """Test for public method with args and kwargs.
        """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.y, 3)

    def test_to_dictionary(self):
        """Test for public method to_dictionary.
        """
        r1 = Rectangle(15, 4, 0, 6)
        r1_dictionary = r1.to_dictionary()
        r_dictionary = {'x': 10, 'y': 16, 'id': 20, 'height': 24, 'width': 15}
        self.assertEqual(len(r1_dictionary), len(r_dictionary))
        self.assertEqual(type(r1_dictionary), dict)
        r2 = Rectangle(6, 4)
        r2.update(**r1_dictionary)
        r2_dictionary = r2.to_dictionary()
        self.assertEqual(len(r1_dictionary), len(r2_dictionary))
        self.assertEqual(type(r2_dictionary), dict)
        self.assertFalse(r1 == r2)


if __name__ == '__main__':
    unittest.main()
