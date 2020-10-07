#!/usr/bin/python3
"""COntains:
Function read_lines
"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file (UTF8)
    and prints it to stdout
    """

    with open(filename, "r", encoding="utf-8") as f:
        if nb_lines > 0:
            for i in range(nb_lines):
                print(f.readline(), end="")
        else:
            for line in f:
                print(line, end='')
