#!/usr/bin/python3
"""Defines a square class based on rectangle"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """A Square (special case of recatngle)"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the square object

        Args:
            size (int): the size of the squre (width and height)
            x (int): x cordinate
            y (int): y cordinate
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """sets or gets the size of the suare"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.width = value

    def __str__(self):
        """Returns the print() and str() representation of a square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """Updates the Square object by assigning new values to attributes."""

        if args:
            n_args = len(args)
            if n_args >= 1:
                if args[0] is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    self.id = args[0]
            if n_args >= 2:
                self.size = args[1]
            if n_args >= 3:
                self.x = args[2]
            if n_args > 3:
                self.y = args[3]
        elif kwargs:
            for key, val in kwargs.items():
                if key == 'id':
                    if val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = val
                elif key == 'size':
                    self.size = val
                elif key == 'x':
                    self.x = val
                elif key == 'y':
                    self.y = val
