#!/usr/bin/python3
"""Module for task 10"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area():
        """ area implementation"""
        return (self.__size * self.__size)
