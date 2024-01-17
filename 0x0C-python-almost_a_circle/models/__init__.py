#!/usr/bin/python3
"""Module base.py - This module establishes a Base class as the foundation for all other models in the project."""

class Base:
    """
    The Base class, serving as the cornerstone for all other classes within the project.
    It handles unique identification for each instance.
    """
    __nb_objects = 0  # Tracks the number of instances created

    def __init__(self, id=None):
        """
        Initializes a new Base instance.

        Parameters:
            id (int, optional): Unique identifier for the instance. Automatically generated if not provided.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
