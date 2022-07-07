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

    def to_json(self, attrs=None):
        """Retrieves the dictionary representation
        of a Student instance

        Args:
            attrs: list of attributes

        Returns:
            the dict representation of the instance.

        """

        if type(attrs) is list and all([type(x) == str for x in atttrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__.copy()
