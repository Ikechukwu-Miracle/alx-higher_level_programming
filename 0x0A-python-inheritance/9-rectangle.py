#!/usr/bin/python3
"""Defines a class that uses the super class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Reprents a subclass of BaseGeometry."""

    def __init__(self, width, height):
        """Initializes an instance of Rectangle

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """Defines what is printed when print() is called the instance name"""

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
