#!/usr/bin/python3
"""
This module defines a function to convert a JSON string to a Python object.
"""

import json

def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: Python object represented by the JSON string.
    """
    return json.loads(my_str)

if __name__ == "__main__":
    my_str = '{"name": "John", "age": 30, "city": "New York"}'
    print(from_json_string(my_str))
