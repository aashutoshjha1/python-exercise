#!/usr/bin/env python3

class SequenceIterator:
     def __init__(self, sequence):
         self.sequence = sequence
         self.k = -1
     
     def __next__(self):
         self.k +=1
         if self.k < len(self.sequence):
              return (self.sequence[self.k])
         else:
             raise StopIteration()
      
     def __iter__(self):
         return self


seq = [2,4,5,6]
seq_obj = SequenceIterator(seq)
for i in seq_obj:
    print(i)



