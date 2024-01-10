#!/usr/bin/python3
""" Adds arguments to a list, then saves them in a file """

import sys

if __name__ == "__main__":
    # Importing the necessary functions
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        # Loading the existing list
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # Initializing an empty list
        items = []

    # Adding the arguments to the list
    items.extend(sys.argv[1:])

    # Saving the list in a file
    save_to_json_file(items, "add_item.json")
