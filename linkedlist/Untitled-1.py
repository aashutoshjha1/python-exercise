#!/usr/bin/env python3

# -*- coding: utf-8 -*-

class LinkedinQueue:

    class Node:
        def __init__(self, data, next):
            self.data = data
            self.next = next
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def enqueue(self, data):
        new_node = self.Node(data, None)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.size == 0:
            self.tail = None
        return data
    
    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
    
    def peek(self):
        if self.size == 0:
            return None
        return self.head.data
    
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0   

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "Queue: [" + ", ".join(elements) + "]"   
    
    def __repr__(self):
        return self.__str__()   
LinkedQueue_obj = LinkedinQueue()
# Example usage:
LinkedQueue_obj.enqueue(1)
LinkedQueue_obj.enqueue(2)
LinkedQueue_obj.enqueue(3)