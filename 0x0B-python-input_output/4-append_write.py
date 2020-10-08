#!/usr/bin/python3
"""COntains:
Function append_write
"""


def append_write(filename="", text=""):
    with open(filename, "a", encoding="UTF8") as f:
        chars_written = f.write(text)
    return chars_written
