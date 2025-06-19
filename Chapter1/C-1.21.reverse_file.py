#!/usr/bin/env python3
import sys

list2 = []
a = sys.stdin.readlines()
with open("file1.txt", "w") as file1:
   try:
      file1.writelines(a)
   except EOFError as e:
      print("wrote data to file")
      pass
  
with open("file1.txt", "r") as file2: 
     for i in file2:
         list2.append(i)
     b = reversed(list2)
     for i in list(b):
         print(i, end = '')


       

   
