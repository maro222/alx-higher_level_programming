#!/usr/bin/python3
"""A module for text_indentation """


def text_indentation(text):
    """A function"""
    temp = ""
    if type(text) != type(temp):
        raise TypeError("text must be a string")
    for ch in text:
        temp += ch
        if ch in ['.', '?', ':']:
            print(f"{temp.strip()}\n")
            temp = ""
    print(temp.strip(), end='')
