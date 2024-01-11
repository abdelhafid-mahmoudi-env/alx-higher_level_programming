#!/usr/bin/python3
"""Module load add save"""

import sys
import os
import json
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


if not os.path.isfile("add_item.json"):
    initial_list = []
else:
    initial_list = load_from_json_file("add_item.json")

initial_list.extend(sys.argv[1:])

save_to_json_file(initial_list, "add_item.json")
