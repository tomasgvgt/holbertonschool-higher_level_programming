#!/usr/bin/python3
"""Contains:
Function read_file
"""


def read_file(filename=""):
    """function that reads a text file (UTF8)
    and prints it to stdout
    """
    # the with keyword, closes the file when the block inside
    # is finnished.
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
