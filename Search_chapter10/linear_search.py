#!/usr/bin/env python3


def search(new, s):
    for i in new:
        if i == s:
           return "found number in list"
    return "not found"


new = [2,3,10,4,3]
s = 4
print(search(new,s))

