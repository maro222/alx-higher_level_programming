#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    mylist = my_list.reverse()
    for i in range(len(mylist)):
        print("{:d}".format(i))
