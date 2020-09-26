#!/usr/bin/python3
"""This module contains:
function that prints name and last name
"""


def say_my_name(first_name, last_name=""):
    """Prints name and last name.
    Args:
        first_name (str): first name.
        last_name (str): last name.
    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
