#!/usr/bin/python3
"""
This module defines a function to write a string to a text file.
"""

def write_file(filename="", text=""):
    """
    Writes a string to a text file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)

if __name__ == "__main__":
    filename = "my_first_file.txt"
    text = "Holberton School"
    print(write_file(filename, text))
