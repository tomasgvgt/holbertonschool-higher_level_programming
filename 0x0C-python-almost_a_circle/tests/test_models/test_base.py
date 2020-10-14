#!/usr/bin/python3
"""Unittest for class Base
"""
# import TestCase from unittest
from unittest import TestCase
# import classes from program
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

# Create a subclass of the class TestCase(unittest):
class TestBase(TestCase):
    """Holds the tests for Base
    """

    def test_init(self):
        """Test creation of a new instance"""
        base_object = Base()
        base_object_id_7 = Base(7)
        # Test if base_object is type Base
        self.assertIsInstance(base_object, Base)
        # Test if base objects have correct id
        self.assertEqual(base_object.id, 1)
        self.assertEqual(base_object_id_7.id, 7)

    def test_to_json_string(self):
        """Test the public method to_json_string"""
        r1 = Rectangle(20, 10, 2, 4)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        # Test if json_dictionary is a string
        self.assertIsInstance(json_dictionary, str)
        # Test if it returns "[]" when the list is empty
        json_empty = Base.to_json_string([])
        self.assertEqual(json_empty, "[]")
        # Test if it returns "[]" when the list is None
        json_None = Base.to_json_string(None)
        self.assertEqual(json_None, "[]")
