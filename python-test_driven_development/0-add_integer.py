#!/usr/bin/python3
"""
Add two integers a and b
"""

def add_integer(a, b=98):
    """
    Add two integers a and b.

    Args:
        a (int or float): first number
        b (int or float, optional): second number, defaults to 98

    Raises:
        TypeError: if a or b is not an int or float
        OverflowError: if float too large to convert to int

    Returns:
        int: the sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    try:
        a_int = int(a)
        b_int = int(b)
    except OverflowError:
        raise OverflowError("float too large to convert to int")

    return a_int + b_int
