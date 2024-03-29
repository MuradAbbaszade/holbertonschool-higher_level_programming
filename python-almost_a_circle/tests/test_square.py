#!/usr/bin/python3
"""Tests"""
import os
import unittest
from models.square import Square


class TestBase(unittest.TestCase):
    def test_square(self):
        s0 = Square(1, 2)
        self.assertEqual(s0.size, 1)
        self.assertEqual(s0.x, 2)
        s1 = Square(1, 2, 3)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_square1(self):
        s0 = Square(1, 2, 3, 4)
        self.assertEqual(s0.size, 1)
        self.assertEqual(s0.x, 2)
        self.assertEqual(s0.y, 3)
        self.assertEqual(s0.id, 4)

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_value_errors(self):
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        s0 = Square(1, id=66)
        self.assertEqual(str(s0), "[Square] (66) 0/0 - 1")

    def test_to_dictionary(self):
        s0 = Square(3, id=55)
        self.assertEqual(s0.to_dictionary(), {"id": 55, "size": 3, "x": 0, "y": 0})

    def test_update(self):
        s0 = Square(1, 2, 3, 4)
        s0.update(5, 6, 7, 8)
        self.assertEqual(s0.id, 5)

    def test_create(self):
        s0_dictionary = {"x": 3, "y": 4, "id": 89, "size": 1}
        s0 = Square.create(**s0_dictionary)
        self.assertEqual(str(s0), "[Square] (89) 3/4 - 1")

    def test_save_to_file(self):
        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([Square(1, 2, id=13)])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 13, "size": 1, "x": 2, "y": 0}]')

    def test_load_from_file1(self):
        try:
            os.remove("Square.json")
        except:
            pass

        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_2(self):
        try:
            os.remove("Square.json")
        except:
            pass

        s0 = Square(5, 5)

        inp = [s0]
        Square.save_to_file(inp)
        out = Square.load_from_file()

        self.assertEqual(inp[0].__str__(), out[0].__str__())
