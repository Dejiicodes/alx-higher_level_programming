#!/usr/bin/python3

"""
This module defines a class MyList that inherits from list.
"""


class MyList(list):
    """Custom list class."""

    def print_sorted(self):
        """Prints the list in sorted order."""
        print(sorted(self))

# Test cases
if __name__ == "__main__":
    ml = MyList()
    ml.append(1)
    ml.append(3)
    ml.append(2)
    ml.append(-1)
    ml.append(-5)
    ml.append(-3)
    ml.append(0)
    ml.print_sorted()
