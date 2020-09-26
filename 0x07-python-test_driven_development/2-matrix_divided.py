#!/usr/bin/python3
"""This module contains:
function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Returns a new matrix with all the elements
    of passed matrix divided by div

    Args:
        matrix (list of lists): matrix.
        div (int or float): Divisor for all elements of matrix.
    Raises:
        TypeError: div must be a number.
        ZeroDivisionError: division by zero.
        TypeError: matrix must be a matrix (list of lists)
            of integers/floats.
        TypeError: Each row of the matrix should be of thesam size.
    """
    # String for this type of error (pep8 bothers for lenght of line)
    error_int_fl = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError(error_int_fl)
    new_matrix = [[round(float(elem)/float(div), 2) for elem in row]
                  for row in matrix]
    return new_matrix
