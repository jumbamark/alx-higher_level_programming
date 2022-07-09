#!/usr/bin/python3
"""Module containing the Test cases for Base class
"""

import unittest
import os
from models.base import Base


class TestBase(unittest.TestCase):
    """Suite to test Base class
    """

    def setUp(self):
        """Method invoked for each test
        """
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test assigned id"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_type(self):
        """Test for type and instance"""
        b6 = Base()
        self.assertEqual(type(b6), Base)
        self.assertTrue(isinstance(b6, Base))
