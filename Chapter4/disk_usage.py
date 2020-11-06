#!/bin/env/python
import os
def disk_usage(path):
    """
    this function resursiverly check file size in each diretory and return size of path/directory
    provided.
    """
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for file in os.listdir(path):
             subdir = os.path.join(path, file)
             print(subdir)
             total +=disk_usage(subdir)
    print ("{} for path {}".format(total, path)) 
    return total
path = "/home/akjha/Documents/Aashutosh_cfengine/" 
disk_usage(path)
  
