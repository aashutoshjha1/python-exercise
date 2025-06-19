#!/usr/bin/env python3

class Binary:
    def __init__(self,sequence):
       self.sequence = sequence 
    
    def binarysearch(self, num, low, high):
         if len(self.sequence) == 0 :
            print(f"passed list has no element {self.sequence}")
         
         mid = ((low + high ) // 2)
         print(mid)
         if num == self.sequence[mid]:
              
              print(f"match found for {num} on index {mid}")
              return True
         elif num > self.sequence[mid]:
                self.binarysearch(num, mid+1, high)
         else:
               self.binarysearch(num, low, mid-1)
         return False
         
          
sequence = [2,3,4,6,7,8,9,10]
binary_obj = Binary(sequence)
binary_obj.binarysearch(7,0, len(sequence))
binary_obj.binarysearch(4,0, len(sequence))
binary_obj.binarysearch(10,0, len(sequence))                
        
