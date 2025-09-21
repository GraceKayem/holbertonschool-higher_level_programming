#!/usr/bin/python3
"""
4-print_square module

This module contains a function that prints a square using the # character.
"""


def print_square(size):
    """
    Prints a square of the given size using the '#' character.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')

    for x in range(size):
        print('#' * size)
