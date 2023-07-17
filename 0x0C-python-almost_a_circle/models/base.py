#!/usr/bin/python3
"""Write the first class Base with a private class"""
import json
import os.path
import csv
import turtle


class Base:
    """This class will be the “base” of all other classes in this project.
     The goal of it is to manage id attribute in all your future classes
      and to avoid duplicating the same code (by extension, same bugs)

    nb_objects = private class attribute which is going to increment
                in case the id is None
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor

        Args:
            id ([int]): [increase id to avoid duplicating the same
             code]. Defaults to None.

        To call a class attribute it must be preced the name of the class
        or with the method __class__
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that return a JSON string representation

        The main features of a static method is that they can be
        called without having an instance of the class, plus such
        methods do not have access to the outside, so they cannot
        access any other attributes or call any other function within
        the class

        Args:
            list_dictionaries ([dict]): [list of dictionaries]

        Returns:

        json.dumps(): Output JSON object as string
        [can convert a Python object into a JSON string]
        """
        if list_dictionaries is None or not bool(list_dictionaries):
            return("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes the JSON string representation of
           list_objs to a file

        This method shares a feature with the static method, such a feature
        is that this method can be called without creating an instance of
        the class. The difference lies in the ability to access other
        methods and attributes of the class. However, such methods do not
        have access to instance attributes since no instance was created to
        be used

        Args:
            list_objs ([dict]): [list of dictionaries]

        """
        filename = cls.__name__ + ".json"
        ls = []
        # create and open a file
        with open(filename, mode="w", encoding="UTF8") as file:
            if list_objs is not None:
                # access to every object(instance) of the list
                for objs in list_objs:
                    """convert every object into a dictionary via function
                    to_dictionary and then append them into a list"""
                    ls.append(cls.to_dictionary(objs))
            """write or overwrite the file with the list of dictionaries
            previosuly created or a empty list in case list_objs is None"""
            file.write(cls.to_json_string(ls))

    @staticmethod
    def from_json_string(json_string):
        """Static method that returns the list of the JSON string
         representation

        Args:
            json_string ([string]): [ is a string representing a list of
             dictionaries]

        Returns:
            [list]: [return the list represented by json_string]

        json.loads(s): Load JSON data from a string [expects to get its
        text from a string object.]
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return list(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Create a Rectangle or Square instance with “dummy”
        mandatory attributes

        update the instance with the attributes inside dictionary

        Returns:
            [object]: [an instance with all attributes already set]
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(4, 3)
        elif cls.__name__ == 'Square':
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        json_ls = []
        filename = cls.__name__ + ".json"
        if os.path.isfile(filename):
            with open(filename, encoding="UTF8") as file:
                # read the JSON file (dictionary)
                json_dic = file.read()
                # convert from JSON dictionary into a list of strings
                json_list_of_str = cls.from_json_string(json_dic)
                for str_instance in json_list_of_str:
                    # create the instances and add them to the list
                    json_ls.append(cls.create(**str_instance))
            return json_ls
        else:
            return json_ls

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        ls = []
        # create and open a file
        with open(filename, mode="w", encoding="UTF8") as file:
            if list_objs is not None:
                # access to every object(instance) of the list
                for objs in list_objs:
                    """convert every object into a dictionary via function
                    to_dictionary and then append them into a list"""
                    ls.append(cls.to_dictionary(objs))
            """write or overwrite the file with the list of dictionaries
            previosuly created or a empty list in case list_objs is None"""
            file.write(cls.to_json_string(ls))

    @classmethod
    def load_from_file_csv(cls):
        csv_ls = []
        filename = cls.__name__ + ".csv"
        if os.path.isfile(filename):
            with open(filename, encoding="UTF8") as file:
                # read the JSON file (dictionary)
                csv_dic = file.read()
                # convert from JSON dictionary into a list of strings
                csv_list_of_str = cls.from_json_string(csv_dic)
                for str_instance in csv_list_of_str:
                    # create the instances and add them to the list
                    csv_ls.append(cls.create(**str_instance))
            return csv_ls
        else:
            return csv_ls

    @staticmethod
    def draw(list_rectangles, list_squares):
        """staticmethod"""
        screen = turtle.Screen()
        screen.setup(1200, 720)
        t = turtle.Turtle()
        t.penup()
        t.goto(-turtle.window_width() / 2, turtle.window_height() / 2)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.left(90)
        t.pendown()

        max_height = 0

        t.color("red", "pink")
        for r in list_rectangles:
            t.begin_fill()
            t.forward(r.width)
            t.right(90)
            t.forward(r.height)
            t.right(90)
            t.forward(r.width)
            t.right(90)
            t.forward(r.height)
            t.right(90)
            t.end_fill()
            t.penup()
            t.forward(r.width + 50)
            t.pendown()
            max_height = r.height if r.height >= max_height else max_height

        t.penup()
        t.goto(-turtle.window_width() / 2, turtle.window_height() / 2)
        t.forward(50)
        t.right(90)
        t.forward(max_height + 100)
        t.left(90)
        t.pendown()

        t.color("green", "cyan")
        for s in list_squares:
            t.begin_fill()
            t.forward(s.size)
            t.right(90)
            t.forward(s.size)
            t.right(90)
            t.forward(s.size)
            t.right(90)
            t.forward(s.size)
            t.right(90)
            t.end_fill()
            t.penup()
            t.forward(s.size + 50)
            t.pendown()

        turtle.done()
