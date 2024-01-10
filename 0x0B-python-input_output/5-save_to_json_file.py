#!/usr/bin/python3
"""Module to write a Python object into a file in JSON format."""

import json


def save_to_json_file(my_obj, filename):
    """Writes a Python object into a text file in JSON format.

    Args:
        my_obj: The Python object to serialize.
        filename (str): The path of the file to write to.

    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
