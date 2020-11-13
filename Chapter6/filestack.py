#!/bin/env python
import site
site.addsitedir("/home/akjha/Python_data_structure/python-exercise/Chapter6")
import stackclass 
def reversefile(file):
    S = stackclass.ArrayStack()
    with open("/home/akjha/netstat_data_domain", "r") as file1:
        for line in file1:
             S.push(line.rstrip("/n"))
    
    with open("/home/akjha/netstat_data_domain", "w") as file2:
        while not S.is_empty():
            file2.write(S.pop() + "\n")
            


reversefile("/home/akjha/netstat_data_domain") 

