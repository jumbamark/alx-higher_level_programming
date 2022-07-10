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
        self.r1 = Square(5)

    def test_new_square(self):
        self.assertEqual(self.r1.id, 1)
