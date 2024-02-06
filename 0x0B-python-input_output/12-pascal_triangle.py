#!/usr/bin/python3
"""
This module defines a function to generate Pascal's triangle up to a specified number of rows.
"""

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): Number of rows to generate.

    Returns:
        list: List of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle

if __name__ == "__main__":
    n = 5
    print(pascal_triangle(n))
