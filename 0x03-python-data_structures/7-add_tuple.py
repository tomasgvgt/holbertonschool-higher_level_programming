#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    # Use value 0 if a tupple has less than 2 elements
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    sum_a = tuple_a[0] + tuple_b[0]
    sum_b = tuple_a[1] + tuple_b[1]
    return sum_a, sum_b
