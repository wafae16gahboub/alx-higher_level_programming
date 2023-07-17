#!/usr/bin/python3
"""Unittest Rectangle class"""
import unittest
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8
import sys
from io import StringIO


class TestRectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual((r1.id), 1)
        r2 = Rectangle(2, 10)
        self.assertEqual((r2.id), 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual((r3.id), 12)
        r4 = Rectangle(10, 2, 0, 0)
        self.assertEqual((r4.id), 3)

    def test_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        self.assertTrue("height must be an integer")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        self.assertTrue("width must be > 0 ")
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        self.assertTrue("width must be an integer")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.height = -10
        self.assertTrue("height must be > 0 ")
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        self.assertTrue("x must be an integer")
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)
        self.assertTrue("y must be >= 0")
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.y = {}
        self.assertTrue("y must be an integer")
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1, 3)
        self.assertTrue("x must be >= 0")

    def test_area_rectangle(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)
        with self.assertRaises(TypeError):
            r4 = Rectangle(1.5, 5.6, 0, 0, 12)
            print(r4.area())
        self.assertTrue("width must be an integer")

    def test_display_rectangle(self):
        disp = "####\n####\n####\n"
        r1 = Rectangle(4, 3)
        tmp = StringIO()
        sys.stdout = tmp
        r1.display()
        self.assertEqual(tmp.getvalue(), disp)
        tmp.close()

        disp = "\n\n  ##\n  ##\n  ##\n"
        r2 = Rectangle(2, 3, 2, 2)
        tmp = StringIO()
        sys.stdout = tmp
        r2.display()
        self.assertEqual(tmp.getvalue(), disp)
        tmp.close()

    def test_str_rectangle(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 5/5")

    def test_update_rectangle(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")     
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (2) 10/10 - 10/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")

    def test_instance_to_dict_rectangle(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 1,
                                        'height': 2, 'width': 10})

    def test_rectangle_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/rectangle.py'])
        self.assertEqual(result.total_errors, 0)
