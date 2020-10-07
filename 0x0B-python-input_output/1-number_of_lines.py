#!/usr/bin/python3
"""Contains:
Function number_of_lines
"""


def number_of_lines(filename=""):
    """returns the number of lines of a text file"""
    with open(filename) as f:
        lines_list = f.readlines()
    return len(lines_list)
