#!/usr/bin/python3
"""module for task 4"""


def inherits_from(obj, a_class):
    """Write a function that returns True if the object is an
       instance of a class that inherited (directly or indirectly)
       from the specified class ; otherwise False.
    """
    if type(obj) != a_class:
        return (issubclass(type(obj), a_class))
    return (False)
