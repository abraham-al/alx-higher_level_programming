#!/usr/bin/python3
for chars in range(97, 123):
    if chars != 101 and chars != 113:
        print("{:c}".format(chars), end="")
