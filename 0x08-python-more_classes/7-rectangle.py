#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Represents a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle class object.

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets and sets the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Sets / gets the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0

        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """Returns the printable representation of the rectangle.

        Rectangle is represented by '#'
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        rec_str = ""

        for _ in range(self.__height):
            rec_str += str(self.print_symbol) * self.__width + "\n"

        return rec_str.rstrip("\n")

    def __repr__(self):
        """Returns the formal string representation of the rectangle"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when an instance is deleted"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
