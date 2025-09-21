#!/usr/bin/python3
"""
This module provides a function to print a full name in a formatted way.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first name> <last name>'.

    Parameters:
    first_name (str): The first name of the person.
    last_name (str, optional): The last name of the person. Defaults to an empty string.

    Raises:
    TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}".strip())
