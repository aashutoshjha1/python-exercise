#!/usr/bin/env python3

def merge_sorted(arr1, arr2):
     i = j = 0
     sorted_list = []
     while i < len(arr1) and j < len(arr2):
         if arr1[i] < arr2[j]:
               sorted_list.append(arr1[i])
               i +=1
         else:
             sorted_list.append(arr2[j])
             j +=1
     
     while i < len(arr1):
           sorted_list.append(arr1[i])
           i +=1
     while j < len(arr2):
         sorted_list.append(arr2[j]) 
         j +=1

     return sorted_list 

def merge_sort(arr):

    if len(arr) == 1:
         return arr
    mid = len(arr)//2
    arr1 = arr[:mid] 
    print(arr1)
    arr2 = arr[mid:]
    print(arr2)
    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)
    return merge_sorted(arr1, arr2)

seq1 = [8,12 ,20,9,24,10,35,30,11]
print(merge_sort(seq1))

