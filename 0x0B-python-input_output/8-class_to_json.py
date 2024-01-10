#!/usr/bin/python3
"""Module for converting an object of a class to a dictionary for JSON."""


def class_to_json(obj):
    """Return the description of an object for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary describing the object.
    """
    return obj.__dict__
