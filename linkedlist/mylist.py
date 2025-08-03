#!/usr/bin/env python3

import ctypes

class mylist:

    def __init__(self):
        self.size = 1
        self.number = 0
        self.array = self.make_aray(self.size)

    def make_aray(self, capacity):  
        return (capacity * ctypes.py_object)()
    
    def append(self, value):
        if self.number == self.size:
            self.reseize_array(self.size * 2)
        
        self.array[self.number] = value
        self.number += 1 

    def reseize_array(self, capacity):
        new_array = self.make_aray(capacity)
        for i in range(self.number):
            new_array[i] = self.array[i]
        self.array = new_array
        self.size = capacity

    

    def __len__(self):
        return self.number
    
    def getitem(self, index):
        if index < 0 or index >= self.number:
            raise IndexError("Index out of range")
        return self.array[index]
    
    def __getitem__(self, index):
        if index < 0 or index >= self.number:
            raise IndexError("Index out of range")
        return self.array[index]
    
    def __setitem__(self, index, value):
        if index < 0 or index >= self.number:
            raise IndexError("Index out of range")
        self.array[index] = value

    def __delitem__(self, index):
        if index < 0 or index >= self.number:
            raise IndexError("Index out of range")
        for i in range(index, self.number - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.number - 1] = None
        self.number -= 1

    def __str__(self):
        return "[" + ",".join(str(self.array[i]) for i in range(self.number)) + "]"  

    def pop(self):
        if self.number == 0:
             raise IndexError("list is empty can not do pop")
        value = self.array[self.number - 1]
        self.array[self.number - 1] = None
        self.number -= 1
        return value
    
    
    def clear(self):
        if self.number == 0:
            pass # List is already empty, no action needed.
        else:
            for i in range(self.number):
                self.array[i] = None
                self.number -= 1
            self.size = 1

    def find(self, num):
        
        for i in range(self.number - 1):
            if self.array[i] == num:
                return (num , i)
            
        return None
    
    def insert(self, index, num):
        
       
        if self.number == self.size:
            self.reseize_array(self.size * 2)
        
        arraynew = self.array
        if index > self.number:
            self.array[self.number] = num
            self.number +=1

        else:
            
            if index > self.number:
                for i in range(index-1):
                    arraynew[i] = self.array[i]
                    arraynew[index] = num
                    self.number +=1
            self.array = arraynew
            
            if index == 0:
                for i in range(self.number-1):
                    arraynew[i+1] = self.array[i]
                arraynew[0] = num 
                self.number += 1
            
            
        return self.array
    
            


                



           
        
            

    

list_obj = mylist()
len(list_obj)
print(list_obj)
list_obj.append(10)
list_obj.append(20)
list_obj.append(30)
print(list_obj)
print(list_obj.getitem(1))
print(list_obj.getitem(0))
print(list_obj[1])
#print(list_obj.getitem(5))
print(list_obj)
print(list_obj.pop())
list_obj.clear()
print(list_obj)
list_obj.append(40)
list_obj.append(10)
list_obj.append(10)
print(list_obj.find(10))
#list_obj.pop()
#list_obj.pop()
#list_obj.insert(2,10)
#list_obj.insert(1,20)
print(list_obj) 
list_obj.insert(0,10)
print(list_obj)
list_obj.insert(5,3)
print(list_obj)









    
