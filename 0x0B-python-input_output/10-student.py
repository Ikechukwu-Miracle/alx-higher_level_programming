#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """A Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes an instance of the student class.

        Args:
            first_name (str): the first name of the student
            last_name (str): the last name of the student
            age (int): the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student class

        Arg:
            attrs (list): attribute to represent
        """
        if type(attrs) == list:
            for elem in attrs:
                if (type(elem)) == str:
                    return {x: getattr(self, x) for x in attrs \
                        if hasattr(self, x)}
        return self.__dict__
