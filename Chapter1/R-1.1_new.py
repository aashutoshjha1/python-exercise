#!/usr/bin/env python3

def is_multiple(n,m):
    if n % m == 0:
        return True
    else:
        return False

print(is_multiple(8,2))

print(is_multiple(8,3))
print(is_multiple(15,1))
print(is_multiple(15,3))


