#!/usr/bin/env python3

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        first_point = 0
        second_point = 0
        
        while first_point < len(s) and second_point < len(t):
            if s[first_point] == t[second_point]:
                first_point += 1
            second_point += 1
        
        if first_point == len(s):
            return True
        else:
            return False
        

        


