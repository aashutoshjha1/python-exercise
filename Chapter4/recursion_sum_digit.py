#!/usr/bin/env python3
def recursion_sum(n):
    sum = 0
    num_str = str(n)
    length = len(str(n))
    while length >  0:
       sum = sum + int(num_str[length-1])
       length -=1
    return sum

print(recursion_sum(7898))

