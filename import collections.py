#!/usr/bin/env python3

import collections

def sum(values):
    s = 0
    if not isinstance(values, (int, float)):
        raise TypeError("value {values} must be numeric")
    else:
        return (s + values)
    

print(sum("a"))


    
    