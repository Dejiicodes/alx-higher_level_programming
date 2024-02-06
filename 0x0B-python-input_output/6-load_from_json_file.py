#!/usr/bin/python3
"""
This module defines a function to create a Python object from a JSON file.
"""

import json

def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load from.

    Returns:
        object: Python object loaded from the JSON file.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)

if __name__ == "__main__":
    filename = "my_obj.json"
    print(load_from_json_file(filename))
