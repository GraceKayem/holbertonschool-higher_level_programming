#!/usr/bin/python3
"""
4-print_square module

This module contains a function that prints a square using the # character.
"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for _ in range(size):
        print("#" * size)

