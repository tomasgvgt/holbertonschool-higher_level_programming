#!/usr/bin/python3
"""COntains:
Function append_write
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    and returns the number of characters added"""
    # Opening the file with access mode append
    with open(filename, "a", encoding="UTF8") as f:
        chars_written = f.write(text)
    return chars_written
