#!/usr/bin/python3
"""Defines a class called Square"""

class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """initialzes a new instance of square

        Args:
        size(int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """Gets and Sets the size of the square"""
        return self.__size

    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val

    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)
