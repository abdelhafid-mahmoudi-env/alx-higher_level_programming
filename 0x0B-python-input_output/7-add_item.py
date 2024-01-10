#!/usr/bin/python3
""" Adds arguments to a list, then saves it to a file """

import sys

if __name__ == "__main__":
    # Importing the necessary functions
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        # Loading the existing list
        current_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # Initializing an empty list
        current_list = []

    # Adding the arguments to the current list
    current_list.extend(sys.argv[1:])

    # Saving the current list to a file
    save_to_json_file(current_list, "add_item.json")
