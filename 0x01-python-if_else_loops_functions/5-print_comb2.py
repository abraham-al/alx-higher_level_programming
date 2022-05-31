#!/usr/bin/python3
for num in range(0, 100):
    if num in [99]:
        print("{:d}".format(num))
        break
    print("{:02d}, ".format(num), end="")
