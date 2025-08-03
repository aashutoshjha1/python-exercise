#!/usr/bin/env python3

def selection_sort(seq):
    
    for i in range(len(seq)-1):
        min = i
        for j in range(i+1, len(seq)):
            if seq[j] < seq[min]:
                min = j
        seq[min], seq[i] = seq[i], seq[min]
       
    return seq


seq = [10,4,20,1,6,3]
print(selection_sort(seq))





