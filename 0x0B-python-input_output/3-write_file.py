#!/usr/bin/python3
"""Contains:
Function write_file
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, "w", encoding="UTF8") as f:
        chars_written = f.write(text)
    return chars_written
