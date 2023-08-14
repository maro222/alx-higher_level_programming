#!/usr/bin/python3i
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    mmax = my_list[0]
    for i in range(1, len(my_list)):
        if mmax < my_list[i]:
            mmax = my_list[i]
    return (mmax)
