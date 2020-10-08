#!/usr/python3
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

    def to_json(self):
        """retrieves a dictionary representation of
        a Student instance"""
        return self.__dict__
