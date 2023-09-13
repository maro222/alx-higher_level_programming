#!/usr/bin/python3
"""Module for task_6"""
import json


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file"""
    with open(filename, 'r', encoding='UTF-8') as f:
        obj = json.load(f)
    return obj
