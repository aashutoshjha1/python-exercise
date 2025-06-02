#!/usr/bin/env python3

print("enter no of row for pattern")
n = int(input())

for i in range(n):
    for j in range(0, i+1):
        print(j, end=" ")
    print()


