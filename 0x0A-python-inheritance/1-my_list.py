#!/usr/bin/python3
"""COntains:
class MyList(list)
"""


class MyList(list):
    def print_sorted(self):
        """Prints a list, sorted in ascending order"""
        print(sorted(self))
