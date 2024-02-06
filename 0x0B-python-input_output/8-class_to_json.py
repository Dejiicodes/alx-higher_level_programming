#!/usr/bin/python3
"""
This module defines a function to load, add, and save to a JSON file.
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

def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a file in JSON format.

    Args:
        my_obj: The Python object to save.
        filename (str): The name of the file to save to.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)

def load_add_save(filename, key, value):
    """
    Loads a JSON file, adds a new key-value pair, and saves the updated JSON to the file.

    Args:
        filename (str): The name of the JSON file to load from and save to.
        key: The key to add to the JSON.
        value: The value associated with the key.
    """
    try:
        data = load_from_json_file(filename)
    except FileNotFoundError:
        data = {}
    data[key] = value
    save_to_json_file(data, filename)

if __name__ == "__main__":
    filename = "add_item_advanced.json"
    key = "name"
    value = "John"
    load_add_save(filename, key, value)
