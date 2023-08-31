#!/usr/bin/env python3
for i in range(90, 65, -1):
    print("{:c}".format(i if (i % 2 == 0) else (i + 32)), end='')
