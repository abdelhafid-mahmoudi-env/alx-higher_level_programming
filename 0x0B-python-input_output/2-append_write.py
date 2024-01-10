#!/usr/bin/python3
"""Module to append a string to the end of a text file."""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file.

    Args:
        filename (str): The path to the file to be modified.
        text (str): The text to append to the end of the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
