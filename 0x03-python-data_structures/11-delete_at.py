#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if idx >= length or idx < 0:
        return (my_list)
    for i in range(idx, length - 1):
        my_list[i] = my_list[i + 1]
    del my_list[length - 1]
    return (my_list)
