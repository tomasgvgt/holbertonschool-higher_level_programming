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
            # Read only the number of lines specified
            for i in range(nb_lines):
                print(f.readline(), end="")
        else:
            # Read all lines
            print(f.read(), end='')
