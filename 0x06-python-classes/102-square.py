#!/usr/bin/python3
"""Defines a square with a specified size."""
class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initializes a new square.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If `value` is not a number (float or integer).
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.__size ** 2

    def __lt__(self, other):
        """Checks if the area of the current square is less than the area of another square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if the area of the current square is less than or equal to the area of another square."""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Checks if the area of the current square is equal to the area of another square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if the area of the current square is not equal to the area of another square."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Checks if the area of the current square is greater than the area of another square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if the area of the current square is greater than or equal to the area of another square."""
        return self.area() >= other.area()
