#!/usr/bin/python3
"""COntains:
Function load_from_json_file
"""


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    import json
    with open(filename, "r") as f:
        json_object = json.load(f)
    return json_object
