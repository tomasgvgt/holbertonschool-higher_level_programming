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
        # Test if ID exists
        self.assertTrue(hasattr(base_object, 'id'))

    def test_to_json_string(self):
        """Test the static method to_json_string"""
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

    def test_from_json_string(self):
        """Test the static method from_json_string"""
        list_input = [
            {'id': 90, 'width': 5, 'height': 2},
            {'id': 10, 'width': 6, 'height': 7}
        ]
        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        # Test if it returns a list
        self.assertIsInstance(list_output, list)
        # Test if it returns an empty list when the input is None or empty
        list_output = Base.from_json_string(None)
        self.assertEqual(list_output, [])
        list_output = Base.from_json_string("")
        self.assertEqual(list_output, [])
