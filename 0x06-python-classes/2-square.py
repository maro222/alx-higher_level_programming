#!/usr/bin/python3
""" This Module Contain Empty Class"""


class Square:
    """ define square Class of size attribute

        Attributes:
               size: (int) size of square
        methosd:
               __init__: initialize size of square
    """

    def __init__(self, size=0):
        """ This is initialize magic class

        Args:
            size: size of Square instacnce
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
