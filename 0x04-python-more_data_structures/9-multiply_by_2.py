#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    for key, val in new_dic.items():
        new_dic.update({key: val*2})
    return (new_dic)
