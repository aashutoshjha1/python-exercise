#!/usr/bin/env python3

def pair_prod(n):
    list2 = []
    for i in n:
        for j in n:
            if i == j:
                pass 
            else:
               list2.append((i,j)) 
    return list2


list = [2,3,4,2,3,5,6,7]
print(pair_prod(list))


