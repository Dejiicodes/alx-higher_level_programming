#!/usr/bin/python3

class MyList(list):
    """Subclass of list that prints sorted list."""

    def print_sorted(self):
        """Print the list, but sorted (ascending sort)."""
        print(sorted(self))
