#!/usr/bin/python3
"""
function that writes an Object to a text file, using a JSON representation
"""


import json

def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file in JSON format.

    Args:
        my_obj: The Python object to serialize.
        filename: The name of the file to write to.

    Returns:
        None
    """
    
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dumps(my_obj, file)
