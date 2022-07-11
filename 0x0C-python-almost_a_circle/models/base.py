#!/usr/bin/python3

"""
Module that defines a Base class for other classes in the project.
"""
import json


class Base:
    """Represents a Base class with a private class attribute.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of a Base instance

        Args:
            id: id of the instance
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Method that returns the JSON string representation
        of list_dictionaries.

        Args:
            list_dictionaries: list of dictionaries
        Returns:
            If "list_dictionaries" is "None" or empty return "[]"
            Otherwise, return the JSON string representation
            of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or
           not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)
