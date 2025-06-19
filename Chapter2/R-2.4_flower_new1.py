#!/usr/bin/env python3

class Flower:
    
    def __init__(self, name,petals, price):
        self._name =  "BlueJasmine"
        self._petals = 10 
        self._price = 12.5

    def setitem(self, name, petals, price):
        self._name = name
        self._petals = petals
        self._price = price

    def print(self):
        print(self._name)
        print(self._petals)
        print(self._price)


a = Flower("new", 5, 10.0)
#b = Flower()
print(a._name)

a.print()
d = a.setitem("newflower", 2 , 1.0)
d = a.print()
print(a._name)
print(a._petals)
print(a._price)


