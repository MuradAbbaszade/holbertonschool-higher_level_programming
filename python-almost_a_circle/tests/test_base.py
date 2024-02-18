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

    def test5(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 12}]), '[{"id": 12}]')

    def test6(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{"id": 89}])

if __name__ == "__main__":
    unittest.main()
