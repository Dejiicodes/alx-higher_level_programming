#!/usr/bin/python3
"""Defines a class that does the same as the given Python bytecode."""
import math

class MagicClass:
    """Defines a class that does the same as the given Python bytecode."""

    def __init__(self, radius=0):
        """Initializes a new MagicClass instance.

        Args:
            radius (int): The radius of the circle (default is 0).
        """
        self.__radius = 0
        self.radius = radius

    @property
    def radius(self):
        """Retrieves the radius of the circle."""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Sets the radius of the circle.

        Args:
            value (int): The radius of the circle.

        Raises:
            TypeError: If `value` is not a number (float or integer).
        """
        if not isinstance(value, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = value

    def area(self):
        """Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
