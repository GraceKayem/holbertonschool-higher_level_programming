#!/usr/bin/python3
"""
    Add two integers a and b 
"""

def add_integer(a, b=98):
    """
    Add two integers a and b 

    Args:
        a (int or float): num 1
        b (int, float or optional): num 2 - defaults to 98.

    Raises:
        TypeError: a must be an integer or b must be an integer

    Returns:
        int: a plus b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
