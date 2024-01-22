#!/usr/bin/python3

def safe_print_integer(value):
    """
    Safely prints an integer value.

    Args:
    value (int): The integer value to be printed.

    Returns:
    bool: True if the integer was printed successfully, False otherwise.
    """
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    else:
        return True
