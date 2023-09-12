#!/usr/bin/python3
"""Module for task 0"""


def read_file(filename=""):
    """ a function that reads a text file (UTF8) and prints it to stdout """
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
        for line in data:
            print(line, end="")
