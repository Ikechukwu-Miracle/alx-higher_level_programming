#!/usr/bin/python3
"""Divides the elements in a matrix and
Returns a new matrix of the divided elements
"""


def matrix_divided(matrix, div):
    """Returns a new matrix after dividing the elements of a matrix

    Args:
        matrix(list of lists): matrix
        div(int/float): dividing number
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """

    if not all(isinstance(row, list)
            and all(isinstance(x, (int, float))
                for x in row) for row in matrix):
        m = "matrix must be a matrix"
        n = " (list of lists) of integers/floats"
        raise TypeError(m + n)

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    div_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return div_matrix
