#!/usr/bin/python3


# Removes all characters c and C from string
def no_c(my_string):
    new_string = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            # my_string[i] not in "Cc"
            new_string += my_string[i]
    return new_string
