#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):        
    def __init__(self, width, height):
        #validating input
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        #setting the variables to private
        self.__width = width
        self.__height = height
