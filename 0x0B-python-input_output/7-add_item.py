#!/usr/bin/python3
""" Appends arguments to a list and then saves it to a file. """

import sys

if __name__ == "__main__":
    # Import necessary functions
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        # Load the existing list
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # Initialize an empty list
        my_list = []

    # Append the arguments to the list
    my_list.extend(sys.argv[1:])

    # Save the list to a file
    save_to_json_file(my_list, "add_item.json")
