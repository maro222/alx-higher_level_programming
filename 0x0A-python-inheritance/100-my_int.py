#!/usr/bin/python3
"""Module for advanced task"""


class MyInt(int):
    """class MyInt"""
    def __init__(self, num):
        self.num = num

    def __eq__(self, other):
        return (self.num != other)

    def __ne__(self, other):
        return (self.num == other)
