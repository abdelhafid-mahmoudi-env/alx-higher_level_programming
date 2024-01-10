#!/usr/bin/python3
import sys
import os.path
import json

def save_to_json_file(my_obj, filename):
    """Save an object to a JSON file."""
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)

def load_from_json_file(filename):
    """Load an object from a JSON file."""
    if not os.path.exists(filename):
        return []
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    filename = "add_item.json"
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []

    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, filename)
