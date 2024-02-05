#!/usr/bin/python3

class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Raise an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")
