#!/usr/bin/pyhton3


# Deletes an element of a list at a given index
def delete_at(my_list=[], idx=0):
    if idx >= len(my_list) or idx < 0:
        return my_list
    del my_list[idx]
    return my_list
