#!/usr/bin/python3
"""Module for inserting a line after a specific string in a file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text after a line containing a specific string.

    Args:
        filename (str): The path to the file to be modified.
        search_string (str): The string to search for in the file.
        new_string (str): The new string to insert.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

