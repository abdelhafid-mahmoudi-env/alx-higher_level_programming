mport sys
import os
import json
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Check if the JSON file exists, if not, create an empty list
if not os.path.isfile("add_item.json"):
    initial_list = []
else:
    initial_list = load_from_json_file("add_item.json")

# Extend the list with command-line arguments
initial_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(initial_list, "add_item.json")
