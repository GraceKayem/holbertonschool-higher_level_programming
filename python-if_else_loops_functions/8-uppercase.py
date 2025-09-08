#!/usr/bin/python3
def uppercase(string):
    for i in string:
        if 97 <= ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print()