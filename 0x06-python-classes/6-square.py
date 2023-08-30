#!/usr/bin/python3
""" This Module Contain Empty Class"""


class Square:
    """ define square Class of size attribute

        Attributes:
               size: (int) size of square
        methosd:
               __init__: initialize size of square
    """

    def __init__(self, size=0, position=(0, 0)):
        """ This is initialize magic class

        Args:
            size: size of Square instacnce
            position: position of square
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        self.__position = position

    @property
    def size(self):
        """ This function return value of __size

            Return:
                __size: (int)size of square
        """
        return (self.__size)

    @size.setter
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

    @property
    def position(self):
        """ return position os Square

            Return:
                __positon : position of square
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ set a new position to __posititon
            Args:
                position: the new position to be set
        """
        if type(value) is tuple and len(value) == 2:
            if type(value[0]) is int and type(value[1]) is int and
            value[0] >= 0 and value[1] >= 0:
                self.__position = value
            else:
                raise TypeError("position must be a tuple of"
                                "2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ This Method calculate the area of square

            Return:
                the Area of square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """this Method print square in # form"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()

            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end="")
                print()
