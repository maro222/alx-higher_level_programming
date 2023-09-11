#!/usr/bin/python3
"""module for task 6"""


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
