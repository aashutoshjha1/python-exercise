#!/usr/bin/env python3
import os

def list_file(path):
    if os.path.isfile(path):
       print(path)
    elif os.path.isdir(path):
        print(f" directory name is ****** {path}")
        for filename in os.listdir(path):
             childpath = os.path.join(path, filename)
             list_file(childpath)


path = "/Users/a0j0b83/Documents/python-exercise"
list_file(path)

