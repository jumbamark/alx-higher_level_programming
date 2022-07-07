#!/usr/bin/python3

"""
Module containing a function that counts number of lines in a file
"""


def number_of_lines(filename=""):
    """
    writes a string to a text file (UTF8) and returns the number
    of characters written

    Args:
        filename: name of the file

    Returns:
        number of lines

    """

    count = 0

    with open(filename, encoding="utf-8") as f:
        for line in f:
            count += 1

    return count
