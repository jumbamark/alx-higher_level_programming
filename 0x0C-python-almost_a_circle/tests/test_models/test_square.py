#!/usr/bin/python3
"""Test cases for the Square class.
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Suite to test Square class"""

    def setUp(self):
        """Method invoked for each test.
        """
        Base._Base__nb_objects = 0
        self.s1 = Square(5)

    def test_new_square(self):
        """Test new Square instances.
        """
        self.assertEqual(self.s1.id, 1)

    def test_is_Base_instance(self):
        """Test Square is a Base instance.
        """
        self.assertEqual(True, isinstance(self.s1, Base))

    def test_is_Rectangle_instance(self):
        """Test Square is a Rectangle instance.
        """
        self.assertEqual(True, isinstance(self.s1, Rectangle))

    def test_access_private_attrs(self):
        """Trying to access a private attribute.
        """
        with self.assertRaises(AttributeError):
            self.s1.__width
            self.s1.__heught

    def test_str(self):
        """Test __sstr__ representation.
        """
        s1 = Square(14, 5, 2, 3)
        self.assertEqual(str(s1), "[Square] (3) 5/2 - 14")

    def test_update(self):
        """Test update method on Square.
        """

        s1 = Square(8)
        s1.update(30)
        self.assertEqual(s1.id, 30)

    def test_to_dictionary(self):
        """Test for public method to_dictionary.
        """
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s_dictionary = {'x': 2, 'y': 1, 'id': 1, 'size': 10}
        self.assertEqual(len(s1_dictionary), len(s_dictionary))
        self.assertEqual(type(s1_dictionary), dict)
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        s2_dictionary = s2.to_dictionary()
        self.assertEqual(len(s1_dictionary), len(s2_dictionary))
        self.assertEqual(type(s2_dictionary), dict)
        self.assertFalse(s1 == s2)


if __name__ == "__main__":
    unittest.main()
