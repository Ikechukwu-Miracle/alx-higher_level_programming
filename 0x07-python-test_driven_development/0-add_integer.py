#!/usr/bin/python3
"""Function adds two integers or float numbers and
and returns their sum.
The numbers can be either float or integers.
The float numbers are type casted to int.
"""


def add_integer(a, b=98):
    """Returns integer sum of two numbers.
    Args:
    a(int/ float): first number
    b(int/ float): second number
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
