#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test with an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test with a list containing one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_integers(self):
        """Test with a list of negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_at_beginning(self):
        """Test with the maximum integer at the beginning of the list."""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_max_at_end(self):
        """Test with the maximum integer at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_repeated_elements(self):
        """Test with a list of repeated elements."""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

if __name__ == '__main__':
    unittest.main()
