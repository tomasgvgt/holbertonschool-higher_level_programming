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
    arguments = load_from_json_file(filename)
except:
    arguments = []

arguments.extend(sys.argv[1:])
save_to_json_file(arguments, filename)
