#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    mylist = [0, 0]
    for i in range(2):
        if i < len(tuple_a):
            mylist[i] += tuple_a[i]
        if i < len(tuple_b):
            mylist[i] += tuple_b[i]
    new_tuple = (mylist[0], mylist[1])
    del mylist
    return (new_tuple)
