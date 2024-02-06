#!/usr/bin/python3
"""
This module defines a function to multiply each value in a dictionary by 2.
"""

def multiply_by_2(a_dictionary):
    """
    Multiplies each value in a dictionary by 2.

    Args:
        a_dictionary (dict): The dictionary whose values are to be multiplied.

    Returns:
        dict: A new dictionary with the values multiplied by 2.
    """
    return {key: value * 2 for key, value in a_dictionary.items()}

if __name__ == "__main__":
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    new_dict = multiply_by_2(my_dict)
    print(new_dict)
