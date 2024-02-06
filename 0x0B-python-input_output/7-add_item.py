#!/usr/bin/python3
"""
This module defines a function to load, add, and save to a JSON file.
"""

import json

def add_item_to_json_file(filename, key, value):
    """
    Loads a JSON file, adds a new key-value pair, and saves the updated JSON to the file.

    Args:
        filename (str): The name of the JSON file to load from and save to.
        key: The key to add to the JSON.
        value: The value associated with the key.
    """
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    data[key] = value
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(data, file)

if __name__ == "__main__":
    filename = "add_item.json"
    key = "name"
    value = "John"
    add_item_to_json_file(filename, key, value)
