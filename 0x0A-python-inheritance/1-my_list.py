#!/usr/bin/python3

class MyList(list):
    """Custom list class."""

    def print_sorted(self):
        """Prints the sorted list."""
        print(sorted(self))

# Test cases
my_list = MyList()
my_list.append(4)
my_list.append(2)
my_list.append(1)
my_list.append(3)
my_list.print_sorted()
