#!/usr/bin/python3
"""Module to convert a Python object into a JSON string."""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of a Python object.

    Args:
        my_obj: The Python object to serialize into JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
