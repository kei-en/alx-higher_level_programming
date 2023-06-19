#!/usr/bin/python3
"""Defines a base class"""
import json


class Base:
    """Base class definition

    'base' for all other classes in this project

    Attributes:
        __nb_objects (int): The number of instatiated Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base

        Args:
            id (int): The id of the new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON representation of a list of dictionaries

        Args:
            list_dictionaries (list): A list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of list_objs to a file

        Args:
            list_objs (list): A list of instances inherited from Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation 'json_string'

        Args:
            json_string (str): A string representation of a list of dictionaries
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
