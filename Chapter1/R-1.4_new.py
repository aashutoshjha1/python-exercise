#!/usr/bin/env python3

def square(n):
     sum = 0 
     for i in range(n):
         sum  = sum + i*i
         
     return sum
     
print(square(10))
print(square(3))

