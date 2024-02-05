#!/usr/bin/python3

class MyInt(int):
    """Subclass of int with == and != operators inverted."""

    def __eq__(self, other):
        """Return True if self is not equal to other."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Return True if self is equal to other."""
        return super().__eq__(other)
