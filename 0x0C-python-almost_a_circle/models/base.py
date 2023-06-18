#!/usr/bin/python3
"""Defines a base class"""


class Base:
    """Base class definition
    
    'base' for all other classes in this project
    
    Attributes:
        __nb_objects (int): The number of instatiated Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base
        
        Args:
            id (int): The id of the new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects