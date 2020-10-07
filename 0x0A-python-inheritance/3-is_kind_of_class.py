#!/usr/bin/python3
"""COntains:
function is_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """Returns boolean
    Depending if obj is an instance of a class
    or an instance of a class that inherited
    """
    return isinstance(obj, a_class)
