#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
            print(" ".join("{:d}".format(element) for element in row))
    # with list comprehension
    # [[print(" ".join("{:d}".format(elm) for elm in row))] for row in matrix]
