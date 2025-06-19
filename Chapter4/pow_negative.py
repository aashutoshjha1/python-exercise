#!/usr/bin/env python3

def pow(x,n):
   r = 1
   while n <= 0:
      r = r/ x
      print(r)
      n +=1
      print("hi")
   return r

print(pow(2,-2))
print(pow(2,-4))
