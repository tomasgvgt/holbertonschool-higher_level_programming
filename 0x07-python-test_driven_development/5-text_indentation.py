#!/usr/bin/python3
"""This module contains:
function that prints a text with 2 new lines after each of this
characters: '.' '?' and ':'
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of this
    characters: '.' '?' and ':'
    Args:
        text (str): text to print.
    Raises:
        TypeError: text must be a string
"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    aux = '.'
    for c in text:
        if c is " " and aux in ['.', '?', ':']:
            continue
        print(c, end="")
        if c in ['.', '?', ':']:
            print()
            print()
        aux = c
