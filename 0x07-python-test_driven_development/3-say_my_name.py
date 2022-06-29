#!/usr/bin/python3

"""
This module contains a function that prints a full name
"""


def say_my_name(first_name, last_name=""):
    """Function that prints first name and last name

    Args:
        first_name: first name
        last_name: last name

    Raises:
        TypeError: If first_name or last_name is not string

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
