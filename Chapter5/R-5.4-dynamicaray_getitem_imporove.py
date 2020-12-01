#!/bin/env python
import ctypes
class DynamicArray:
    """ Dynamic array same as python linkedin List"""
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
    def __len__(self):
        """ Return length of array"""
        return self.n
    def __getitem__(self, item):
        """ based on index no. returnthe item on the index """
        if item < -(self.n)  or item > self.n:
             raise IndexError("invalid index no. for this array")
        return self.A[item]
    def appenditem(self, append_item):
         """append item in array"""
         if self.n == self.capacity:
             self.resize(2*self.capacity)
         self.A[self.n] = append_item
         self.n +=1
    def resize(self, newcap):
       """ resize array if it is full """
       B = self.make_array(newcap)
       for k in range(self.n):
           b[k] = self.A[k]
       self.A = B
       self.capacity = newcap
     
    def make_array(self, newcap):
        return (newcap * ctypes.py_object)()


a = DynamicArray()
print(a.n)
#oprint(a.__len__())
print(len(a))
a.appenditem(4)
print(a.n)
print(a.__getitem__(0))
print(a.__getitem__(-1))


