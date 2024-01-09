#!/usr/bin/python3
"""Module for add_attribute method."""


def add_attribute(obj, attr, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (object): The object to add an attribute to.
        attr (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
