#!/usr/bin/python3
"""Definition of class Square"""


class Square:
    """Class Square.

    Attributes:
    size: size of square.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and (len(vale) == 2) and
            (isinstance(value[0], int) and isinstance(value[1], int)) and
                (value[0] >= 0 and value[1] >= 0)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print((" " * self.__position[0]) + ("#" * self.__size))
