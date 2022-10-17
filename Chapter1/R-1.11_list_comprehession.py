#!/usr/bin/env python3

""" Demonstrate how to use Python’s list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256]. """
import math

list1 = [int(math.pow(2,a)) for a in range(0,20) if math.pow(2,a) <=256 ]

print(list1)

