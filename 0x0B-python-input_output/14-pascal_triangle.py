#!/usr/bin/python3
"""COntains:
Function pascal_triangle(n)
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal’s triangle of n
    Returns an empty list if n <= 0
    """
    # Triangle is a list of lists of ints.
    triangle = []
    if n <= 0:
        return triangle
    # Create n rows for the triangle
    for row in range(n):
        # Append new list with 1 as first element
        # every time a new row starts
        triangle.append([1])
        if row > 1:
            # Create all the elements between the 1st and last
            # element of each row.
            for col in range(row - 1):
                # Each element is the sum of the two elements above it
                triangle[row].append(
                    triangle[row - 1][col] + triangle[row - 1][col + 1])
        if row > 0:
            # Create last element of each row (always 1)
            triangle[row].append(1)
    return triangle
