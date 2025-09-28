#!/usr/bin/python3
"""
Write a function that returns True if the object is exactly an instance
of the specified class; otherwise False.
"""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class; otherwise False.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match.

    Returns:
        bool: True if obj is exactly an instance of a_class, else False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
