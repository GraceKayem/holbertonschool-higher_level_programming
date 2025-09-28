#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
Task based on 8-rectangle.py.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        # setting the variables to private
        self.__width = width
        self.__height = height

        # validating input
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    # the area() method must be implemented
    def area(self):
        return self.__width * self.__height

    # print() should print, and str() should return the rectangle description
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
