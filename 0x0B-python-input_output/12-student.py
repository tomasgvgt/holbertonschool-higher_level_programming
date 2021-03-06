#!/usr/bin/python3
"""COntains:
class Student
"""


class Student:
    """Represents Students"""
    def __init__(self, first_name, last_name, age):
        """Initializes Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of
        a Student instance"""
        if attrs is None:
            # If there is no attributes, return all the dict.
            return self.__dict__
        # If there are attributes, only those should be retrieved.
        new_dictionary = {}
        for key in attrs:
            try:
                # Add to the new_dictionary only the key: value found in attrs
                new_dictionary[key] = self.__dict__[key]
            except:
                pass
        return new_dictionary
