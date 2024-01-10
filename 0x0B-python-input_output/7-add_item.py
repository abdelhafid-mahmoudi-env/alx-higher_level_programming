#!/usr/bin/python3
"""Module for managing JSON data."""

import json
import os.path
import sys
from sys import argv

# Rename the functions as needed
save_json_data = __import__('7-save_to_json_file').save_to_json_file
load_json_data = __import__('8-load_from_json_file').load_from_json_file

json_filename = "add_item.json"
json_data = []

if os.path.exists(json_filename):
    json_data = load_json_data(json_filename)

for item in argv[1:]:
    json_data.append(item)

save_json_data(json_data, json_filename)
