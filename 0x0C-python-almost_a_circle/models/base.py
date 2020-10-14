#!/usr/bin/python3
"""COntains:
class Base
"""
import json


class Base:
    """This class is the Base of all other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Init method to create objects of class Base"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        list_objs is a list of instances who inherits of base.
        Example: list of Rectangle or list of Square instances
        """
        # the file name must be: "<Class name>.json"
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as f:
            # If the list_objs is none, save an empty list
            if list_objs is None:
                f.write("[]")
            else:
                # Create a list of dictionaries
                list_of_dict = []
                # Create a dictionary for each object parsed in list_objs
                for obj in list_objs:
                    # Use the instance method to_dictionary, to create
                    # a dictionary for each object
                    obj_to_dict = cls.to_dictionary(obj)
                    # Append each dicionary created, to the list_of_dict
                    list_of_dict.append(obj_to_dict)
                # Create a JSON string for the list_of_dict
                json_string = cls.to_json_string(list_of_dict)
                # Write json_string into the file
                f.write(json_string)
