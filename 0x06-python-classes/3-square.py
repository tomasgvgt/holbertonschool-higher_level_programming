#!/usr/bin/pythton3
""" Definition of class Square"""


class Square:
    """class Square.

    Attributes:
        size: size of square
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Returns the current square area"""
        return self.__size ** 2
