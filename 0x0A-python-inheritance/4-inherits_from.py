#!/usr/bin/python3
"""Defines an inherited class-checking function."""



def inherits_from(obj, a_class):
    '''the object is an instance of a class that inherited (directly or indirectly)
    obj (any): The object to check.
    a_class (type): The class to match the type of obj to.
    returns None
    '''
    return type(obj) != a_class and isinstance(obj, a_class)
