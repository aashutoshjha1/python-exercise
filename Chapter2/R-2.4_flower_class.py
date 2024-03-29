#!/usr/bin/env python3

class Flower:

    def __init__(self, name: str, petals: float, price: int):
        if isinstance(name, str):
             self.name = name
        else:
            print("name should be string")
        self.petals = petals
        self.price = price
        
    def set_name(self, name):
        self.name = name
        
    def set_petals(self, petals):
        self.petals = petals
        
    def set_price(self,price):
        self.price = price
        
    def get_flowername(self):
        return self.name
        
    def get_flowerpetals(self):
        return self.petals
        
    def get_flowerprice(self):
        return self.price
        

flower_obj = Flower(6, 5, 10)
print(flower_obj.get_flowername())
print(flower_obj.get_flowerpetals())
print(flower_obj.get_flowerprice())
flower_obj.set_name(5)
print(flower_obj.get_flowername())
flower_obj.set_petals("new")
print(flower_obj.get_flowerpetals())

