#!/usr/bin/env python3

class Iteration:
     """"
     This class will implement iterator to call next element 

     """
     def __init__(self, sequence):
          """" 
          take iterator sequence
          """
          self.seq = sequence
          self.item  = -1
     
     def get_len(self):
         
         return len(self.seq)
          
     def __next__(self):
          self.item +=1
          if self.item < len(self.seq):
              return (self.seq[self.item])
              #self.item +=1
          else:
              raise StopIteration
     def __iter__(self):
           """ this function convert iterable to iterator """
           return self

list1 = [2,4,6,7,8,9]
iter_obj = Iteration(list1)
print(iter_obj.__iter__())
print(iter_obj.__next__())
while True:
    print(iter_obj.__next__())

