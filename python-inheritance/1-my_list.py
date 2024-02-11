#!/usr/bin/python3
"""My list module"""


class MyList(list):
    """MyList"""
    def print_sorted(self):
        """Print sorted"""
        print(sorted(self))
