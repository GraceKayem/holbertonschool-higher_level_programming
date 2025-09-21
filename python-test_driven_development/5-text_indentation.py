#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ?, :

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Characters after which we add 2 new lines
    separators = {'.', '?', ':'}
    start = 0

    for i, char in enumerate(text):
        if char in separators:
            # Print the segment including the separator
            print(text[start:i+1].strip())
            print()
            start = i + 1

    # Print any remaining text after the last separator
    remaining = text[start:].strip()
    if remaining:
        print(remaining)
