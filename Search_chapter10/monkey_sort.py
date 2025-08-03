#!/usr/bin/env python3

import random

def monkey_sort(seq):
    print(len(seq) - 1)
    for i in range(len(seq)):
        if seq[i] > seq[i+1]:
           
          random.shuffle(seq)
        else:
           return f"sorted: {seq} "


seq = [2,1,3,6,4,5]
print(monkey_sort(seq))

