#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        if ord(str[c]) >= 65 and ord(str[c]) <= 90:
            num = 0
        else:
            num = 32
        print("{:c}".format(ord(str[c]) - num), end='')
    print()
