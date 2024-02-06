#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then save them to a file.
"""

import sys
import os.path

args = sys.argv[1:]

if not os.path.exists("add_item.json"):
    with open("add_item.json", "w") as file:
        file.write("[]")

with open("add_item.json", "r") as file:
    data = file.read()
    if data:
        items = eval(data)
    else:
        items = []

items.extend(args)

with open("add_item.json", "w") as file:
    file.write(str(items))
