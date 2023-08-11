#!/usr/bin/python3
import sys
if __name__ == "__main__":

    len = len(sys.argv) - 1

    if len == 0:
        print("{:d} arguments.".format(0))
    elif len == 1:
        print("{:d} argument:".format(1))
    else:
        print("{:d} arguments:".format(len))
        for i in range(1, len + 1):
            print("{:d}: {:s}".format(i, sys.argv[i]))
