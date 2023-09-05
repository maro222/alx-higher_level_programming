#!/usr/bin/python3
""" this a module for class Rectangle"""


class Rectangle:
    """ this is an empty Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Instantiation"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for width attribute"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setter for width attribute"""
        if type(value) is not int:
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ calcul the area of rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ calculthe perimeter of rectangle"""
        if (self.__height == 0 or self.__width == 0):
            return 0
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """ magic method str() """
        if self.__width == 0 or self.__height == 0:
            return ""
        return (((str(self.print_symbol) * self.__width) + "\n")
                * self.__height)[:-1]

    def __repr__(self):
        """repr() should return a string representation
           of the rectangle to be able to recreate a new instance
           by using eval() (see example below) """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return rect_1
        else:
            return rect_2
