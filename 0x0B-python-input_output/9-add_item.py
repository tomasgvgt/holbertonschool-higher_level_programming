#!/usr/bin/python3
"""script that adds all arguments to a Python list
and then save them to a file
"""


import json
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
filename = "add_item.json"

try:
    # Tries to load the content of the json file into my_list
    my_list = load_from_json_file(filename)
except:
    # If the file doesnt existe yet, create an empty list
    my_list = []

# Extend the list adding all the arguments starting from argument 1
my_list.extend(sys.argv[1:])
# Writes my_list into the file, in json format
save_to_json_file(my_list, filename)
