#!/usr/bin/python3
"""
This module defines a function to convert a Python object to a JSON string.
"""

import json

def to_json_string(my_obj):
    """
    Converts a Python object to a JSON string.

    Args:
        my_obj: The Python object to convert.

    Returns:
        str: JSON string representation of the Python object.
    """
    return json.dumps(my_obj)

if __name__ == "__main__":
    my_obj = {"name": "John", "age": 30, "city": "New York"}
    print(to_json_string(my_obj))
