#!/usr/bin/env python3
import time

""" Demonstrate how to use Python’s list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256]. """
import math
start_time = time.time()

#list1 = [int(math.pow(2,a)) for a in range(0,20) if math.pow(2,a) <=256 ]
list2 = [int(math.pow(2,a)) for a in range(0,9)]

#print(list1)
print(list2)
end_time = time.time()
print(end_time-start_time)
