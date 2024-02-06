#!/usr/bin/python3
"""
This module defines a function to update a dictionary with a new key-value pair.
"""

def update_dictionary(a_dictionary, key, value):
    """
    Updates a dictionary with a new key-value pair.

    Args:
        a_dictionary (dict): The dictionary to be updated.
        key: The key to be added or updated.
        value: The value to be associated with the key.
    """
    a_dictionary[key] = value

if __name__ == "__main__":
    d = {'language': "C", 'number': 89, 'track': "Low level"}
    update_dictionary(d, 'language', "Python")
    print(d)
    update_dictionary(d, 'city', "San Francisco")
    print(d)
