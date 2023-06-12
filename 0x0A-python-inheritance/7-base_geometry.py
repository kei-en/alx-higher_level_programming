#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Represent base geometry"""

    def area(self):
        """No implementation"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer
        Args:
            name (str): The name of the parameter
            value (int): The parameter to validate
            Return:
                TypeError: If value is not an integer
                TypeError: if value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be greater than 0".format(name))
