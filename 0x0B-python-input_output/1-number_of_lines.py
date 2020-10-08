#!/usr/bin/python3
"""Contains:
Function number_of_lines
"""


def number_of_lines(filename=""):
    """returns the number of lines of a text file"""
    with open(filename) as f:
        lines_list = f.readlines()
    return len(lines_list)

    # Other way 1:
    # with open(filename) as f:
    #    lines = 0
    #    while f.readline()
    #        lines += 1
    # return lines

    # Other way 2:
    # with open(filename) as f:
    #    lines = 0
    #    for line in f:
    #        lines += 1
    # return lines
