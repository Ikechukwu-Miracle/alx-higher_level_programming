#!/usr/bin/python3
"""Defines a class Square that is a sub class of rectangle"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """A square, sub class of rectangle."""

    def __init__(self, size):
        """Inintializes a new instance of Square.

        Args:
            size (int): size (width and height) of the square
        """

        self.integer_validator("size" size)
        super.__init__(size, size)
        self.__size = size
