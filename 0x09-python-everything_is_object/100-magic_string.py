#!/usr/bin/python3
def magic_string():
    magic_string.x = getattr(magic_string, x, -1) + 1
    return "BestSchool" + ", BestSchool" * magic_string.x
