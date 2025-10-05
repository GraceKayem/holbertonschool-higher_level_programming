#!/usr/bin/python3
"""
function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object
"""

import json


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.

    Args:
        obj: Instance of a class.

    Returns:
        dict: The dictionary representation of obj.
    """
    return obj.__dict__
