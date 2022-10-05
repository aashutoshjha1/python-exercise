#!/usr/bin python3
def odd_pair(n: list):
   
    """
       from list get distinct pair of no from sequence.
    """
    odd_list_pair = []
    for i in (range(len(n))):
         for j in range(1,len(n)):
               if n[i] == n[j]:
                    pass
               # pass not distict pair
               if (n[i]+n[j]) % 2 != 0:
                    odd_list_pair.append((n[i], n[j]))

    return odd_list_pair              

list1 = [2,3,8,9,12,1,5,4]
print(odd_pair(list1))

