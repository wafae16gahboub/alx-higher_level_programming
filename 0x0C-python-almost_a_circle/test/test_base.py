#!/usr/bin/python3
"""Unittest Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
import json
import pep8

class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        b1 = Base()
        self.assertEqual((b1.id), 1)

        b2 = Base(12)
        self.assertEqual((b2.id), 12)

        b3 = Base()
        self.assertEqual((b3.id), 2)

    def test_dic_to_json_str(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dict, str)

        s1 = Square(10, 7, 2)
        dictionary = s1.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dict, str)

        empty_dict = Base.to_json_string([])
        self.assertEqual(empty_dict, "[]")

        none_dict = Base.to_json_string(None)
        self.assertEqual(none_dict, "[]")

    def test_save_json_str_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()), [{"y": 8, "x": 2,
                                                    "id": 1, "width": 10,
                                                     "height": 7},
                                                   {"y": 0, "x": 0,
                                                     "id": 2, "width": 2,
                                                      "height": 4}])
        os.remove("Rectangle.json")

        s1 = Square(10, 7, 2)
        s2 = Square(2, 4)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            self.assertEqual(json.loads(file.read()), [{"x": 7, "id": 3,
                                                         "size": 10, "y": 2},
                                                        {"x": 4, "id": 4,
                                                          "size": 2, "y": 0}])
        os.remove("Square.json")

    def test_from_json_str_to_dic(self):
        list_input = [ {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7} ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

        list_output = Rectangle.from_json_string(None)
        self.assertEqual([], list_output)

        list_output = Rectangle.from_json_string([])
        self.assertEqual([], list_output)

    def test_create_dict_to_instane(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)
        self.assertTrue(r1, r2)
        self.assertFalse(r1 == r2)
        self.assertFalse(r1 is r2)

        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)
        self.assertTrue(s1, s2)
        self.assertFalse(s1 == s2)
        self.assertFalse(s1 is s2)

    def test_load_from_file_to_instance(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertNotEqual(list_rectangles_input, list_rectangles_output)
        self.assertTrue(list_rectangles_input, list_rectangles_output)
        self.assertFalse(list_rectangles_input == list_rectangles_output)
        self.assertFalse(list_rectangles_input is list_rectangles_output)

    def test_base_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base.py'])
        self.assertEqual(result.total_errors, 0)
