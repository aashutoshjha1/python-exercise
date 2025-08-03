#!/usr/bin/env python3

def binary_search(seq, num, low, high):
    
    if low == high:
       if low == num:
          return "number found"
       else:
          return "number not  found"
    if low < high:
       mid = (low+high) //2
       if seq[mid] == num:
          return f"found on index : {mid}"
       if seq[mid] < num:
          return binary_search(seq, num, mid+1, high)
       else:
           return binary_search(seq, num, low, mid -1)
    else:
        return "not found"    


seq = [2,3,4,5,6,8]
num = 4
print(binary_search(seq, num, 0, 5))


