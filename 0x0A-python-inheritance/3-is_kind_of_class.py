#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    '''function: is_kind_of_class
    obj: an object
    a_class: a class
    Returns: Bool
    '''
    return isinstance(obj, a_class)
