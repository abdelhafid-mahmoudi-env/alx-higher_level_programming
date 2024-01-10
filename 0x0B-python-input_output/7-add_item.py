#!/usr/bin/python3
"""A script that adds all command-line arguments to a Python list, and then saves them to a file."""

import sys

# Importing the necessary functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def main():
    filename = "add_item.json"

    try:
        # Loading the existing list from the file
        items = load_from_json_file(filename)
    except FileNotFoundError:
        # If the file does not exist, start with an empty list
        items = []

    # Add command-line arguments to the list
    items.extend(sys.argv[1:])

    # Save the updated list back to the file
    save_to_json_file(items, filename)
