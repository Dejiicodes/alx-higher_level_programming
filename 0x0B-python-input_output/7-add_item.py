#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then save them to a file.
"""

import sys
import json
import os.path

args = sys.argv[1:]

if not os.path.exists("add_item.json"):
    with open("add_item.json", "w") as file:
        json.dump([], file)

with open("add_item.json", "r") as file:
    items = json.load(file)

if not isinstance(items, list):
    items = []

items.extend(args)

with open("add_item.json", "w") as file:
    json.dump(items, file)
