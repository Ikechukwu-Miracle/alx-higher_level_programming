#!/usr/bin/python3
"""Defines a rectangle class which inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """A rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initiates an instance of the rectangle class.

        Args:
            width (int): the width of the rectangle
            height (int): height of the rectangle
            x (int): x cordinate
            y (int): y cordinate
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """sets / gets the width"""
        return self.__width

    @width.setter
    def width(self, val):
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """sets / gets the height"""
        return self.__height

    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """sets / gets the x cordinate"""
        return self.__x

    @x.setter
    def x(self, val):
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """sets / gets the width"""
        return self.__y

    @y.setter
    def y(self, val):
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """Returns area of the rectangle"""

        return self.__width * self.__height

    def display(self):
        """prints the rectangle using '#'."""

        if self.__width == 0 or self.__height == 0:
            print("")
            return

        [print() for y in range(self.y)]
        for h in range(self.__height):
            for x in range(self.x):
                print("", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """print() and str() representation of rectangle"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                self.y, self.width, self.height)
