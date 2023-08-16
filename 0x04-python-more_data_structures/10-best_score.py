#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    mmax, key = float('-inf'), ""
    for k, v in a_dictionary.items():
        if mmax < v:
            mmax = v
            key = k
    return (key)
