#!/usr/bin/python3
"""
Module 4-inherits_from
Contains a function that checks if the object is an instance of a class that
inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or
    indirectly) from the specified class. It returns False if the object is an
    instance of the class itself.

    Args:
    obj (any): The object to be checked
    a_class (type): The class to compare against

    Returns:
    bool: True if obj is an instance of a subclass of a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
