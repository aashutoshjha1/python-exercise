#!/usr/bin/env python3

class Flower:
    
    def __init__(self, name= "rose", petals=10, price= 8.0):
        self._name = name
        self._petals = petals 
        self._price = price
     
    def print(self):
        print(self._name)
        print(self._petals)
        print(self._price)


a = Flower("rose", 5 , 6.0)
b = Flower()
a.print()
b.print()

