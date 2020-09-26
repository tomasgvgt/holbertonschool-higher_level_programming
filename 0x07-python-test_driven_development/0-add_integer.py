#!/usr/bin/python3
"""This module contains:
a function that adds two integers
"""


def add_integer(a, b=98):
    """Returns the sum of two integers.

    Args:
        a (int or float): First number.
        b (int or float): Second number.
    """
    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
