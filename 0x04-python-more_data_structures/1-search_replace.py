#!/usr/bin/python3


def search_replace(my_list, search, replace):
     # Replaces all occurrrences of an element by another in new list
     new_list =  [replace if elem == search else elem for elem in my_list]
     # new_list = list(map
     #   ((lambda elem: replace if elem == search else elem), my_list))
     return new_list
