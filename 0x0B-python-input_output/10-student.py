#!/usr/bin/python3

"""Module that defines the class Student(based on 9-student.py)
"""


class Student:
    """class Student tha defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves the dictionary representation
        of a Student instance

        Args:
            attrs: list of attributes

        Returns:
            the dict representation of the instance.

        """

        my_dict = dict()
        if type(attrs) is list and all([type(x) is str for x in atttrs]):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
                return my_dict
            return self.__dict__.copy()
