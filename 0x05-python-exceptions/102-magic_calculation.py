#!/usr/bin/python3

def magic_calculation(a, b):
    """
    Performs a magic calculation based on the values of 'a' and 'b'.

    Args:
    a (int): An integer value.
    b (int): Another integer value.

    Returns:
    int: The result of the magic calculation.
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += (a ** b) / i
        except Exception as e:
            result = b + a
            break
    return result
