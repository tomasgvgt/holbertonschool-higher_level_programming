#!/usr/bin/python3
"""COntains:
class Rectangle(BaseGeometry)
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """CLass Rectangle"""
    def __init__(self, width, height):
        """Initiates Rectangle object
        validating that width and height are positive integers
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area of rectangle object"""
        return self.__width * self.__height

    def __str__(self):
        """str magic method"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
