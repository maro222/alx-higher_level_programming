#!/usr/bin/python3
"""module for task 9"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """instaniation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        area of thee Rectangle
        """
        return ((self.__width * self.__height))

    def __str__(self):
        """
        string format of the class
        """
        return (f"Rectangle {self.__width}/{self.__height}")
