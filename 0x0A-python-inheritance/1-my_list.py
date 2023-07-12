#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """a subclass for list"""
    def __init__(self):
        """initializing the object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
