#!/usr/bin/python3
"""module for advance task"""


def add_attribute(obj, attr_name, attr_value):
    """function for add attribute if possible"""
    if '__dict__' not in dir(obj):

        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
