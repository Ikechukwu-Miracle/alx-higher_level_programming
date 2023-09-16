#!/usr/bin/python3
"""The base model class for the project"""

class Base:
    """Base for all other classes in the project.

    Private Class Attributes:
        __nb_objects (int): number of instances of base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base class.

        Args:
            id (int): identity of new Base object.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
