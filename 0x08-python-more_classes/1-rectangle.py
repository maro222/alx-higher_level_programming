#!/usr/bin/python3
""" this a module for class Rectangle"""


class Rectangle:
    """ this is an empty Rectangle class"""

    def __init__(self, width=0, height=0):
        """ Instantiation"""
        self.width(width)
        self.height(height)

    @property
    def width(self):
        """getter for width attribute"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setter for width attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """getter for height attribute"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setter for height attribute"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
