#!/usr/bin/python3
"""COntains:
class Base
"""
import json
import os.path


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
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

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        # If the instance to create is of class Rectangle
        if cls.__name__ == "Rectangle":
            # Create a dummy instance of class Rectangle
            dummy_instance = cls(2, 3)
        # If the instance to create is of class Square
        if cls.__name__ == "Square":
            # Create a dummy instance of class Square
            dummy_instance = cls(2)
        # Update the dummy_instance with the values passed in **dictionary
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        # Filename must be <class name>.json
        file_name = cls.__name__ + ".json"
        instance_list = []
        # Try to open the filename and create the list of instances
        try:
            with open(file_name) as f:
                # Read the json file and save its contents
                json_string = f.read()
                # Use the static method from_json_strig to create a list
                # of dictionaries
                obj_list = cls.from_json_string(json_string)
                # Go through the list
                for dictio in obj_list:
                    # Create an instance using the dictionary
                    instance = cls.create(**dictio)
                    # Append the instance to the list
                    instance_list.append(instance)
                return instance_list
        except:
            # If ther filename doesnt exist, return an empty list
            return instance_list
