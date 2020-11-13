#!/bin/env python
class Empty(Exception):
    """ Exception Class to catch exception in Array Stack"""
    pass

class ArrayStack:
    """ Stack implementation using python list. """
    def __init__(self):
         """ Initilaize a stack. """
         self.stacklist = []
    def __len__(self):
         return self.len(self.stacklist)
     
    def is_empty(self):
        """ Check if stacklist is empty"""
        return len(self.stacklist) == 0
      
    def push(self, ele):
        """ Push element in stack. """
        self.stacklist.append(ele)

    def pop(self):
         """ Remove top element from list. """
         if self.is_empty():
              raise Empty("stack does not have any element")
         return self.stacklist.pop()

