#!/usr/bin/python3
def uppercase(str):
    for c in range(str.len()):
        if ord(str[c]) >= 65 and ord(str[c]) <= 90:
            print("{:c}".format(str[c]), end='')
        else:
            print("{:c}".format(ord(str[c]) - 32), end='')
    print()
