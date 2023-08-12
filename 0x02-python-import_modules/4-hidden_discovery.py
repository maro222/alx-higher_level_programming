#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    for name in range(len(names)):
        if name[0] == '_' and name[1] == '_':
            continue
        print("{:s}".format(name))
