#!/usr/bin/env python3

def factorial(n):
    """
    Find factorial of no till 1 to n and using generator to get next value 
    """
    
    
    result = 1
    while n > 0:
        result = result * n
        n = n -1
    return result 

def factorial1(n):
    for i in range(1, n+1):
        result = 1
        if i == 1:
            yield result 
        else:     
            while i > 0:
                result = result * i
                i = i -1
            yield result 
            



#print(factorial(6))
a = (factorial1(6))

for j in (factorial1(6)):
    print(j)
for k in (factorial1(6)):
    print(k)
