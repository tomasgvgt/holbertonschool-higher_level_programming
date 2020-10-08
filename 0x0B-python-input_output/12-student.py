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
        for s in attrs:
            try:
                new_dictionary[s] = self.__dict__[s]
            except:
                pass
        return new_dictionary
