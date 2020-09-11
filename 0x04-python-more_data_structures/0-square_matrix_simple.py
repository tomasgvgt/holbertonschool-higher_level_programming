#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    square_matrix = [[x**2 for x in row] for row in matrix]
    # square_matrix = [list(map(lambda x: x**2, elem)) for elem in matrix]
    return(square_matrix)
