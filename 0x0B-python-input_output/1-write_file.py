#!/usr/bin/python3
"""Module to write a string into a text file."""


def write_file(filename="", text=""):
    """Writes a string into a text file.

    Args:
        filename (str): The path to the file to write.
        text (str): The text to write into the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
