#!/usr/bin/env python3

# -*- coding: utf-8 -*-

class DoubleLinkedListNode:
    class Node:
        def __init__(self, value, prev, next):
            self.value = value
            self.prev = prev
            self.next = next
        
        def __str__(self):
            return str(self.value) if self.value is not None else "None"
    
    def __init__(self):
        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def add_first(self, value):
        new_node = self.Node(value, self.header, self.header.next)
        self.header.prev = new_node
        self.header.next = new_node
        self.size += 1


    def insert_between(self, prev_node, next_node, value):
        new_node = self.Node(value, prev_node, next_node)
        prev_node.next = new_node
        next_node.prev = new_node
        self.size += 1
        return new_node
    
    def ___str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current))  # calls Node.__str__()
            current = current.next
        return " <-> ".join(values)

    
DoubleLinkedListNode_obj = DoubleLinkedListNode()
DoubleLinkedListNode_obj.add_first(10)
DoubleLinkedListNode_obj.add_first(20)
print(DoubleLinkedListNode_obj)  # Output: 20 <-> 10

