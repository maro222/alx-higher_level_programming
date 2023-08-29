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

    def area(self):
        """ This Method calculate the area of square

            Return:
                the Area of square
        """
        return (self.__size * self.__size)

    def size(self):
        """ This function return value of __size

            Return:
                __size: (int)size of square
        """
        return (self.__size)

    def size(self, size):
        """ This function set value of __size

            Args:
                size: (int)size to be set to __size
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
