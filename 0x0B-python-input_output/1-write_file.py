#!/usr/bin/python3
"""Module for task 1"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file
       (UTF8) and returns the number of characters written
    """
    with open(filename, 'w', encoding='UTF-8') as f:
        n_ch = f.write(text)
    return (n_ch)
