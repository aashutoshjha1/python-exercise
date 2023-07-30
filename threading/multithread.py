#!/usr/bin/env python3

import time
import threading

count = 500000

start = time.time()

def countdown(count):
    while count > 0 :
        count -=1

t1 = threading.Thread(target=countdown, args=(count//2,))
t2 = threading.Thread(target=countdown, args=(count//2,))

t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print("time taken with multi thread {0}".format(end-start))


