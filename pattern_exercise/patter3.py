#!/usr/bin/env python

print("enter no of row for pattern")
n = int(input())
print("\n")
for i in range(n):
    for j in range(i, -1, -1):
        print("*", end=" ")
    print()


