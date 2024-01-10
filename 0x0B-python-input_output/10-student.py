#!/usr/bin/python3
"""Module defining the Student class with attribute filtering."""


class Student:
    """Class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new instance of the Student class.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name  # Store the first name.
        self.last_name = last_name    # Store the last name.
        self.age = age                # Store the age.

    def to_json(self, attrs=None):
        """Convert the Student instance to a dictionary.

        Args:
            attrs (list): List of attributes to include in the dictionary.

        Returns:
            dict: A dictionary containing selected attributes of the student.
        """
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            # Create a dictionary with specified attributes if they exist.
            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }
        # Return the default dictionary representation of the student.
        return self.__dict__
