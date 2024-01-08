#!/usr/bin/python3
""" Module for the function is_kind_of_class. """

def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if it is an instance of a class
    that is inherited from, the specified class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or inherits from a_class,
        otherwise False.
    """
    return isinstance(obj, a_class)
