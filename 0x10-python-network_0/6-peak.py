#!/usr/bin/python3

def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return
    sorted_list = sorted(list_of_integers)
    return sorted_list[-1]
