#!/usr/bin/env python3

def merge_sorted(arr1, arr2, arr):
     i = j = k = 0
     while i < len(arr1) and j < len(arr2):
         if arr1[i] < arr2[j]:
               arr[k] = arr1[i] 
               i +=1
         else:
             arr[k] = arr2[j]
             j +=1
         k +=1
     
     while i < len(arr1):
           arr[k] = arr1[i]
           i +=1
           k +=1
     while j < len(arr2):
         arr[k] = arr2[j]
         j +=1
         k +=1
    

def merge_sort(arr):

    if len(arr) == 1:
         return arr
    mid = len(arr)//2
    arr1 = arr[:mid] 
    arr2 = arr[mid:]
    merge_sort(arr1)
    merge_sort(arr2)
    merge_sorted(arr1, arr2, arr)
    return arr
seq1 = [8,12 ,20,9,24,10,35,30,11]
print(merge_sort(seq1))

