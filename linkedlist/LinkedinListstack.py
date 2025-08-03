#!/usr/bin/env python3

class LinkedinStack:
    class Node:
        def __init__(self, element, next):
             self.element = element
             self.next = next
    
    def __init__(self):
        self.head = None
        self.size = 0
    def is_empty(self):
        return self.size == 0
    def __len__(self):
        return self.size
    
    def push(self, element):
        new_node = self.Node(element, self.head)
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        element = self.head.element
        self.head = self.head.next
        self.size -= 1
        return element
    
    def top(self):  
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self.head.element

    def __str__(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.element))
            current = current.next
        return "LinkedinStack: [" + ", ".join(elements) + "]"

    def __repr__(self):
        return self.__str__()   
    
    def push_at(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("index out of bounds")
        if index == 0:
            self.push(element)
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node = self.Node(element, current.next)
            current.next = new_node
            self.size += 1
    
linkedinstack_obj = LinkedinStack()
linkedinstack_obj.push(1)
linkedinstack_obj.push(2)
linkedinstack_obj.push(3)


