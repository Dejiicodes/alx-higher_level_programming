#!/usr/bin/python3
"""
This module defines a function to append a string to the end of a text file.
"""

def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)

if __name__ == "__main__":
    filename = "my_first_file.txt"
    text = "Holberton School"
    print(append_write(filename, text))
