#!/usr/bin/python3
"""Defines a class called Square"""

class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """initialzes a new instance of square

        Args:
        size(int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
