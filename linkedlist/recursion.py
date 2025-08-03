#!/usr/bin/env python3

def power(n, x):
   
    if x == 0 :
       return 1 
    elif x == 1:
        return n
    else:
        return n * power( n, x-1)

if __name__ == '__main__':

   print(power(2,3))
   print(power(2,0))
   print(power(2,8))


