#!/usr/bin/env python3

def result_sum(func, arr):

   sum = 0
   for i in arr:
       if func(i):
           sum = sum +i
   return sum


arr = [4,5,3,6]
even_sum  = lambda x:x%2 == 0
odd_sum  = lambda y:y%2 !=0
 
print(result_sum(even_sum,arr))
print(result_sum(odd_sum,arr))
