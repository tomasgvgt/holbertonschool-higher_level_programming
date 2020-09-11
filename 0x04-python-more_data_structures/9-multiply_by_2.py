#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    # return {k: 2 * v for k, v in _dictionary.items()}
    return {key: a_dictionary[key] * 2 for key in a_dictionary}
