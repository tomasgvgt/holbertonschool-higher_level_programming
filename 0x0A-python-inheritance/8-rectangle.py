#!/usr/bin/python3
"""COntains:
class Rectangle(BaseGeometry)
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """CLass Rectangle"""
    def __init__(self, width, height):
        """Special Method __init__"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
