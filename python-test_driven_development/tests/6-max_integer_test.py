#!/usr/bin/python3
import unittest

max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
        
    def test1(self):
        self.assertIsNone(max_integer([]))

    def test2(self):
        self.assertEqual(max_integer([-1, -3, -5, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -5, -1]), -1)
        self.assertEqual(max_integer([1, 2, 5, 4, 3]), 5)
        
    def test3(self):
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)
        self.assertEqual(max_integer([5, 2, -3, 4]), 5)

    def test4(self):
        self.assertEqual(max_integer([1]), 1)
