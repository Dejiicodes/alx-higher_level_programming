#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Safely performs division and prints the result.

    Args:
    a (float): The numerator.
    b (float): The denominator.

    Returns:
    float or None: The result of the division if successful, None if there was an error (e.g., division by zero).
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
