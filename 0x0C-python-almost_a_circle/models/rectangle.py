#!/usr/bin/python3
"""COntains:
class Rectangle(Base)
"""
from models.base import Base


class Rectangle(Base):
    """Class that represents a Rectangle
    Inherits from base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance of Rectangle.
        Uses init from class Base,
        and adds width, height, x and y attributes
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints the Rectangle instance
        with the character '#'"""
        for y in range(self.y):
            print('')
        for row in range(self.height):
            for x in range(self.x):
                print(' ', end='')
            for col in range(self.width):
                print('#', end='')
            print('')

    def __str__(self):
        """Returns a readable string of the passed instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        atributes = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for index, value in enumerate(args):
                setattr(self, atributes[index], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return self.__dict__
