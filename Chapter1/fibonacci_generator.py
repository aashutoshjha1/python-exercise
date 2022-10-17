#!/usr/bin/env python3

def gen_fin():
    """
    This is generator function to get Fibonacci series.
    """
    a = 0
    b = 1
    while True:
      yield a 
      r = a+b
      a = b
      b = r
   

iter_obj = gen_fin()
print(iter_obj)
#print(iter_obj.next())
#print(next(iter_obj))
#print(next(iter_obj))
#print(next(iter_obj))
#print(next(iter_obj))
#print(next(iter_obj))
#print(next(iter_obj))
list1 = []
for i in range(10):
    list1.append(next(iter_obj))    
print(list1)


