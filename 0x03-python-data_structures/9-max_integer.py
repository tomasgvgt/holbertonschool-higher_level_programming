#!/usr/bin/python3


# Finds the biggest integer of a list
def max_integer(my_list=[]):
    if not my_list:
        return None
    highest = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > highest:
            highest = my_list[i]
    return highest
