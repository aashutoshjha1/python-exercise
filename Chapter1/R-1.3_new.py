#!/usr/bin/env python3

def minmax(data):
    min = data[0]
    max = data[0]
    
    if len(data) <= 1:
         print( " Both smallest and largets number is {data[0]}")
    else:
        for i, v in enumerate(data):
             if data[i] < min:
                 min = data[i]
             elif data[i] > max:
                 max = data[i] 

    return min, max


def minmax_other(data):
    min = data[0]
    max = data[0]
    if len(data) <= 1:
        print( " Both smallest and largets number is {data[0]}")
    else:
        for i in range(0, len(data)):
             if data[i] < min:
                  min = data[i]
             elif data[i] > max:
                 max = data[i]
    return min, max
             

data = [4,6,8,5,6,1]
print(minmax(data))
print(minmax_other(data))
    
