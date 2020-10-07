#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that
    inherited from a_class
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
