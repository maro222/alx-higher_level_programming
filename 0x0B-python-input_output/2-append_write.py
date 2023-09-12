#!/usr/bin/python3
"""Module for task 2"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file
       (UTF8) and returns the number of characters added
    """
    with open(filename, 'a', encoding='UTF-8') as f:
        n_ch = f.write(text)
    return (n_ch)
