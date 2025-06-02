#!/usr/bin/env python3

def pair_prod(n):
    list2 = []
    for i in n:
        for j in n:
           if i == j:
               pass
           elif ((i * j) % 2) == 0:
                list2.append((i,j))
            
    return list2

list2 = [3,4,5,6,8,2]
print(pair_prod(list2)) 
