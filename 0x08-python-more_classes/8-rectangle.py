#!/usr/bin/python3
"""Contains a class that defines a rectangle"""


class Rectangle:
    """Class that defines a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Instance method:
        Returns the area of the rectangle object.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Instance method:
        Returns the perimeter of the rectangle object.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Special method:
        In this case I worte it so it:
        Returns a string of the rectangle with the character #"""
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect
        if type(self.print_symbol) != str:
            self.print_symbol = str(self.print_symbol)
        for row in range(self.__height):
            rect += (self.print_symbol * self.__width) + '\n'
        return rect[:-1]

    def __repr__(self):
        """Special method:
        In this case I wrote is so it:
        Returns a string representation of the creation of
        a rectangle object
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Special method called when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
