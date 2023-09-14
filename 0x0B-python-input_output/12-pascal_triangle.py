#!/usr/bin/python3
"""Defines a function that returns a pascal traingle
of a given number.
"""


def pascal_triangle(n):
    """Returns a pascal triangle of size n.

    Arg:
        n (int): size of the pascal triangle
    """

    if n <= 0:
        return []

    triangle = []
    for rowNum in range(n):
        row = []
        coef = 1

        for k in range(rowNum + 1):
            row.append(coef)
            coef = coef * (rowNum - k) // (k + 1)

        triangle.append(row)

    return triangle
