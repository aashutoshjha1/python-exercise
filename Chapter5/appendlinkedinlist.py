#!/bin/env python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def reverselist(self):
        currentnode = self.head
        prev = None
        while currentnode is not None:
            next = currentnode.next
            currentnode.next = prev
            prev = currentnode
            currentnode = next
        self.head = prev
            
    def pushlist(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
   
    def appendlist(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
             
        else:
            last = self.head
            while (last.next) != None:
               last = last.next
            last.next = new_node
        
    def printlist(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next


List_obj = LinkedList()
List_obj.appendlist(1)
List_obj.appendlist(10)
List_obj.appendlist(100)
List_obj.appendlist(1000)
List_obj.printlist()
List_obj.reverselist()
List_obj.printlist()



            
        

