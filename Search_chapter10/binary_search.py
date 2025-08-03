#!/usr/bin/env python3

def binary_search(seq, num):
    
    low = 0
    high = len(seq) -1
    if low == high:
       if low == num:
          return "number found"
       else:
          return "not found"
    while low <= high:
       mid = low+high //2
       if seq[mid] == num:
          return f"found on index : {mid}"
       if seq[mid] < num:
          low = mid + 1
       else:
           high = mid - 1
    return "not found"    


seq = [2,3,4,5,6,8]
num = 4
print(binary_search(seq, num))

