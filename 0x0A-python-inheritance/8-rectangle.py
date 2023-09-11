#!/usr/bin/python3
"""module for task 8"""


class BaseGeometry:
    """
    class BaseGeometry
    """
    def area(self):
        """
        raise an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        that validates value:
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """instaniation"""
        BaseGeometry.integer_validator("width", width)
        self.__width = width
        BaseGeometry.integer_validator("height", height)
        self.__height = height
