#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        """Test an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when the max integer is at the beginning"""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_max_in_middle(self):
        """Test when the max integer is in the middle"""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_element(self):
        """Test a list with only one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test a list of floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_int_float(self):
        """Test a list of integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3]), 3)

    def test_negative_numbers(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer([-1, -5, -3, -4]), -1)

    def test_duplicate_max(self):
        """Test a list with duplicate max values"""
        self.assertEqual(max_integer([2, 3, 3, 1]), 3)

    def test_strings_in_list(self):
        """Test a list containing strings raises TypeError"""
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])

    def test_none_in_list(self):
        """Test a list containing None raises TypeError"""
        with self.assertRaises(TypeError):
            max_integer([1, None, 2])

if __name__ == "__main__":
    unittest.main()
