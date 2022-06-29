"""Unittest for the max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function
    """

    def test_max_int(self):
        """Test with a regular list of ints

        Should return max result

        """
        list_test = [12, 8, 5, 99]
        result = max_integer(list_test)
        self.assertEqual(result, 99)

    def test_empty_list(self):
        """Test with an empty list: should return None
        """
        list_test = []
        result = max_integer(list_test)
        self.assertEqual(result, None)

    def test_not_int(self):
        """
        Test with a list of non-ints and ints

        Should raise a TypeError exception

        """
        list_test = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, list_test)

    def test_float(self):
        """Test with a list of ints and floats
        should return the max
        """
        list_test = [3, 4.5, 2]
        result = max_integer(list_test)
        self.assertEqual(result, 4.5)

    def test_identical(self):
        """Test with alist of identical values
        should return the value
        """
        list_test = [15, 15, 15, 15]
        result = max_integer(list_test)
        self.assertEqual(result, 15)

    def test_unique(self):
        """Test with a list of one int
        should return the value of this int
        """
        list_test = [60]
        result = max_integer(list_test)
        self.assertEqual(result, 60)


if __name__ == '__main__':
    unittest.main()
