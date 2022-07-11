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

    def test_str(self):
        """Test __sstr__ representation.
        """
        s1 = Square(14, 5, 2, 3)
        self.assertEqual(str(s1), "[Square] (3) 5/2 - 14")
