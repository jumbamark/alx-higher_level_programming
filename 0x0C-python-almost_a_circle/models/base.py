#!/usr/bin/python3

"""
Module that defines a Base class for other classes in the project.
"""
import json
import os
import csv


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs in csv format
        and saves it to a file

        Args:
            list_objs: list of instances
        """

        if (type(list_objs) != list and
           list_objs is not None or
           not all(isinstance(x, cls) for x in list_objs)):
            raise TypeError("list_objs must be a list of instances")

        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as f:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file.

        Returns:
                list of instances
        """
        filename = cls.__name__ + ".csv"
        my_list = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                reader = csv.reader(f, delimiter=',')
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                for x, row in enumerate(reader):
                    if x > 0:
                        i = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(i, fields[j], int(e))
                        my_list.append(i)
        return my_list
