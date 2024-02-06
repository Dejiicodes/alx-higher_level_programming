#!/usr/bin/python3
"""
This module defines a function to save a Python object to a file in JSON format.
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a file in JSON format.

    Args:
        my_obj: The Python object to save.
        filename (str): The name of the file to save to.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)

if __name__ == "__main__":
    my_obj = {"name": "John", "age": 30, "city": "New York"}
    filename = "my_obj.json"
    save_to_json_file(my_obj, filename)
