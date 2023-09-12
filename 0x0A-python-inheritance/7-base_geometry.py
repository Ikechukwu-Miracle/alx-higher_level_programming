#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Repesents a geometry class"""

    def area(self):
        """Method to determine area of the geomertry"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as int.

        Args:
            name (str): name of the parameter to validate
            value (int): value to validate
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
