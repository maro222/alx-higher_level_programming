#!/usr/bin/python3
"""module for task 1"""


class MyList(list):
    """class that have print_sorted function"""
    def print_sorted(self):
        """function that prints the list, but sorted (ascending sort)"""
        print(sorted(self))
