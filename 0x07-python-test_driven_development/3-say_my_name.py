#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    temp = ""
    if type(first_name) != type(temp):
        raise TypeError("first_name must be a string ")
    if type(last_name) != type(temp):
        raise TypeError("last_name must be a string")
    print("My name is {}".format(first_name), end='')
    if last_name != "":
        print("{}".format(last_name), end='')
    print()


if __name__ == '__main__':
    import doctest
    doctest.testfile("3-say_my_name.txt")
