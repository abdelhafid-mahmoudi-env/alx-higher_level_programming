#!/usr/bin/python3
"""Module for converting an object of a class to a dictionary for JSON."""

import sys

if __name__ == "__main__":
    save_json = __import__('5-save_to_json_file').save_to_json_file
    load_json = __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_json("add_item.json")
    except FileNotFoundError:
        # Initialisation d'une liste vide
        items = []

    items.extend(sys.argv[1:])

    save_json(items, "add_item.json")
