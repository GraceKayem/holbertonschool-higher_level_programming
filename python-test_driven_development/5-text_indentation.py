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

    for l in '.:?':
        text = text.replace(l, '{}\n'.format(l))
    lines = text.splitlines()
    for index, line in enumerate(lines):
        print(line.strip(), end='' if index == len(lines) - 1 else '\n\n')
