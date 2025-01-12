#!/usr/bin/env python3

import time

count = 50000000
start = time.time()

def countdown(count):
    while count > 0:
        count -=1

countdown(count)
end = time.time()

print("time taken for single thread : {0}".format(end - start))


