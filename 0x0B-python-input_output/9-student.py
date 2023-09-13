#!/usr/bin/python3
"""Module for task_9"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        res = {}
        res = self.__dict__.copy()
        return res
