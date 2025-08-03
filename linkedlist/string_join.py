#!/usr/bin/env python3

class Node:
   
    def __init__(self, data):
          self.data = data
          self.next = None
    
    def __str__(self):
        if self.data is not None:
            return str(self.data)
        else:            
            return None 
        
class Linkedlist:

    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values) if values else "Empty List"
 
    def __len__(self):
        return self.size

    def insert_node(self, value):
         new_node = Node(value)
         new_node.next = self.head
         self.head = new_node
         self.size +=1

    def insert_end(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
            self.size +=1
            return 
            
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        self.size +=1    
  
    def insert_between(self, pos, value):
        new_node = Node(value)
        if pos >= self.size:
            self.insert_end(value)
        if pos == 0:
           self.insert_node(value)

        else:
            current = self.head
            position = 1
            while position < pos:
                  current = current.next
                  position += 1
            #current.next = new_node
            new_node.next = current.next
            current.next = new_node
            self.size += 1

    def delete_by_Value(self, value):
        if self.head == None:
            return "emply linkedlist"
        current = self.head
        if current.data == value:
           self.head = current.next
           self.size -=1
           
        else:
            while current.next is not None:
                if current.next.data == value:
                    break
                current = current.next 
                 
            if current.next == None:
               return "value not found"
            else:
                current.next = current.next.next
                self.size -=1
 
    def reverse(self):
          
          curr = self.head
          prev_node = None
          
          while curr is not None:
              next_node = curr.next
              curr.next = prev_node
              prev_node = curr
              curr = next_node

          self.head = prev_node       


a = Node(5)
print(a)
print(a.data)
print(a.next)

b = Node(10)
print(b)


c = Linkedlist()
print(c)
print(len(c))
c.insert_node(3)

print(c)
print(len(c))
print(c)
print(len(c))

c.insert_node(35)
c.insert_node(2)
c.insert_node(9)
c.insert_node(20)
c.insert_node(11)

print(c)


#print(c.odd_sum())


print(c.reverse())
print(c)

