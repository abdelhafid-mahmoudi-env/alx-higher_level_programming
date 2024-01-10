#!/usr/bin/python3
"""Module for managing JSON data."""

import sys
import os.path
from sys import argv
from importlib import import_module

# Check if the save_to_json_file and load_from_json_file functions exist
try:
    save_to_json_file = import_module('7-save_to_json_file').save_to_json_file
    load_from_json_file = import_module('8-load_from_json_file').load_from_json_file
except (ImportError, AttributeError):
    sys.exit(1)

json_filename = "add_item.json"
json_data = []

# Load existing data from the JSON file if it exists
if os.path.exists(json_filename):
    json_data = load_from_json_file(json_filename)

# Add command line arguments to the JSON data
for item in argv[1:]:
    json_data.append(item)

# Save the updated JSON data to the file
save_to_json_file(json_data, json_filename)
