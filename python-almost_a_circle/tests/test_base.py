#!/usr/bin/python3
"""Base model"""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    def test1(self):
        base_instance = Base(1)
        self.assertEqual(base_instance.id, 1)

    def test2(self):
        base_instance = Base(-1)
        self.assertEqual(base_instance.id, -1)

    def test3(self):
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)
        base_instance = Base(None)
        self.assertEqual(base_instance.id, 2)

    def test4(self):
        base_instance = Base("a")
        self.assertEqual(base_instance.id, "a")

if __name__ == "__main__":
    unittest.main()
