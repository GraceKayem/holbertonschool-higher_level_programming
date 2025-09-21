#!/usr/bin/python3
"""
This module provides a function to print text with 2 new lines after
each '.', '?', or ':' character.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', or ':' character.

    Parameters:
    text (str): The text to be printed.

    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ".?:"
    start = 0

    for i, char in enumerate(text):
        if char in separators:
            segment = text[start:i + 1].strip()
            print(segment)
            print()
            start = i + 1

    remaining = text[start:].strip()
    if remaining:
        print(remaining)
