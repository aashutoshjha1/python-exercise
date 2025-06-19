#!/usr/bin/env python3
import sys

list1 = [2,3,4,5]
list2 = [6,7,8,9]

def list_mult(a,b):
    c = []
    for i,j in zip(a,b):
        num = i*j
        c.append(num)
    return c


print(list_mult(list1, list2))


       

   
