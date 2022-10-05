#!/usr/bin/env python3
def reverse_list(n:list):
     """ Create reverse of list without using inbuilt function"""
     reverse_list = []
     for i in n:
         reverse_list.insert(0,i)
     return reverse_list

list1 = [2,3,4,5,6]
print(reverse_list(list1))

