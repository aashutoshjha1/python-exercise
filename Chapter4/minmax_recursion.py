#!/usr/bin/env python3

def minmax(seq, index = 0, min = None, max = None):
   if index == len(seq):
      return min, max

   if min is None or min > seq[index] :
      min = seq[index]
   if max is None or max < seq[index]:
       max = seq[index]
      
   return minmax(seq, index+1 , min , max)


eq = [8,3,4,5,6]
print(minmax(eq))
eq1 = [20,10,11,19,83,16,312,98]
print(minmax(eq1))
eq2 = [2]
print(minmax(eq2))
