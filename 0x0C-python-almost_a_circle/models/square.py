#!/usr/bin/python3
"""COntains:
class Square(Rectangle)
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that represents a Square.
    Inherits from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializar for instances of class Square.
        Uses id, x, y, width, height, from Rectangle.
        It assigns width and height to size.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str method.
        Return a readable string with the information of a Square instance"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args and len(args) > 0:
            atributes = ["id", "size", "x", "y"]
            for index, value in enumerate(args):
                setattr(self, atributes[index], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary representation of an instance"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
        """Another way:

        return self.__dict__
        """
