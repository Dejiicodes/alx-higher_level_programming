#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module containing a class for representing a square.

This module provides a simple implementation of a square.

Example:
    Create a square with side length 5:

    >>> square = Square(5)

Attributes:
    module_level_variable1 (int): An example module-level variable.
    module_level_variable2 (int): Another example module-level variable.

Todo:
    * Add support for calculating the area of the square.

"""

class Square:
    """Class representing a square.

    Attributes:
        side_length (int): The length of each side of the square.

    """

    def __init__(self, side_length=0):
        """Initialize a square with a given side length.

        Args:
            side_length (int, optional): The length of each side of the square.
                Defaults to 0.

        """
        self.side_length = side_length

    def calculate_area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.side_length ** 2

# Create an instance of the Square class with a side length of 5
my_square = Square(5)

# Calculate the area of the square
area = my_square.calculate_area()
print(f"The area of the square is: {area}")
