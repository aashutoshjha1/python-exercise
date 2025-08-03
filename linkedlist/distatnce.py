#!/usr/bin/env python3

def mindistance(a):

    count = {}
    dist = []
    
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[j] == a[i]:
                dist.append(j-i)
    return dist

a = [1, 2, 3, 4, 10]
print(mindistance(a))

