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
        # base_object = Base()
        base_object_id_7 = Base(7)
        # Test if base_object is type Base
        self.assertIsInstance(base_object_id_7, Base)
        # Test if base objects have correct id
        # self.assertEqual(base_object.id, 3)
        self.assertEqual(base_object_id_7.id, 7)
        # Test if ID exists
        self.assertTrue(hasattr(base_object_id_7, 'id'))

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

    def test_save_to_file(self):
        """Tests the class method save_to_file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        # Create a file with a json representation of r1 and r2
        Rectangle.save_to_file([r1, r2])
        # Open the file
        with open("Rectangle.json", "r") as f:
            # Read the file and create a list
            list_of_obj = Base.from_json_string(f.read())
        # Verify if there are two objects in the list
        self.assertEqual(len(list_of_obj), 2)
        # Verify if with and height of r1 are correct
        self.assertEqual(list_of_obj[0]["width"], 10)
        self.assertEqual(list_of_obj[0]["height"], 7)

    def test_create(self):
        """Test the class method create"""
        r3 = Rectangle(2, 4)
        dictionary = {"width": 2, "height": 4, "id": 1}
        r4 = Rectangle.create(**dictionary)
        self.assertEqual(r3.width, r4.width)
