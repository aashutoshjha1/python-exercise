#!/usr/bin/env python3

def factorial(n):
     if n == 0 or n == 1:
         factorail_result = 1
    
     else: 
         factorail_result = n * factorial(n-1)
         
     return factorail_result


print(factorial(5))

