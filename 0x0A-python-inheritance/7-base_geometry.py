#!/usr/bin/python3
"""COntains:
clasee BaseGeometry
"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        """Raises an exception:
        Area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if value is a positive integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
