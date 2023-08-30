#!/usr/bin/python3
"""Defines  a MagicClass that works like a bytecode"""

import math

class MagicClass:
    """Reprents MagicClass of a circle"""


    def __init__(self, radius=0):
        """Initializes the class.

        Arg:
            radius(int or float): The radius of the class.
        """

        if type(radius) is not float and type(radius) is not int:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns area of the class"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Returns circumference of the class"""
        return 2 * self.__radius * math.pi
