#!/usr/bin/python3
"""A script that adds all command-line arguments to a Python list, and then saves them to a file."""

import sys
import json

# Importing the necessary functions from previous tasks
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_items_to_list(filename, items):
    """Adds items to a list and saves it to a JSON file.

    Args:
        filename (str): The name of the file.
        items (list): A list of items to add.
    """
    try:
        current_list = load_from_json_file(filename)
    except (FileNotFoundError, json.JSONDecodeError):
        current_list = []

    current_list.extend(items)
    save_to_json_file(current_list, filename)
