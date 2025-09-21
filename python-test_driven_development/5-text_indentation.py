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

    for char in ".:?":
        text = text.replace(char, "{}\n".format(char))

    lines = text.splitlines()
    for i, line in enumerate(lines):
        print(line.strip(), end='' if i == len(lines) - 1 else '\n\n')
