#/bin/env python
class Node:
    def __init__(self, node):
        self.data = node
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def pushlist(self, element):
         data = Node(element)
         data.next = self.head 
         self.head = data
    
    def find_second_last(self):
        if self.head == None:
           print("no lemenet in list ")
           return 
        else:
           last = self.head
           while last.next:
              self.head = last.next
           print(self.head.data)
    def printlist(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next 
    def countlist(self):
        count = 0
        if self.head == None:
             count = 0
             return
        last = self.head
        count = 1
        while last.next != None:
            count +=1
            last = last.next
        #oprint(count)
        return count
   
    def find_last(self):
        if self.head == None:
           print("no element")
        else:
           nextele = self.head
           last = self.head
           while last.next != None:
                 last = last.next
           nextele = last
           print(nextele.data)
    
    def find_Second_last(self):
         len  = self.countlist()
         print(len)
         if len == 0:
             print("no element")
         elif len == 1:
             print("onlyone element in list")
         else:
              last = self.head
              for i in range(1, len-1):
                  last = last.next
              print(last.data)
         
    


list_obj = LinkedList()
list_obj.pushlist(10)
list_obj.pushlist(12)
list_obj.pushlist(14)
list_obj.pushlist(16)
list_obj.printlist()
list_obj.countlist()
list_obj.find_last()
list_obj.find_Second_last()
