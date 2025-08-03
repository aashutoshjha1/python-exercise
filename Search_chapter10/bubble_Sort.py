#!/usr/bin/env python3


def bubble_sort(seq):
    
    for i in range(len(seq) - 1):
        for j in range(len(seq) - i - 1):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
            else:
                pass
      
    return seq



seq = [2,3,20,1,8,5,15,4]
print(bubble_sort(seq))
        
