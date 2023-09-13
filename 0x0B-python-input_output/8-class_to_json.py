#!/usr/bin/python3
"""Module for task_8"""


def class_to_json(obj):
    """
     a function that returns the dictionary description with
     simple data structure (list, dictionary, string, integer and boolean)
     for JSON serialization of an object
    """
    dic = {}
    if '__dict__' in dir(obj):
        dic = obj.__dict__.copy()
    return dic
