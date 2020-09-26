#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Classs to test max_integer"""

    def test_type(self):
        """Tests types"""

        self.assertRaises(TypeError, max_integer, 98)
        self.assertRaises(TypeError, max_integer, -9999999)
        self.assertRaises(TypeError, max_integer, False)

    def test_result(self):
        """Test results"""

        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer("aloha"), 'o')
        self.assertEqual(max_integer([-999, 99, 109.9, -9999]), 109.9)

    def test_no_value(self):
        """Test no value passed"""
        self.assertIsNone(max_integer())
