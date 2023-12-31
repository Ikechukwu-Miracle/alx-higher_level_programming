#!/usr/bin/python3
"""Defines a class called Square"""

class Square:
    """Represents a square"""


    def __init__(self, size=0, position=(0,0)):
        """initialzes a new instance of square

        Args:
        size(int): size of the square
        position(int, int): position of the square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Gets and set the position of the square"""
        return self.__position

    @position.setter
    def position(self, val):
        if not isinstance(val, tuple) or len(val) != 2:
            raise TypeError("position must be a tuple of two positive integers")

        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of two positive integers")
        self.__position = val

    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square using the '#' character.

        The '#' represents the size of the square.
        """

        if self.__size == 0:
            print()

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size, end="")
            print()
