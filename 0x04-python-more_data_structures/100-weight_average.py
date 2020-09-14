#!/usr/bin/python3
def weight_average(my_list=[]):
    # Returns the wheighted average of all integers tuple:
    # (<score>, <weight>)
    if not my_list or len(my_list) == 0:
        return 0
    dividend = 0
    divisor = 0
    for tup in my_list:
        dividend += tup[0] * tup[1]
        divisor += tup[1]
    return dividend / divisor
