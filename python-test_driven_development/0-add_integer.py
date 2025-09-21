#!/usr/bin/python3
"""
0-add_integer module.

This module contains a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Return the sum of a and b, cast to integers if necessary.

    Args:
        a (int/float): first number to add
        b (int/float, optional): second number to add, default is 98

    Raises:
        TypeError: if a or b are not integers or floats

    Returns:
        int: sum of a and b as integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
