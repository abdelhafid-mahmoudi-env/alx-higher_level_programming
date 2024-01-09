#!/usr/bin/python3
"""
A module for reading and printing the contents of a text file.

This module provides a function to read a given text file and print its contents to standard output.
"""


def read_file(filename=""):
    """
    Read a text file and print its contents to stdout.

    Args:
        filename (str): The name of the file to be read.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
