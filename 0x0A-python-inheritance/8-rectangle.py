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
