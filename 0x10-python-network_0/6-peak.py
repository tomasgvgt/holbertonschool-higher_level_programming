#!/usr/bin/python3
"""Finds a peak in a list of integers"""


def find_peak(list_of_integers):
    """Finds peaks"""
    if not list_of_integers:
        return
    list_of_integers.sort()
    return list_of_integers[-1]
