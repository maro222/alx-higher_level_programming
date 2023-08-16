#!/usr/bin/python3
def uniq_add(my_list=[]):
    sett = set(my_list)
    res = 0
    for x in sett:
        res += x
    return (res)
