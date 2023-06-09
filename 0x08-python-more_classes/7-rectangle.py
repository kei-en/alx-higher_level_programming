#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Class Rectangle definition
    Attributes:
        number_of_instances (int): number of instances
        print_symbol (any): symbol used for string representation
    """
    number_of_instances = 0
    print_symbol = "#"

    @property
    def width(self):
        """Sets size to value"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """Initializes Rectangle with width"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def area(self):
        """Return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Return the printable representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""

        return ((str(self.print_symbol) * self.__width + "\n")
                * self.__height)[:-1]

    def __repr__(self):
        """Return the string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints message when instance is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
