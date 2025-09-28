#!/usr/bin/python3
"""
Return True if obj is an instance of a subclass (direct or indirect) 
of a_class; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a subclass (direct or indirect)
    of a_class; otherwise False.
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
