#!/usr/bin/python3
"""
Module that defines a function add_integer(a, b=98)
which adds two numbers (integers or floats) after rounding them.
"""

def add_integer(a, b=98):
    """
    Add two integers or floats after rounding them.

    Args:
        a (int or float): first number
        b (int or float, optional): second number, defaults to 98

    Raises:
        TypeError: if a or b is not an int or float

    Returns:
        int: the sum of a and b after rounding
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return round(a) + round(b)
