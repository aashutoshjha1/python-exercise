#!/usr/bin/env python3

class Node:
   
   def __init__(self, data):
      self.data = data
      self.next = None

class Linkedlist:
    
     def __init__(self):
         self.head = None
         self.size = 0
     
     def insert(self, value):
        new_node = Node(value)
        if self.head is None:
              self.head = new_node
              return 
        curr = self.head
        while curr.next:
          curr = curr.next
        curr.next = new_node
        
     def traverse(self):
          curr = self.head
          nodes = []
          while curr:
               nodes.append(str(curr.data))
               curr = curr.next
          return "->".join(nodes)

     def delete_pointer(self, pointer):
          count = 0
          curr = self.head
          if pointer == 0:
             new_node = self.head.next
             self.head = new_node
             return
          curr = self.head
          while count < pointer:
                curr = curr.next
                count +=1
          curr.next = curr.next.next
           
          

ll = Linkedlist()
ll.insert(1)
ll.insert(2)
ll.insert(5)
ll.insert(8)

ll.insert(10)

print(ll.traverse())
ll.delete_pointer(2)
print(ll.traverse())
    
              
       
