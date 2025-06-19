#!/usr/bin/env python3

class CustomRange:
      def __init__(self, start=0, step=1, stop=None):
             self.start = start
             self.stop = stop
             self.step = step
             if self.stop == None:
                  self.start, self.stop = 0, self.start
             if stop == 0:
                 raise ValueError("step can not be 0")
             self._length = 0
             self.current = start

      def __len__(self):
           self._length = max(0, (self.stop - self.start + self.step - 1) // self.step)
           return self._length

      def __iter__(self):
         return self 
           
      def __next__(self):
              answer = self.current
              self.current +=1
              return answer  
     
      def __getitem__(self, index):
          if index < 0:
               index = index + self._length
      
          if not 0 <= index < self._length:
              raise IndexError("index not in range")
           
          return self.start + self.step * index
     
      def print_range(self):
          print(' '.join(str(next(self)) for i in range(self.stop)))

a = CustomRange(1,1,10)
for i in a:
    print(i)

print(a.__len__())
print(a.__getitem__(4)) 
print(a.print_range())



                              
           
