#!/usr/bin/python3
"""Module for task_12"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a
       list of lists of integers representing the Pascal’s triangle of n
    """
    my_list = []
    llist = []

    if n <= 0:
        return []
    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                llist.append(1)
            else:
                llist.append(my_list[i-1][j-1] + my_list[i-1][j])
        my_list.append(llist.copy())
        llist.clear()
    return my_list
