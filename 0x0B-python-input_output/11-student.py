#!/usr/bin/python3
"""Module defining the Student class with JSON update capability."""


class Student:
    """Class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new instance of Student."""
        self.first_name = first_name    # Store the first name.
        self.last_name = last_name      # Store the last name.
        self.age = age                  # Store the age.

    def to_json(self, attrs=None):
        """Return a dictionary representation of the instance.

        Args:
            attrs (list): Attributes to include in the dictionary.

        Returns:
            dict: Dictionary of specified attributes.
        """
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            # Create a dictionary with specified attributes if they exist.
            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }
        # Return the default dictionary representation of the student.
        return self.__dict__

    def reload_from_json(self, json):
        """Update attributes from a dictionary.

        Args:
            json (dict): Dictionary of new attributes.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
