#!/usr/bin/env python3

import time

start_time = time.time()
time.sleep(4)
end_time = time.time()

elapsed_time = end_time - start_time

print(elapsed_time)

def list_time():
    list1 = [2,4,5]
    for i in range(100):
        list1.append(i)
   
start_time = time.time()
print(start_time)
list_time()
endtime = time.time()
print(f"endtime :{endtime}")
elapsed_time = end_time - start_time

print(f"elapsed_time : {elapsed_time}")
 
