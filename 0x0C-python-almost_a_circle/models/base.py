#!/usr/bin/python3
"""The base model class for the project"""
import json
import csv
import turtle


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON representation of a list of dictionaries.

        Arg:
            list_dictionaries (list): the list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of a list of objects to a file.

        Args:
            list_objs (list): list of inherited instances of Base
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jFile:
            if list_objs is None or list_objs == []:
                jFile.write("[]")
            else:
                dicts = []
                for obj in list_objs:
                    dicts.append(obj.to_dictionary())
                jFile.write(Base.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of JSON string represetation.

        Args:
            json_string (str): the JSON string
        """

        json_list = []
        if json_string is None or json_string == "{}":
            return json_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a class initialized from a dictionary of attributes.

        Args:
            dictionary (dict): key/value pair being analyzed
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                newInst = cls(1, 1)
            else:
                newInst = cls(1)
            newInst.update(**dictionary)
            return newInst

    @classmethod
    def load_from_file(cls):
        """Returns a list of classes instantiated from a JSON string file"""

        filename = f"{cls.__name__}.json"

        try:
            with open(filename) as jFile:
                jFile_data = jFile.read()
                dicts = Base.from_json_string(jFile_data)
                return [cls.create(**dic) for dic in dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writs CSV representation of the a list of objects to a file.

        Arg:
            list_objs (list): a list of class instances that inherits
            from base.
        """
        filename = f"{cls.__name__}.csv"
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        else:
            fieldnames = ["id", "size", "x", "y"]

        with open(filename, "w", newline="") as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
            for o in list_objs:
                writer.writerow(o.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of classes instantiated from a csv file"""

        filename = f"{cls.__name__}.csv"

        try:
            with open(filename, mode="r", newline="") as csvFile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                dicts = csv.DictReader(csvFile, fieldnames=fieldnames)
                dicts = [dict([key, int(val)] for key, val in dic.items())
                         for dic in dicts]
                return [cls.create(**dic) for dic in dicts]
        except FileNotFoundError:
            return []

        @staticmethod
        def draw(list_rectangles, list_squares):
            """Draws Rectangles and squares using turtle.

            Args:
                list_rectangles (list): list of Rectangle objects
                list_squares (list): list of square objects
            """
            t = turtle.Turtle()
            t.screen.bgcolor("#000000")
            t.pensize(3)

            t.color("#ffffff")
            for rec in list_rectangles:
                t.showturtle()
                t.up()
                t.goto(rec.x, rec.y)
                t.down()
                t.begin_fill()
                t.fillcolor("#ffff00")
                for _ in range(2):
                    t.forward(rec.width)
                    t.left(90)
                    t.forward(rec.height)
                    t.left(90)
                t.hideturtle()

            for sq in list_squares:
                t.showturtle()
                t.up()
                t.goto(sq.x, sq.y)
                t.down()
                t.begin_fill()
                t.fillcolor("#ffff00")
                for _ in range(4):
                    t.forward(sq.width)
                    t.left(90)
                t.hideturtle()
