#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """subclass for the list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints out the sorted list"""
        print(sorted(self))
