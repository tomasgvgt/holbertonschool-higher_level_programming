#!/usr/bin/python3
"""COntains:
function is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """Returns boolean , depending if an boject is or
    not an instance of a class
    """
    return type(obj) == a_class
