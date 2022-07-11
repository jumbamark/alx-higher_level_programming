#!/usr/bin/python3

"""
Module that defines a Base class for other classes in the project.
"""
import json
import os


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

    @staticmethod
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

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes the JSON string
        representation of list_objs

        Args:
            list_objs: list of instances who inherits of Base
        """
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string
        representation "json_string".

        Args:
            json_string: string to convert to list
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            dictionary: used as **kwargs

        Returns:
            instance created
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(10, 10)
        else:
            dummy = cls(10)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Deserializes csv file from a file.

        Returns:
            list of instances
        """
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        for csv_elem in csv_list:
            dict_csv = {}
            for kv in enumerate(csv_elem):
                dict_csv[list_keys[kv[0]]] = int(kv[1])
            matrix.append(dict_csv)

        list_ins = []

        for index in range(len(matrix)):
            list_ins.append(cls.create(**matrix[index]))

        return list_ins
