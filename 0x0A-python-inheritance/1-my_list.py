#!/usr/bin/python3
"""module for task 1"""


class MyList(list):
    """function that prints the list, but sorted (ascending sort)"""
    def print_sorted(self):
        print(sorted(self))
