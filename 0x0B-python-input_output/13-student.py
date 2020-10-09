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
            return self.__dict__
        new_dictionary = {}
        for key in attrs:
            try:
                new_dictionary[key] = self.__dict__[key]
            except:
                pass
        return new_dictionary

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        if not json:
            return
        # Make the dictionary if the instance, thesame as the json dictionary.
        self.__dict__ = json

        """Other way:
        # look for all the keys in json
        for key in json:
            try:
                # Set the attribute of the object to the one in json
                setattr(self, key, json[key])
            except:
                # pass if there was no attribute name thesame as that key
                pass
        """
