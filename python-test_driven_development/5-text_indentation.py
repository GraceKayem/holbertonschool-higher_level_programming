#!/usr/bin/python3
"""
5-text_indentation module.

This module provides a function to print text with
two new lines after each '.', '?', and ':' character.
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    end_chars = ".?:"
    start = 0

    for index, char in enumerate(text):
        if char in end_chars:
            print(text[start:index + 1].strip())
            print()
            start = index + 1

    remaining = text[start:].strip()
    if remaining:
        print(remaining)
