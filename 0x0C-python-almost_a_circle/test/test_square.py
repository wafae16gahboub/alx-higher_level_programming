#!/usr/bin/python3
"""Unittest Square class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8
import sys
from io import StringIO


class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        s1 = Square(10)
        self.assertEqual((s1.id), 1)
        r2 = Square(2, 10)
        self.assertEqual((r2.id), 2)
        r3 = Square(2, 0, 0, 12)
        self.assertEqual((r3.id), 12)

    def test_area_square(self):
        s1 = Square(3, 2)
        self.assertEqual(s1.area(), 9)
        s2 = Square(2, 10)
        self.assertEqual(s2.area(), 4)
        s3 = Square(8, 0, 12)
        self.assertEqual(s3.area(), 64)
        with self.assertRaises(TypeError):
            s4 = Square(1.5, 0, 12)
            print(s4.area())
        self.assertTrue("size must be an integer")

    def test_display_square(self):
        disp = "  ##\n  ##\n"
        s1 = Square(2, 2)
        tmp = StringIO()
        sys.stdout = tmp
        s1.display()
        self.assertEqual(tmp.getvalue(), disp)
        tmp.close()

        disp = "\n\n\n ###\n ###\n ###\n"
        s2 = Square(3, 1, 3)
        tmp = StringIO()
        sys.stdout = tmp
        s2.display()
        self.assertEqual(tmp.getvalue(), disp)
        tmp.close()

    def test_update_square(self):
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/1 - 7")

    def test_instance_to_dict_square(self):
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 1, 'x': 2,
                                        'size': 10, 'y': 1})

    def test_square_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/square.py'])
        self.assertEqual(result.total_errors, 0)
