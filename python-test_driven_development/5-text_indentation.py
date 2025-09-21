#!/usr/bin/python3
"""
5-text_indentation module.

This module provides a function to print text with
two new lines after each '.', '?', and ':' character.
"""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?', or ':'"""
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    end_chars = ".?:"
    start = 0

    for i, char in enumerate(text):
        if char in end_chars:
            print(text[start:i + 1].strip())
            print()
            start = i + 1

    remaining = text[start:].strip()
    if remaining:
        print(remaining)
