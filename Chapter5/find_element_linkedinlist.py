#!/bin/env python
class Node:
     def  __init__(self,data):
          self.node = data
          self.next = None
          


class Linkedinlist:
     def __init__(self, list1, index):
          self.head = None
          self.testlist = list1
          self.index = index
     def getitem(self):
         length = 0
         for tmp in self.testlist:
            while tmp is not None:
               length += 1
         return length    
          
     
list_obj = Linkedinlist([2,3,4,5], 3)
print(list_obj.getitem())
       
