#!/usr/bin/python3
"""COntains:
class Square(Rectangle)
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """CLass Square"""
    def __init__(self, size):
        """Instantiator:
        size will be private
        size must be a positive integer
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns area of a square"""
        return self.__size ** 2

    def __str__(self):
        """str magic method"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
