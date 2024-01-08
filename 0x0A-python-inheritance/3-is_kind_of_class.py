#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Contains a function that checks if an object is an instance of, or if the object
is an instance of a class that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an instance of a class
    that inherited from, the specified class.

    Args:
    obj (any): The object to be checked
    a_class (type): The class to compare against

    Returns:
    bool: True if obj is an instance of a_class or if obj is an instance of a class that
          inherited from a_class, otherwise False.
    """
    return isinstance(obj, a_class)

