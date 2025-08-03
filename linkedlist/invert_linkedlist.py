#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class invertlinkedlist:
    class Node:
        def __init__(self,value , next):
            self.value = value
            self.next = next
        
    def __init__(self):
        self.head = None
        self.size = 0

    def ___len__(self):
        return self.size    
    
    def add_first(self, value):
        new_node = self.Node(value, self.head)
        self.head = new_node
        self.size += 1
    
    
    
    def invert(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def __str__(self):  
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.value))
            current = current.next
        
    


invertlinkedlist_obj = invertlinkedlist()
invertlinkedlist_obj.add_first(10)
invertlinkedlist_obj.add_first(20)
invertlinkedlist_obj.add_first(30)
print("Original List:", invertlinkedlist_obj)
invertlinkedlist_obj.invert()
print("Inverted List:", invertlinkedlist_obj)